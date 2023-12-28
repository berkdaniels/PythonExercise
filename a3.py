"""A board is a list of list of str. For example, the board
    ANTT
    XSOB
is represented as the list
    [['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']]

A word list is a list of str. For example, the list of words
    ANT
    BOX
    SOB
    TO
is represented as the list
    ['ANT', 'BOX', 'SOB', 'TO']
"""


def is_valid_word(wordlist, word):
    
    for obj in wordlist:
        if word == obj:
            return True
    
    return False
    """ (list of str, str) -> bool

    Return True if and only if word is an element of wordlist.

    >>> is_valid_word(['ANT', 'BOX', 'SOB', 'TO'], 'TO')
    True
    """


def make_str_from_row(board, row_index):
    stro=''
    for i in range(len(board)):
       if i==row_index:
           sublist=board[i]
           for si in range(len(sublist)):
               stro=stro+sublist[si]
               
    return stro
    """ (list of list of str, int) -> str

    Return the characters from the row of the board with index row_index
    as a single string.

    >>> make_str_from_row([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 0)
    'ANTT'
    """


def make_str_from_column(board, column_index):
    stco=''
    for i in range(len(board)):
        sublist=board[i]
        for si in range(len(sublist)):
            if si == column_index:
                stco=stco+sublist[si]
    return stco
    """ (list of list of str, int) -> str

    Return the characters from the column of the board with index column_index
    as a single string.

    >>> make_str_from_column([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 1)
    'NS'
    """


def board_contains_word_in_row(board, word):
    """ (list of list of str, str) -> bool

    Return True if and only if one or more of the rows of the board contains
    word.

    Precondition: board has at least one row and one column, and word is a
    valid word.

    >>> board_contains_word_in_row([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'SOB')
    True
    """

    for row_index in range(len(board)):
        if word in make_str_from_row(board, row_index):
            return True

    return False


def board_contains_word_in_column(board, word):
    for column_index in range(len(board[0])):
            if word in make_str_from_column(board , column_index):
                return True
    return False
    """ (list of list of str, str) -> bool

    Return True if and only if one or more of the columns of the board
    contains word.

    Precondition: board has at least one row and one column, and word is a
    valid word.

    >>> board_contains_word_in_column([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'NO')
    False
    """


def board_contains_word(board, word):
    for i in range(len(board)):
        if board_contains_word_in_column(board, word) == True or board_contains_word_in_row(board, word) == True:
            return True

    return False
            
            
           
        
    """ (list of list of str, str) -> bool

    Return True if and only if word appears in board.

    Precondition: board has at least one row and one column.

    >>> board_contains_word([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'ANT')
    True
    """


def word_score(word):
    score=0
    if len(word) < 3:
        score = 0
    elif len(word) >=3 and len(word) <=6:
        score = 1* len(word)
    elif len(word) >=7 and len(word) <=9:
        score= score= 2 *len(word)
    else:
        score= 3 * len(word)
    return score
    
    """ (str) -> int

    Return the point value the word earns.

    Word length: < 3: 0 points
                 3-6: 1 point per character for all characters in word
                 7-9: 2 points per character for all characters in word
                 10+: 3 points per character for all characters in word

    >>> word_score('DRUDGERY')
    16
    """


def update_score(player_info, word):
    player_info[1]=player_info[1] + word_score(word)
        
    """ ([str, int] list, str) -> NoneType

    player_info is a list with the player's name and score. Update player_info
    by adding the point value word earns to the player's score.

    >>> update_score(['Jonathan', 4], 'ANT')
    """


def num_words_on_board(board, words):
    count=0
    for i in range(len(words)):
        word=words[i]
        if board_contains_word(board, word) == True:
            count+=1
    return count

    

    
    """ (list of list of str, list of str) -> int

    Return how many words appear on board.

    >>> num_words_on_board([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], ['ANT', 'BOX', 'SOB', 'TO'])
    3
    """


def read_words(words_file):
    wl=[]
    wrd=''
    lines=words_file.readlines()
    for line in lines:
        wrd=line.rstrip('\n')
        wl.append(wrd)
    return wl
        
    
    
	 # this reads in one line at a time, just as if the file were a list
    # code here to remove the newline from the word    
    # ... and place it in a new list
    """ (file open for reading) -> list of str

    Return a list of all words (with newlines removed) from open file
    words_file.

    Precondition: Each line of the file contains a word in uppercase characters
    from the standard English alphabet.
    """


def read_board(board_file):
    blst=[]
    for ln in board_file:
        inlst=[]
        wrd=ln.rstrip()
        for char in range(len(wrd)):
            inlst.append(wrd[char])
        blst.append(inlst)
    return blst
    """ (file open for reading) -> list of list of str

    Return a board read from open file board_file. The board file will contain
    one row of the board per line. Newlines are not included in the board.
    """

