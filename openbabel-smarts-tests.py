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
                    required=False,
                    help='input pefix')

args = parser.parse_args()
prefix = args.prefix


###### from PDB

smarts_pattern_to_test = '[!$([#1,#6,F,Cl,Br,I,o,s,nX3,#7v5,#15v5,#16v4,#16v6,*+1,*+2,*+3])]'
smarts = pybel.Smarts(smarts_pattern_to_test)

mol = next(pybel.readfile("pdb", "GG.pdb"))

patternFound = smarts.findall(mol)

triggeredatomsList = [x[0] for x in patternFound]
print ("%s | %s:" % (prefix, triggeredatomsList) )
