import numpy as np
from Robo_BDP.Classe_JOG import Player, Ball
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

def Attacker5(P, B, gain = [1.5, .07]):
   vmax = P.pPar.vmax
   wmax = P.pPar.wmax
   c = 5e-2

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

    # Setando a posição desejado como uma posição ficticia atrás da bola,
    # porém com o mesmo angulo entre a bola e o centro do gol do adversário
   xd = xball - c if abs(xball - c) < 0.7 else xball
   yd = yball + c * np.sin(phi) if abs(yball + c * np.sin(phi)) < 0.6 else yball 


   if alpha > np.pi/2:
      k1 *= -1
      alpha -= np.pi
   elif alpha < -np.pi/2:
      k1 *= -1
      alpha += np.pi

   rho = np.sqrt((xball-xr)**2 + (yball-yr)**2)
   drho = ((xball - xr) * (vxball - vxr) + (yball - yr) * (vyball - vyr)) / rho
   
   v = vmax * np.tanh(k1 * rho) + drho * 0.1
   w = wmax * alpha * k2

   P.pSC.Ud[0, 0] = v
   P.pSC.Ud[1, 0] = w


   if rho < 7/100:
    P.pSC.Ud[0, 0] = 0
    if np.abs(phi) < np.pi/2:
        if phi < 0:
            P.pSC.Ud[1, 0] = wmax
        else:
            P.pSC.Ud[1, 0] = -wmax
    else:
        if phi < 0:
            P.pSC.Ud[1, 0] = wmax
        else:
            P.pSC.Ud[1, 0] = -wmax    

   
   return P

def Attacker6(P, P2, B, gain = [1.5, .07]):
    vmax = P.pPar.vmax
    wmax = P.pPar.wmax

    k1 = gain[0]
    k2 = gain[1]
    krepulsive = k1

    xball = B.pPos.X[0,0]
    yball = B.pPos.X[1,0]
    vxball = B.pPos.X[6, 0]
    vyball = B.pPos.X[7, 0]

    xr = P.pPos.Xc[0,0]
    yr = P.pPos.Xc[1,0]
    yaw_r = P.pPos.X[5,0]
    vxr = P.pPos.X[6, 0]
    vyr = P.pPos.X[7, 0]

    x_partener = P2.pPos.X[0, 0]
    y_partener = P2.pPos.X[1, 0]

    phi = np.arctan2(yball - yr, xball - xr)
    alpha = normalizeAngle(- phi + yaw_r)

    theta = np.arctan2(yball, xball - 0.8)
    xd = xball  #- c if abs(xball - c) < 0.7 else xball
    yd =  yball #+ c * np.sin(theta) if abs(yball + c * np.sin(theta)) < 0.6 else yball 


    if alpha > np.pi/2:
        k1 *= -1
        krepulsive *= -1
        alpha -= np.pi
    elif alpha < -np.pi/2:
        k1 *= -1
        krepulsive *= -1
        alpha += np.pi

    rho = np.sqrt((xd-xr) ** 2 + (yd-yr) ** 2)
    rho_original = rho
    drho = ((xball - xr) * (vxball - vxr) + (yball - yr) * (vyball - vyr)) / rho
    rho_partener = np.sqrt((x_partener - xr)**2 + (y_partener - yr)**2)

    if rho < 0.15:
        rho *= 2

    if distance((xr, yr), (xball, yball)) - distance((x_partener, y_partener), (xball, yball)) < 0:
        krepulsive = 0  

    v = vmax * np.tanh(k1 * rho) + drho * 0.1 -  0.05 * krepulsive / rho_partener
    w = wmax * alpha * k2

    P.pSC.Ud[0, 0] = v
    P.pSC.Ud[1, 0] = w

    if rho_original < 8 / 100:
        if yr >= 0:
            if abs(phi) < np.pi / 4:
                P.pSC.Ud[1, 0] = -wmax
            elif -np.pi/4 > phi > -3 * np.pi / 4:
                P.pSC.Ud[1, 0] = wmax
            elif np.pi/4 < phi < 3 * np.pi / 4:
                P.pSC.Ud[1, 0] = -wmax
            else:
                P.pSC.Ud[1, 0] = -wmax
        else:
            if abs(phi) < np.pi / 4:
                P.pSC.Ud[1, 0] = wmax
            elif -np.pi/4 > phi > -3 * np.pi / 4:
                P.pSC.Ud[1, 0] = wmax
            elif np.pi/4 < phi < 3 * np.pi / 4:
                P.pSC.Ud[1, 0] = -wmax
            else:
                P.pSC.Ud[1, 0] = wmax
    return P

def Defenser6(P, B, gain = [1.5, .07]):
    vmax = P.pPar.vmax
    wmax = P.pPar.wmax

    k1 = gain[0]
    k2 = gain[1]

    xball = B.pPos.X[0,0]
    yball = B.pPos.X[1,0]
    vxball = B.pPos.X[6, 0]
    vyball = B.pPos.X[7, 0]

    xr = P.pPos.Xc[0,0]
    yr = P.pPos.Xc[1,0]
    yaw_r = P.pPos.X[5,0]
    vxr = P.pPos.X[6, 0]
    vyr = P.pPos.X[7, 0]

    xd = xball if xball > 0.56 else 0.60
    
    if abs(yball) < 0.31:
        yd = yball
    elif yball > 0:
        yd = 0.31
    else:
        yd = -0.31

    phi = np.arctan2(yd - yr, xd - xr)
    alpha = normalizeAngle(- phi + yaw_r)
    theta = np.arctan2(yd, xd - 0.8)
    
    if alpha > np.pi/2:
        k1 *= -1
        alpha -= np.pi
    elif alpha < -np.pi/2:
        k1 *= -1
        alpha += np.pi

    rho = np.sqrt((xd-xr) ** 2 + (yd-yr) ** 2)
    rho_ball = np.sqrt((xball-xr) ** 2 + (yball-yr) ** 2)
    #drho = ((xball - xr) * (vxball - vxr) + (yball - yr) * (vyball - vyr)) / rho

    if rho < 0.15:
        rho *= 2

    v = vmax * np.tanh(k1 * rho) #+ drho * 0.1
    w = wmax * alpha * k2

    P.pSC.Ud[0, 0] = v
    P.pSC.Ud[1, 0] = w

    if rho_ball < 8 / 100:
        if yr >= 0:
            if abs(phi) < np.pi / 4:
                P.pSC.Ud[1, 0] = -wmax
            elif -np.pi/4 > phi > -3 * np.pi / 4:
                P.pSC.Ud[1, 0] = wmax
            elif np.pi/4 < phi < 3 * np.pi / 4:
                P.pSC.Ud[1, 0] = -wmax
            else:
                P.pSC.Ud[1, 0] = -wmax
        else:
            if abs(phi) < np.pi / 4:
                P.pSC.Ud[1, 0] = wmax
            elif -np.pi/4 > phi > -3 * np.pi / 4:
                P.pSC.Ud[1, 0] = wmax
            elif np.pi/4 < phi < 3 * np.pi / 4:
                P.pSC.Ud[1, 0] = -wmax
            else:
                P.pSC.Ud[1, 0] = wmax
    return P

def Defenser(P, P2, B, gain = [1.5, .07]):
   vmax = P.pPar.vmax
   wmax = P.pPar.wmax

   k1 = gain[0]
   k2 = gain[1]
   krepulsive = k1

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
      krepulsive *= -1
      alpha -= np.pi
   elif alpha < -np.pi/2:
      k1 *= -1
      krepulsive *= -1
      alpha += np.pi

   rho = np.sqrt((xball-xr) ** 2 + (yball-yr) ** 2)
   drho = ((xball - xr) * (vxball - vxr) + (yball - yr) * (vyball - vyr)) / rho

   rho_partener = np.sqrt((x_partener - xr)**2 + (y_partener - yr)**2)

   if distance((xr, yr), (xball, yball)) - distance((x_partener, y_partener), (xball, yball)) < 0:
       krepulsive = 0
   
   v = vmax * np.tanh(k1 * rho) + drho * 0.1 -  0.05 * krepulsive / rho_partener
   w = wmax * alpha * k2

   P.pSC.Ud[0, 0] = v
   P.pSC.Ud[1, 0] = w

   if rho < 7/100:
        P.pSC.Ud[0, 0] = 0
        if np.abs(phi) < np.pi/2:
            if phi < 0:
                P.pSC.Ud[1, 0] = wmax
            else:
                P.pSC.Ud[1, 0] = -wmax
        else:
            if phi < 0:
                P.pSC.Ud[1, 0] = wmax
            else:
                P.pSC.Ud[1, 0] = -wmax   

   return P


def OfficialAttacker_Save(P : Player, P2 : Player, G : Player, B : Ball, gain : list = [1.5, .07]) -> Player:
    vmax = P.pPar.vmax
    wmax = P.pPar.wmax

    k1 = gain[0]
    k2 = gain[1]
    krepulsive = k1
    kgk = k1

    xball = B.pPos.X[0,0]
    yball = B.pPos.X[1,0]
    vxball = B.pPos.X[6, 0]
    vyball = B.pPos.X[7, 0]

    xr = P.pPos.Xc[0,0]
    yr = P.pPos.Xc[1,0]
    yaw_r = P.pPos.X[5,0]
    vxr = P.pPos.X[6, 0]
    vyr = P.pPos.X[7, 0]

    x_partener = P2.pPos.X[0, 0]
    y_partener = P2.pPos.X[1, 0]

    x_goal_kp = G.pPos.X[0, 0]
    y_goal_kp = G.pPos.X[1, 0]

    phi = np.arctan2(yball - yr, xball - xr)
    alpha = normalizeAngle(- phi + yaw_r)

    xd = xball  
    yd =  yball 

    if alpha > np.pi/2:
        k1 *= -1
        kgk *= -1
        krepulsive *= -1
        alpha -= np.pi
    elif alpha < -np.pi/2:
        k1 *= -1
        kgk *= -1
        krepulsive *= -1
        alpha += np.pi

    rho = np.sqrt((xd-xr) ** 2 + (yd-yr) ** 2)
    rho_original = rho
    drho = ((xball - xr) * (vxball - vxr) + (yball - yr) * (vyball - vyr)) / rho
    rho_partener = np.sqrt((x_partener - xr)**2 + (y_partener - yr)**2)
    rho_gk = np.sqrt((x_goal_kp - xr)**2 + (y_goal_kp - yr)**2)

    if rho < 0.15:
        rho *= 2

    if distance((xr, yr), (xball, yball)) - distance((x_partener, y_partener), (xball, yball)) < 0:
        krepulsive = 0

    if abs(yball) > 0.31:
        kgk = 0
        

    v = vmax * np.tanh(k1 * rho) + drho * 0.1 -  0.05 * krepulsive / rho_partener - 0.25 * kgk / rho_gk
    w = wmax * alpha * k2

    P.pSC.Ud[0, 0] = v
    P.pSC.Ud[1, 0] = w

    if P.LadoAtaque == -1 :
        if rho_original < 8 / 100:
            if yr >= 0:
                if abs(phi) < np.pi / 4:
                    P.pSC.Ud[1, 0] = -wmax
                elif -np.pi/4 > phi > -3 * np.pi / 4:
                    P.pSC.Ud[1, 0] = wmax
                elif np.pi/4 < phi < 3 * np.pi / 4:
                    P.pSC.Ud[1, 0] = -wmax
                else:
                    P.pSC.Ud[1, 0] = -wmax
            else:
                if abs(phi) < np.pi / 4:
                    P.pSC.Ud[1, 0] = wmax
                elif -np.pi/4 > phi > -3 * np.pi / 4:
                    P.pSC.Ud[1, 0] = wmax
                elif np.pi/4 < phi < 3 * np.pi / 4:
                    P.pSC.Ud[1, 0] = -wmax
                else:
                    P.pSC.Ud[1, 0] = wmax
    else:
        if rho_original < 8 / 100:
            if yr >= 0:
                if abs(phi) < np.pi / 4:
                    P.pSC.Ud[1, 0] = wmax
                elif -np.pi/4 > phi > -3 * np.pi / 4:
                    P.pSC.Ud[1, 0] = -wmax
                elif np.pi/4 < phi < 3 * np.pi / 4:
                    P.pSC.Ud[1, 0] = wmax
                else:
                    P.pSC.Ud[1, 0] = wmax
            else:
                if abs(phi) < np.pi / 4:
                    P.pSC.Ud[1, 0] = -wmax
                elif -np.pi/4 > phi > -3 * np.pi / 4:
                    P.pSC.Ud[1, 0] = -wmax
                elif np.pi/4 < phi < 3 * np.pi / 4:
                    P.pSC.Ud[1, 0] = wmax
                else:
                    P.pSC.Ud[1, 0] = -wmax
    return P



def OfficialAttacker(P : Player, P2 : Player, G : Player, B : Ball, gain : list = [1.5, .07]) -> Player:
    vmax = P.pPar.vmax
    wmax = P.pPar.wmax

    k1 = gain[0]
    k2 = gain[1]
    krepulsive = k1
    kgk = k1
    kv = 1

    xball = B.pPos.X[0,0]
    yball = B.pPos.X[1,0]
    vxball = B.pPos.X[6, 0]
    vyball = B.pPos.X[7, 0]

    xr = P.pPos.Xc[0,0]
    yr = P.pPos.Xc[1,0]
    yaw_r = P.pPos.X[5,0]
    vxr = P.pPos.X[6, 0]
    vyr = P.pPos.X[7, 0]

    x_partener = P2.pPos.X[0, 0]
    y_partener = P2.pPos.X[1, 0]

    x_goal_kp = G.pPos.X[0, 0]
    y_goal_kp = G.pPos.X[1, 0]

    phi = np.arctan2(yball - yr, xball - xr)
    alpha = normalizeAngle(- phi + yaw_r)

    

    xd = xball  
    yd =  yball 

    if alpha > np.pi/2:
        kv *= -1
        k1 *= -1
        kgk *= -1
        krepulsive *= -1
        alpha -= np.pi
    elif alpha < -np.pi/2:
        kv *= -1
        k1 *= -1
        kgk *= -1
        krepulsive *= -1
        alpha += np.pi

    rho = np.sqrt((xd-xr) ** 2 + (yd-yr) ** 2)
    rho_original = rho
    drho = ((xball - xr) * (vxball - vxr) + (yball - yr) * (vyball - vyr)) / rho
    rho_partener = np.sqrt((x_partener - xr)**2 + (y_partener - yr)**2)
    rho_gk = np.sqrt((x_goal_kp - xr)**2 + (y_goal_kp - yr)**2)

    #if rho < 0.15:
    #    rho *= 2

    if distance((xr, yr), (xball, yball)) - distance((x_partener, y_partener), (xball, yball)) < 0:
        krepulsive = 0

    if abs(yball) > 0.31:
        kgk = 0
    
    #if abs(rho) < 0.15:
    #    k1 *= 1.1

    
    if rho < 0.50 and alpha < np.deg2rad(10):
        vmod = np.sqrt(vxball ** 2 + vyball ** 2) * kv * .09
    else: # Ultima mudança que eu fiz!
        vmod = 0.22515 * kv # Ao inves de ser zero eu configurei uma velocidade minima (100 RPM)
        
    print(vxball, vyball, vmod)
    v = vmax * np.tanh(k1 * rho) + drho * 0.01 -  0.04 * krepulsive / rho_partener - 0.04 * kgk / rho_gk + vmod
    w = wmax * alpha * k2

    P.pSC.Ud[0, 0] = v
    P.pSC.Ud[1, 0] = w

    # print(np.rad2deg(phi))

    if P.LadoAtaque == -1 :
        if rho_original < 7 / 100:
            if yr >= 0:
                if abs(phi) < np.pi / 4:
                    P.pSC.Ud[1, 0] = -wmax

                elif -np.pi/4 > phi > -3 * np.pi / 4:
                    P.pSC.Ud[1, 0] = wmax
                elif np.pi/4 < phi < 3 * np.pi / 4:
                    P.pSC.Ud[1, 0] = -wmax
                else:
                    k1 = gain[0]
                    k2 = gain[1]
                    krepulsive = k1
                    kgk = k1
                    phi = np.arctan2(0 - yr, -.8 - xr)
                    alpha = normalizeAngle(- phi + yaw_r)
                    if alpha > np.pi/2:
                        k1 *= -1
                        kgk *= -1
                        krepulsive *= -1
                        alpha -= np.pi
                    elif alpha < -np.pi/2:
                        k1 *= -1
                        kgk *= -1
                        krepulsive *= -1
                        alpha += np.pi

                    w = wmax * alpha * k2
                    P.pSC.Ud[0, 0] = vmax * np.tanh(k1) 
                    P.pSC.Ud[1, 0] = w
            else:
                if abs(phi) < np.pi / 4:
                    P.pSC.Ud[1, 0] = wmax
                    
                elif -np.pi/4 > phi > -3 * np.pi / 4:
                    P.pSC.Ud[1, 0] = wmax
                elif np.pi/4 < phi < 3 * np.pi / 4:
                    P.pSC.Ud[1, 0] = -wmax
                else:
                    k1 = gain[0]
                    k2 = gain[1]
                    krepulsive = k1
                    kgk = k1
                    phi = np.arctan2(0 - yr, -.8 - xr)
                    alpha = normalizeAngle(- phi + yaw_r)
                    if alpha > np.pi/2:
                        k1 *= -1
                        kgk *= -1
                        krepulsive *= -1
                        alpha -= np.pi
                    elif alpha < -np.pi/2:
                        k1 *= -1
                        kgk *= -1
                        krepulsive *= -1
                        alpha += np.pi

                    w = wmax * alpha * k2
                    P.pSC.Ud[0, 0] = vmax * np.tanh(k1) 
                    P.pSC.Ud[1, 0] = w
                    
    else: # Ataca para positivo
        if rho_original < 7 / 100:
            if yr >= 0:
                if abs(phi) < np.pi / 4:
                    k1 = gain[0]
                    k2 = gain[1]
                    krepulsive = k1
                    kgk = k1
                    phi = np.arctan2(0 - yr, .8 - xr)
                    alpha = normalizeAngle(- phi + yaw_r)
                    if alpha > np.pi/2:
                        k1 *= -1
                        kgk *= -1
                        krepulsive *= -1
                        alpha -= np.pi
                    elif alpha < -np.pi/2:
                        k1 *= -1
                        kgk *= -1
                        krepulsive *= -1
                        alpha += np.pi

                    w = wmax * alpha * k2
                    P.pSC.Ud[0, 0] = vmax * np.tanh(k1) 
                    P.pSC.Ud[1, 0] = w
                elif -np.pi/4 > phi > -3 * np.pi / 4:
                    P.pSC.Ud[1, 0] = -wmax
                elif np.pi/4 < phi < 3 * np.pi / 4:
                    P.pSC.Ud[1, 0] = wmax
                else:
                    P.pSC.Ud[1, 0] = wmax
            else:
                if abs(phi) < np.pi / 4:
                    k1 = gain[0]
                    k2 = gain[1]
                    krepulsive = k1
                    kgk = k1
                    phi = np.arctan2(0 - yr, .8 - xr)
                    alpha = normalizeAngle(- phi + yaw_r)
                    if alpha > np.pi/2:
                        k1 *= -1
                        kgk *= -1
                        krepulsive *= -1
                        alpha -= np.pi
                    elif alpha < -np.pi/2:
                        k1 *= -1
                        kgk *= -1
                        krepulsive *= -1
                        alpha += np.pi

                    w = wmax * alpha * k2
                    P.pSC.Ud[0, 0] = vmax * np.tanh(k1) 
                    P.pSC.Ud[1, 0] = w
                    
                elif -np.pi/4 > phi > -3 * np.pi / 4:
                    P.pSC.Ud[1, 0] = -wmax
                elif np.pi/4 < phi < 3 * np.pi / 4:
                    P.pSC.Ud[1, 0] = wmax
                else:
                    P.pSC.Ud[1, 0] = -wmax
    return P


def OfficialDefenser(P : Player, B : Player, gain = [1.5, .07]):
    vmax = P.pPar.vmax
    wmax = P.pPar.wmax
    dt = 70e-3

    k1 = gain[0]
    k2 = gain[1]

    xball = B.pPos.X[0,0]
    yball = B.pPos.X[1,0]
    vxball = B.pPos.X[6, 0]
    vyball = B.pPos.X[7, 0]

    xr = P.pPos.Xc[0,0]
    yr = P.pPos.Xc[1,0]
    yaw_r = P.pPos.X[5,0]
    vxr = P.pPos.X[6, 0]
    vyr = P.pPos.X[7, 0]

    if P.LadoAtaque == -1 :
        center_goal = 0.72
        lim_goal = 0.56
        xd = xball + vxball * dt if xball > lim_goal else center_goal
    else:
        center_goal = -0.72
        lim_goal = -0.56
        xd = xball + vxball * dt if xball < lim_goal else center_goal

    
    
    if abs(yball) < 0.31:
        yd = yball + vyball * dt
    elif yball > 0:
        yd = 0.31
    else:
        yd = -0.31

    phi = np.arctan2(yd - yr, xd - xr)
    alpha = normalizeAngle(- phi + yaw_r)
    theta = np.arctan2(yd, xd - 0.8)
    
    if alpha > np.pi/2:
        k1 *= -1
        alpha -= np.pi
    elif alpha < -np.pi/2:
        k1 *= -1
        alpha += np.pi

    rho = np.sqrt((xd-xr) ** 2 + (yd-yr) ** 2)
    rho_ball = np.sqrt((xball-xr) ** 2 + (yball-yr) ** 2)
    drho = ((xball - xr) * (vxball - vxr) + (yball - yr) * (vyball - vyr)) / rho_ball

    if rho < 0.15:
        rho *= 2

    v = vmax * np.tanh(k1 * rho) - drho * 0.25
    w = wmax * alpha * k2

    P.pSC.Ud[0, 0] = v
    P.pSC.Ud[1, 0] = w

    if P.LadoAtaque == -1 :
        if rho_ball < 8 / 100:
            if yr >= 0:
                if abs(phi) < np.pi / 4:
                    P.pSC.Ud[1, 0] = -wmax
                elif -np.pi/4 > phi > -3 * np.pi / 4:
                    P.pSC.Ud[1, 0] = wmax
                elif np.pi/4 < phi < 3 * np.pi / 4:
                    P.pSC.Ud[1, 0] = -wmax
                else:
                    P.pSC.Ud[1, 0] = -wmax
            else:
                if abs(phi) < np.pi / 4:
                    P.pSC.Ud[1, 0] = wmax
                elif -np.pi/4 > phi > -3 * np.pi / 4:
                    P.pSC.Ud[1, 0] = wmax
                elif np.pi/4 < phi < 3 * np.pi / 4:
                    P.pSC.Ud[1, 0] = -wmax
                else:
                    P.pSC.Ud[1, 0] = wmax
    else:
        if rho_ball < 8 / 100:
            if yr >= 0:
                if abs(phi) < np.pi / 4:
                    P.pSC.Ud[1, 0] = wmax
                elif -np.pi/4 > phi > -3 * np.pi / 4:
                    P.pSC.Ud[1, 0] = -wmax
                elif np.pi/4 < phi < 3 * np.pi / 4:
                    P.pSC.Ud[1, 0] = wmax
                else:
                    P.pSC.Ud[1, 0] = wmax
            else:
                if abs(phi) < np.pi / 4:
                    P.pSC.Ud[1, 0] = -wmax
                elif -np.pi/4 > phi > -3 * np.pi / 4:
                    P.pSC.Ud[1, 0] = -wmax
                elif np.pi/4 < phi < 3 * np.pi / 4:
                    P.pSC.Ud[1, 0] = wmax
                else:
                    P.pSC.Ud[1, 0] = -wmax
    return P


def new_controller(P : Player, B : Player, gain = [1.5, .07]):
    vmax = P.pPar.vmax
    wmax = P.pPar.wmax

    k1 = gain[0]
    k2 = gain[1]
    krepulsive = k1
    kgk = k1
    kv = 1

    xball = B.pPos.X[0,0]
    yball = B.pPos.X[1,0]
    vxball = B.pPos.X[6, 0]
    vyball = B.pPos.X[7, 0]

    xr = P.pPos.Xc[0,0]
    yr = P.pPos.Xc[1,0]
    yaw_r = P.pPos.X[5,0]
    vxr = P.pPos.X[6, 0]
    vyr = P.pPos.X[7, 0]

    phi = np.arctan2(yball - yr, xball - xr)
    alpha = normalizeAngle(- phi + yaw_r)

    xd = xball  
    yd =  yball 

    K = np.array([[np.cos(yaw_r), np.sin(yaw_r)],
         [-np.sin(yaw_r), np.cos(yaw_r)]])
    
    X = np.array([[vxball + 1 * (xball - xr)],
         [vyball + 1 * (yball - yr)]])
    


def distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def circunference(x, R, x0=0, y0=0):
    return np.sqrt(R**2 - (x - x0)**2) + y0


def normalizeAngle(angle):
    return np.mod(angle+np.pi, 2*np.pi) - np.pi