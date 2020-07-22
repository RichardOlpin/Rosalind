"""
Problem
Assume that an alphabet 𝒜 has a predetermined order; that is, we write the alphabet as a
permutation 𝒜=(a1,a2,…,ak), where a1<a2<⋯<ak. For instance, the English alphabet is
organized as (A,B,…,Z).

Given two strings s and t having the same length n, we say that s precedes t in the
 lexicographic order (and write s<Lext) if the first symbol s[j] that doesn't match t[j]
 satisfies sj<tj in 𝒜.

Given: A collection of at most 10 symbols defining an ordered alphabet, and a positive
integer n (n≤10).

Return: All strings of length n that can be formed from the alphabet,
ordered lexicographically (use the standard order of symbols in the English alphabet).

"""
import itertools


def enumerate_kmers(letters, kmer_length):
    alphabet = [str(x) for x in letters.split()]
    kmers = sorted(list(itertools.product(alphabet, repeat=kmer_length)))
    return "\n".join(["".join(k) for k in kmers])

letters = ""
kmer_length = 2
print(enumerate_kmers())