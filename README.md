# BallroomDanceStepClassification
First Phase of "Real-Time Feedback System For Ballroom Dance Performance Using Multimodal Data"

# Real-Time Feedback System For Ballroom Dance Performance Using Multimodal Data

## Overview

This repository contains the implementation and documentation of dissertation "Real-time feedback system for ballroom dance performance utilizing multimodal data". The system incorporates advanced machine learning techniques, specifically Long Short-Term Memory networks with attention mechanisms (LRCN) and Convolutional LSTM, to recognize dance steps from the Ballroom Dance Dataset. The dataset encompasses videos of dancers with varying levels of experience, contributing to a robust and versatile solution.

## Key Features

- **Dance Step Recognition:**
  - Implemented a dance step recognition system capable of identifying specific steps within ballroom dance performances.
  - Leveraged state-of-the-art machine learning techniques, including LRCN and Convolutional LSTM, to enhance the accuracy and reliability of step recognition.
- **Front-End Development:**
  - Created an interactive front-end for the solution using HTML.
  - Integrated a Flask API to facilitate communication between the front end and the machine learning model.

## Technologies Used

- **Machine Learning:**
  - LRCN (Long Short-Term Memory networks with attention mechanisms)
  - Convolutional LSTM

- **Web Development:**
  - HTML
  - Flask API

## Current Status

The current version of the system is proficient in accurately identifying specific dance steps from ballroom dance performances. The front end provides a user-friendly interface for interacting with the system.

## Ongoing Development

The project is actively being developed to introduce real-time dance step recognition and feedback. The ongoing enhancements aim to provide instantaneous analysis and constructive feedback during live ballroom dance performances.


## Acknowledgments

Special thanks to the creators of the Ballroom Dance Dataset for providing valuable data for the development and evaluation of this system.

@Inbook{Matsuyama2021,
author="Matsuyama, Hitoshi
and Hiroi, Kei
and Kaji, Katsuhiko
and Yonezawa, Takuro
and Kawaguchi, Nobuo",
editor="Ahad, Md Atiqur Rahman
and Inoue, Sozo
and Roggen, Daniel
and Fujinami, Kaori",
title="A Basic Study on Ballroom Dance Figure Classification with LSTM Using Multi-modal Sensor",
bookTitle="Activity and Behavior Computing",
year="2021",
publisher="Springer Singapore",
address="Singapore",
pages="209--226",
abstract="The paper presents a ballroom dance figure classification method with LSTM using video and wearable sensors. Ballroom dance is a popular sport among people regardless of age or sex. However, learning ballroom dance is very difficult for less experienced dancers as it has many complex types of ``dance figures'', which is a completed set of footsteps. Therefore, we aim to develop a system to assist dance exercise which gives advice proper to each dance figure characteristic by recognizing dance figures correctly. While the major approach to recognize dance performance is to utilize video, we cannot simply adopt it for ballroom dance because the images of dancers overlap each other. To solve the problem, we propose a hybrid figure recognition method combining video and wearable sensors to enhance its accuracy and robustness. We collect video and wearable sensor data of seven dancers including acceleration, angular velocity, and body parts location change by pose estimation. After that, we preprocess them and put them into an LSTM-based deep learning network. As a result, we confirmed that our approach achieved an F1-score of 0.86 for 13 figure types recognition using the multi-modal sensors with trial-based fivefold cross-validation. We also performed user-based cross-validation, and sliding window algorithms. In addition, we compared the results with our previous method using Random Forest and also evaluated the robustness with occlusions. We found the LSTM-based method worked better than Random Forest with keypoint data. On the other hand, LSTM could not perform well with a sliding window algorithm. We consider the LSTM-based method would work better with a larger dance figure data, which is our next work. In addition, we will investigate how to solve occlusion problems with pose estimation.",
isbn="978-981-15-8944-7",
doi="10.1007/978-981-15-8944-7_13",
url="https://doi.org/10.1007/978-981-15-8944-7_13"
}
