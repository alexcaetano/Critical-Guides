###########################################################################################
###
### As before except:
###
### Initialise a string variable Protein_Sequence to receive the aa codes
###
### Append aa codes to Protein_Sequence rather than printing them.
### Append the '.'s to indicate spare bases rather than printing them.
###
### return Protein_Sequence when done ... and so becomes a function.
###
###########################################################################################

# A tuple of all Legal Codons. 
Legal_Codons = (
     "UUU", "UUC", "UUA", "UUG", "UCU", "UCC", "UCA", "UCG",
     "UAU", "UAC", "UAA", "UAG", "UGU", "UGC", "UGA", "UGG",
     "CUU", "CUC", "CUA", "CUG", "CCU", "CCC", "CCA", "CCG",
     "CAU", "CAC", "CAA", "CAG", "CGU", "CGC", "CGA", "CGG",
     "AUU", "AUC", "AUA", "AUG", "ACU", "ACC", "ACA", "ACG",
     "AAU", "AAC", "AAA", "AAG", "AGU", "AGC", "AGA", "AGG",
     "GUU", "GUC", "GUA", "GUG", "GCU", "GCC", "GCA", "GCG",
     "GAU", "GAC", "GAA", "GAG", "GGU", "GGC", "GGA", "GGG");

# A Dictionary to assosiate Codons with Amino Acid Codes. 
Gencode = { "UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
            "UCU":"S", "UCC":"s", "UCA":"S", "UCG":"S",
            "UAU":"Y", "UAC":"Y", "UAA":"*", "UAG":"*",
            "UGU":"C", "UGC":"C", "UGA":"*", "UGG":"W",
            "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
            "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
            "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
            "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
            "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
            "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
            "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
            "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
            "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
            "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
            "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
            "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G",}

def rnatoaa(rna):       # A Fnction to turn RNA into Protein. 

    # First check for impossible Bases, Issue a Warning if found and continue
    if not rna.isalpha():
        print "Warning - This Sequence contains non-alpha Charaters?!";

    RNA=rna.upper();              # All Upper Case, as Dictionary expects. 
    RNA=RNA.replace("T","U");     # All "T"s "U"s, as Dictionary expects. 

    RNA_Length = len(RNA);        # Compute the Length of the Sequence. 
    Codon_Count = RNA_Length / 3; # Compute the Number of Codons. 
    Spare_Bases = RNA_Length % 3; # Compute the Number of Bases left over. 
    CDS_Length = RNA_Length - Spare_Bases;
                                  # Compute the Length of the Coding Sequence. 

    Protein_Sequence = "";   # Initialise a string variable to receive aa codes.

    for Codon_Start in range( 0, CDS_Length, 3):       # Along the CDS, 
        Next_Codon = RNA[Codon_Start:Codon_Start + 3]; # pick the Codon. 
        if Next_Codon in Legal_Codons:                 # If the codon is good, 
           Protein_Sequence += Gencode[Next_Codon];    # Add its corresponding aa code. 
        else:                                          # Otherwise, 
           Protein_Sequence += "?";                    # Add a query. 

    for Extra_Bases in range(Spare_Bases): # Add "."s to indicate 
        Protein_Sequence += ".";           # Spare_Bases. 

    return Protein_Sequence; # Done! Print a Newline to celebrate. 

#TEST BED
#========

Sequences = ("AGCGACTCGATGCATGACGCACGCGATATCGAGCTATAG", # All Good 
             "AGCGACTCGGACGCACGCGATATCGAGCTATAGGA",     # 2 extra Bases 
             "gcgCGCCGCAGCCCCCCccccccGGTGTAGACTGCA",    # Some Lower Case 
             "gcgCGCCGCAGCCCCC123CCCCGGTGTAGACTGCA",    # Some Numeric 
             "acagggtcgcgcGCATTTCHchshahGGACTACTTTAS"); # Some illegal BP codes 

for Sequence in Sequences:
    print rnatoaa(Sequence);

print; print;

print Legal_Codons[14];

print Gencode["AUG"];
