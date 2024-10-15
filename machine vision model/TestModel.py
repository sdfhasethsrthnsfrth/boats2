from ultralytics import YOLO
import torch
import os
from datetime import datetime

if __name__ == '__main__':
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    # Load a model
    model = YOLO("best.pt") #Load the model that had best results int training, manually place in folder
    model.to(device)
    
    #Define source for test images
    source = r"C:\Users\VLK_DEV\Documents\BoatVisualization\TestModel\test_images\*.jpg"
    
    # Create a folder for test results
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    results_folder = f"Test_results_{timestamp}"
    os.makedirs(results_folder, exist_ok=True)  # Create the folder if it doesn't exist

    # Run inference on the source
    results = model(source, stream=True)  # generator of Results objects
    
    # Process results list
    for i, result in enumerate(results):
        boxes = result.boxes  # Boxes object for bounding box outputs
        masks = result.masks  # Masks object for segmentation masks outputs
        keypoints = result.keypoints  # Keypoints object for pose outputs
        probs = result.probs  # Probs object for classification outputs

        # Display the result to the screen, this will pop-up the image (Not recommended for large datasets)
        #result.show()  

        # Save the result to disk
        result.save(filename=os.path.join(results_folder, f"result_{i}.jpg"))  # Save each result with a unique filename
