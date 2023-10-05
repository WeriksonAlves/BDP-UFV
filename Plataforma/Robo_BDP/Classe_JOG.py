import numpy as np
import math
from matplotlib.patches import Polygon
import matplotlib.pyplot as plt

class Player:
    def __init__(self, ID=0, LadoAtaque=0, Funcao=0):
        # Properties or Parameters
        self.pCAD = None  # Pioneer 3DX 3D image
        self.pID = ID     # Identification
        self.LadoAtaque = LadoAtaque
        self.Funcao = Funcao

        # Navigation Data and Communication
        self.pData = None  # Flight Data
        self.pCom = None   # Communication

        # Initialize control variables, parameters, and flags
        self.iControlVariables()
        self.iParameters()
        self.iFlags()

        # # Load and make CAD
        # self.mCADload()
        self.mCADmake()

        # self._Kinematicmodeling = np.array([[np.cos(self.pPos.X[5,0]), -self.pPar.a * np.sin(self.pPos.X[5,0] + self.pPar.alpha)],
        #                                     [np.sin(self.pPos.X[5,0]),  self.pPar.a * np.cos(self.pPos.X[5,0] + self.pPar.alpha)],
        #                                     [0, 1]])

    def iControlVariables(self):
        """
        Control variable initialization
        """
        self.pPos = pPos()
        self.pSC = pSC()

    def iParameters(self):
        """
        Parameter initialization
        """
        self.pPar = pPar()

    def iFlags(self):
        """
        Flag initialization
        """
        self.pFlag = iFlags()
        
    def sKinematicModel(self):
        """
        Update the robot's pose based on the control signal using the kinematic model.

        Args:
            p3dx: An instance of the Pioneer3DX class.
        """
        # Kinematic Matrix
        K = np.array([
            [np.cos(self.pPos.X[5,0]), -self.pPar.a * np.sin(self.pPos.X[5,0] + self.pPar.alpha)],
            [np.sin(self.pPos.X[5,0]), self.pPar.a * np.cos(self.pPos.X[5,0] + self.pPar.alpha)],
            [0, 1]
        ])

        # Current position
        # self.pPos.X[[0, 1, 5]] = self.pPos.Xd[[0, 1, 5]]
        # print('Posição', self.pPos.X[[0, 1, 5]])
        self.pPos.X[[0, 1, 5]] = self.pPos.X[[0, 1, 5]] + K @ self.pSC.U[[0, 1]] * self.pPar.Ts
        # print('Mudança', K @ self.pSC.U[[0, 1]] * self.pPar.Ts)
        
        # First-time derivative of the current position
        self.pPos.X[[6, 7, 11]] = np.dot(K, self.pSC.U[[0, 1]])

        # Angle limitation per quadrant
        for ii in range(3, 6):
            if abs(self.pPos.X[ii]) > np.pi:
                if self.pPos.X[ii] < 0:
                    self.pPos.X[ii] = self.pPos.X[ii] + 2 * np.pi
                else:
                    self.pPos.X[ii] = self.pPos.X[ii] - 2 * np.pi

        # Pose of the robot's center
        self.pPos.Xc[[0, 1, 5]] = self.pPos.X[[0, 1, 5]] - np.dot(np.array([[np.cos(self.pPos.X[5,0]), -np.sin(self.pPos.X[5,0]), 0],
                                                                            [np.sin(self.pPos.X[5,0]), np.cos(self.pPos.X[5,0]), 0],
                                                                            [0, 0, 1]]), 
                                                                  np.array([[self.pPar.a * np.cos(self.pPar.alpha)],
                                                                            [self.pPar.a * np.sin(self.pPar.alpha)],
                                                                            [0]]))
        
    def sInvKinematicModel(self, dXr):
        """
        Calculate the robot velocity based on the reference velocity using the inverse kinematic model.

        Args:
            dXr: A 2x1 or 3x1 NumPy array representing the reference velocity [dx, dy] or [dx, dy, dtheta].

        Returns:
            Ur: A 2x1 or 3x1 NumPy array representing the calculated robot velocity [V, omega].
        """
        # Determine vector length
        l = len(dXr)

        if l == 2:
            # Inverse Kinematic Matrix (2D)
            Kinv = np.array([
                [np.cos(self.pPos.X[5,0]), np.sin(self.pPos.X[5,0])],
                [-np.sin(self.pPos.X[5,0]) / self.pPar.a, np.cos(self.pPos.X[5,0]) / self.pPar.a]
            ])
        elif l == 3:
            # Inverse Kinematic Matrix (3D)
            Kinv = np.array([
                [np.cos(self.pPos.X[5,0]), np.sin(self.pPos.X[5,0]), 0],
                [-np.sin(self.pPos.X[5,0]) / self.pPar.a, np.cos(self.pPos.X[5,0]) / self.pPar.a, 0],
                [0, 0, 0]
            ])
        else:
            print('Invalid vector length (please verify dXr).')
            Kinv = np.zeros((l, 3))

        # Reference control signal
        Ur = np.dot(Kinv, dXr)

        return Ur

    # Dynamic model
    def sDynamicModel(self):
        # Implement this method as needed
        pass

    def rSetPose(self, Xo):
        """
        Set the robot's pose.

        Args:
            Xo: A 1x4 NumPy array representing the new pose [x, y, z, psi].
                Defaults to None.
        """
        if Xo is not None:
            self.pPos.Xc[[0, 1, 2, 5]] = Xo


        translation_vector = np.array([
            [self.pPar.a * np.cos(self.pPar.alpha)],
            [self.pPar.a * np.sin(self.pPar.alpha)],
            [0],
            [1]
        ])

        rotation_matrix = np.array([[np.cos(self.pPos.X[5,0]), -np.sin(self.pPos.X[5,0]), 0, 0],
                                    [np.sin(self.pPos.X[5,0]), np.cos(self.pPos.X[5,0]), 0, 0],
                                    [0, 0, 1, 0],
                                    [0, 0, 0, 1]])

        

        new_pose = np.dot(rotation_matrix, translation_vector)
        new_pose[3,0] = self.pPos.Xc[[5]]
        
        self.pPos.X[[0, 1, 2, 5]] = self.pPos.Xc[[0, 1, 2, 5]] + new_pose

        self.pPos.Xa = self.pPos.X

        if self.pFlag.Connected:
            # The position is given in millimeters and
            # the heading in degrees
            self.set_pose(self.pPos.Xc[0,0] , self.pPos.Xc[1,0], self.pPos.Xc[5,0])

    def rGetSensorData(self):
        """
        Get sensor data and update robot pose.
        """
        # Store past position
        self.pPos.Xa = self.pPos.X.copy()

        if self.pFlag.Connected: # Real BDP - Robot pose             
            # Current position
            # print('Xc: [%.3f, %.3f, %.3f], ' %(self.pPos.Xc[0,0],self.pPos.Xc[1,0],self.pPos.Xc[5,0]), end='')

            self.pPos.X[[0, 1, 5]] = self.pPos.Xc[[0, 1, 5]] + np.dot(np.array([[np.cos(self.pPos.X[5,0]), -np.sin(self.pPos.X[5,0]), 0],
                                                                                [np.sin(self.pPos.X[5,0]), np.cos(self.pPos.X[5,0]), 0],
                                                                                [0, 0, 1]]), 
                                                                    np.array([[self.pPar.a * np.cos(self.pPar.alpha)],
                                                                                [self.pPar.a * np.sin(self.pPar.alpha)],
                                                                                [0]]))
            # print('X: [%.3f, %.3f, %.3f], ' %(self.pPos.X[0,0],self.pPos.X[1,0],self.pPos.X[5,0]), end='')

            # Robot velocities: First-time derivative of the current position
            self.pPos.X[[6, 7, 11]] = (self.pPos.X[[0, 1, 5]] - self.pPos.Xa[[0, 1, 5]]) / self.pPar.Ts

        else:
            # Simulation
            # Robot center position
            self.pPos.X[[0, 1, 5]] = self.pPos.Xc[[0, 1, 5]] + np.array([[self.pPar.a * math.cos(self.pPos.X[5,0])],
                                                                         [self.pPar.a * math.sin(self.pPos.X[5,0])],
                                                                         [0]])

    def rSendControlSignals(self):
        """
        Send control signals to the self.
        """
        K2 = self.pPar.r*np.array([[1/2, 1/2], [1/self.pPar.d, -1/self.pPar.d]])
        #  CRIAR: Normalizar valores entre -100 e 100%

        self.pSC.RPM = (np.linalg.inv(K2)@self.pSC.Ud)
        self.pSC.RPM = self.pSC.RPM*60/(2*np.pi) # Em RPM

        if self.pFlag.Connected:
            K2 = self.pPar.r*np.array([[1/2, 1/2], [1/self.pPar.d, -1/self.pPar.d]])
            #  CRIAR: Normalizar valores entre -100 e 100%

            self.pSC.RPM = (np.linalg.inv(K2)@self.pSC.Ud)
            self.pSC.RPM = self.pSC.RPM*60/(2*np.pi) # Em RPM
        else:
            self.pSC.U = self.pSC.Ud
            self.sKinematicModel()
            
    def __conver2byte(self, elements:np.array) -> str : 
        string_empty = ''
        for value in elements:
            string_empty += str(value) + ','
        string_empty = string_empty[:-1] + '\n'
        return string_empty.encode('utf-8')

    def get_x(self):
        # X(0)
        return self.pPos.X[0,0]

    def get_y(self):
        # X(1)
        return self.pPos.X[1,0]

    def get_psi(self):
        # X(3)
        return self.pPos.X[5,0]

    def get_vel(self):
        # Vel. Linear norma p.pPos.X 7,8,9
        return math.sqrt((self.pPos.X[6]) ** 2 + (self.pPos.X[7]) ** 2 + (self.pPos.X[8]) ** 2)

    def get_rotvel(self):
        # Vel. Angular norma p.pPos.X 10,11,12
        return math.sqrt((self.pPos.X[9]) ** 2 + (self.pPos.X[10]) ** 2 + (self.pPos.X[11]) ** 2)

    def set_vel(self, vel):
        # Definir a velocidade angular por p.pSC.U(2)
        self.pSC.U[0] = vel

    def set_rotvel(self, rotvel):
        # Definir a velocidade angular por p.pSC.U(2)
        self.pSC.U[1] = rotvel

    def set_pose(self, x,y,ang):
        # Transformação Homogênea:
        trans_matrix = np.array([[np.cos(ang), (-1) * np.sin(ang), 0, x],
                                 [np.sin(ang), np.cos(ang), 0, y],
                                 [0, 0, 1, 0],
                                 [0, 0, 0, 1]])

        self.square_points[0, :] = np.dot(trans_matrix, np.concatenate((self.origin[0, :], [0, 1]), axis=0))[0:2]

        self.square_points[1, :] = np.dot(trans_matrix, np.concatenate((self.origin[1, :], [0, 1]), axis=0))[0:2]

        self.square_points[2, :] = np.dot(trans_matrix, np.concatenate((self.origin[2, :], [0, 1]), axis=0))[0:2]

        self.square_points[3, :] = np.dot(trans_matrix, np.concatenate((self.origin[3, :], [0, 1]), axis=0))[0:2]

        self.shape.set_xy(self.square_points)

    def Draw(self, fig, axis):
        grid_1 = fig.add_subplot()
        grid_1.add_patch(self.shape)

    # Make CAD
    def mCADmake(self):
        # Simulation:
        self.square_points = np.array([[-0.04, -0.04],
                                       [-0.04, 0.04],
                                       [0.04, 0.04],
                                       [0.04, -0.04]])

        self.origin = np.array([[-0.04, -0.04],
                                [-0.04,  0.04],
                                [ 0.04,  0.04],
                                [ 0.04, -0.04]])

        self.shape = Polygon(self.square_points, closed=False)
    
    # Set CAD color
    def mCADcolor(self, color):
        self.shape.set_color(color)

    def ExecutarAcao(self):
        if self.Funcao == 0:
            print(f'Goleiro {self.Funcao}')
        elif self.Funcao == 1:
            print(f'Defensor {self.Funcao}')
        elif self.Funcao == 2:
            print(f'Atacante {self.Funcao}')








class Ball:
    def __init__(self):
        # Properties or Parameters
        self.pCAD = None  # Pioneer 3DX 3D image

        # Navigation Data and Communication
        self.pData = None  # Flight Data
        self.pCom = None   # Communication

        # Initialize control variables, parameters, and flags
        self.iControlVariables()
        self.iParameters()
        self.iFlags()

    def iControlVariables(self):
        """
        Control variable initialization
        """
        self.pPos = pPos()
        self.pSC = pSC()

    def iParameters(self):
        """
        Parameter initialization
        """
        self.pPar = pPar()
        self.pPar.a = 0  # point of control
        self.pPar.alpha = 0  # angle of control
        self.pPar.r = 21.25e-3 # Raio da roda
        self.pPar.d = 21.25e-3 # Larguda do robôs

    def iFlags(self):
        """
        Flag initialization
        """
        self.pFlag = iFlags()
        
    def bGetSensorData(self):
        """
        Get sensor data and update ball pose.
        """
        # Store past position
        self.pPos.Xa = self.pPos.X.copy()

        # Current position
        self.pPos.X[[0, 1, 5]] = self.pPos.Xc[[0, 1, 5]] + np.dot(np.array([[np.cos(self.pPos.X[5,0]), -np.sin(self.pPos.X[5,0]), 0],
                                                                            [np.sin(self.pPos.X[5,0]), np.cos(self.pPos.X[5,0]), 0],
                                                                            [0, 0, 1]]), 
                                                                np.array([[self.pPar.a * np.cos(self.pPar.alpha)],
                                                                            [self.pPar.a * np.sin(self.pPar.alpha)],
                                                                            [0]]))
        
        # ball velocities: First-time derivative of the current position
        self.pPos.X[[6, 7, 11]] = (self.pPos.X[[0, 1, 5]] - self.pPos.Xa[[0, 1, 5]]) / self.pPar.Ts

    def get_vel_linang(self, current, past, t_amo):
        '''
        Calculate vel lin and ang => [6,7,11]

        In:
            current: self.pPos.Xd[[1,2,5]]
            past: self.pPos.Xda[[1,2,5]]
        
        Out: self.pPos.Xd[[6,7,11]]
        '''
        return (current - past)/t_amo





class pPos:
    def __init__(self):
        # .......... Robot pose ..........
        self.X = np.zeros((12, 1),dtype = np.float64)  # Current pose (point of control)
        self.Xa = np.zeros((12, 1),dtype = np.float64)  # Past pose

        self.Xc = np.zeros((12, 1),dtype = np.float64)  # Current pose (center of the robot)

        self.Xd = np.zeros((12, 1),dtype = np.float64)  # Desired pose
        self.Xda = np.zeros((12, 1),dtype = np.float64)  # Past desired pose

        self.Xr = np.zeros((12, 1),dtype = np.float64)  # Reference pose
        self.Xra = np.zeros((12, 1),dtype = np.float64)  # Past reference pose

        # First time derivative:
        self.dX = np.zeros((12, 1),dtype = np.float64)  # Current pose
        self.dXd = np.zeros((12, 1),dtype = np.float64)  # Desired pose
        self.dXr = np.zeros((12, 1),dtype = np.float64)  # Reference pose

        # Pose error:
        self.Xtil = self.Xd - self.X

class pSC:
    def __init__(self):
        # .......... Signals of Control  ..........
        # Linear and Angular Velocity:
        self.U = np.array([[0], [0]],dtype=np.float64)  # Current
        self.Ua = np.array([[0], [0]],dtype=np.float64)  # Past
        self.Ud = np.array([[0], [0]],dtype=np.float64)  # Desired
        self.Uda = np.array([[0], [0]],dtype=np.float64)  # Past desired
        self.Ur = np.array([[0], [0]],dtype=np.float64)  # Reference
        self.Kinematics_control = 0

        # Linear and Angular Acceleration:
        self.dU = np.array([[0], [0]],dtype=np.float64)  # Current
        self.dUd = np.array([[0], [0]],dtype=np.float64)  # Desired

        # RPM
        self.RPM = np.array([[0], [0]],dtype=np.float64)

class pPar:
    def __init__(self):
        self.Model = 'BDPJOG'  # robot model

        # Sample time
        self.Ts = 0.04  # For numerical integration
        self.ti = None  # Flag time

        # Dynamic Model Parameters
        self.g = 9.8  # [kg.m/s^2] Gravitational acceleration

        # [kg]
        # self.m = 0.429  # 0.442;

        # [m and rad]
        self.a = 32e-3  # point of control
        self.alpha = 0  # angle of control
        self.r = 21.5e-3 # Raio da roda
        self.d = 75e-3 # Larguda do robôs

        self.vmax = 1.051  # 
        self.wmax = 26 
        # self.r = 21.5 # Raio da roda
        # self.d = 75 # Larguda do robôs

        # self.pPar.theta = [0.5338, 0.2168, -0.0134, 0.9560, -0.0843, 1.0590]

class iFlags:
    def __init__(self):
        # Flags
        self.Connected = 0
        self.JoyON = 0
        self.GPS = 0
        self.EmergencyStop = 0