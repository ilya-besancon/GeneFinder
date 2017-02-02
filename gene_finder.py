# -*- coding: utf-8 -*-
"""
This has been a very interesting learning experience.
Who knew that strings could be manipulated in so many ways!
And all in the name of Science...

@author: Ilya Besancon

"""

import random
from amino_acids import aa, codons, aa_table   # you may find these useful
from load import load_seq


def shuffle_string(s):
    """Shuffles the characters in the input string
        NOTE: this is a helper function, you do not
        have to modify this in any way """
    return ''.join(random.sample(s, len(s)))

# YOU WILL START YOUR IMPLEMENTATION FROM HERE DOWN ###


def get_complement(nucleotide):
    n = nucleotide
    if n == 'T':
        return 'A'
    if n == 'A':
        return 'T'
    if n == 'C':
        return 'G'
    if n == 'G':
        return 'C'
    # TODO: implement this
    pass


def get_reverse_complement(dna):
        w = dna
        blank = ''
        l = len(w)
        ind = -1
        while 0 < (l + ind + 1):
            letter = w[ind]
            letter = get_complement(letter)
            blank = blank + letter
            neg = -1
            ind = ind + neg
        return blank
        # TODO: implement this
        pass


# get_reverse_complement('ATATAT')


def rest_of_ORF(dna):
    # stop codos = 'TGA', 'TAG' or 'TAA'
    neworf = []
    count = 0
    i = 3
    while i < len(dna):
        if dna[i:i+3] == 'TGA' or dna[i:i+3] == 'TAG' or dna[i:i+3] == 'TAA':
            neworf.append(dna[:i])
            i = i + 3
            count += 1
        else:
            i = i + 3
    if count == 0:
        neworf.append(dna[:])
    return(neworf)


rest_of_ORF('ATGCCCTGA')


def find_all_ORFs_oneframe(dna):
    # start = dna.find('ATG')
    # print(stop1)
    oneframe = []
    n = 0
    while n < len(dna):
        if dna[n: n + 3] == 'ATG':
            stop1 = rest_of_ORF(dna[n:])
            oneframe.append(stop1)
            n = n + len(stop1[-1])
            print(n)
        else:
            n = n + 3
            print(n)
    return oneframe

# shift + enter runs highlighted


find_all_ORFs_oneframe("ATGCCCTAG")


def find_all_ORFs(dna):
        allORF = []
        a = find_all_ORFs_oneframe(dna[0:])
        # returns: a list of non-nested ORFs
        b = find_all_ORFs_oneframe(dna[1:])
        c = find_all_ORFs_oneframe(dna[2:])
        allORF.extend([a, b, c])
        return allORF


def find_all_ORFs_both_strands(dna):
    blank_list = []
    reverse_dna = get_reverse_complement(dna)
    blank_list.extend(find_all_ORFs(dna))
    blank_list.extend(find_all_ORFs(reverse_dna))
    return blank_list


find_all_ORFs_both_strands("ATGCGAATGTAGCATCAAA")


# stop here for week 1!!


def longest_ORF(dna):
    """ Finds the longest ORF on both strands of the specified DNA and returns it
        as a string
    >>> longest_ORF("ATGCGAATGTAGCATCAAA")
    'ATGCTACATTCGCAT'
    """
    # TODO: implement this
    pass


def longest_ORF_noncoding(dna, num_trials):
    """ Computes the maximum length of the longest ORF over num_trials shuffles
        of the specfied DNA sequence

        dna: a DNA sequence
        num_trials: the number of random shuffles
        returns: the maximum length longest ORF """
    # TODO: implement this
    pass


def coding_strand_to_AA(dna):
    """ Computes the Protein encoded by a sequence of DNA.  This function
        does not check for start and stop codons (it assumes that the input        DNA sequence represents an protein coding region).

        dna: a DNA sequence represented as a string
        returns: a string containing the sequence of amino acids encoded by the
                 the input DNA fragment

        >>> coding_strand_to_AA("ATGCGA")
        'MR'
        >>> coding_strand_to_AA("ATGCCCGCTTT")
        'MPA'
    """
    # TODO: implement this
    pass


def gene_finder(dna):
    """ Returns the amino acid sequences that are likely coded by the specified dna

        dna: a DNA sequence
        returns: a list of all amino acid sequences coded by the sequence dna.
    """
    # TODO: implement this
    pass


if __name__ == "__main__":
    import doctest
    doctest.testmod()
