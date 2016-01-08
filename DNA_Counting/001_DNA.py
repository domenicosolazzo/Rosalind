#!/user/bin/env python
'''
Solution to the ROSALIND bioinformatics problem.

Title: Counting DNA Nucleotides
Rosalind ID: DNA
Rosalind #: 001
URL: http://rosalind.info/problems/dna/
'''

from collections import Counter

def base_count(dna):
    '''Returns the count of each base appearing in the given DNA sequence.'''
    base_count = Counter(dna)
    return [base_count[base] for base in 'ACGT']

def main():
    '''Runs and saves the results'''
    # Read the input
    with open('data/dna_input.txt') as input_data:
        dna = input_data.read().strip()

        # Get the count of each base appearing in the DNA sequence
        count = map(str, base_count(dna))

        # Print and save the answer
        print ' '.join(count)
        with open('output/p_001_DNA.txt', 'w') as output:
            output.write(' '.join(count))

if __name__ == '__main__':
    main()
