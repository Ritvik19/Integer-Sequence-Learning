import numpy as np

def checkTripletSum(seq):
    """
    checks whether a sequence is a triplet sum sequence

    Parameters
    ----------
    seq : list
        The list containing the sequence

    Returns
    -------
    True/False
    """
    
    for i in range(2,len(seq),3):
        if seq[i] != seq[i-1]+seq[i-2]:
            return False
    return True

def predictNextTerm_TripletSum(seq):
    """
    predicts the next term of a triplet sum sequence

    Parameters
    ----------
    seq : list
        The list containing the sequence

    Returns
    -------
    next_term :
        the next term of the triplet sum sequence
    """
    
    if len(seq)%3 == 2:
        return seq[-2]+seq[-1]
    return None

def checkTripletProd(seq):
    """
    checks whether a sequence is a triplet product sequence

    Parameters
    ----------
    seq : list
        The list containing the sequence

    Returns
    -------
    True/False
    """
    for i in range(2,len(seq),3):
        if seq[i] != seq[i-1]*seq[i-2]:
            return False
    return True

def predictNextTerm_TripletProd(seq):
    """
    predicts the next term of a triplet product sequence

    Parameters
    ----------
    seq : list
        The list containing the sequence

    Returns
    -------
    next_term :
        the next term of the triplet product sequence
    """
    if len(seq)%3 == 2:
        return seq[-2]*seq[-1]
    return None

def checkTripletDiff(seq):
    """
    checks whether a sequence is a triplet difference sequence

    Parameters
    ----------
    seq : list
        The list containing the sequence

    Returns
    -------
    True/False
    """
    for i in range(2,len(seq),3):
        if seq[i] != abs(seq[i-1]-seq[i-2]):
            return False
    return True

def predictNextTerm_TripletDiff(seq):
    """
    predicts the next term of a triplet difference sequence

    Parameters
    ----------
    seq : list
        The list containing the sequence

    Returns
    -------
    next_term :
        the next term of the triplet difference sequence
    """
    if len(seq)%3 == 2:
        if seq[2] == seq[1]-seq[0]:
            return seq[-1]-seq[-2]
        else:
            return seq[-2]-seq[-1]
    return None

def checkTripletPyth(seq):
    """
    checks whether a sequence is a pythagorean triplet sequence

    Parameters
    ----------
    seq : list
        The list containing the sequence

    Returns
    -------
    True/False
    """
    for i in range(2,len(seq),3):
        if seq[i] != (seq[i-1]**2+seq[i-2]**2)**0.5:
            return False
    return True

def predictNextTerm_TripletPyth(seq):
    """
    predicts the next term of a pythagorean triplet sequence

    Parameters
    ----------
    seq : list
        The list containing the sequence

    Returns
    -------
    next_term :
        the next term of the pythagorean triplet sequence
    """
    if len(seq)%3 == 2:
        return int((seq[-1]**2+seq[-2]**2)**0.5)
    return None