import numpy as np

def checkSubsequenceRepetition(seq, order):
    """
    checks whether a sequence is a subsequence repetitive sequence

    Parameters
    ----------
    seq : list
        The list containing the sequence

    order : int
        Order of subsequence to be checked


    Returns
    -------
    True/False
    """
    n = len(seq)
    if n > order:
        subsequence = seq[:order]
        for i in range(n//order):
            if seq[i*order:(i+1)*order] != subsequence:
                return False
        return seq[(n-1)%order] == seq[-1]
    return False

def predictNextTerm_ModeFallback(seq, order):
    """
    predicts the next term of a subsequence repetitive sequence

    Parameters
    ----------
    seq : list
        The list containing the sequence

    order : int
        Order of subsequence

    Returns
    -------
    next_term :
        the next term of the subsequence repetitive sequence
    """
    return seq[n%order]