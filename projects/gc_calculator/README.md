# GC Content Calculator

## Introduction
This project is a Python-based utility designed to calculate the GC content of DNA sequences. 

GC content (the percentage of nitrogenous bases in a DNA molecule that are either Guanine or Cytosine) is a critical metric in genomics, 
as it influences the thermal stability of DNA and can be used to identify gene-rich regions of a genome.

## Scientific Context
In cancer research, particularly regarding Ovarian Cancer, analyzing GC content is vital for understanding genomic stability. 
This tool was tested using a sequence from the human BRCA1 gene, a well-known tumor suppressor gene. 
Mutations or stability issues in BRCA1 are heavily linked to increased risks of hereditary breast and ovarian cancer.

## Project Structure
gc_content_calculator.py: The core script containing the calculation logic and file-handling protocols.

dna_sequence.txt: A sample data file containing a partial sequence of the BRCA1 gene for testing and validation.

## Impact Statement
This tool demonstrates the transition from foundational Python scripting to the development of reproducible bioinformatics software. 
By automating the extraction of GC metrics from raw text files, it establishes a workflow for larger-scale genomic data processing required in clinical research roles.
