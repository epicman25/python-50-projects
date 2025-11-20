# Face Recognition System

**Difficulty Level:** Advanced (Est. 4-6 Hours)

## Project Description
Build a system that recognizes faces, not just detects them. This involves a multi-step pipeline: (1) Use `opencv` to detect faces in images. (2) Use a deep learning model (e.g., `face_recognition` library) to create a 128-dimension "encoding" for each face. (3) Compare these encodings to a database of "known" face encodings to find a match.

## Possible Folder Structure
```
face_recognition/
├── main.py            # (Runs the recognition on new image)
├── create_encodings.py # (Scans 'known_faces' dir)
├── known_faces/
│   ├── person1.jpg
│   └── person2.jpg
├── encodings.pickle
└── requirements.txt
```

## Inputs and Expected Outputs
- **Input:** An unknown image with `person1.jpg` in it
- **Output:** The image is displayed with a label "person1" over the face

## Learning Objectives
- Advanced computer vision
- Face recognition algorithms
- Deep learning for face encoding
- Image processing pipeline
- Real-world AI application
