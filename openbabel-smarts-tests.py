from openbabel import openbabel
from openbabel import pybel

import argparse
import pathlib

def mkdirp(location):
    sciezka = pathlib.Path(location)
    sciezka.mkdir(parents=True, exist_ok=True)


parser = argparse.ArgumentParser(description='out file prefix')
parser.add_argument('--prefix',
                    dest='prefix',
                    required=True,
                    help='input pefix')

args = parser.parse_args()
prefix = args.prefix


mkdirp("outputs")

##### FROM SMILES

# here provide the SMILES for the test molecule(s). If you don't have a better idea, leave as it is
testing_molecule = 'CC(C)(F)c1ccc(cc1)C[C@H](N)CC[NH3+].[H]O[C@@]1([H])[C@@]([H])(O[C@]([H])(C([H])([H])OP(O)([O-])=O)[C@@]1([H])O[H])n1c([H])nc2c1n([H])c(nc2=O)N([H])[H]'

smarts_pattern_to_test = '[!$([#1,#6,F,Cl,Br,I,o,s,nX3,#7v5,#15v5,#16v4,#16v6,*+1,*+2,*+3])]'
# smarts_pattern_to_test = '[#1;$([#1]-[C])]'


mol = pybel.readstring("smi",testing_molecule)

smarts = pybel.Smarts(smarts_pattern_to_test)

print (smarts.findall(mol))
