import time
import constants as c
from robot import ROBOT
import pybullet as p
import pybullet_data
import os
import pyrosim.pyrosim as pyrosim
from world import WORLD
import math
import numpy as np
import cv2

class SWARM_SIMULATION:
    def __init__(self,directOrGUI, swarmNumber, botNumber, overallBot):

        self.directOrGUI = directOrGUI
        if self.directOrGUI == "DIRECT":
            p.connect(p.DIRECT) 
        elif self.directOrGUI == 'GUI':
            p.connect(p.GUI) 

        self.swarmNumber = swarmNumber
        self.botNumber = botNumber
        self.overallBot = overallBot
        self.bestBrains = self.Get_Brain_IDs()

        if c.swarmType == 'case1':
            self.brainID = self.bestBrains[self.overallBot//c.botsPerSwarm]  

        if c.swarmType == 'case2' or c.swarmType == 'case3':
            self.brainID = self.bestBrains[self.overallBot] 

        p.setPhysicsEngineParameter(fixedTimeStep=c.timeStepSize,
                                    numSolverIterations=c.numSolverIterations)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.configureDebugVisualizer(p.COV_ENABLE_GUI, 0)
        p.setGravity(0, 0, c.gravityConstant)

        self.robot = ROBOT(self.brainID, self.swarmNumber, self.botNumber)
        self.world = WORLD()

        # Initialize camera parameters
        self.camera_width = 500
        self.camera_height = 880
        self.camera_pos = [0, 0, 18]  # Adjust the position 
        self.camera_target_pos = [0, 0, 0]  # Adjust the target position
        self.camera_up_vector = [-1, 0, 0]
        
        # Adjust the field of view (FOV) (in degrees)
        self.camera_fov = 90  

        # Compute camera matrices
        self.camera_view_matrix = p.computeViewMatrix(self.camera_pos, self.camera_target_pos, self.camera_up_vector)
        self.camera_projection_matrix = p.computeProjectionMatrixFOV(
            fov=self.camera_fov, aspect=float(self.camera_width) / self.camera_height,
            nearVal=0.01, farVal=100.0)
        
        # Initialize video writer
        if self.directOrGUI == "GUI":
            self.video_writer = cv2.VideoWriter(f'swarm{self.swarmNumber}_bot{self.botNumber}_overall{self.overallBot}.mov',
                                                cv2.VideoWriter_fourcc(*'mp4v'),
                                                30,  # Frame rate 
                                                (self.camera_width, self.camera_height))


    def capture_image(self):
        # Capture image from the camera
        (_, _, px, _, _) = p.getCameraImage(
            width=self.camera_width, height=self.camera_height,
            viewMatrix=self.camera_view_matrix,
            projectionMatrix=self.camera_projection_matrix,
            renderer=p.ER_BULLET_HARDWARE_OPENGL)
        rgb_array = np.reshape(px, (self.camera_height, self.camera_width, 4))
        # image is RGBA, use only RGB channels
        rgb_array = rgb_array[:, :, :3]
        return rgb_array

    def Run(self):
        # Write initial position
        self.robot.Record_XY(self.swarmNumber, self.botNumber, self.overallBot)
        for i in range(c.loopLength):

            p.stepSimulation()
            self.robot.Sense(i)
            self.robot.Think()
            self.robot.Act(i)
            
            # take in timestep i, write x and y positions to a file
            self.robot.Record_XY(self.swarmNumber, self.botNumber, self.overallBot)


            if self.directOrGUI == "GUI":
                time.sleep(c.sleepRate)
                # Capture image at each step
                image = self.capture_image()
                # Convert image to compatible depth (e.g., CV_8U)
                image = image.astype(np.uint8)
                # Save the image
                self.video_writer.write(cv2.cvtColor(image, cv2.COLOR_RGB2BGR))
        if self.directOrGUI == "GUI":
            self.video_writer.release()


    def Get_Fitness(self):
        self.robot.Write_Playback_Fitness()

    def Get_Brain_IDs(self):
        with open("bestBrains.txt", "r") as f:
            bestBrains = [int(line.strip()) for line in f]
        return bestBrains

    def Cleanup(self):
        p.disconnect()
