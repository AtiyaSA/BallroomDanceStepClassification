# -*- coding: utf-8 -*-
"""
@author: atiya
"""

from flask import Flask, request, render_template
import os
import joblib
from predict import predict_on_video
from sklearn import preprocessing
le = preprocessing.LabelEncoder()
from keras.models import load_model
from moviepy.editor import VideoFileClip
import warnings
warnings.filterwarnings("ignore")

app = Flask(__name__)

path = 'C:\\Users\\atiya\\OneDrive - The University of Liverpool\\Dissertation\\FrontEnd\\BallroomDancing\\'
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
MODELS_FOLDER = 'models'
app.config['MODELS_FOLDER'] = MODELS_FOLDER
if not os.path.exists(MODELS_FOLDER):
    os.makedirs(MODELS_FOLDER)
OUT_FOLDER = 'static'
app.config['OUT_FOLDER'] = OUT_FOLDER
if not os.path.exists(OUT_FOLDER):
    os.makedirs(OUT_FOLDER)

@app.route('/',methods=['GET'])
def index():
    return render_template('index.html')    

@app.route('/upload', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
      f = request.files['fileName']
      # f = request.get_json()
      #df_json = json_normalize(f)
      # selectedTrainModel = df_json['selectedTrainModel'].iloc[0]
      #file = df_json['fileName'].iloc[0]
      file_name = f.filename
      try:
          if file_name.endswith('.mp4'):
              f.filename = 'upload.mp4'
              #path = main_path + '/' + file 
          elif file_name.endswith('.MP4'):
              f.filename = 'upload.mp4'
          elif file_name.endswith('.mov'):
              f.filename = 'upload.mp4'
          elif file_name.endswith('.avi'):
              f.filename = 'upload.mp4'
          elif file_name.endswith('.wav'):
              f.filename = 'upload.mp4'
          
          f.save(os.path.join(app.config['UPLOAD_FOLDER'], f.filename))
          return render_template('predict.html')
      except:
          return "An error occurred while processing the file."
      # Handle GET request or other cases
    return render_template('upload.html')

     
@app.route("/predict", methods = ['GET', 'POST'])
def predict_vd():
    if request.method == 'POST':
        if request.form['model'] == "Convolution LSTM":
            model_name = "ConvLSTM.h5"
        elif request.form['model'] == "LRCN":
            model_name = "LRCN.h5"
        try:
            model = load_model(os.path.join(path, os.path.join(app.config['MODELS_FOLDER'], model_name)))
            # print(path+"classes.npy")
            le = joblib.load(path+"classes.joblib")
            video_file_path = os.path.join(app.config['UPLOAD_FOLDER'], "upload.mp4")
            output_file_path = os.path.join(app.config['OUT_FOLDER'], "output.mp4")
            predict_on_video(video_file_path, output_file_path, model, le)
            clip = VideoFileClip(output_file_path)
            clip.write_videofile(os.path.join(app.config['OUT_FOLDER'], "output_.mp4"), codec="libx264")
            return render_template('output.html')
        except:
            return "Test Fail"
    return render_template('predict.html')
    

if __name__ == '__main__':
    app.run()