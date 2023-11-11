# -*- coding: utf-8 -*-
"""
@author: atiya
"""

# Import the required libraries.
import cv2
import numpy as np
from collections import deque



def predict_on_video(video_file_path, output_file_path, model, le,SEQUENCE_LENGTH = 14, input_true_labels = None):
    '''
    This function will perform action recognition on a video using the LRCN model.
    Args:
    video_file_path:  The path of the video stored in the disk on which the action recognition is to be performed.
    output_file_path: The path where the ouput video with the predicted action being performed overlayed will be stored.
    SEQUENCE_LENGTH:  The fixed number of frames of a video that can be passed to the model as one sequence.
    '''
    IMAGE_HEIGHT , IMAGE_WIDTH = 64, 64
    # labels_df = pd.read_csv(input_true_labels, header = None, index_col=0)
    # labels_df.columns = ['labels']
    # labels_df.reset_index(drop = True, inplace = True)
    # Initialize the VideoCapture object to read from the video file.
    video_reader = cv2.VideoCapture(video_file_path)

    # Get the width and height of the video.
    original_video_width = int(video_reader.get(cv2.CAP_PROP_FRAME_WIDTH))
    original_video_height = int(video_reader.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Initialize the VideoWriter Object to store the output video in the disk.
    video_writer = cv2.VideoWriter(output_file_path, cv2.VideoWriter_fourcc('M', 'P', '4', 'V'),
                                   video_reader.get(cv2.CAP_PROP_FPS), (original_video_width, original_video_height))

    # Declare a queue to store video frames.
    frames_queue = deque(maxlen = SEQUENCE_LENGTH)

    # Initialize a variable to store the predicted action being performed in the video.
    predicted_class_name = ''

    # idx = 0

    # Iterate until the video is accessed successfully.
    while video_reader.isOpened():

        # Read the frame.
        ok, frame = video_reader.read()

        # Check if frame is not read properly then break the loop.
        if not ok:
            break

        # Resize the Frame to fixed Dimensions.
        resized_frame = cv2.resize(frame, (IMAGE_HEIGHT, IMAGE_WIDTH))

        # Normalize the resized frame by dividing it with 255 so that each pixel value then lies between 0 and 1.
        normalized_frame = resized_frame / 255

        # Appending the pre-processed frame into the frames list.
        frames_queue.append(normalized_frame)

        # Check if the number of frames in the queue are equal to the fixed sequence length.
        if len(frames_queue) == SEQUENCE_LENGTH:
            # Pass the normalized frames to the model and get the predicted probabilities.
            predicted_labels_probabilities = model.predict(np.expand_dims(frames_queue, axis = 0))[0]
            # print(predicted_labels_probabilities)
            # Get the index of class with highest probability.
            predicted_label = np.argmax(predicted_labels_probabilities)
            # Get the class name using the retrieved index.
            predicted_class_name = le.inverse_transform([predicted_label])[0] #+ '/' + labels_df['labels'][idx]
        # Write predicted class name on top of the frame.
        cv2.putText(frame, predicted_class_name, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        
        # plt.imshow(frame);plt.axis('off')
        # Write The frame into the disk using the VideoWriter Object.
        video_writer.write(frame)
        # print(predicted_class_name)
        # # print(predicted_labels_probabilities)
        # plt.imshow(frame);plt.axis('off')
        # plt.show()
        # idx += 1

    # Release the VideoCapture and VideoWriter objects.
    video_reader.release()
    video_writer.release()
    
    