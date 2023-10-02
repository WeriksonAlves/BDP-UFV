import numpy as np

def Attacker(P, gain = [1, 0.7]): # Sung-On Lee

    wmax = P.pPar.wmax    # rad/s
    vmax = P.pPar.vmax    # m/s

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
    
    P.pSC.Ud[0, 0] = vmax * np.tanh(k1 * 1.25*r * np.cos(phi))
    P.pSC.Ud[1, 0] = (-k1 * np.sin(phi) * np.cos(phi) - (k2*phi))

    if r < 10/100:
        P.pSC.Ud[0, 0] = 0
        if np.abs(psi) < np.pi / 2:
            P.pSC.Ud[1, 0] = wmax
        else:
            P.pSC.Ud[1, 0] = -wmax

    return P