import numpy as np

def checkRecurrence(seq, order= 2, minlength = 7):
    """
    checks whether a sequence is a linear recurrence sequence

    Parameters
    ----------
    seq : list
        The list containing the sequence

    order : int
        Order of polynomial sequence to be checked

    minlength : int, optional
        Min length of the sequence

    Returns
    -------
    coeffs : list
        A list containing the coefficients if the sequence is a linear recurrence sequence

    None :
        if the sequence is not a linear recurrence sequence
    """
    if len(seq)< max((2*order+1), minlength):
        return None
    
    # Set up the system of equations 
    A,b = [], []
    for i in range(order):
        A.append(seq[i:i+order])
        b.append(seq[i+order])
    A,b =np.array(A), np.array(b)
    try: 
        if np.linalg.det(A)==0:
            return None
    except TypeError:
        return None

    #  Solve for the coefficients (c0, c1, c2, ...)
    coeffs = np.linalg.inv(A).dot(b)  
    
    #  Check if the next terms satisfy recurrence relation
    for i in range(2*order, len(seq)):
        predict = np.sum(coeffs*np.array(seq[i-order:i]))
        error = abs(predict-seq[i])/seq[i] if seq[i] != 0  else abs(predict-seq[i])
        if error>10**(-2):
            return None
    
    return list(coeffs)

def predictNextTerm_Recurrence(seq, coeffs):
    """
    predicts the next term of a linear recurrence sequence

    Parameters
    ----------
    seq : list
        The list containing the sequence

    coeffs : list
        A list containing the coefficients if the sequence is a linear recurrence sequence

    Returns
    -------
    next_term :
        the next term of the linear recurrence sequence
    """
    
    order = len(coeffs)
    predict = np.sum(coeffs*np.array(seq[-order:]))
    return int(round(predict))