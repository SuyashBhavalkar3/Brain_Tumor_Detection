from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.models import User 
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import render

from .models import *
from django.db import IntegrityError


from django.shortcuts import render

def upload_imz(request):
    return render(request, 'upload_images.html')

def index(requests):
    return render(requests,'index.html')

from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
# from .models import BrainImage  # Import if using models.py

import os
import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
from PIL import Image
import cv2
from keras.models import load_model

def get_className(classNo):
    if classNo == 0:
        return "No Brain Tumor"
    elif classNo == 1:
        return "Yes Brain Tumor"

def getResult(img):
    image = cv2.imread(img)
    image = Image.fromarray(image, 'RGB')
    image = image.resize((64, 64))
    image = np.array(image)
    input_img = np.expand_dims(image, axis=0)
    result = model.predict(input_img)
    predicted_class = np.argmax(result, axis=1)[0]
    return get_className(predicted_class)

# Load the model outside the view function (consider using a global variable or configuration file)
model = load_model("C:\\Users\\Ruturaj\\EDAI_2_final\\BrainTumorDetection\\DETECTION\\BrainTumor10EpochsCategorical.h5")  # Adjust model path as needed
from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
import os

def upload(request):
    if request.method == 'POST':
        try:
            # Check if 'file' key exists in request.FILES
            if 'file' not in request.FILES:
                raise ValueError("No file uploaded")

            f = request.FILES['file']
            fs = FileSystemStorage()  # Use Django's storage system
            filename = fs.save(f.name, f)  # Securely save the uploaded file
            uploaded_file_url = fs.url(filename)  # Get the URL for the uploaded file

            # Process the image and get the result
            image_path = os.path.join(fs.location, filename)  # Construct the full path
            result = getResult(image_path)

            # Optionally, save the image and result (if using models.py)
            # brain_image = BrainImage(image=uploaded_file_url, result=result)
            # brain_image.save()

            return render(request, 'upload_images.html', {'result': result, 'image_url': uploaded_file_url})
        except ValueError as ve:
            error_message = str(ve)
            return render(request, 'upload_images.html', {'error_message': error_message})
        except Exception as e:
            error_message = "Error processing the uploaded file: " + str(e)
            return render(request, 'upload_images.html', {'error_message': error_message})
    else:
        return HttpResponse("Invalid Method")


  
