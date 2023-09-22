import pygame as pg
import time
from Controle.Class_Control import*
import serial

# Inicializa a biblioteca pg
pg.init()

Var_MyTeam_Color_BGR = np.array([0,255,255])
Color_Player_1 = np.array([255,0,0])
Var_AttackSide = 1
Var_P1_Function = 0

# Inicializa os robôs(pode dar erro pq a gente tem q fornecer alguns parâmetros, verifica isso por favor)
robots = [MY_TEAM(Var_MyTeam_Color_BGR,Color_Player_1,Var_AttackSide,Var_P1_Function), MY_TEAM(Var_MyTeam_Color_BGR,Color_Player_1,Var_AttackSide,Var_P1_Function)]
print(robots)

# Captura os joysticks
joysticks = []
for i in range(pg.joystick.get_count()):
    joystick = pg.joystick.Joystick(i)
    joystick.init()
    joysticks.append(joystick)

def check_analog(joysticks, robots):
    for i,joystick in enumerate(joysticks):
        x_axis = joystick.get_axis(2)
        y_axis = joystick.get_axis(1)
        left_speed = int(-y_axis * 60 - x_axis * 15)
        right_speed = int(-y_axis * 60 + x_axis * 15)        
        left_speed,right_speed = set_speed(left_speed,right_speed)
        robots[i].rBDP_pSC_PWM = np.array([[left_speed + 150, right_speed + 150]]).T
                    
def check_RT(joysticks, robots):
    for i,joystick in enumerate(joysticks):
       
        robots[i].rBDP_pSC_PWM = np.array([[50,250]]).T
def check_LT(joysticks, robots):
    for i,joystick in enumerate(joysticks):
        robots[i].rBDP_pSC_PWM = np.array([[250,50]]).T

# Seta os maximos do sinal
def set_speed(left ,right):
    left_speed = max(min(left,100),-100)
    right_speed = max(min(right,100),-100)
    return left_speed,right_speed

start = time.time()
porta = serial.Serial('COM9', 115200, timeout=2)
porta.close()
porta.open()

# while True:
#     porta.write([1, 2, 50, 250, 200, 100, 50, 250, 3, 10])
#     # if time.time() - start > 1:
#     #     break            
# 
# Loop principal
while True:
    # Captura eventos dos joysticks
    for event in pg.event.get():
        
        if event.type == pg.JOYAXISMOTION:
            # Lê os valores dos joysticks
            check_analog(joysticks, robots)

        if event.type == pg.JOYBUTTONDOWN:

                if event.button == 4:
                    # print('LB')
                    check_LT(joysticks, robots)
                if event.button == 5:
                    # print('RB')
                    check_RT(joysticks, robots)  
            
    # Aguarda um tempo para evitar sobrecarga do processador(pode tirar se quiser)
    time.sleep(0.001)
    print(robots[1].rBDP_pSC_PWM[0,0],robots[1].rBDP_pSC_PWM[1,0])
    #tem que escrever na porta com a função que a gente tem.(não sei qual é)
    # porta.write([1, 2, int(robots[0].rBDP_pSC_PWM[0,0]), int(robots[0].rBDP_pSC_PWM[1,0]), int(150), int(150), int(150), int(150), 3, 10])
    porta.write([1, 2, int(robots[0].rBDP_pSC_PWM[0,0]), int(robots[0].rBDP_pSC_PWM[1,0]), int(robots[1].rBDP_pSC_PWM[0,0]), int(robots[1].rBDP_pSC_PWM[1,0]), int(150), int(150), 3, 10])
    