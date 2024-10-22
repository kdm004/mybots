import pybullet as p
import pybullet_data


class WORLD:
    def __init__(self):
        self.planeID = p.loadURDF("plane.urdf")
        print(f"Here is plane ID {self.planeID}")
        self.environment = p.loadSDF("world.sdf")





   
