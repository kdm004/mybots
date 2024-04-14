import cv2
import numpy as np
import glob

# Create a black rectangle image with text
def create_image_with_text(x_coordinate):
    # Create black rectangle image for the background
    img = np.zeros((225, 800, 3), dtype=np.uint8)

    # Add text (x coordinate rounded to 4 decimals)
    text = f'X Coordinate: {x_coordinate:.4f}'
    cv2.putText(img, text, (60, 120), cv2.FONT_HERSHEY_SIMPLEX, 2, (355, 355, 355), 2)

    return img



for i in range(10): 
    position_files = glob.glob(f"trajectories/*o{i}.txt")
    for position_file in position_files:

        # Read txt file and extract x coordinates
        with open(position_file, 'r') as file:
            lines = file.readlines()
            x_coordinates = [float(line.split()[0]) for line in lines]

        # Define the total duration of the video in seconds
        total_duration = 33

        # Calc time interval between frames
        num_frames = len(x_coordinates)
        frame_duration = total_duration / num_frames

        # Create video writer object
        output_video = cv2.VideoWriter(f'swarm0_bot{i}.mov', cv2.VideoWriter_fourcc(*'mp4v'), 30, (800, 225))

        # Generate each frame and add to the video
        for x_coordinate in x_coordinates:
            frame = create_image_with_text(x_coordinate)
            output_video.write(frame)

        # Release video writer
        output_video.release()
