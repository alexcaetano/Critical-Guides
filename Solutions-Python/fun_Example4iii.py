###########################################################################################
###
### As for Part(ii) except:
###
### A check is required to ensure the value of the Reading Frame Parameter is in range 
###
### The Length of the RNA sequence must be adjusted to reflect ignored bases frm the front,
### due to Reading Frame selections other than 1.
###
### Prepend '.'s to indicate bases ignored due to Reading Frame selections other than 1.
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

def rnatoaa(rna, Reading_Frame = 1):       # A Fnction to turn RNA into Protein.

    # Check for impossible Reading Frame, Issue a Warning if found and continue
    Reading_Frame = int(float(Reading_Frame));
    if Reading_Frame not in range(1,4):
        print "Warning - Reading_Frame out of range! Assuming Reading Frame 1.";
        Reading_Frame = 1;

    Reading_Frame_Increment = Reading_Frame - 1;  # Increment must be in range 0 -> 2 

    # Check for impossible Bases, Issue a Warning if found and continue
    if not rna.isalpha():
        print "Warning - This Sequence contains non-alpha Charaters?!";

    RNA=rna.upper();              # All Upper Case, as Dictionary expects. 
    RNA=RNA.replace("T","U");     # All "T"s "U"s, as Dictionary expects. 

    RNA_Length = len(RNA) - Reading_Frame_Increment;
                                  # Compute the Length of the Sequence. 
    Codon_Count = RNA_Length / 3; # Compute the Number of Codons. 
    Spare_Bases = RNA_Length % 3; # Compute the Number of Bases left over. 
    CDS_Length = RNA_Length - Spare_Bases;
                                  # Compute the Length of the Coding Sequence. 

    Protein_Sequence = "";   # Initialise a string variable to receive aa codes.

    for Codon_Start in range(Reading_Frame_Increment, CDS_Length, 3):
                                                       # Along the CDS, 
        Next_Codon = RNA[Codon_Start:Codon_Start + 3]; # pick the Codon. 
        if Next_Codon in Legal_Codons:                 # If the codon is good, 
           Protein_Sequence += Gencode[Next_Codon];    # Add its corresponding aa code. 
        else:                                          # Otherwise, 
           Protein_Sequence += "?";                    # Add a query. 

    for Extra_Bases in range(Reading_Frame_Increment): # Add "."s to front 
        Protein_Sequence = "." + Protein_Sequence;     #  to indicate Reading Frame. 

    for Extra_Bases in range(Spare_Bases): # Add "."s to end 
        Protein_Sequence += ".";           # to indicate Spare_Bases. 

    return Protein_Sequence; # Done! Print a Newline to celebrate. 

#TEST BED
#========

Sequences = ("AGCGACTCGATGCATGACGCACGCGATATCGAGCTATAG", # All Good 
             "AGCGACTCGGACGCACGCGATATCGAGCTATAGGA",     # 2 extra Bases 
             "gcgCGCCGCAGCCCCCCccccccGGTGTAGACTGCA",    # Some Lower Case 
             "gcgCGCCGCAGCCCCC123CCCCGGTGTAGACTGCA",    # Some Numeric 
             "acagggtcgcgcGCATTTCHchshahGGACTACTTTAS"); # Some illegal BP codes 

print "Reading_Frame parameter ommitted";
for Sequence in Sequences:
    print rnatoaa(Sequence);
print;


for Reading_Frame in range(5):
    print "Reading_Frame parameter set " + str(Reading_Frame);
    print;
    print rnatoaa(Sequence,Reading_Frame)
    for Sequence in Sequences:
       print rnatoaa(Sequence,Reading_Frame);
    print;

print "Reading Frame set to a float? 2.9";
print rnatoaa(Sequence,2.9);
print "Reading Frame set to a string? 2.9";
print rnatoaa(Sequence,"2.9");

print Legal_Codons[14];

print Gencode["AUG"];
