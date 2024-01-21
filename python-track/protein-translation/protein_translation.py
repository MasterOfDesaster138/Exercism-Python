"""Instructions
Translate RNA sequences into proteins.

RNA can be broken into three nucleotide sequences called codons, and then translated to a polypeptide like so:

RNA: "AUGUUUUCU" => translates to

Codons: "AUG", "UUU", "UCU" 
=> which become a polypeptide with the following sequence 
=> Protein: "Methionine", "Phenylalanine", "Serine"

There are 64 codons which in turn correspond to 20 amino acids; 
however, all of the codon sequences and resulting amino acids are not important in this exercise. 
If it works for one codon, the program should work for all of them. 
However, feel free to expand the list in the test suite to include them all.

There are also three terminating codons (also known as 'STOP' codons); 
if any of these codons are encountered (by the ribosome),
all translation ends and the protein is terminated.

All subsequent codons after are ignored, like this:
RNA: "AUGUUUUCUUAAAUG" => Codons: "AUG", "UUU", "UCU", "UAA", "AUG" => Protein: "Methionine", "Phenylalanine", "Serine"

Note the stop codon "UAA" terminates the translation and the final methionine is not translated into the protein sequence.
Below are the codons and resulting Amino Acids needed for the exercise.

Codon	            Protein
AUG	                Methionine
UUU, UUC	        Phenylalanine
UUA, UUG	        Leucine
UCU, UCC, UCA, UCG	Serine
UAU, UAC	        Tyrosine
UGU, UGC	        Cysteine
UGG	                Tryptophan
UAA, UAG, UGA	    STOP
"""
protein_to_codon = {
    "Methionine":       ["AUG"],
    "Phenylalanine":    ["UUU", "UUC"],
    "Leucine":          ["UUA", "UUG"],
    "Serine":           ["UCU", "UCC", "UCA", "UCG"],
    "Tyrosine":         ["UAU", "UAC"],
    "Cysteine":         ["UGU", "UGC"],
    "Tryptophan":       ["UGG"],
    "STOP":             ["UAA", "UAG", "UGA"]
}


def proteins(strand: str):    
    # Find all proteins in sequences_list based on the codons
    polypeptide: list[str] = []
    protein_sequences = parse_strand(strand)

    # Check if the sequence matches any codon
    for codon in protein_sequences:
        for key, value in protein_to_codon.items():
            if codon in value:
                # Stop parsing if a STOP-codon appears
                if key == "STOP":
                    return polypeptide
                else:
                    polypeptide.append(key)
                    break
    return polypeptide
    
    
def parse_strand(strand: str) -> list[str]:
    """Parse strand into sequences with a length of 3 chars"""
    protein_sequences = []
    
    for i in range(0, len(strand), 3):
        protein_sequences.append(strand[i:i+3])

    return protein_sequences


if __name__ == "__main__":
    proteins("AUG")