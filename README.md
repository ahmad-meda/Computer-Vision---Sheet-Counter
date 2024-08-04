# Sheet Stack Counting Application

This application automates the process of counting sheets in a stack using computer vision techniques. Users can upload images of sheet stacks through a web interface, and the application will process the images to determine the number of sheets.

The Flask Application runs the app while the 'Sheet Counter Code' conatins codethat shows the lines highlighted to count the sheets.

## Features

- **Image Upload**: Users can upload images of sheet stacks.
- **Image Processing**: The application preprocesses the images using grayscale conversion, Gaussian blur, and edge detection.
- **Sheet Counting**: The number of sheets is determined by analyzing contours in the edge-detected image.
- **Result Display**: The result, including the number of sheets and the processing time, is displayed to the user.

## Requirements

- Python 3.6+
- Flask
- OpenCV
- Werkzeug
- Tailwind CSS (via CDN)

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/ahmad-meda/Chatbot-Jessup-Cellars/tree/main
    cd jessup-cellars-chatbot
    ```

2. **Create and activate a virtual environment**:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. **Install the required packages**:
    ```sh
    pip install Flask opencv-python-headless
    ```
4. **Ensure your `static/uploads/` file is in the project directory**.

## Running the Application

1. **Start the Flask application**:
    ```sh
    python app.py
    ```
2. **Start the python application**:
    ```sh
    python main.py
    ```
3. **Open your web browser and go to**: `http://127.0.0.1:5000/`

## Usage

### Upload an Image

1. On the homepage, click on the "Upload Image" section.
2. Choose an image file (allowed formats: png, jpg, jpeg, gif) and click "Upload".

### View Results

1. After uploading, the application will process the image.
2. The number of sheets and the processing time will be displayed along with the uploaded image.
