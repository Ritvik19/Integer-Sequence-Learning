import numpy as np
from collections import Counter

def checkUnit(seq):
    """
    checks whether a sequence is a unit sequence

    Parameters
    ----------
    seq : list
        The list containing the sequence

    Returns
    -------
    True/False
    """
    return len(set(seq)) == 1

def predictNextTerm_Unit(seq):
    """
    predicts the next term of a unit sequence

    Parameters
    ----------
    seq : list
        The list containing the sequence

    Returns
    -------
    next_term :
        the next term of the unit sequence
    """       
    return seq[0]

def sod(n):
    """
    calculates the sum of digits of a number
    """
    s = 0
    for d in str(n):
        s += int(d)
    return s

def checkSeq_sod(seq):
    """
    checks whether a sequence is a sequence with sum of digits as term difference

    Parameters
    ----------
    seq : list
        The list containing the sequence

    Returns
    -------
    True/False
    """    
    if min(seq) >= 0: 
        for i in range(1,len(seq)):
            if seq[i] != seq[i-1]+sod(seq[i-1]):
                return False
        return True
    return False

def predictNextTerm_Seq_sod(seq):
    """
    predicts the next term of a sequence with sum of digits as term difference

    Parameters
    ----------
    seq : list
        The list containing the sequence

    Returns
    -------
    next_term :
        the next term of the sequence with sum of digits as term difference
    """    
    return seq[-1] + sod(seq[-1])

def checkModeFallback(seq):
    """
    checks if the mode of a sequence can be a next term

    Parameters
    ----------
    seq : list
        The list containing the sequence

    Returns
    -------
    True/False
    """    
    
    c = Counter(seq)
    mode = c.most_common(1)[0][0]
    return mode == seq[-1]

def predictNextTerm_ModeFallback(seq):
    """
    returns the mode of a sequence

    Parameters
    ----------
    seq : list
        The list containing the sequence

    Returns
    -------
    mode
    """
    c = Counter(seq)
    return c.most_common(1)[0][0]