# this module helps to train custom model on our
# dataset

from ultralytics import YOLO  # importing YOLO

# Load a model
model = YOLO("yolov8n.yaml")  # build a new model from scratch

# Use the model
results = model.train(data="config.yaml", epochs=100)  # train the model
metrics = model.val()  # evaluate model performance on the validation set

path = model.export(format="onnx")  # export the model to ONNX format
