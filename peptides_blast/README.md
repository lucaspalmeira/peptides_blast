# Peptides Blast

> Lucas Palmeira: scientific initiation scholarship holder at the Laboratory of Bioinformatics and Computational Chemistry - UESB.

## Motivations

Necessary to the laboratory's needs and the research progress, it was necessary to create alternatives to accelerate and automate tasks, such as an explosion algorithm execution for a search of homologous sequences as well as the download of homologous structures deposited in the Protein Data Bank (https://www.rcsb.org/).

## Project description

The blastp algorithm is performed on the peptide sequences in order to find homologous structures deposited in the Protein Data Bank (https://www.rcsb.org/).

## Prerequisites

Installed biopython library:

Biopython (https://biopython.org/)

```bash
$ pip3 install biopython
```

Wget installed (https://pypi.org/project/wget/):

```bash
$ pip3 install wget
```
urllib (https://docs.python.org/pt-br/3/library/urllib.html)

```bash
$ pip3 install urlib
```

Python release version used in the project: 3.8

# Run

Running

```bash
$ python3 search.py 
```

or

```bash
$ chmod +x search.py
$ ./search.py
```