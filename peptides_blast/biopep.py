#! /usr/bin/python3.8

from Bio.Blast import NCBIWWW
from Bio import SeqIO
from Bio.PDB import *
import urllib
import wget
##########################################################
## Search for homologous structures (Protein Data Bank) ##
## from peptide sequences.                              ##
## by Lucas Sousa Palmeira.                             ##
##########################################################
class Peptide:
    def __init__(self, peptide):
        self.peptide = peptide

    def createfasta(self):
        with open(f'pep{self.peptide}.fasta', 'a') as writing:
            writing.write('>pep' + self.peptide + '\n')
            # >pepSFYGKV
            writing.write(self.peptide)
            # SFYGKV

    def createali(self):
        with open(f'pep{self.peptide}.ali', 'a') as writing:
            writing.write(f'>P1;pep{self.peptide}\n')
            # first line
            writing.write(f'sequence:pep{self.peptide}:::::::0.00: 0.00\n')
            # second line
            writing.write(self.peptide + '*')
            # third line

    def runblast(self):
       with open(f'pep{self.peptide}.log', 'w') as file:
           reading_fasta = SeqIO.read(f'pep{self.peptide}.fasta', format='fasta')
           print('Starting NCBIWWWW search...')
           result = NCBIWWW.qblast('blastp', 'pdb', reading_fasta.seq, format_type='Text')
           print(result.read(), file=file)
           print('Search completed.')

    def identity(self, percent):
        with open(f'pep{self.peptide}.log', 'r') as line:
            line_35 = line.readlines()[34]
            percent_sign = line_35.find('%')
            two_digits = percent_sign - 2
            three_digits = percent_sign - 3
            percent_x = line_35[two_digits:percent_sign]
            percent_z = line_35[three_digits:percent_sign]

        if percent_x == 'AM':
            print('No homologous sequence was found.')
        elif int(percent_x) >= int(percent):
            print(f'Identity = {str(percent_x)}%')
        elif percent_z == '100':
            print('Identity = 100%')

    def pdb(self):
        with open(f'pep{self.peptide}.log', 'r') as file:
            pdb = file.readlines()[34]
            code_pdb = pdb[0:4]
        try:
            link = 'https://files.rcsb.org/download/{}.pdb'.format(code_pdb)
            wget.download(link)
        except urllib.error.HTTPError:
            print('urllib.error.HTTPError: HTTP Error 404: Not Found.')