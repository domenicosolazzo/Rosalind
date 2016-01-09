#!/user/bin/env python
'''
Solution to the ROSALIND bioinformatics problem.

Title: Counting DNA Nucleotides
Rosalind ID: RNA
Rosalind #: 002
URL: http://rosalind.info/problems/rna/
'''

def translate_to_rna(dna):
    '''Translate the given DNA sequence to an RNA sequence'''
    return dna.replace('T', 'U')

def main():
    '''Run the script'''
    # Read the input
    with open('data/rosalind_rna.txt') as input_data:
        dna = input_data.read().strip()
        
    # Translate the DNA sequence to an RNA sequence
    rna = translate_to_rna(dna)

    # Print and save the answer
    print rna
    with open('output/002_RNA.txt', 'w') as output_data:
        output_data.write(rna)

if __name__ == '__main__':
    main()
