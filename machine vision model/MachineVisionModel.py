from ultralytics import YOLO
import torch
import os

if __name__ == '__main__':
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')


    # Load a model
    model = YOLO("yolov8m.yaml")  # Build a new model
    model.to(device)

    # Train the model
    val_results = model.train(data="config.yaml", epochs=300)
    
    # Validate the model
    metrics = model.val()
    print(metrics.box.map)   # Map50-95
    print(metrics.box.map50)  # Map50
    print(metrics.box.map75)  # Map75
    print(metrics.box.maps)    # List of map50-95 for each category
    

    
    