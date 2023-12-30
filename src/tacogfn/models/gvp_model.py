import torch
import torch.nn as nn

from src.pharmaconet.src.scoring import pharmacophore_model
from src.tacogfn.models.gvp import GVP, GVPConvLayer, LayerNorm, tuple_index

NUM_INTERACTION_TYPES = len(pharmacophore_model.INTERACTION_TYPES)


class GVP_embedding(nn.Module):
    """
    Modified based on https://github.com/drorlab/gvp-pytorch/blob/main/gvp/models.py
    GVP-GNN for Model Quality Assessment as described in manuscript.

    Takes in protein structure graphs of type `torch_geometric.data.Data`
    or `torch_geometric.data.Batch` and returns a scalar score for
    each graph in the batch in a `torch.Tensor` of shape [n_nodes]

    Should be used with `gvp.data.ProteinGraphDataset`, or with generators
    of `torch_geometric.data.Batch` objects with the same attributes.

    :param node_in_dim: node dimensions in input graph, should be
                        (6, 3) if using original features
    :param node_h_dim: node dimensions to use in GVP-GNN layers
    :param node_in_dim: edge dimensions in input graph, should be
                        (32, 1) if using original features
    :param edge_h_dim: edge dimensions to embed to before use
                       in GVP-GNN layers
    :seq_in: if `True`, sequences will also be passed in with
             the forward pass; otherwise, sequence information
             is assumed to be part of input node embeddings
    :param num_layers: number of GVP-GNN layers
    :param drop_rate: rate to use in all dropout layers
    """

    def __init__(
        self,
        node_in_dim,
        node_h_dim,
        edge_in_dim,
        edge_h_dim,
        seq_in=False,
        num_layers=3,
        drop_rate=0.1,
    ):
        super(GVP_embedding, self).__init__()

        if seq_in:
            self.W_s = nn.Embedding(NUM_INTERACTION_TYPES, NUM_INTERACTION_TYPES)
            node_in_dim = (node_in_dim[0] + NUM_INTERACTION_TYPES, node_in_dim[1])

        self.W_v = nn.Sequential(
            LayerNorm(node_in_dim),
            GVP(node_in_dim, node_h_dim, activations=(None, None)),
        )
        self.W_e = nn.Sequential(
            LayerNorm(edge_in_dim),
            GVP(edge_in_dim, edge_h_dim, activations=(None, None)),
        )

        self.layers = nn.ModuleList(
            GVPConvLayer(node_h_dim, edge_h_dim, drop_rate=drop_rate)
            for _ in range(num_layers)
        )

        ns, _ = node_h_dim
        self.W_out = nn.Sequential(LayerNorm(node_h_dim), GVP(node_h_dim, (ns, 0)))

    def forward(self, h_V, edge_index, h_E, seq):
        """
        :param h_V: tuple (s, V) of node embeddings
        :param edge_index: `torch.Tensor` of shape [2, num_edges]
        :param h_E: tuple (s, V) of edge embeddings
        :param seq: if not `None`, int `torch.Tensor` of shape [num_nodes]
                    to be embedded and appended to `h_V`
        """
        seq = self.W_s(seq)
        h_V = (torch.cat([h_V[0], seq], dim=-1), h_V[1])
        h_V = self.W_v(h_V)
        h_E = self.W_e(h_E)
        for layer in self.layers:
            h_V = layer(h_V, edge_index, h_E)
        out = self.W_out(h_V)

        return out
