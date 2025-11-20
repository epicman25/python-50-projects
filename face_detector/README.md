# Face Detection with OpenCV

**Difficulty Level:** Intermediate (Est. 2-3 Hours)

## Project Description
Use the `opencv-python` library to perform simple face detection on an image. This requires finding a pre-trained Haar Cascade XML file (which OpenCV provides). The script should load an image, load the cascade, detect faces (which returns coordinates), and then draw rectangles around the detected faces and display the image.

## Possible Folder Structure
```
face_detector/
├── main.py
├── image.jpg
├── haarcascade_frontalface_default.xml
└── requirements.txt
```

## Inputs and Expected Outputs
- **Input:** `image.jpg` (containing faces)
- **Output:** A window pops up showing the same image, but with blue rectangles drawn around the faces

## Learning Objectives
- Computer vision with OpenCV
- Image processing
- Face detection algorithms
- Haar Cascade classifiers
