import pyrosim.pyrosim as pyrosim
import pybullet as p



class OBSTACLE_WORLD:
    '''
    Creates a new file which starts up the virtual environment and loads any obstacles 
    '''
    def __init__(self):        
        self.planeId = p.loadURDF("plane.urdf")
        p.loadSDF("obstacleWorld.sdf")


