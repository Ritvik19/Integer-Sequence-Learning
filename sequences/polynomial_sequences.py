import numpy as np 

def checkPolynomial(seq, order= 2, minlength = 4):
    """
    checks whether a sequence is a polynomial sequence

    Parameters
    ----------
    seq : list
        The list containing the sequence

    order : int
        Order of polynomial sequence to be checked

    minlength : int, optional
        Min length of the sequence

    Returns
    ------
    coeffs : list
        A list containing the coefficients if the sequence is a polynomial sequence

    None :
        if the sequence is not a polynomial sequence
    """
        
    if len(seq)< max((2*order+1), minlength):
        return None
    
    # Set up the system of equations 
    A = [[i**j for j in range(order+1)] for i in range(order+1)]
    b = seq[:order+1]
    A,b =np.array(A), np.array(b)
    try: 
        if np.linalg.det(A)==0:
            return None
    except TypeError:
        return None
   
    #  Solve for the coefficients (c0, c1, c2, ...)
    coeffs = np.linalg.inv(A).dot(b)  
    
    #  Check if the next terms satisfy recurrence relation
    for i in range(order, len(seq)):
        predict = np.sum(coeffs*np.array([i**j for j in range(order+1)]))
        error = abs(predict-seq[i])/seq[i] if seq[i] != 0  else abs(predict-seq[i])
        if error>10**(-2):
            return None
    
    return list(coeffs)
    
    
def predictNextTerm_Polynomial(seq, coeffs):
    """
    predicts the next term of a polynomial sequence

    Parameters
    ----------
    seq : list
        The list containing the sequence

    coeffs : list
        A list containing the coefficients if the sequence is a polynomial sequence

    Returns
    ------
    next_term :
        the next term of the polynomial sequence
    """    
    
    order = len(coeffs)
    predict = np.sum(coeffs*np.array([i**j for j in range(order+1)]))
    return int(round(predict))    