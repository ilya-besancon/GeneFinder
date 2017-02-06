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
        else:
            n = n + 3
    return oneframe

# shift + enter runs highlighted


find_all_ORFs_oneframe("ATGCCCTAG")


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


def find_all_ORFs_both_strands(dna):
    # returns list of all orfs
    blank_list = []
    new_list = []
    reverse_dna = get_reverse_complement(dna)
    blank_list.extend(find_all_ORFs(dna))
    blank_list.extend(find_all_ORFs(reverse_dna))
    for i in blank_list:
        new_list += i
    return new_list


find_all_ORFs_both_strands("ATGCGAATGTAGCATCAAA")

# stop here for week 1!!


def longest_ORF(dna):
    # returns string of longest reading frame
    currentmax = ''
    new_list = find_all_ORFs_both_strands(dna)
    for i in range(len(new_list)):
        if len(new_list[i]) > len(new_list[0]):
            currentmax = new_list[i]
    return currentmax


longest_ORF("ATGCGAATGTAGCATCAAA")


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
    return val


longest_ORF_noncoding("ATGCGAATGTAGCATCAAA", 30)


def coding_strand_to_AA(dna):
    # converts dna strand into codons and makes list of amino acids
        aminoacids = ''
        codon = ''
        for letter in dna:
            codon += letter
            if len(codon) == 3:
                aminoacids += aa_table[codon]
                codon = ''
        return aminoacids


coding_strand_to_AA("ATGCCCGCTTT")


def gene_finder(dna):
    codon_seq = ''
    threshold = longest_ORF_noncoding(dna, 300)
    print(threshold)
    allorfs = find_all_ORFs_both_strands(dna)
    length = len(allorfs)
    print(length)
    for i in range(length):
        print(len(allorfs[i]))
        if len(allorfs[i]) > threshold:
            codon_seq += allorfs[i]
    amino_seq = coding_strand_to_AA(codon_seq)
    return amino_seq


""" Having some issues implimenting this last section. My threshold comes
out to be some huge number 6000+ and so I'm guessing that it
isn't parsing correctly. As a result, my amino acid sequence
contains both very short and very long strings.
"""

dna = load_seq("./data/X73525.fa")
gene_finder(dna)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
