# These are the fragments used in the original paper, each fragment is a tuple
# (SMILES string, attachment atom idx).
# The attachment atom idx is where bonds between fragments are legal.
GFLOWNET_FRAGMENTS = [
    ["Br", [0]],
    ["C", [0]],
    ["C#N", [0]],
    ["C1=CCCCC1", [0, 2, 3]],
    ["C1=CNC=CC1", [0, 2]],
    ["C1CC1", [0]],
    ["C1CCCC1", [0]],
    ["C1CCCCC1", [0, 1, 2, 3, 4, 5]],
    ["C1CCNC1", [0, 2, 3, 4]],
    ["C1CCNCC1", [0, 1, 3]],
    ["C1CCOC1", [0, 1, 2, 4]],
    ["C1CCOCC1", [0, 1, 2, 4, 5]],
    ["C1CNCCN1", [2, 5]],
    ["C1COCCN1", [5]],
    ["C1COCC[NH2+]1", [5]],
    ["C=C", [0, 1]],
    ["C=C(C)C", [0]],
    ["C=CC", [0, 1]],
    ["C=N", [0]],
    ["C=O", [0]],
    ["CC", [0, 1]],
    ["CC(C)C", [1]],
    ["CC(C)O", [1]],
    ["CC(N)=O", [2]],
    ["CC=O", [1]],
    ["CCC", [1]],
    ["CCO", [1]],
    ["CN", [0, 1]],
    ["CNC", [1]],
    ["CNC(C)=O", [0]],
    ["CNC=O", [0, 2]],
    ["CO", [0, 1]],
    ["CS", [0]],
    ["C[NH3+]", [0]],
    ["C[SH2+]", [1]],
    ["Cl", [0]],
    ["F", [0]],
    ["FC(F)F", [1]],
    ["I", [0]],
    ["N", [0]],
    ["N=CN", [1]],
    ["NC=O", [0, 1]],
    ["N[SH](=O)=O", [1]],
    ["O", [0]],
    ["O=CNO", [1]],
    ["O=CO", [1]],
    ["O=C[O-]", [1]],
    ["O=PO", [1]],
    ["O=P[O-]", [1]],
    ["O=S=O", [1]],
    ["O=[NH+][O-]", [1]],
    ["O=[PH](O)O", [1]],
    ["O=[PH]([O-])O", [1]],
    ["O=[SH](=O)O", [1]],
    ["O=[SH](=O)[O-]", [1]],
    ["O=c1[nH]cnc2[nH]cnc12", [3, 6]],
    ["O=c1[nH]cnc2c1NCCN2", [8, 3]],
    ["O=c1cc[nH]c(=O)[nH]1", [2, 4]],
    ["O=c1nc2[nH]c3ccccc3nc-2c(=O)[nH]1", [8, 4, 7]],
    ["O=c1nccc[nH]1", [3, 6]],
    ["S", [0]],
    ["c1cc[nH+]cc1", [1, 3]],
    ["c1cc[nH]c1", [0, 2]],
    ["c1ccc2[nH]ccc2c1", [6]],
    ["c1ccc2ccccc2c1", [0, 2]],
    ["c1ccccc1", [0, 1, 2, 3, 4, 5]],
    ["c1ccncc1", [0, 1, 2, 4, 5]],
    ["c1ccsc1", [2, 4]],
    ["c1cn[nH]c1", [0, 1, 3, 4]],
    ["c1cncnc1", [0, 1, 3, 5]],
    ["c1cscn1", [0, 3]],
    ["c1ncc2nc[nH]c2n1", [2, 6]],
]


CROSSDOCK_50CUTOFF_BRICS_FRAGMENTS = [
    ['c1ccccc1', [0, 1, 2, 3, 4]],
 ['N', [0]],
 ['C', [0]],
 ['O', [0]],
 ['C=O', [0]],
 ['CO', [0, 1]],
 ['Cl', [0]],
 ['CC', [0, 1]],
 ['F', [0]],
 ['O=CO', [1]],
 ['CC=O', [0, 1]],
 ['c1ccncc1', [0, 1, 2, 4, 5]],
 ['CCC', [0, 1, 2]],
 ['C1CCOC1', [0, 1, 2, 4]],
 ['O=S=O', [1]],
 ['CN', [0, 1]],
 ['O=P(O)(O)O', [2, 4]],
 ['C1CCNCC1', [0, 1, 3]],
 ['CCC=O', [0, 1, 2]],
 ['FC(F)F', [1]],
 ['Br', [0]],
 ['NC=O', [1]],
 ['S', [0]],
 ['C#N', [0]],
 ['CC(C)C', [0, 1]],
 ['C1CNCCN1', [2, 5]],
 ['C1CCOCC1', [0, 1, 2, 4, 5]],
 ['CC(=O)O', [0]],
 ['C1CCCCC1', [2, 5]],
 ['CNC', [1]],
 ['c1ncc2nc[nH]c2n1', [0, 8]],
 ['[O][N]=O', [1]],
 ['C1CCNC1', [0, 1, 3, 4]],
 ['C1CC1', [0]],
 ['O=P(O)(O)OP(=O)(O)O', [8, 2]],
 ['CCC(=O)O', [0, 1]],
 ['C[SH](=O)=O', [0, 1]],
 ['C1COCCN1', [5]],
 ['c1cncnc1', [0, 1, 3, 5]],
 ['CCO', [0]],
 ['N[SH](=O)=O', [1]],
 ['O=c1cc[nH]c(=O)[nH]1', [2, 4]],
 ['CCCC', [0, 3]],
 ['c1ccsc1', [1, 3]],
 ['N=CN', [1]],
 ['c1cn[nH]c1', [0, 1, 2, 4]],
 ['I', [0]],
 ['C1CCCC1', [4]],
 ['c1ccc2ccccc2c1', [4]],
 ['CC(N)C(=O)O', [0]],
 ['CCC(C)O', [0, 1, 3]],
 ['O=P(O)(O)OP(=O)(O)OP(=O)(O)O', [2]],
 ['O=C(O)CCCC(=O)O', [5]],
 ['c1c[nH]nn1', [0, 2]],
 ['CS', [1]],
 ['c1cscn1', [0, 3]],
 ['CCN', [0]],
 ['O=c1nc[nH]c2[nH]cnc12', [9, 3]],
 ['c1c[nH]cn1', [2]],
 ['C1=c2ccccc2=NC1', [3]],
 ['[O][P](=O)O', [3]],
 ['C#C', [0, 1]],
 ['c1ccoc1', [1]]]


ZINC250K_50CUTOFF_BRICS_FRAGMENTS = [
    ["C1=CC=CC=C1", [0, 1, 2, 3, 4, 5]],
    ["C", [0]],
    ["N", [0]],
    ["C=O", [0]],
    ["CC", [0, 1]],
    ["O", [0]],
    ["CO", [0, 1]],
    ["CC=O", [0, 1]],
    ["F", [0]],
    ["Cl", [0]],
    ["C1CCNCC1", [0, 1, 2, 3, 4, 5]],
    ["CCC", [0, 1, 2]],
    ["C1=CC=NC=C1", [0, 1, 2, 4, 5]],
    ["CN", [0, 1]],
    ["C1=CNN=C1", [0, 1, 2, 4]],
    ["CCC=O", [0, 1, 2]],
    ["S", [0]],
    ["C1CCNC1", [0, 1, 2, 3, 4]],
    ["C1CC1", [0, 1, 2]],
    ["C1=CSC=C1", [0, 1, 3, 4]],
    ["C1CNCCN1", [1, 2, 4, 5]],
    ["O=S=O", [1]],
    ["C1CCCCC1", [0, 2, 3, 4, 5]],
    ["Br", [0]],
    ["C1=CSC=N1", [0, 1, 3]],
    ["CC(C)C", [0, 1, 3]],
    ["O=[N+][O-]", [1]],
    ["C1=COC=C1", [0, 1, 3, 4]],
    ["C1COCCN1", [0, 1, 3, 4, 5]],
    ["C1CCCC1", [2, 3, 4]],
    ["C#N", [0]],
    ["CNC", [0, 1]],
    ["C1CCOC1", [0, 1, 2, 4]],
    ["FC(F)F", [1]],
    ["C1=CN=CN=C1", [0, 1, 3, 5]],
    ["O=CO", [1]],
    ["C1=NC=NO1", [0, 2]],
    ["CCCC", [0, 1, 2, 3]],
    ["NC=O", [0, 1]],
    ["C1=CON=C1", [0, 1, 4]],
    ["O=C1CCCN1", [2, 3, 4, 5]],
    ["C1=CNC=N1", [0, 1, 2, 3]],
    ["CCO", [0, 1]],
    ["O=CC=O", [1, 2]],
    ["C[SH](=O)=O", [0, 1]],
    ["C1=NC=NN1", [0, 2, 4]],
    ["C1=CNC=C1", [0, 1, 2, 3, 4]],
    ["CS", [0, 1]],
    ["C1=NN=CN1", [0, 3, 4]],
    ["C1=CC=C2NC=NC2=C1", [0, 1, 4, 5, 8]],
    ["CCCC=O", [0, 1, 2, 3]],
    ["C1=CC=C2NC=CC2=C1", [0, 1, 2, 4, 5, 6]],
    ["C1CCOCC1", [0, 1, 2, 4, 5]],
    ["C1=CC=C2SC=NC2=C1", [0, 1, 2, 5, 8]],
    ["C1=CC=C2C=CC=CC2=C1", [0, 4, 5, 6, 7, 9]],
    ["C1=CC=C2OCOC2=C1", [0, 2]],
    ["C1=NN=CS1", [0, 3]],
    ["C1=NN=NN1", [0, 4]],
    ["C=CC", [2]],
    ["CCC(C)C", [0, 1, 2, 3]],
    ["C1CCC1", [0, 1, 2, 3]],
    ["C1=NN=CO1", [0, 3]],
    ["C1=CC=C2OCCOC2=C1", [0, 2, 5, 6]],
    ["CC(C)O", [0, 1, 2]],
    ["O=S1(=O)CCCC1", [4, 5]],
    ["C1=COC=N1", [0, 1, 3]],
    ["C1CCCNCC1", [0, 1, 4, 5, 6]],
    ["CC(C)C=O", [0, 1, 3]],
    ["CC(F)(F)F", [0]],
    ["C1=CC=C2NCCC2=C1", [0, 1, 4, 5, 6]],
    ["C1=CC=C2CCCC2=C1", [0, 4, 5, 6]],
    ["CC(=O)O", [0]],
    ["C1=CN=CC=N1", [0, 3, 4]],
    ["C1=CNN=N1", [0, 1, 2]],
    ["C1=CN=C2C=CC=CC2=C1", [0, 1, 4, 7, 9]],
    ["CC(N)=O", [0, 2]],
    ["CC(C)CC=O", [0, 3, 4]],
    ["O=C1CNC(=O)N1", [2, 6]],
    ["OC(F)F", [0]],
    ["C1=CC=C2CNCCC2=C1", [0, 1, 4, 5, 6]],
    ["CCCO", [0, 1, 2]],
    ["CC#N", [0]],
    ["N[SH](=O)=O", [0, 1]],
    ["C1CNCCNC1", [2, 5]],
    ["O=C1C=CC=CN1", [2, 3, 4, 5, 6]],
    ["CCN", [0, 1]],
    ["C1=CC=C2CCCCC2=C1", [0, 4, 5, 7]],
    ["C#CC", [0, 2]],
    ["C1=CN=NC=C1", [1, 4]],
    ["C1=CC=C2OC=CC2=C1", [0, 2, 5, 6]],
    ["C1=CC=C2OC=NC2=C1", [0, 1, 5]],
    ["C1CCCCCC1", [4, 5]],
    ["C1=CC=C2N=CC=CC2=C1", [0, 1, 2, 5, 6, 7]],
    ["NC(N)=S", [0, 2]],
    ["O=C1NC=NC2=CC=CC=C12", [8, 2, 3]],
    ["I", [0]],
    ["C1=CC=C2OCCC2=C1", [0, 2, 5, 6]],
    ["CCCCC", [0, 1, 2]],
    ["O=C1CCCCN1", [2, 4, 5, 6]],
    ["C1=CCCCC1", [0, 3, 4]],
    ["CC[SH](=O)=O", [0, 2]],
    ["NNC=O", [0, 2]],
    ["O=CNNC=O", [1, 4]],
    ["O=C1NC(=O)C2=CC=CC=C12", [8, 2, 7]],
    ["O=C1CNCCN1", [2, 3, 6]],
    ["C1=CC2=NC=CN2C=C1", [1, 4, 5, 7, 8]],
    ["O=C1C=CC=NN1", [2, 3, 4, 6]],
    ["C=N", [0, 1]],
    ["C=NNC=O", [0, 3]],
    ["C1CSCCN1", [0, 1, 3, 4, 5]],
    ["CCC#N", [0, 1]],
    ["C1=CC=C2NCCCC2=C1", [0, 4, 7]],
    ["O=C1CCC(=O)N1", [3, 6]],
    ["C1C2CC3CC1CC(C2)C3", [8, 3, 7]],
    ["CCC(=O)O", [0, 1]],
    ["C1CNC1", [0, 1, 2]],
    ["[O-]", [0]],
    ["CC(C)(C)C=O", [0, 4]],
    ["C[S+][O-]", [0, 1]],
    ["C1=CCCC1", [2, 3, 4]],
    ["CC(=O)NNC=O", [0, 5]],
    ["O=C1C=CN=CN1", [2, 3, 5]],
    ["OC(F)(F)F", [0]],
    ["O=CCCC=O", [1, 4]],
    ["CC(F)F", [0]],
    ["CCC(C)C=O", [0, 1, 4]],
    ["O=C1C=CCN1", [2, 3, 4, 5]],
    ["C1CCSC1", [0, 1, 2, 4]],
    ["CC(C)(C)O", [0, 3]],
    ["C1=CC2=CCN=C2C=C1", [0, 3, 4]],
    ["CCC(N)=O", [0, 1]],
    ["NC=S", [0, 1]],
    ["C1=CC=C2OCCCC2=C1", [0, 6, 7]],
    ["O=C1C=CC2=CC=CC=C2O1", [2, 3, 7]],
    ["O=C1NN=CC2=CC=CC=C12", [2, 4]],
    ["C1=CC=C2OCCCOC2=C1", [0, 2]],
    ["C1=CCNCC1", [0, 3]],
    ["FCF", [1]],
    ["C1=NNCC1", [0, 2, 3]],
    ["C1=CN=NC1", [0, 1, 4]],
    ["CC(C)(C)C", [0, 4]],
    ["C=NNC(C)=O", [0, 4]],
    ["CCC(C)O", [0, 1, 3]],
    ["C1=CN2N=CN=C2N=C1", [8, 1, 4, 0]],
    ["C1CC2CCC1C2", [1, 2, 6]],
    ["CCC(F)(F)F", [0]],
    ["S=C1NC=NN1", [2, 3, 5]],
    ["O=C1NC=NN1", [2, 3, 5]],
    ["C1=CC2=NN=CN2C=C1", [5]],
    ["O=CCCO", [1, 3]],
    ["O=C1C=CNC(=O)N1", [2, 3, 4, 7]],
    ["C=NN", [0, 2]],
    ["C1=CC=C2SCCC2=C1", [5, 6]],
    ["C1=CC=[N+]C=C1", [0, 1, 3, 4]],
    ["CCCCO", [0, 1, 2]],
    ["O=C1COC2=CC=CC=C2N1", [10, 2, 7]],
    ["C1CCSCC1", [0, 1, 2, 5]],
    ["C1=CC2=C(CCNC2)S1", [6, 7]],
    ["C1=NNN=N1", [0, 2]],
    ["C1=NC=NS1", [0, 2]],
    ["CCl", [0]],
    ["O=C1NC2=CC=CC=C2O1", [2, 6]],
    ["O=C1NCCN1", [2, 5]],
    ["C1=CC2=C(CCCC2)S1", [0, 1, 5]],
    ["O=C1CCC2=CC=CC=C2N1", [10, 3, 6]],
    ["C1=CSN=N1", [0, 1]],
    ["C1=CC=C2NN=CC2=C1", [0, 1, 6]],
    ["C1=CN=C2NN=CC2=C1", [0, 1, 4, 6, 8]],
    ["C1=CC2=CN=CN=C2S1", [0, 1, 3, 5]],
    ["O=C1NC(=O)C2=C(N=CN2)N1", [8, 9, 2, 10]],
    ["CCCC#N", [0, 1, 2]],
    ["C1CC2CNCCN2C1", [4, 5]],
    ["CCCCC=O", [0, 3, 4]],
    ["C1CSCN1", [0, 4]],
    ["CC[S+][O-]", [2]],
    ["CCS(C)(=O)=O", [0]],
    ["O=[SH](=O)O", [1, 3]],
    ["C1=NN=C2CCCCCN12", [0]],
    ["O=C1NC=NC2=C1C=CS2", [8, 2, 3, 7]],
    ["O=C1NC2=CC=CC=C2N1", [9, 2, 5]],
    ["CC(C)CCC=O", [4, 5]],
    ["C1=CC=C2N=CC=NC2=C1", [0, 5, 6]],
    ["C1=CC=C2SC=CC2=C1", [5, 6]],
    ["CCCS(C)(=O)=O", [0, 1]],
    ["CS(C)(=O)=O", [0, 2]],
    ["CCCl", [0, 1]],
    ["C=C(C)C", [2]],
    ["C1=CC2=C(C=C1)NC=C2", [8, 1, 4]],
    ["CN=C(N)N", [3, 4]],
    ["O=C1C=CN=C2C=CC=CN12", [8, 2, 3, 6]],
    ["C1=NC2=C(CCCC2)S1", [0, 4]],
    ["C1=CN2C=CSC2=N1", [0, 1]],
    ["NC=NO", [1, 3]],
    ["O=C1NCCO1", [2]],
    ["O=CC[SH](=O)=O", [1, 3]],
    ["C1=NNC2=C1CCCC2", [2, 5]],
    ["C1=CC2=NN=CN2N=C1", [8, 5]],
    ["C1=CC=C2C(=C1)NCC1CC=CC21", [1, 7]],
    ["C1=CC=C2OCC=CC2=C1", [0, 6]],
    ["O=C1CCCO1", [2, 4]],
    ["C1=CC=C2N=CN=CC2=C1", [0, 5, 7]],
    ["CCC[SH](=O)=O", [0, 3]],
    ["C#C", [0]],
    ["CCC(=O)NNC=O", [0, 1, 6]],
    ["C1CCC2NCCCC2C1", [4, 5]],
    ["C1=CC=C2COCC2=C1", [0]],
    ["CCCC(C)C", [0, 1]],
    ["CCCCCO", [1]],
    ["CCC(C)C(=O)O", [1, 2]],
    ["C1COC1", [0]],
    ["C1CCN2CCOCC2C1", [5]],
    ["C1=CC2=C(C=C1)OCO2", [0, 1, 5]],
    ["C1=CC2=C(C=C1)OCCO2", [0, 1, 5]],
    ["C1CCC2(CCSC2)OC1", [1]],
    ["C1CCC2(CCOC2)OC1", [1]],
    ["C1=NN=C2CCCN12", [0]],
    ["C1=NN2CCCCC2=N1", [0, 6]],
    ["C[S+](C)[O-]", [0, 2]],
    ["C1=NC=NC=N1", [0, 2, 4]],
    ["C1CCN2CCNCC2C1", [5, 6]],
    ["C1=NCCS1", [0, 2, 3]],
    ["C1=CN2N=CC=C2N=C1", [0, 1, 4, 5, 8]],
    ["NN", [0]],
    ["C1=NOCC1", [0, 3]],
    ["CC(C)C#N", [0]],
    ["O=C1NC=CCN1", [3, 4, 5]],
    ["O=C1NC(=O)C2(CCCCC2)N1", [8, 2, 6]],
    ["C1=CC=C2C=NC=CC2=C1", [4, 7]],
    ["C1=NCCN1", [0, 3, 4]],
    ["C1=CN=C2NC=NC2=C1", [0, 4, 5]],
    ["N#CCC=O", [2, 3]],
    ["FC(F)S", [3]],
    ["O=C1C=CC2=CC=CC=C2N1", [2, 3]],
    ["C1CC2CCC(CN1)N2", [8, 7]],
    ["C1=CSN=C1", [0, 1, 4]],
    ["CC(C)CCO", [3]],
    ["C1CCC2(CCC2)OC1", [1]],
    ["C1CCCCCCC1", [3]],
    ["O=C1C=NC=CN1", [2, 6]],
    ["C1CCC2NCCC2C1", [4, 5]],
    ["C1CC2COCCN2C1", [5]],
    ["CCC(C)(C)C", [1, 3]],
    ["C1=NC2=C(CNCC2)S1", [0, 5]],
    ["CC(C)=O", [0]],
    ["C1CC2CCC2O1", [3, 4]],
    ["O=C1C=CNN1", [2, 3, 4, 5]],
    ["C1CN2CCN1CC2", [0]],
    ["C1=CC2=C(C=C1)CCC2", [1, 6]],
    ["O=C1CCCCCN1", [2, 7]],
    ["O=CNO", [1, 3]],
    ["C1=NN=C2SC=NN12", [0, 5]],
    ["C1=CC2=C(C=C1)OCC2", [0, 5, 7]],
    ["O=[SH](=O)N=CO", [1, 4]],
    ["CC=NNC=O", [1, 4]],
    ["C1=CC2=C3C(=C1)CCCC3CC2", [11]],
    ["C1CNCCSC1", [2, 3]],
    ["C1C[S+]CCN1", [2, 3, 5]],
    ["C1CSCCS1", [1]],
    ["CC(C)(C)CC=O", [5]],
    ["C1COCCO1", [1]],
    ["NC(=S)NNC=O", [0, 5]],
    ["C1=CC2=C(C=C1)CNCC2", [0, 5, 6, 7]],
    ["O=C1CC2=CC=CC=C2N1", [9, 2, 5]],
    ["CCCC(=O)O", [0, 2]],
    ["C1CCC2(CCCC2)OC1", [1]],
    ["C1CC2(CCN1)OCCO2", [5]],
    ["CC(C=O)[S+](C)[O-]", [2, 5]],
    ["C1=CC=C2NN=NC2=C1", [4]],
    ["C1=NC=NC2=C1C=NN2", [0, 8]],
    ["C1CCCNCCC1", [4]],
    ["C1=[N+]CCC1", [1]],
    ["C1=CNC2=NC=NN2C1", [0, 1, 5, 8]],
    ["C1=NON=C1", [0, 4]],
    ["O=C1CSC2=CC=CC=C2N1", [2, 7]],
    ["CC(C)N", [0, 2]],
    ["O=CCC[SH](=O)=O", [1, 4]],
    ["O=CC(F)(F)F", [1]],
    ["C=NNC(=O)C=O", [0, 5]],
    ["CC(O)CO", [0]],
    ["C=C[SH](=O)=O", [0, 2]],
    ["O=CCO", [1, 2]],
    ["C1CSCCO1", [0]],
    ["CC(C=O)[SH](=O)=O", [2, 4]],
    ["CC#CC", [0, 3]],
    ["C[S+]([O-])CC=O", [0, 4]],
    ["CC(C)CC(C)O", [0]],
    ["CS(=O)(=O)CC=O", [0, 5]],
    ["C1CC2CNCC1CN2", [8, 4]],
    ["C1CCC2(CCOCC2)OC1", [1]],
    ["O=S1(=O)CCCN1", [6]],
    ["C1=CC=C2C(=C1)NC1=C2CCNC1", [11, 12]],
    ["C1=CC=C2OCCNC2=C1", [5, 7]],
    ["O=C1NCNC2=CC=CC=C12", [2, 3]],
    ["O=C1CCC=NN1", [4, 6]],
    ["C1CNC2CCCC2C1", [2]],
    ["C1=CC2=C(N=C1)NC=C2", [8, 1]],
    ["C1=CC=C2C(=C1)CCC21CC1", [9]],
    ["C1=CC2=C(CNCC2)S1", [0, 1, 5]],
    ["C1=CN=C2CCCCC2=C1", [4]],
    ["O=C1NC(=O)C2C3C=CC(C3)C12", [2]],
    ["O=C1NCCCC12CCNC2", [9, 2]],
    ["C1CCC2(CC1)CCCCO2", [7]],
    ["C1=CC2=C(NN=C2)S1", [0, 4, 6]],
    ["O=C1NCC2=C1OC1=CC=CC=C1C2=O", [2, 10, 3]],
    ["C1=NN=C2CCCCN12", [0, 4]],
    ["C#CCO", [0]],
    ["C1=NNC2=C1N=CN2", [0, 2, 6, 7]],
    ["C1=CC2=NC=CN=C2C=C1", [5]],
    ["O=S1(=O)N=CC2=CC=CC=C21", [4]],
    ["C1=CC2=C(C=C1)C1C=CCC1CN2", [1, 11]],
    ["CCC(C)CC=O", [4, 5]],
    ["CC(C=O)S(C)(=O)=O", [2, 5]],
    ["C1CCC2(CCSCC2)OC1", [1]],
    ["O=CCCl", [1]],
    ["CCC(C)(C)O", [0]],
    ["O=C1NN=NC2=CC=CC=C12", [2]],
    ["C1=NC=C2C=NNC2=N1", [0, 2, 6]],
    ["C1=NN=CC1", [0, 4]],
    ["C1CCC2OCCNC2C1", [7]],
    ["C1=CN=C2CCCC2=C1", [4]],
    ["CCCN", [0]],
    ["C1=CN=C2ON=CC2=C1", [8, 1, 6]],
    ["C1=CC2CCC1C2", [3]],
    ["C1CCC2CNCC2C1", [5]],
    ["O=C1CCC2SCCN12", [4, 7]],
    ["C1=CC2=C(C=C1)OC=C2", [4, 7]],
    ["CC(C)(C)S(C)(=O)=O", [0]],
    ["O=C1NC(=O)C(=O)N1", [2, 7]],
    ["O=C1CNC2=CC=CC=C2N1", [3]],
    ["O=C1NC(=O)C2CCCCC12", [2]],
    ["C1=CC2=CN=CN2C=C1", [3, 5]],
    ["C1=CC2=C(C=C1)NN=C2", [4]],
    ["O=C1CCCC1", [2]],
    ["C1=CC2=NCN=C2C=C1", [4]],
    ["C1CCN2CCCC2C1", [6]],
    ["C1=CC=C2OCOCC2=C1", [0, 2]],
    ["C1=CC=C2SCCCC2=C1", [0, 7]],
    ["O=C1NN=C2C=CC=CN12", [2]],
    ["O=C1C=CC2=C(C=CC=C2)O1", [8, 3, 7]],
    ["O=S1(=O)C=CCC1", [5]],
    ["O=C1C=CN=C2SC=CN12", [3]],
    ["C1=CCC2CNCC2C1", [5]],
    ["C1=CC2=C(C=C1)SC=N2", [1, 7]],
    ["C1=CCN=C1", [0, 1, 2, 4]],
    ["C1=CC2=CN=CN=C2C=C1", [3, 5]],
    ["CCC(C)CO", [1]],
    ["CCC(C)(N)C=O", [5]],
    ["CC=NNC(C)=O", [1, 5]],
    ["C#CCN", [0]],
    ["C1=NN=C2CCNCCN12", [0, 6]],
    ["CC(N)(C=O)C(F)(F)F", [3]],
    ["C1CC2CCC1O2", [1]],
    ["CC(C)CO", [0]],
    ["CCCS(=O)(=O)CC", [1]],
    ["O=C1NC(=O)C2CC=CCC12", [2]],
    ["C1=CN2CCNCC2=C1", [5, 6]],
    ["O=C1CCC2=C(NN=C2)N1", [8, 3, 6]],
    ["CCN=C(N)N", [4, 5]],
    ["C1=CC2=C(N=CN=C2)S1", [7]],
    ["C1=NC2=C(CCC2)S1", [0]],
    ["C1=CC2=C(CCC2)S1", [0, 1]],
    ["O=S1(=O)CCCCC1", [5]],
    ["CN=CN", [2, 3]],
    ["CC(C)[SH](=O)=O", [3]],
    ["O=C1NCC23C=CC(CC12)O3", [8, 2]],
    ["O=C1NCC2=C1NN=C2", [8, 2, 3]],
    ["CC(C(=O)O)C(F)(F)F", [1]],
    ["O=C1CCC2(CCNCC2)CN1", [11, 7]],
    ["CCCC(C)CC", [1]],
    ["CC(C)(C)CN", [0]],
    ["O=CNN[SH](=O)=O", [1, 4]],
    ["O=C1C=COC2=CC=CC=C12", [3]],
    ["CCC(C)CCO", [3]],
    ["O=C1CCC2(CCCNC2)CN1", [8, 11]],
    ["CC(O)CC(C)(C)C", [5]],
    ["O=[SH](=O)C(F)F", [1]],
    ["C1=CC=C2NCCNCC2=C1", [4, 6, 7]],
    ["C1=NNN=C1", [0, 2]],
    ["CC(=O)NN", [0, 4]],
    ["C1=NN=C2CNCCN12", [0, 5]],
    ["O=S1(=O)CCNCC1", [5]],
    ["CCC(C=O)CC", [3]],
    ["CC(O)CCC=O", [5]],
    ["S=C1NC=CCN1", [3, 4, 5]],
    ["O=C1CCCCC1", [2]],
    ["O=C1CSC=N1", [2, 4]],
    ["NCCCC=O", [2, 4]],
    ["C1=CC=C2CSCCC2=C1", [4]],
    ["C1=CC2=C(C=C1)OCCC2", [8, 4]],
    ["CC(C)CC(=O)O", [3]],
    ["CCC(C)CC", [1]],
    ["C=NO", [0, 2]],
    ["C#CCCO", [0]],
    ["CCS(=O)(=O)CC", [0]],
    ["C1=CC2=C(CCSC2)S1", [7]],
    ["CC(C)CC#N", [3]],
    ["O=C1NC(=O)C2(CCCC2)N1", [2]],
    ["O=CCCC(=O)O", [1]],
    ["CCCCC(C)C", [1]],
    ["C1=CC2=CC=NC=C2C=C1", [1]],
    ["CN(C)[SH](=O)=O", [3]],
    ["O=CN=C1NC2=CC=CC=C2S1", [8, 1, 4]],
    ["C1=CC2=NC=NN2C=C1", [8, 4]],
    ["C1COCO1", [3]],
    ["CBr", [0]],
    ["C1=CN2C=CN=C2N=C1", [4]],
    ["O=C1CCNC2=CC=CC=C2N1", [3, 4]],
    ["CC(=O)NNC(C)=O", [0, 6]],
    ["C1=NNC2=C1CCC2", [0, 2]],
    ["CCCCCC", [0]],
    ["O=C1NCC2CNCCN12", [6]],
    ["O=C1CSCN1", [4, 5]],
    ["O=C1CCC2C(=O)N=CN=C2N1", [8, 3]],
    ["N=N", [0, 1]],
    ["C1=CC2=C(C=C1)NC=N2", [0, 5, 6]],
    ["CCCC[SH](=O)=O", [4]],
    ["N=CN", [1]],
    ["O=CCCC(F)(F)F", [1]],
    ["C1=CC2=NC3CNCCC3=C2C=C1", [5, 6]],
    ["C1=NC=NC2=C1N=CN2", [0]],
    ["C1=NC=C2CNCCC2=N1", [0, 5]],
    ["C1CC2(C1)CCC2", [1, 3]],
    ["O=CCl", [1]],
    ["O=C1NC=CS1", [2, 3]],
    ["C1=NN2CCCNC2=C1", [0, 3, 5]],
    ["C1=CN=CC1", [0, 1, 3, 4]],
    ["C1=CC=C2ON=CC2=C1", [6]],
    ["O=C1NC=NC2=C1C=NN2", [9, 2]],
    ["CC(CCl)C[SH](=O)=O", [5]],
    ["C1=CN=C2N=CN=CC2=C1", [1, 7]],
    ["C1=CC2=C(C=C1)CCCC2", [1, 6, 7]],
    ["C1=NC2=C(CNCC2)N1", [6]],
    ["CCN=CN", [3, 4]],
    ["C1CC2CCC(C1)N2", [0, 7]],
    ["O=C1OCC2=CC=CC=C12", [3]],
    ["O=C1OCCC2=CC=CC=C12", [3]],
    ["CC(C)C(C)(C)O", [4]],
    ["O=C1NC(=O)C2=C(C=CS2)N1", [2, 10]],
    ["C=NNC(=O)CC", [0, 5]],
    ["C=C", [0]],
    ["O=C1CCCC(=O)N1", [3, 4]],
    ["C1CCC2CC2C1", [4]],
    ["CCC(C)=O", [1]],
    ["C1CNC2CCNCC2C1", [2, 6]],
    ["C1=CC=C2CCC2=C1", [4]],
    ["O=C1NC2=NN=CN2C2=CC=CC=C12", [2, 6]],
    ["O=C1NN=C2CNCCN12", [2, 6]],
    ["C1=NN2CCCNCC2=C1", [0, 6]],
    ["C1CCN2CC3CNCC3C2C1", [7]],
    ["C1CC2CCCC(C1)N2", [0, 8]],
    ["C1=COC2=C(C=NN2)C1", [0, 1, 5, 8]],
    ["O=C1CCC2=C(N=CNC2=O)N1", [3, 7]],
    ["S=C1N=NCN1", [4, 5]],
    ["CCCC(C)C=O", [5]],
    ["O=C1C=CNN=C1", [3, 4, 6]],
    ["N=C1NC(=O)CCS1", [0, 2, 6]],
    ["O=C1NCCC2=CC=CC=C12", [2, 3, 4]],
    ["C1=CC=C2N=C3NC=CC3=NC2=C1", [8, 6, 7]],
    ["N=C1NC(=O)CS1", [0, 2, 5]],
    ["C1=CC2=NSN=C2C=C1", [1]],
    ["C1=CC2=NN=NN2N=C1", [8]],
    ["O=C1NN=CO1", [2, 4]],
    ["O=C1NS(=O)(=O)C2=CC=CC=C12", [2]],
    ["C1CC[S+]CC1", [0, 3]],
    ["CC=NN", [1, 3]],
    ["CC[S+](C)[O-]", [1, 3]],
    ["C1CNCC2(C1)CCNC2", [8, 2]],
    ["O=C1NC(=O)C2=C(N=C3NC=CN32)N1", [9, 10, 2, 13]],
    ["C=CCCC", [4]],
    ["CCC(CC)C(=O)O", [2]],
    ["CC(C)CC(C=O)CN", [5]],
    ["CCC(C)N", [3]],
    ["O=C1NCC(=O)N2CCCC12", [2, 3]],
    ["C1=NNCN1", [0, 3, 4]],
    ["O=C1NCCCO1", [2]],
]
