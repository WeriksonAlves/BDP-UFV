import numpy as np

# class Controls:
def Ctrl_tgh(P, gains = [0.5,0.5]): 
    """ 
    Hyperbolic Tangent Function
    g = [vmax ka kt umax]  = [m/s rad/s] [.9,.1]
    """
    # Instantaneous Error:
    P.pPos.Xtil = (P.pPos.Xd - P.pPos.X)
    
    for ii in range(3, 6):
        if abs(P.pPos.Xtil[ii]) > np.pi:
            if P.pPos.Xtil[ii] < 0:
                P.pPos.Xtil[ii] = P.pPos.Xtil[ii] + 2 * np.pi
            else:
                P.pPos.Xtil[ii] = P.pPos.Xtil[ii] - 2 * np.pi

    A = np.array([
        [np.cos(P.pPos.X[5,0]), -P.pPar.a * np.sin(P.pPos.X[5,0] + P.pPar.alpha)],
        [np.sin(P.pPos.X[5,0]), P.pPar.a * np.cos(P.pPos.X[5,0] + P.pPar.alpha)]])

    K = np.diag(gains)

    Func = np.linalg.pinv(A) @ (P.pPos.Xd[[6,7]] + K @ np.tanh(P.pPos.Xtil[[0,1]]))
    P.pSC.Ud[[0]] = Func[0]
    P.pSC.Ud[[1]] = Func[1]

    return P


# class Controls:
def Ctrl_tgh_2(P, gains = [1,1,1]): 
    """ 
    Hyperbolic Tangent Function
    g = [vmax ka kt umax]  = [m/s _ _ rad/s]
    """
    # Instantaneous Error:
    P.pPos.Xtil = (P.pPos.Xd - P.pPos.X)
    
    for ii in range(3, 6):
        if abs(P.pPos.Xtil[ii]) > np.pi:
            if P.pPos.Xtil[ii] < 0:
                P.pPos.Xtil[ii] = P.pPos.Xtil[ii] + 2 * np.pi
            else:
                P.pPos.Xtil[ii] = P.pPos.Xtil[ii] - 2 * np.pi

    A = np.array([[np.cos(P.pPos.X[5,0]), -P.pPar.a * np.sin(P.pPos.X[5,0] + P.pPar.alpha)],
                  [np.sin(P.pPos.X[5,0]), P.pPar.a * np.cos(P.pPos.X[5,0] + P.pPar.alpha)],
                  [0,1]])

    K = np.diag(gains)

    Func = np.linalg.pinv(A) @ (P.pPos.Xd[[6,7,11]] + K @ np.tanh(P.pPos.Xtil[[0,1,5]]))
    print(Func)
    P.pSC.Ud[[0]] = Func[0]
    P.pSC.Ud[[1]] = Func[1]

    return P