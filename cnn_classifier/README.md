# Keras CNN Image Classifier

**Difficulty Level:** Advanced (Est. 4-6 Hours)

## Project Description
Build, train, and evaluate a Convolutional Neural Network (CNN) using `tf.keras`. Classify images from a standard dataset like MNIST or CIFAR-10. The project must follow a modular, OOP-based structure, separating data loading, model definition, and training into different modules.

## Possible Folder Structure
```
cnn_classifier/
├── config_files/
│   └── config.ini     # (Hyperparams: epochs, batch_size)
├── data_loader/
│   └── data_loader.py # (Class to load and prep tf.data)
├── model/
│   └── cnn_model.py   # (Function/class defines Keras model)
├── main.py            # (Main training/evaluation script)
└── requirements.txt
```

## Inputs and Expected Outputs
- **Input:** The `config.ini` file and the dataset (e.g., MNIST)
- **Output:** Console logs of training/validation accuracy per epoch, and a final "Test Accuracy: 99.1%"

## Learning Objectives
- Deep learning with Keras/TensorFlow
- CNN architecture design
- Image classification
- Modular deep learning code structure
- Configuration-driven training
