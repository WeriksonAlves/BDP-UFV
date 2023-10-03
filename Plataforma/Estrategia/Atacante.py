import numpy as np

def Attacker(P, gain = [1.5, 0.9]): # Sung-On Lee

    wmax = P.pPar.wmax    # rad/s
    vmax = P.pPar.vmax    # m/s

    vmin = 0.3377   # m/s   -> 150 RPM
    wmin = 2.8143 / 2   # rad/s -> 50 RPM

    k1 = gain[0]
    k2 = gain[1]

    x = P.pPos.X[0,0]
    y = P.pPos.X[1,0]

    xd = P.pPos.Xd[0, 0]
    yd = P.pPos.Xd[1, 0]

    yaw = P.pPos.X[5, 0]
    
    psi = np.arctan2(yd - y, xd - x)
    phi = - yaw + psi

    if psi < 0:
        phi = -phi

    if phi > np.pi:
        phi = phi - 2 * np.pi
    
    if phi < -np.pi:
        phi = phi + 2 * np.pi

    r = np.sqrt((xd - x)**2 + (yd - y)**2)
    
    P.pSC.Ud[0, 0] = vmax * np.tanh(k1 * 1.25*r * np.cos(phi))
    P.pSC.Ud[1, 0] = (-k1 * np.sin(phi) * np.cos(phi) - (k2*phi))

    if (abs(P.pSC.Ud[0, 0]) < vmin) and (P.pSC.Ud[0, 0] < 0):
        P.pSC.Ud[0, 0] = -vmin
    
    if (abs(P.pSC.Ud[0, 0]) < vmin) and (P.pSC.Ud[0, 0] > 0):
        P.pSC.Ud[0, 0] = vmin
    
    if (abs(P.pSC.Ud[1, 0]) < wmin) and (P.pSC.Ud[1, 0] < 0):
        P.pSC.Ud[1, 0] = -wmin
    
    if (abs(P.pSC.Ud[1, 0]) < wmin) and (P.pSC.Ud[1, 0] > 0):
        P.pSC.Ud[1, 0] = wmin

    if r < 10/100:
        P.pSC.Ud[0, 0] = 0
        #print(np.rad2deg(psi))
        if np.abs(psi) < np.pi/2:
            if psi < 0:
                P.pSC.Ud[1, 0] = wmax
            else:
                P.pSC.Ud[1, 0] = -wmax
        else:
            if psi < 0:
                P.pSC.Ud[1, 0] = wmax
            else:
                P.pSC.Ud[1, 0] = -wmax    

    return P

def Attacker2(P, gain = [1.2, 2.8]): # Escola de Inverno
    '''
    Até agora é o melhor, mas falta mexer aqui para atacar
    do outro lado, até agora está atacando apenas para o lado direito
    '''

    wmax = P.pPar.wmax    # rad/s
    vmax = P.pPar.vmax    # m/s

    vmin = 0.4503       # m/s   -> 200 RPM

    k1 = gain[0]
    k2 = gain[1]
    c = 0.03

    # Pose atual do robo
    x = P.pPos.X[0,0] 
    y = P.pPos.X[1,0] 
    yaw = P.pPos.X[5, 0]

    # Posicao da bola (assumindo que a posicao da bola vem no Xd)
    xball = P.pPos.Xd[0, 0]
    yball = P.pPos.Xd[1, 0]

    # Angulo entre a bola e centro do gol do adversario
    theta = np.arctan2(yball, xball - 0.8)

    # Setando a posição desejado como uma posição ficticia atrás da bola,
    #  porém com o mesmo angulo entre a bola e o centro do gol do adversário
    xd = xball - c if abs(xball - c) < 0.7 else xball
    yd = yball + c * np.sin(theta) if abs(yball + c * np.sin(theta)) < 0.6 else yball
    
    # Angulo entre a posicao desejada e o robô
    psi = np.arctan2(yd - y, xd - x)

    # Erro do angulo
    phi = yaw - psi
    alpha = normalizeAngle(psi - yaw)

    r = np.sqrt((xd - x)**2 + (yd - y)**2)

    # Se caso o destino está atrás do robô
    # Alterar a frente para as costas
    if abs(alpha) > np.pi/2:
        k1 = -k1
        phi = normalizeAngle(phi + np.pi) 

    # Calculando a velocidade linear e a angular
    P.pSC.Ud[0, 0] = k1 * np.tanh(2 * r * np.cos(phi))
    P.pSC.Ud[1, 0] = k2 * phi  + k1 * (np.tanh(r) / r) * np.sin(phi) * np.cos(phi)

    # Se caso a velocidade linear for menor que o minimo
    # Alterar para o valor minino setado.
    if (abs(P.pSC.Ud[0, 0]) < vmin) and (P.pSC.Ud[0, 0] < 0):
        P.pSC.Ud[0, 0] = -vmin
    
    if (abs(P.pSC.Ud[0, 0]) < vmin) and (P.pSC.Ud[0, 0] > 0):
        P.pSC.Ud[0, 0] = vmin

    # Se caso estiver em um raio de 8cm do destino
    # começa a girar no sentido de mandar a bola pro gol
    if r < 8/100:
        if yd < 0:
            P.pSC.Ud[1, 0] = -wmax
        else:
            P.pSC.Ud[1, 0] = wmax
    return P

def Attacker3(P, gain = [1, 2]): # Sugestão do sacola
    wmax = P.pPar.wmax    # rad/s
    vmax = P.pPar.vmax    # m/s

    vmin = 0.4503   # m/s   -> 200 RPM
    wmin = 2.8143 / 2   # rad/s -> 50 RPM

    k1 = gain[0]
    k2 = gain[1]
    c = 0.05

    # Pose atual do robo
    x = P.pPos.X[0,0]
    y = P.pPos.X[1,0]
    yaw = P.pPos.X[5, 0]

    # Posicao da bola (assumindo que a posicao da bola vem no Xd)
    xball = P.pPos.Xd[0, 0] 
    yball = P.pPos.Xd[1, 0]

    # Angulo entre a bola e centro do gol do adversario
    theta = np.arctan2(yball, xball - 0.8)

    # Setando a posição desejado como uma posição ficticia atrás da bola,
    # porém com o mesmo angulo entre a bola e o centro do gol do adversário
    xd = xball - c if abs(xball - c) < 0.7 else xball
    yd = yball + c * np.sin(theta) if abs(yball + c * np.sin(theta)) < 0.6 else yball 

   
    if yaw < 0:
        if (yaw + np.pi) - theta < np.deg2rad(20):
            xd = 0.8
            yd = 0
    else:
        if (yaw + np.pi) - theta < np.deg2rad(20):
            xd = 0.8
            yd = 0


    # Angulo entre a posicao desejada e o robô
    psi = np.arctan2(yd - y, xd - x)


    phi = yaw - psi
    alpha = normalizeAngle(psi - yaw)

    r = np.sqrt((xd - x)**2 + (yd - y)**2)

    if abs(alpha) > np.pi/2:
        k1 = -k1
        phi = normalizeAngle(phi + np.pi) 

    P.pSC.Ud[0, 0] = k1 * np.tanh(2 * r * np.cos(phi))
    P.pSC.Ud[1, 0] = k2 * phi  + k1 * (np.tanh(r) / r) * np.sin(phi) * np.cos(phi)

    if (abs(P.pSC.Ud[0, 0]) < vmin) and (P.pSC.Ud[0, 0] < 0):
        P.pSC.Ud[0, 0] = -vmin
    
    if (abs(P.pSC.Ud[0, 0]) < vmin) and (P.pSC.Ud[0, 0] > 0):
        P.pSC.Ud[0, 0] = vmin

    return P

def Attacker4(P, gain = [1, .1]):
   vmax = P.pPar.vmax
   wmax = P.pPar.wmax

   k1 = gain[0]
   k2 = gain[1]

   xball = P.pPos.Xd[0,0]
   yball = P.pPos.Xd[1,0]
   
   xr = P.pPos.X[0,0]
   yr = P.pPos.X[1,0]
   yaw_r = P.pPos.X[5,0]


   phi = np.arctan2(yball - yr, xball - xr)
   alpha = normalizeAngle(- phi + yaw_r)


   if alpha > np.pi/2:
      k1 *= -1
      alpha -= np.pi
   elif alpha < -np.pi/2:
      k1 *= -1
      alpha += np.pi

   rho = np.sqrt((xball-xr)**2 + (yball-yr)**2)
   
   v = vmax * np.tanh(k1 * rho)
   w = wmax * alpha * k2

   P.pSC.Ud[0, 0] = v
   P.pSC.Ud[1, 0] = w
   
   return P

def Attacker5(P, B, gain = [1, .1]):
   vmax = P.pPar.vmax
   wmax = P.pPar.wmax

   k1 = gain[0]
   k2 = gain[1]

   xball = B.pPos.X[0,0]
   yball = B.pPos.X[1,0]
   vxball = B.pPos.X[6, 0]
   vyball = B.pPos.X[7, 0]
   
   xr = P.pPos.X[0,0]
   yr = P.pPos.X[1,0]
   yaw_r = P.pPos.X[5,0]
   vxr = P.pPos.X[6, 0]
   vyr = P.pPos.X[7, 0]


   phi = np.arctan2(yball - yr, xball - xr)
   alpha = normalizeAngle(- phi + yaw_r)


   if alpha > np.pi/2:
      k1 *= -1
      alpha -= np.pi
   elif alpha < -np.pi/2:
      k1 *= -1
      alpha += np.pi

   rho = np.sqrt((xball-xr)**2 + (yball-yr)**2)
   drho = ((xball - xr) * (vxball - vxr) + (yball - yr) * (vyball - vyr)) / rho
#    print('drho: %.5f, vxball: %.5f, vxr: %.5f' %(drho,vxball,vxr))
   
   v = vmax * np.tanh(k1 * rho) + drho * 0.1
   w = wmax * alpha * k2

   P.pSC.Ud[0, 0] = v
   P.pSC.Ud[1, 0] = w
   
   return P

def Attacker6(P, P2, B, gain = [1, .1]):
   vmax = P.pPar.vmax
   wmax = P.pPar.wmax

   k1 = gain[0]
   k2 = gain[1]

   xball = B.pPos.X[0,0]
   yball = B.pPos.X[1,0]
   vxball = B.pPos.X[6, 0]
   vyball = B.pPos.X[7, 0]
   
   xr = P.pPos.X[0,0]
   yr = P.pPos.X[1,0]
   yaw_r = P.pPos.X[5,0]
   vxr = P.pPos.X[6, 0]
   vyr = P.pPos.X[7, 0]

   x_partener = P2.pPos.X[0, 0]
   y_partener = P2.pPos.X[1, 0]

   phi = np.arctan2(yball - yr, xball - xr)
   alpha = normalizeAngle(- phi + yaw_r)


   if alpha > np.pi/2:
      k1 *= -1
      alpha -= np.pi
   elif alpha < -np.pi/2:
      k1 *= -1
      alpha += np.pi

   rho = np.sqrt((xball-xr) ** 2 + (yball-yr) ** 2)
   drho = ((xball - xr) * (vxball - vxr) + (yball - yr) * (vyball - vyr)) / rho

   rho_partener = np.sqrt((x_partener - xr)**2 + (y_partener - yr)**2)
   #print(f'Rho_par: {rho_partener}, k1: {k1}')
   
   v = vmax * np.tanh(k1 * rho) + drho * 0.1 -  0.05 * k1 / rho_partener
   w = wmax * alpha * k2

   P.pSC.Ud[0, 0] = v
   P.pSC.Ud[1, 0] = w

   return P

def distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def circunference(x, R, x0=0, y0=0):
    return np.sqrt(R**2 - (x - x0)**2) + y0


def normalizeAngle(angle):
    return np.mod(angle+np.pi, 2*np.pi) - np.pi