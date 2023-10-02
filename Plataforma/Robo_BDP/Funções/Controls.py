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
def Ctrl_tgh_int(P, gains1 = np.array([0.7,0.4]), gains2 = np.array([0.9,0.9])): 
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

    Func = np.linalg.pinv(A) @ (P.pPos.Xd[[6,7]] + K1 @ np.tanh(K1 @ np.linalg.inv(K2) @ P.pPos.Xtil[[0,1]]))
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

def f1(P, gain = [0.8, 0.7]): # Sung-On Lee

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
        phi = phi - 2 * np.pi
    if phi < -np.pi:
        phi = phi + 2 * np.pi
    r = np.sqrt((xd - x)**2 + (yd - y)**2)
    
    P.pSC.Ud[0, 0] = 1.5 * np.tanh(2 * k1 * 1.25*r * np.cos(phi))
    P.pSC.Ud[1, 0] = -k1 * np.sin(phi) * np.cos(phi) - (k2*phi)

    return P
    
def f3(P, gain = [1, 1]): # Escola de Inverno -> Bom pro Goleiro! # Ganho bom 1, 1

    k1 = gain[0]
    k2 = gain[1]
    # k3 = gain[2]

    x = P.pPos.X[0,0]
    y = P.pPos.X[1,0]

    xd = P.pPos.Xd[0, 0]
    yd = P.pPos.Xd[1, 0]

    yaw = P.pPos.X[5, 0]
    
    psi = np.arctan2(yd - y, xd - x)
    phi = yaw - psi
    alpha = normalizeAngle(psi - yaw)

    r = np.sqrt((xd - x)**2 + (yd - y)**2)

    if abs(alpha) > np.pi/2:
        k1 = -k1
        phi = normalizeAngle(phi + np.pi) 

    P.pSC.Ud[0, 0] = k1 * np.tanh(2 * r * np.cos(phi))
    P.pSC.Ud[1, 0] = k2 * phi  + k1 * (np.tanh(r) / r) * np.sin(phi) * np.cos(phi) 

    return P

def f4(P, gain = [0.5, 0.5, .5]):
    k1 = gain[0]
    k2 = gain[1]
    k3 = gain[2]
    a = P.pPar.a

    x = P.pPos.X[0,0] + a * np.cos(P.pPos.X[5, 0])
    y = P.pPos.X[1,0] + a * np.sin(P.pPos.X[5, 0])

    xd = P.pPos.Xd[0, 0]
    yd = P.pPos.Xd[1, 0]

    psi = P.pPos.X[5, 0]

    xtil = xd - x
    ytil = yd - y

    Vx = 0 + k1 * xtil
    Vy = 0 + k2 * ytil

    psi_alpha = np.arctan2(yd - y, xd - x)
    alpha = psi_alpha - psi

    if alpha > np.pi:
        alpha = alpha - 2 * np.pi
    
    if alpha < -np.pi:
        alpha = alpha + 2 * np.pi

    if (abs(np.rad2deg(alpha)) >  70) and (abs(np.rad2deg(alpha)) < 110):
        psid = np.arctan2(Vy, Vx)
        Vpsi = k3 * (psid - psi)
    else:
        Vpsi = -Vx / (a * np.cos(alpha)) * np.sin(psi) + Vy/(a * np.cos(alpha)) * np.cos(psi)
    
    
    P.pSC.Ud[0, 0] = Vx * np.cos(psi) + Vy * np.sin(psi) + Vpsi * a * np.sin(alpha)
    P.pSC.Ud[1, 0] = Vpsi
    print(P.pSC.Ud[0, 0], P.pSC.Ud[1, 0])

    return P

def normalizeAngle(angle):
    return np.mod(angle+np.pi, 2*np.pi) - np.pi

def f5(P, B, gain=[.15, .15, .05]):
    kx = gain[0]
    ky = gain[1]
    kpsi = gain[2]

    a = P.pPar.a

    x = P.pPos.X[0, 0]
    y = P.pPos.X[1, 0]
    psi = P.pPos.X[5, 0]

    xd = P.pPos.Xd[0, 0]
    yd = P.pPos.Xd[1, 0]

    vx_bola = B.pPos.X[6, 0]
    vy_bola = B.pPos.X[7, 0]

    xtil = xd - x
    ytil = yd - y
    
    Vx = kx * (xd - x) + vx_bola
    Vy = ky * (yd - y) + vy_bola

    alpha = np.arctan2(ytil, xtil)

    Vpsi = - Vx / (a * np.cos(alpha)) * np.sin(psi) + Vy / (a * np.cos(alpha)) * np.cos(psi)
    

    if (abs(alpha) > np.deg2rad(85)) and (abs(alpha) < np.deg2rad(95)):
        psi_pontod = np.arctan2(vy_bola, vx_bola)
        Vpsi  = psi_pontod + kpsi * psi
    


    v = Vx * np.cos(psi) + Vy * np.sin(psi) + Vpsi * a * np.sin(alpha)
    w = Vpsi

    P.pSC.Ud[0, 0] = v
    P.pSC.Ud[1, 0] = w

    return P

def f6(P, gain=[1.4, 1]):
    kr = gain[0]
    kt = gain[1]

    x = P.pPos.X[0, 0]
    y = P.pPos.X[1, 0]

    xd = P.pPos.Xd[0, 0]
    yd = P.pPos.Xd[1, 0]

    xtil = xd - x
    ytil = yd - y

    theta = np.arctan2(ytil, xtil)

    v = kr *((xtil * np.cos(P.pPos.X[5,0])) + (ytil * np.sin(P.pPos.X[5,0])))
    w = kt * normalizeAngle(theta - P.pPos.X[5,0])

    P.pSC.Ud[0, 0] = np.tanh(v)
    P.pSC.Ud[1, 0] = 20*np.tanh(w)

    return P