import numpy as np

# class Controls:
def Ctrl_tgh(P, gains = [30,50,1]): 
    """ 
    Hyperbolic Tangent Function
    g = [vmax ka kt umax]  = [m/s _ _ º/s]
    """
    # Instantaneous Error:
    P.pPos.Xtil = (P.pPos.Xd - P.pPos.X)

    # Kinematic modeling
    A = np.array([
        [np.cos(P.pPos.X[5,0]), -P.pPar.a * np.sin(P.pPos.X[5,0] + P.pPar.alpha)],
        [np.sin(P.pPos.X[5,0]), P.pPar.a * np.cos(P.pPos.X[5,0] + P.pPar.alpha)],
        [0, 1]])

    K = np.diag(gains)

    P.pSC.Ud[[0,1]] = np.dot(np.linalg.pinv(A), (P.pPos.Xd[[6,7,11]] + np.dot(K, np.tanh(P.pPos.Xtil[[0,1,5]]))   )   )
    
    # P.pSC.Ud[0] = v
    # P.pSC.Ud[1] = w

    # End of the function..........................................
    return P
