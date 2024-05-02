from flask import request,Flask,render_template
from src.mask_detection.utils import encodeImageIntoBase64,decodeImage
import os
import ultralytics
from ultralytics import YOLO
from ultralytics.yolo.v8.detect.predict import DetectionPredictor
from src.mask_detection.exception import AppException
import os
import sys
import json
from flask import jsonify
import subprocess
import time


application=Flask(__name__)

app=application


class ClientApp:
    def __init__(self):
        self.filename='inputImage.jpg'
        




@app.route('/')
def index():
    return render_template('index.html')


@app.route("/predict",methods=["GET","POST"])
def predictRoute():
    
    try:
        image=request.json['image']
        decodeImage(image,clap.filename)
    

        # Define the YOLO command
        command = "yolo task=detect mode=predict model=\"artifacts/prepare_base_model/best.pt\" conf=0.25 source=\"inputImage.jpg\" save='j.jpg'"

        # Execute the YOLO command
        subprocess.run(command, shell=True)
        
        recent_addition=os.listdir('runs/detect')[-1]
        

        
    # Read the contents of the file
        with open(f"{(os.path.abspath('runs/detect'))}\predict\inputImage.jpg",'rb') as f:
            data=f.read()

    # Save the contents to 'data/img.jpg'
        with open(os.path.join('data','img.jpg'), 'wb') as f:
            f.write(data)
        
        os.system("rmdir /s /q runs\\detect")
            
            

            
    
        openencodebase64=encodeImageIntoBase64("data/img.jpg")
        result={'image':openencodebase64.decode('utf-8')}
    

        return jsonify(result)
    except Exception as e:
        raise(AppException(e,sys))
    
    
@app.route("/live", methods=['GET']) 
def predictLive():
    try:
        command="yolo task=detect mode=predict conf=0.25 source=0 model=\"artifacts/prepare_base_model/best.pt\" "
        
        subprocess.run(command,shell=True)
        
        os.system("rmdir /s /q runs\\detect")
        
        return 'camera is starting'
        
        
        
        
    except Exception as e:
        AppException(e,sys)
    
    
if __name__=="__main__":
    clap=ClientApp()
    app.run(host="0.0.0.0",port=8080)



