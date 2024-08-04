import cv2
import numpy as np
import matplotlib.pyplot as plt

def preprocess_image(image_path):
    # Read the image
    image = cv2.imread(image_path)
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Apply Gaussian blur
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    # Edge detection
    edges = cv2.Canny(blurred, 50, 150)
    return edges

def count_sheets(edges):
    # Find contours
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # Filter contours to find horizontal lines
    horizontal_contours = [cnt for cnt in contours if cv2.boundingRect(cnt)[3] < 10]
    return len(horizontal_contours)

def main():
    # Get the image path from the user
    image_path = input("Please enter the path to the image: ")
    
    edges = preprocess_image(image_path)
    sheet_count = count_sheets(edges)
    print(f"Number of sheets: {sheet_count}")
    
    # Display the image and edges for visualization
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.imshow(cv2.imread(image_path))
    plt.title("Original Image")
    plt.subplot(1, 2, 2)
    plt.imshow(edges, cmap='gray')
    plt.title("Edges Detected")
    plt.show()

# Run the main function
if __name__ == "__main__":
    main()
