import numpy as np
from Robo_BDP.Classe_JOG import Player, Ball


def GKStraightLine(GK : Player, B : Ball, gain : list = [1.5, .07]) -> Player:
    # Define a straight line on the y-axis
    y_line = np.array([-.4, .4], dtype=np.float64)  # Y-values range from 0.0 to 1.0, X-coordinate is fixed

    if GK.LadoAtaque == 1:
        # Define another straight line composed of two distinct points
        GoalFund = np.array([-.75, 0], dtype=np.float64)  # Point 1: X=2.0, Y=2.0
        Ball = np.array([B.pPos.Xc[0,0], B.pPos.Xc[1,0]], dtype=np.float64)  # Point 2: X=4.0, Y=3.0

    elif GK.LadoAtaque == -1:
        # Define another straight line composed of two distinct points
        GoalFund = np.array([.75, 0], dtype=np.float64)  # Point 1: X=2.0, Y=2.0
        Ball = np.array([B.pPos.Xc[0,0], B.pPos.Xc[1,0]], dtype=np.float64)  # Point 2: X=4.0, Y=3.0

    # Calculate the slope (m) and y-intercept (b) for Line 2
    m = (Ball[1] - GoalFund[1]) / (Ball[0] - GoalFund[0])
    b = GoalFund[1] - m * GoalFund[0]

    # Calculate the X-coordinate of the intersection point (X)
    X = GoalFund[0]

    # Calculate the Y-coordinate of the intersection point (Y)
    Y = m * X + b

    # The (X, Y) coordinates represent the intersection point
    intersection_point = np.array([X, Y])

    # Print the intersection point
    print("Intersection Point:", intersection_point)
    

    def calculate_desired_velocity(current_position, y_line, point1, point2):
        # Calculate the desired linear velocity and angular velocity
        # based on the intersection of the two lines

        # Implement your logic here

        return desired_velocity

    def check_if_reached_desired_position(current_position, desired_position):
        # Calculate the distance between the current position and the desired position
        distance = np.linalg.norm(current_position - desired_position)

        # Check if the distance is less than 4 centimeters
        if distance < 0.04:
            return True  # The robot has reached the desired position
        else:
            return False
