import numpy as np

# class Controls:
def Ctrl_tgh(P, gains1 = [0.4,0.4]): 
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

    K1 = np.diag(gains1)

    Func = np.linalg.pinv(A) @ (P.pPos.Xd[[6,7]] + K1 @ np.tanh(P.pPos.Xtil[[0,1]]))
    P.pSC.Ud[[0]] = Func[0]
    P.pSC.Ud[[1]] = Func[1]

    return P

# class Controls:
def Ctrl_tgh_int(P, gains1 = [0.4,0.4], gains2 = [0.4]): 
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

    K1 = np.diag(gains1)
    K2 = np.diag(gains2)

    Func = np.linalg.pinv(A) @ (P.pPos.Xd[[6,7]] + K1 @ np.tanh(K2 @ P.pPos.Xtil[[0,1]]))
    P.pSC.Ud[[0]] = Func[0]
    P.pSC.Ud[[1]] = Func[1]

    return P

def ctrl_v22(P, gain = (.02,.02,.05)):
    kx, ky, kpsi = gain

    # Erro

    ux = P.pPos.Xd[[6]] + kx * (P.pPos.Xd[[0]] - P.pPos.X[[0]])
    uy = P.pPos.Xd[[7]] + ky * (P.pPos.Xd[[1]] - P.pPos.X[[1]])

    # Variables definition
    urBDP = np.arctan2(uy,ux) - P.pPos.X[5, 0]
    P.pSC.Ud[1,0] = kpsi * urBDP
    P.pSC.Ud[0,0] = np.cos(P.pPos.X[5,0]) * ux + np.sin(P.pPos.X[5, 0]) * uy + P.pPar.a * P.pSC.Ud[1,0]
    
    return P
    # class Controls:

def Ctrl_tgh_ori(P, gains = [1,1,1]): 
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
    
    P.pSC.Ud[[0]] = Func[0]
    P.pSC.Ud[[1]] = Func[1]

    return P

def f1(P, gain = [0.5, 0.5]):

    k1 = gain[0]
    k2 = gain[1]

    x = P.pPos.X[0,0]
    y = P.pPos.X[1,0]

    xd = P.pPos.Xd[0, 0]
    yd = P.pPos.Xd[1, 0]

    yaw = P.pPos.X[5, 0]
    
    psi = np.arctan2(yd - y, xd - x)
    phi = yaw - psi

    if phi > np.pi:
        phi = phi - 2 * np.pi
    
    if phi < -np.pi:
        phi = phi + 2 * np.pi

    r = np.sqrt((xd - x)**2 + (yd - y)**2)
    
    P.pSC.Ud[0, 0] = k1 * 1.25*r * np.cos(phi)
    P.pSC.Ud[1, 0] = -k1 * np.sin(phi) * np.cos(phi) - (k2*phi)

    return P

def f2(P, gain = [0.5, 0.5]):

    k1 = gain[0]
    k2 = gain[1]

    x = P.pPos.X[0,0]
    y = P.pPos.X[1,0]

    xd = P.pPos.Xd[0, 0]
    yd = P.pPos.Xd[1, 0]

    yaw = P.pPos.X[5, 0]

    psi = np.arctan2(yd - y, xd - x)
    phi = yaw - psi
   

    if phi > np.pi:
        r = np.sqrt((xd - x)**2 + (yd - y)**2)
        print(f'1 => yaw: {yaw}, psi: {psi}, phi: {phi}, phi2: {(-yaw) - psi}, r: {r}')
        phi = (-yaw) - psi
        
        P.pSC.Ud[0, 0] = -(k1 * r * np.cos(phi))
        P.pSC.Ud[1, 0] = -(-k1 * np.sin(phi) * np.cos(phi) - (k2*phi))

        return P
    
    elif phi < -np.pi:
        r = np.sqrt((xd - x)**2 + (yd - y)**2)
        print(f'2 => yaw: {yaw}, psi: {psi}, phi: {phi}, phi2: {(-yaw) - psi}, r: {r}')
        phi = (-yaw) - psi
        

        P.pSC.Ud[0, 0] = (k1 * r * np.cos(phi))
        P.pSC.Ud[1, 0] = (-k1 * np.sin(phi) * np.cos(phi) - (k2*phi))

        return P

    else:
        # print(f'3 = >yaw: {yaw}, psi: {psi}, phi: {phi}, r: {r}')
        r = np.sqrt((xd - x)**2 + (yd - y)**2)
        P.pSC.Ud[0, 0] = k1 * r * np.cos(phi)
        P.pSC.Ud[1, 0] = -k1 * np.sin(phi) * np.cos(phi) - (k2*phi)

        return P