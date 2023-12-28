def get_length(dna):
    return len(dna)
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """


def is_longer(dna1, dna2):
    if len(dna1) < len(dna2):
        return False
    elif len(dna1)== len(dna2):
        return False
    else:
        return True
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """


def count_nucleotides(dna, nucleotide):
    count=0
    for char in dna:
        if char == nucleotide :
            count=count+1
    return count
        
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """


def contains_sequence(dna1, dna2):
    return (dna2 in dna1)
    

    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """
def is_valid_sequence(dna):
    count=0
    for char in dna:
        if char not in "A,C,T,G":
            count = count+1
    if count > 0:
        return False
    else:
        return True
    """  (str) -> bool
    Return True if and only if the given DNA sequence contain A,T,G or C. (must be all capital)
    
    >>> is_valid('ACCTG')
    True
    >>> is_valid('ACDtG')
    False
    >>>is_valid('AE1FD')
    False
    
    """
def insert_sequence(sq1,sq2,index):
    
    return sq1[:index] + sq2 + sq1[index:]

    """  (str, str, int) -> str
    Return the DNA sequence obtained by inserting the second DNA sequence into the first DNA sequence at the given index
    >>>insert_sequence('CCGG','AT',2)
    CCATGG
    >>>insert_sequence('TAT','G',2)
    TAGT
    """
def get_complement(nuckleotide):
    result=""
    if nuckleotide == 'A':
        result = 'T'  
    elif nuckleotide == 'C':
        result = 'G'
    elif nuckleotide == 'T':
        result = 'A'
    else:
        result = 'C'
    return result
        

    """  (str) -> str
    Return the nucleotide's complement.
    >>>get_complement('A')
    T
    >>>get_complement('C')
    G
    """

def get_complementary_sequence(dna):

    result= ""
    for char in dna:
        if char == 'A':
            result=result+'T'  
        elif char == 'C':
             result=result+'G'
        elif char == 'T':
            result=result+'A'
        else:
            result=result+'C'
    return result

    """(str) -> str
    Return the nucleotide's complement Return complement of the giving DNA sequence.
    >>>get_complementary_sequence('ATCG')
    TAGC
    >>>get_complementary_sequence('TTGC')
    AACG
    ​"""
def compress_list(L):
    compressed_list = []
    i = 0
    while i < len(L):
        compressed_list.append(L[i] + L[i + 1])
        i=i+2
    return compressed_list
    """ (list of str) -> list of str

    Return a new list with adjacent pairs of string elements       from Lconcatenated together, starting with indices 0 and 1,    2 and 3,and so on.

    Precondition: len(L) >= 2 and len(L) % 2 == 0

    >>> compress_list(['a', 'b', 'c', 'd'])
    ['ab', 'cd']
    """
def sumev():
    num=1523
    summ=0
    while num<=10503:
        summ=summ+num
        num=num+2
    print(summ)
def while_version(L):
    """ (list of number) -> number
    """
    i = 0
    total = 0

    while i < len(L) and L[i] % 2 != 0:
        total = total + L[i]
        i = i + 1

    return total
def for_version(L):
    found_even = False
    total = 0

    for num in L:
        if num % 2 != 0 and not found_even:
            total = total + num
        else:
            found_even = True
 
    return total

def increment_items(L, increment):
    i = 0
    while i < len(L):
        L[i] = L[i] + increment
        i = i + 1

def mystery(s):
    i = 0
    result = ''

    while not s[i].isdigit():
          result = result + s[i]
          i = i + 1

    return result
def example(L):
    """ (list) -> list
    """
    i = 0
    result = []
    while i < len(L):
        result.append(L[i])
        i = i + 3
    return result
