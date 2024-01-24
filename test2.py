import numpy as np

cubeLength = 0.3
cubeWidth = 0.3
lowerLegCoords = [[0.0, 1.1421582671204817, 0.0], [0.0, -1.8439559085203259, 0.0], [-1.1407196147692744, 0.0, 0.0], [1.0726240087249148, 0.0, 0.0]]

euclideanThreshold = 0.2 * np.sqrt(2) + np.sqrt(cubeLength**2 + cubeWidth**2)
xyList = []

for x in range(8, -12-2, -2):
    for y in range(-6, 6+2, 2):
        cubePosition = np.array([x, y, (0.3)/2 + 0.01])

        # Check distance to each lowerLegCoordinate
        too_close_to_lower_leg = any(
            np.linalg.norm(np.array(coord[:2]) - cubePosition[:2]) < euclideanThreshold
            for coord in lowerLegCoords
        )

        if too_close_to_lower_leg:
            continue  # Skip cube creation if too close to lowerLegCoords

        xyList.append((x, y))
        print((x, y))

print(len(xyList))

# ----


        # euclideanThreshold = 0.2 * np.sqrt(2) + np.sqrt(cubeLength**2 + cubeWidth**2)
        # pyrosim.Start_SDF("world.sdf")
        # for x in range(8, -12-2, -2):
        #     for y in range(-6, 6+2, 2):
        #         cubePosition = np.array([x, y, (0.3)/2 + 0.01])
                
        #         too_close_to_lower_leg = any(
        #             np.linalg.norm(np.array(coord[:2]) - cubePosition[:2]) < euclideanThreshold
        #             for coord in lowerLegCoords
        #         )

        #         if too_close_to_lower_leg:
        #             continue  # Skip cube creation if too close to lowerLegCoords

        #         pyrosim.Send_Cube(name=f"Box{x}{y}", pos=cubePosition, size=[0.3, 0.3, 0.3])
