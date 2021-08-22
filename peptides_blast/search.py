#! /usr/bin/python3.8

from biopep import Peptide

peptides = ['GSVVIVGRIVLSGKPA', 'GDFEEIPEEYL', 'CGGVQAEEQKLISEEDLLRKRREQLKHKLEQL', 'ADCGLRPLFEKKSLEDKTERELLESYI']
for seq in peptides:
    pep = Peptide(seq)
    pep.createfasta()
    pep.createali()
    pep.runblast()
    pep.identity(70)
    pep.pdb()