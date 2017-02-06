# -*- coding: utf-8 -*-
"""
Updated February 6th, most recent version
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
    """ Returns complement nucleotide, string"""
    n = nucleotide
    if n == 'T':
        return 'A'
    if n == 'A':
        return 'T'
    if n == 'C':
        return 'G'
    if n == 'G':
        return 'C'


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

# get_reverse_complement('ATGATAT')


def rest_of_ORF(dna):
    # stop codos = 'TGA', 'TAG' or 'TAA'
    # neworf = []
    # count = 0
    i = 3
    while i < len(dna):
        if dna[i:i+3] == 'TGA' or dna[i:i+3] == 'TAG' or dna[i:i+3] == 'TAA':
            # neworf.append(dna[:i])
            return dna[:i]
        else:
            i = i + 3
    return dna
    # if count == 0:
    #     neworf.append(dna[:])
    # return(neworf)
    #


# rest_of_ORF('ATGCGAATGTAGCATCAAA')


def find_all_ORFs_oneframe(dna):
    # start = dna.find('ATG')
    # print(stop1)
    oneframe = []
    n = 0
    while n < len(dna):
        if dna[n: n + 3] == 'ATG':
            stop1 = rest_of_ORF(dna[n:])
            oneframe.append(stop1)
            n = n + len(stop1)
        else:
            n = n + 3
    return oneframe

# shift + enter runs highlighted


# find_all_ORFs_oneframe("ATGCCCTAGCCCATGCAG")


def find_all_ORFs(dna):
        allORF = []
        a = find_all_ORFs_oneframe(dna[0:])
        # returns: a list of non-nested ORFs
        b = find_all_ORFs_oneframe(dna[1:])
        c = find_all_ORFs_oneframe(dna[2:])
        allORF.extend(a)
        allORF.extend(b)
        allORF.extend(c)
        return allORF


# find_all_ORFs('ATGCGAATGTAGCATATGCAA')


def find_all_ORFs_both_strands(dna):
    """
    >>> find_all_ORFs_both_strands("ATGCGAATGTAGCATCAAA")
    ['ATGCGAATG', 'ATGCTACATTCGCAT']
    """
    # returns list of all orfs
    blank_list = []
    reverse_dna = get_reverse_complement(dna)
    blank_list.extend(find_all_ORFs(dna))
    blank_list.extend(find_all_ORFs(reverse_dna))
    return blank_list


# find_all_ORFs_both_strands("ATGCGAATGTAGCATCAAA")

# stop here for week 1!!


def longest_ORF(dna):
    """
    >>> longest_ORF("ATGCGAATGTAGCATCAAA")
    'ATGCTACATTCGCAT'
    """
    # returns string of longest reading frame
    currentmax = ''
    new_list = find_all_ORFs_both_strands(dna)
    # print("NEW LIST:")
    # print(new_list)
    for i in range(len(new_list)):
        if len(new_list[i]) > len(new_list[0]):
            currentmax = new_list[i]
    return currentmax


# longest_ORF("ATGCGAATGTAGCATCAAA")

def longest_ORF_noncoding(dna, num_trials):
    # returns int length of longest reading frame
    list_values = []
    val = 0
    for i in range(num_trials):
        newdna = shuffle_string(dna)
        longest = longest_ORF(newdna)
        if len(longest) > val:
            val = len(longest)
            list_values.append(val)
    # print(list_values)
    return val


# longest_ORF_noncoding("ATGCGAATGTAGCATCAAA", 300)


def coding_strand_to_AA(dna):
        """
        >>> coding_strand_to_AA("ATGCGA")
        'MR'
        >>> coding_strand_to_AA("ATGCCCGCTTT")
        'MPA'
        """
    # converts dna strand into codons and makes list of amino acids
        aminoacids = ''
        codon = ''
        for letter in dna:
            codon += letter
            if len(codon) == 3:
                aminoacids += aa_table[codon]
                codon = ''
        return aminoacids


def gene_finder(dna):
    amino_seq = []
    threshold = longest_ORF_noncoding(dna, 1500)
    print(threshold)
    allorfs = find_all_ORFs_both_strands(dna)
    length = len(allorfs)
    # print(length)
    for i in range(length):
        # print(len(allorfs[i]))
        if len(allorfs[i]) > threshold:
            codon_seq = coding_strand_to_AA(allorfs[i])
            amino_seq.append(codon_seq)
    return amino_seq


dna = load_seq("./data/X73525.fa")
gene_finder(dna)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
