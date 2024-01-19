# -*- coding: utf-8 -*-
"""xai_app.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XRB_m0JRoi0KugiHw5WSPJzV0udfU69O
"""


import cv2
import numpy as np
import gradio as gr
import matplotlib as plt
from fastai.vision.all import *
from torchvision import transforms
from pytorch_grad_cam import GradCAM
from pytorch_grad_cam.utils.model_targets import ClassifierOutputTarget

# import pathlib
# temp = pathlib.PosixPath
# pathlib.PosixPath = pathlib.WindowsPath

model = load_learner("models/recognizer_model.pkl")

# Transforming to pytorch model
pytorch_model = model.eval()

labels = ['Ayre', 'Catla', 'Chital', 'Ilish', 'Kachki', 'Kajoli', 'Koi', 'Magur', 'Mola Dhela', 'Mrigal', 'Pabda', 'Pangash', 'Poa', 'Puti', 'Rui', 'Shing', 'Silver Carp', 'Taki', 'Telapia', 'Tengra']


found_and_test = {
     'Ayre' : {
        'found': 'Found in South and Southeast Asia',
        'taste': 'Sweet taste',
        'scientific name': 'Sperata aor',
    },
     'Catla' : {
        'found': 'Native to South Asia',
        'taste': 'sweet and nutty flavors',
        'scientific name': 'Catla catla',
    },
     'Chital' : {
        'found': 'Native to South and Southeast Asia',
        'taste': 'sweet taste',
        'scientific name': 'Chitala chitala',
    },
     'Ilish' : {
        'found': 'Found in South Asia',
        'taste': 'sweet and salty taste',
        'scientific name': 'Tenualosa ilisha',
    },
     'Kachki' : {
        'found': 'Found in South and Southeast Asia',
        'taste': 'great when fresh',
        'scientific name': 'Corica soborna Hamilo',
    },
     'Kajoli' : {
        'found': 'Native to Asia',
        'taste': 'delicate and tastes divine',
        'scientific name': 'Ailia coila',
    },
     'Koi' : {
        'found': 'Native to Asia and Europe',
        'taste': 'mild flavor and firm flesh that tastes slightly sweet',
        'scientific name': 'Cyprinus rubrofuscus',
    },
     'Magur' : {
        'found': 'Native to Southeast Asia',
        'taste': 'delicate flavor',
        'scientific name': 'Clarias batrachus',
    },
     'Mola Dhela' : {
        'found': 'Found in South Asia',
        'taste': 'black cod or lobster',
        'scientific name': 'Osteobrama cotio',
    },
     'Mrigal' : {
        'found': 'Native to the Indo-Gangetic riverine systems of South Asia.',
        'taste': 'sweet, mild taste',
        'scientific name': 'Cirrhinus cirrhosus',
    },
     'Pabda' : {
        'found': 'freshwater',
        'taste': 'mild taste',
        'scientific name': 'Ompok bimaculatus',
    },
     'Pangash' : {
        'found': 'Native to South and Southeast Asia',
        'taste': 'Mild, sweet, and moist taste',
        'scientific name': 'Pangasius pangasius',
    },
     'Poa' : {
        'found': 'Found in South Asia',
        'taste': 'Mild and flaky to bold and robust',
        'scientific name': 'Otolithoides pama',
    },
     'Puti' : {
        'found': 'native to Asia',
        'taste': 'does not taste so good but bitter',
        'scientific name': 'Puntius sophore',
    },
     'Rui' : {
        'found': 'Found in South Asia',
        'taste': 'almost free of a "fishy" taste',
        'scientific name': 'Labeo rohita',
    },
     'Shing' : {
        'found': 'native to South Asia',
        'taste': 'sweet, mild taste',
        'scientific name': 'Heteropneustes fossilis',
    },
     'Silver Carp' : {
        'found': 'native to eastern Asia',
        'taste': 'similar in flavor and texture to tilapia and catfish',
        'scientific name': 'Hypophthalmichthys molitrix',
    },
     'Taki' : {
        'found': 'found in South and Southeast Asia',
        'taste': 'mild flavor',
        'scientific name': 'Channa striata',
    },
     'Telapia' : {
        'found': 'native to Africa and the Levant',
        'taste': 'sweet, mild taste',
        'scientific name': 'Oreochromis niloticus',
    },
     'Tengra' : {
        'found': 'found in South and Southeast Asia',
        'taste': 'delicate, slightly sweet taste',
        'scientific name': 'Mystus tengara',
    },
}


def xai_visualization(image, image_tensor, targeted_category, model, target_layers):

  cam = GradCAM(model = model, target_layers = target_layers)

  targets = [ClassifierOutputTarget(targeted_category)]

  grayscale_cam = cam(input_tensor = image_tensor, targets = targets)

  mask = grayscale_cam[0, :]

  plt.figure(figsize=(10,5))

  plt.axis('off')

  plt.imshow(image)

  plt.imshow(mask*255, cmap="plasma", alpha=0.7)

  plt.savefig("xai/xai_visualization.png", dpi=150)


def preprocess_image(image_path):

  # Resizing an image
  image = cv2.resize(
      image_path,
      dsize=(224, 224),
      interpolation=cv2.INTER_CUBIC)

  # Converting image to tensor
  img_tensor = transforms.ToTensor()(image)

  # Converting image to batch
  img_tensor = img_tensor.reshape(1,3,224,224)

  return image, img_tensor

def target_layers_finding(model):
  # Available layers
  layers = list(model.named_modules())

  # For Resnet-50
  target_layers = [layers[len(layers)-20][1]]

  return target_layers

def classify_image(image_path):

  # Model Prediction
  label, _, probs = model.predict(image_path)

  # Predicted Category
  targeted_category = np.argmax(probs)

  # Preprocessed image and image tensor
  image, img_tensor = preprocess_image(image_path)

  # Target layer
  target_layer = target_layers_finding(pytorch_model)

  xai_visualization(image, img_tensor, targeted_category, pytorch_model, target_layer)

  # print(f"Category with most probability: {np.argmax(probs)}")
  xai_image = "xai/xai_visualization.png"

  # return xai_image, dict(zip(labels, map(float, probs)))

  predicted_category = labels[targeted_category]

  information = ""

  if predicted_category in found_and_test.keys():
    information = found_and_test[predicted_category]

  # return image_path, information, dict(zip(labels, map(float, probs)))
  # print(information)
    
  information = f'''
    Scientific Name: {information['scientific name']};\n 
    Taste: {information['taste'].capitalize()};\n 
    Availability: {information['found'].capitalize()}
  '''

  # print(information)

  return xai_image, str(information), dict(zip(labels, map(float, probs)))

# classify_image('test images/unknown_01.jpg')


inputs = gr.Image(
  label = "Input Image"
)

outputs = [
    gr.Image(
      label = "GradCAM visualization", 
      show_label = True
    ),
    gr.Label(
      label = "Information"
    ),
    gr.Label(
      num_top_classes=5, 
      label="Predicted Category"
    )
  ]

examples = [
    'test images/unknown_01.jpg',
    'test images/unknown_02.png',
    'test images/unknown_03.jpg',
    'test images/unknown_04.jpg',
    'test images/unknown_05.jpg',
    'test images/unknown_06.jpg',
    'test images/unknown_07.jpg',
    'test images/unknown_08.jpg',
    'test images/unknown_09.jpg',
    'test images/unknown_10.jpg',
    'test images/unknown_11.jpg',
    'test images/unknown_12.png',
    'test images/unknown_13.jpg',
    'test images/unknown_14.png',
    'test images/unknown_15.png',
    'test images/unknown_16.png',
    'test images/unknown_17.jpg'
]

interface = gr.Interface(
    fn = classify_image,
    inputs = inputs,
    outputs = outputs,
    examples = examples
  )

interface.launch()
