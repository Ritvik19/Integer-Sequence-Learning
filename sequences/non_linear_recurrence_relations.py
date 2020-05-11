import numpy as np

def checkNonLinearRecurrence1(seq, minlength=5): 
    if len(seq)< minlength:
        return None
    
    A,b = [], []
    try: 
        for i in range(1, 4):
            A.append([1, i, seq[i-1]])
            b.append(seq[i])
        A,b =np.array(A), np.array(b)
    
        if np.linalg.det(A)==0:
            return None
    except TypeError as e:
        return None
    
    
    coeffs = np.linalg.inv(A).dot(b)
    
    for i in range(4, len(seq)):
        predict = np.sum(coeffs*np.array([1, i, seq[i-1]]))
        error = abs(predict-seq[i])/seq[i] if seq[i] != 0  else abs(predict-seq[i])
        if error>10**(-2):
            return None
    
    return list(coeffs)

def predictNextTerm_NonLinearRecurrence1(seq, coeffs):
    predict = np.sum(coeffs*np.array([1, i, seq[i-1]]))
    return int(round(predict))

def checkNonLinearRecurrence2(seq, minlength=7): 
    if len(seq)< minlength:
        return None
    
    A,b = [], []
    try: 
        for i in range(1, 5):
            A.append([1, i, i*i, seq[i-1]])
            b.append(seq[i])
        A,b =np.array(A), np.array(b)
    
        if np.linalg.det(A)==0:
            return None
    except TypeError as e:
        return None
    
    
    coeffs = np.linalg.inv(A).dot(b)
    
    for i in range(5, len(seq)):
        predict = np.sum(coeffs*np.array([1, i, i*i, seq[i-1]]))
        error = abs(predict-seq[i])/seq[i] if seq[i] != 0  else abs(predict-seq[i])
        if error>10**(-2):
            return None
    
    return list(coeffs)

def predictNextTerm_NonLinearRecurrence2(seq, coeffs):
    predict = np.sum(coeffs*np.array([1, i, i*i, seq[i-1]]))
    return int(round(predict))

def checkNonLinearRecurrence3(seq, minlength=9): 
    if len(seq)< minlength:
        return None
    
    A,b = [], []
    try: 
        for i in range(1, 6):
            A.append([1, i, i*i, i*i*i, seq[i-1]])
            b.append(seq[i])
        A,b =np.array(A), np.array(b)
    
        if np.linalg.det(A)==0:
            return None
    except TypeError as e:
        return None
    
    
    coeffs = np.linalg.inv(A).dot(b)
    
    for i in range(6, len(seq)):
        predict = np.sum(coeffs*np.array([1, i, i*i, i*i*i, seq[i-1]]))
        error = abs(predict-seq[i])/seq[i] if seq[i] != 0  else abs(predict-seq[i])
        if error>10**(-2):
            return None
    
    return list(coeffs)

def predictNextTerm_NonLinearRecurrence3(seq, coeffs):
    predict = np.sum(coeffs*np.array([1, i, i*i, i*i*i, seq[i-1]]))
    return int(round(predict))

def checkNonLinearRecurrence4(seq, minlength=7): 
    if len(seq)< minlength:
        return None
    
    A,b = [], []
    try: 
        for i in range(2, 6):
            A.append([1, i, seq[i-1], seq[i-2]])
            b.append(seq[i])
        A,b =np.array(A), np.array(b)
    
        if np.linalg.det(A)==0:
            return None
    except TypeError as e:
        return None
    
    
    coeffs = np.linalg.inv(A).dot(b)
    
    for i in range(6, len(seq)):
        predict = np.sum(coeffs*np.array([1, i, seq[i-1], seq[i-2]]))
        error = abs(predict-seq[i])/seq[i] if seq[i] != 0  else abs(predict-seq[i])
        if error>10**(-2):
            return None
    
    return list(coeffs)

def predictNextTerm_NonLinearRecurrence4(seq, coeffs):
    predict = np.sum(coeffs*np.array([1, i, seq[i-1], seq[i-2]]))
    return int(round(predict))

def checkNonLinearRecurrence5(seq, minlength=9): 
    if len(seq)< minlength:
        return None
    
    A,b = [], []
    try: 
        for i in range(2, 7):
            A.append([1, i, i*i, seq[i-1], seq[i-2]])
            b.append(seq[i])
        A,b =np.array(A), np.array(b)
    
        if np.linalg.det(A)==0:
            return None
    except TypeError as e:
        return None
    
    
    coeffs = np.linalg.inv(A).dot(b)
    
    for i in range(7, len(seq)):
        predict = np.sum(coeffs*np.array([1, i, i*i, seq[i-1], seq[i-2]]))
        error = abs(predict-seq[i])/seq[i] if seq[i] != 0  else abs(predict-seq[i])
        if error>10**(-2):
            return None
    
    return list(coeffs)

def predictNextTerm_NonLinearRecurrence5(seq, coeffs):
    predict = np.sum(coeffs*np.array([1, i, i*i, seq[i-1], seq[i-2]]))
    return int(round(predict))

def checkNonLinearRecurrence6(seq, minlength=11): 
    if len(seq)< minlength:
        return None
    
    A,b = [], []
    try: 
        for i in range(2, 8):
            A.append([1, i, i*i, i*i*i, seq[i-1], seq[i-2]])
            b.append(seq[i])
        A,b =np.array(A), np.array(b)
    
        if np.linalg.det(A)==0:
            return None
    except TypeError as e:
        return None
    
    
    coeffs = np.linalg.inv(A).dot(b)
    
    for i in range(8, len(seq)):
        predict = np.sum(coeffs*np.array([1, i, i*i, i*i*i, seq[i-1], seq[i-2]]))
        error = abs(predict-seq[i])/seq[i] if seq[i] != 0  else abs(predict-seq[i])
        if error>10**(-2):
            return None
    
    return list(coeffs)

def predictNextTerm_NonLinearRecurrence6(seq, coeffs):
    predict = np.sum(coeffs*np.array([1, i, i*i, i*i*i, seq[i-1], seq[i-2]]))
    return int(round(predict))

def checkNonLinearRecurrence7(seq, minlength=9): 
    if len(seq)< minlength:
        return None
    
    A,b = [], []
    try: 
        for i in range(2, 7):
            A.append([1, i, seq[i-1], seq[i-2], seq[i-1]*seq[i-2]])
            b.append(seq[i])
        A,b =np.array(A), np.array(b)
    
        if np.linalg.det(A)==0:
            return None
    except TypeError as e:
        return None
    
    
    coeffs = np.linalg.inv(A).dot(b)
    
    for i in range(7, len(seq)):
        predict = np.sum(coeffs*np.array([1, i, seq[i-1], seq[i-2], seq[i-1]*seq[i-2]]))
        error = abs(predict-seq[i])/seq[i] if seq[i] != 0  else abs(predict-seq[i])
        if error>10**(-2):
            return None
    
    return list(coeffs)

def predictNextTerm_NonLinearRecurrence7(seq, coeffs):
    predict = np.sum(coeffs*np.array([1, i, seq[i-1], seq[i-2], seq[i-1]*seq[i-2]]))
    return int(round(predict))

def checkNonLinearRecurrence8(seq, minlength=11): 
    if len(seq)< minlength:
        return None
    
    A,b = [], []
    try: 
        for i in range(2, 8):
            A.append([1, i, i*i, seq[i-1], seq[i-2], seq[i-1]*seq[i-2]])
            b.append(seq[i])
        A,b =np.array(A), np.array(b)
    
        if np.linalg.det(A)==0:
            return None
    except TypeError as e:
        return None
    
    
    coeffs = np.linalg.inv(A).dot(b)
    
    for i in range(8, len(seq)):
        predict = np.sum(coeffs*np.array([1, i, i*i, seq[i-1], seq[i-2], seq[i-1]*seq[i-2]]))
        error = abs(predict-seq[i])/seq[i] if seq[i] != 0  else abs(predict-seq[i])
        if error>10**(-2):
            return None
    
    return list(coeffs)

def predictNextTerm_NonLinearRecurrence8(seq, coeffs):
    predict = np.sum(coeffs*np.array([1, i, i*i, seq[i-1], seq[i-2], seq[i-1]*seq[i-2]]))
    return int(round(predict))

def checkNonLinearRecurrence9(seq, minlength=13): 
    if len(seq)< minlength:
        return None
    
    A,b = [], []
    try: 
        for i in range(2, 9):
            A.append([1, i, i*i, i*i*i, seq[i-1], seq[i-2], seq[i-1]*seq[i-2]])
            b.append(seq[i])
        A,b =np.array(A), np.array(b)
    
        if np.linalg.det(A)==0:
            return None
    except TypeError as e:
        return None
    
    
    coeffs = np.linalg.inv(A).dot(b)
    
    for i in range(9, len(seq)):
        predict = np.sum(coeffs*np.array([1, i, i*i, i*i*i, seq[i-1], seq[i-2], seq[i-1]*seq[i-2]]))
        error = abs(predict-seq[i])/seq[i] if seq[i] != 0  else abs(predict-seq[i])
        if error>10**(-2):
            return None
    
    return list(coeffs)

def predictNextTerm_NonLinearRecurrence9(seq, coeffs):
    predict = np.sum(coeffs*np.array([1, i, i*i, i*i*i, seq[i-1], seq[i-2], seq[i-1]*seq[i-2]]))
    return int(round(predict))

def checkNonLinearRecurrence10(seq, minlength=9): 
    if len(seq)< minlength:
        return None
    
    A,b = [], []
    try: 
        for i in range(3, 8):
            A.append([1, i, seq[i-1], seq[i-2], seq[i-3]])
            b.append(seq[i])
        A,b =np.array(A), np.array(b)
    
        if np.linalg.det(A)==0:
            return None
    except TypeError as e:
        return None
    
    
    coeffs = np.linalg.inv(A).dot(b)
    
    for i in range(8, len(seq)):
        predict = np.sum(coeffs*np.array([1, i, seq[i-1], seq[i-2], seq[i-3]]))
        error = abs(predict-seq[i])/seq[i] if seq[i] != 0  else abs(predict-seq[i])
        if error>10**(-2):
            return None
    
    return list(coeffs)

def predictNextTerm_NonLinearRecurrence10(seq, coeffs):
    predict = np.sum(coeffs*np.array([1, i, seq[i-1], seq[i-2], seq[i-3]]))
    return int(round(predict))

def checkNonLinearRecurrence11(seq, minlength=11): 
    if len(seq)< minlength:
        return None
    
    A,b = [], []
    try: 
        for i in range(3, 9):
            A.append([1, i, i*i, seq[i-1], seq[i-2], seq[i-3]])
            b.append(seq[i])
        A,b =np.array(A), np.array(b)
    
        if np.linalg.det(A)==0:
            return None
    except TypeError as e:
        return None
    
    
    coeffs = np.linalg.inv(A).dot(b)
    
    for i in range(9, len(seq)):
        predict = np.sum(coeffs*np.array([1, i, i*i, seq[i-1], seq[i-2], seq[i-3]]))
        error = abs(predict-seq[i])/seq[i] if seq[i] != 0  else abs(predict-seq[i])
        if error>10**(-2):
            return None
    
    return list(coeffs)

def predictNextTerm_NonLinearRecurrence11(seq, coeffs):
    predict = np.sum(coeffs*np.array([1, i, i*i, seq[i-1], seq[i-2], seq[i-3]]))
    return int(round(predict))

def checkNonLinearRecurrence12(seq, minlength=13): 
    if len(seq)< minlength:
        return None
    
    A,b = [], []
    try: 
        for i in range(3, 10):
            A.append([1, i, i*i, i*i*i, seq[i-1], seq[i-2], seq[i-3]])
            b.append(seq[i])
        A,b =np.array(A), np.array(b)
    
        if np.linalg.det(A)==0:
            return None
    except TypeError as e:
        return None
    
    
    coeffs = np.linalg.inv(A).dot(b)
    
    for i in range(10, len(seq)):
        predict = np.sum(coeffs*np.array([1, i, i*i, i*i*i, seq[i-1], seq[i-2], seq[i-3]]))
        error = abs(predict-seq[i])/seq[i] if seq[i] != 0  else abs(predict-seq[i])
        if error>10**(-2):
            return None
    
    return list(coeffs)

def predictNextTerm_NonLinearRecurrence12(seq, coeffs):
    predict = np.sum(coeffs*np.array([1, i, i*i, i*i*i, seq[i-1], seq[i-2], seq[i-3]]))
    return int(round(predict))

def checkNonLinearRecurrence13(seq, minlength=15): 
    if len(seq)< minlength:
        return None
    
    A,b = [], []
    try: 
        for i in range(3, 11):
            A.append([1, i, seq[i-1], seq[i-2], seq[i-3], seq[i-1]*seq[i-2], seq[i-2]*seq[i-3], seq[i-3]*seq[i-1]])
            b.append(seq[i])
        A,b =np.array(A), np.array(b)
    
        if np.linalg.det(A)==0:
            return None
    except TypeError as e:
        return None
    
    
    coeffs = np.linalg.inv(A).dot(b)
    
    for i in range(11, len(seq)):
        predict = np.sum(coeffs*np.array([1, i, seq[i-1], seq[i-2], seq[i-3], seq[i-1]*seq[i-2], seq[i-2]*seq[i-3], seq[i-3]*seq[i-1]]))
        error = abs(predict-seq[i])/seq[i] if seq[i] != 0  else abs(predict-seq[i])
        if error>10**(-2):
            return None
    
    return list(coeffs)

def predictNextTerm_NonLinearRecurrence13(seq, coeffs):
    predict = np.sum(coeffs*np.array([1, i, seq[i-1], seq[i-2], seq[i-3], seq[i-1]*seq[i-2], seq[i-2]*seq[i-3], seq[i-3]*seq[i-1]]))
    return int(round(predict))

def checkNonLinearRecurrence14(seq, minlength=17): 
    if len(seq)< minlength:
        return None
    
    A,b = [], []
    try: 
        for i in range(3, 12):
            A.append([1, i, i*i, seq[i-1], seq[i-2], seq[i-3], seq[i-1]*seq[i-2], seq[i-2]*seq[i-3], seq[i-3]*seq[i-1]])
            b.append(seq[i])
        A,b =np.array(A), np.array(b)
    
        if np.linalg.det(A)==0:
            return None
    except TypeError as e:
        return None
    
    
    coeffs = np.linalg.inv(A).dot(b)
    
    for i in range(12, len(seq)):
        predict = np.sum(coeffs*np.array([1, i, i*i, seq[i-1], seq[i-2], seq[i-3], seq[i-1]*seq[i-2], seq[i-2]*seq[i-3], seq[i-3]*seq[i-1]]))
        error = abs(predict-seq[i])/seq[i] if seq[i] != 0  else abs(predict-seq[i])
        if error>10**(-2):
            return None
    
    return list(coeffs)

def predictNextTerm_NonLinearRecurrence14(seq, coeffs):
    predict = np.sum(coeffs*np.array([1, i, i*i, seq[i-1], seq[i-2], seq[i-3], seq[i-1]*seq[i-2], seq[i-2]*seq[i-3], seq[i-3]*seq[i-1]]))
    return int(round(predict))

def checkNonLinearRecurrence15(seq, minlength=19): 
    if len(seq)< minlength:
        return None
    
    A,b = [], []
    try: 
        for i in range(3, 13):
            A.append([1, i, i*i, i*i*i, seq[i-1], seq[i-2], seq[i-3], seq[i-1]*seq[i-2], seq[i-2]*seq[i-3], seq[i-3]*seq[i-1]])
            b.append(seq[i])
        A,b =np.array(A), np.array(b)
    
        if np.linalg.det(A)==0:
            return None
    except TypeError as e:
        return None
    
    
    coeffs = np.linalg.inv(A).dot(b)
    
    for i in range(13, len(seq)):
        predict = np.sum(coeffs*np.array([1, i, i*i, i*i*i, seq[i-1], seq[i-2], seq[i-3], seq[i-1]*seq[i-2], seq[i-2]*seq[i-3], seq[i-3]*seq[i-1]]))
        error = abs(predict-seq[i])/seq[i] if seq[i] != 0  else abs(predict-seq[i])
        if error>10**(-2):
            return None
    
    return list(coeffs)

def predictNextTerm_NonLinearRecurrence15(seq, coeffs):
    predict = np.sum(coeffs*np.array([1, i, i*i, i*i*i, seq[i-1], seq[i-2], seq[i-3], seq[i-1]*seq[i-2], seq[i-2]*seq[i-3], seq[i-3]*seq[i-1]]))
    return int(round(predict))

def checkNonLinearRecurrence16(seq, minlength=17): 
    if len(seq)< minlength:
        return None
    
    A,b = [], []
    try: 
        for i in range(3, 12):
            A.append([1, i, seq[i-1], seq[i-2], seq[i-3], seq[i-1]*seq[i-2], seq[i-2]*seq[i-3], seq[i-3]*seq[i-1], seq[i-1]*seq[i-2]*seq[i-3]])
            b.append(seq[i])
        A,b =np.array(A), np.array(b)
    
        if np.linalg.det(A)==0:
            return None
    except TypeError as e:
        return None
    
    
    coeffs = np.linalg.inv(A).dot(b)
    
    for i in range(12, len(seq)):
        predict = np.sum(coeffs*np.array([1, i, seq[i-1], seq[i-2], seq[i-3], seq[i-1]*seq[i-2], seq[i-2]*seq[i-3], seq[i-3]*seq[i-1], seq[i-1]*seq[i-2]*seq[i-3]]))
        error = abs(predict-seq[i])/seq[i] if seq[i] != 0  else abs(predict-seq[i])
        if error>10**(-2):
            return None
    
    return list(coeffs)

def predictNextTerm_NonLinearRecurrence16(seq, coeffs):
    predict = np.sum(coeffs*np.array([1, i, seq[i-1], seq[i-2], seq[i-3], seq[i-1]*seq[i-2], seq[i-2]*seq[i-3], seq[i-3]*seq[i-1], seq[i-1]*seq[i-2]*seq[i-3]]))
    return int(round(predict))

def checkNonLinearRecurrence17(seq, minlength=19): 
    if len(seq)< minlength:
        return None
    
    A,b = [], []
    try: 
        for i in range(3, 13):
            A.append([1, i, i*i, seq[i-1], seq[i-2], seq[i-3], seq[i-1]*seq[i-2], seq[i-2]*seq[i-3], seq[i-3]*seq[i-1], seq[i-1]*seq[i-2]*seq[i-3]])
            b.append(seq[i])
        A,b =np.array(A), np.array(b)
    
        if np.linalg.det(A)==0:
            return None
    except TypeError as e:
        return None
    
    
    coeffs = np.linalg.inv(A).dot(b)
    
    for i in range(13, len(seq)):
        predict = np.sum(coeffs*np.array([1, i, i*i, seq[i-1], seq[i-2], seq[i-3], seq[i-1]*seq[i-2], seq[i-2]*seq[i-3], seq[i-3]*seq[i-1], seq[i-1]*seq[i-2]*seq[i-3]]))
        error = abs(predict-seq[i])/seq[i] if seq[i] != 0  else abs(predict-seq[i])
        if error>10**(-2):
            return None
    
    return list(coeffs)

def predictNextTerm_NonLinearRecurrence17(seq, coeffs):
    predict = np.sum(coeffs*np.array([1, i, i*i, seq[i-1], seq[i-2], seq[i-3], seq[i-1]*seq[i-2], seq[i-2]*seq[i-3], seq[i-3]*seq[i-1], seq[i-1]*seq[i-2]*seq[i-3]]))
    return int(round(predict))

def checkNonLinearRecurrence18(seq, minlength=21): 
    if len(seq)< minlength:
        return None
    
    A,b = [], []
    try: 
        for i in range(3, 14):
            A.append([1, i, i*i, i*i*i, seq[i-1], seq[i-2], seq[i-3], seq[i-1]*seq[i-2], seq[i-2]*seq[i-3], seq[i-3]*seq[i-1], seq[i-1]*seq[i-2]*seq[i-3]])
            b.append(seq[i])
        A,b =np.array(A), np.array(b)
    
        if np.linalg.det(A)==0:
            return None
    except TypeError as e:
        return None
    
    
    coeffs = np.linalg.inv(A).dot(b)
    
    for i in range(14, len(seq)):
        predict = np.sum(coeffs*np.array([1, i, i*i, i*i*i, seq[i-1], seq[i-2], seq[i-3], seq[i-1]*seq[i-2], seq[i-2]*seq[i-3], seq[i-3]*seq[i-1], seq[i-1]*seq[i-2]*seq[i-3]]))
        error = abs(predict-seq[i])/seq[i] if seq[i] != 0  else abs(predict-seq[i])
        if error>10**(-2):
            return None
    
    return list(coeffs)

def predictNextTerm_NonLinearRecurrence18(seq, coeffs):
    predict = np.sum(coeffs*np.array([1, i, i*i, i*i*i, seq[i-1], seq[i-2], seq[i-3], seq[i-1]*seq[i-2], seq[i-2]*seq[i-3], seq[i-3]*seq[i-1], seq[i-1]*seq[i-2]*seq[i-3]]))
    return int(round(predict))