"""
Program Name: gc_content_calculator.py
Author: Garland Moran
Date: 2026-05-15

Description:
This program calculates GC content of a DNA sequence to help identify stable genomic regions.  

Pseudocode:
1. Define calculate_gc_content function:
    a. Count the 'G' nucleotides and store in g_count variable.
    b. Count the 'C' nucleotides and store in c_count variable.
    c. Calculate total sequence length using len() and store in total_legnth variable.
    d. Calculate the GC Content:
        i. If total sequence length = 0, return 0.
        ii. If total sequence length does not = 0, combine G and C counts, divide by total length, and mutliply by 100. 
        iii. Return results.
"""

def calculate_gc_content(sequence): 
    """Function that counts the G and C nucleotides and calculates the 
    GC Content of the opened sequence."""

    # Count the G and C nucelootides in the open sequence
    g_count = sequence.count('G')
    c_count = sequence.count('C')

    # Calculate total length of sequence
    total_length = len(sequence)

    # Calculate the average to determine GC Content
    if total_length == 0:
        return 0, 0, 0.0
    
    return g_count, c_count, (g_count + c_count) / total_length * 100

def main():
    """Main test function."""

    # Open the file
    with open('dna_sequence.txt', 'r') as file:
        dna_string = file.read().strip().upper() # Read file, remove whitespaces and newline characters, and covert to uppcase

    # Run calculate_gc_content function and store it in result variable
    g, c, result = calculate_gc_content(dna_string)

    # Display results
    print('GC Content Report:')
    print(f'Total Sequence Length: {len(dna_string)}') 
    print(f'Total G count: {g}')
    print(f'Total C count: {c}')
    print(f'GC Content: {result:.2f}%') # GC Content rounded to 2 decimal places

if __name__ == '__main__':
    main()
