# TourAI - Crowd Insights

This project is a Flask-based web application that integrates the YOLO model for object detection to count faces in uploaded images. The app provides an interface to upload images, processes them using the YOLO model, and displays the count on a dashboard.

## Features
- Upload images to count the number of people
- Display the count of detected faces on a webpage.
- Update the people count manually via an API endpoint.

## Prerequisites
Before running the app, ensure you have the following installed:

- Python 3.8+
- Flask
- Pillow
- Ultralytics YOLO library

## Installation

1. **Create a Conda environment**:
   ```bash
   conda create --name flask-yolo-app python=3.8
   conda activate flask-yolo-app
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
   Ensure the following libraries are included in your `requirements.txt` file:
   - Flask
   - Pillow
   - ultralytics

## Usage

1. **Run the application**:
   ```bash
   python app.py
   ```
   By default, the application runs on `http://0.0.0.0:8000`.

2. **Access the web interface**:
   Open your browser and navigate to `http://localhost:8000`.

## API Endpoints

### 1. `GET /`
- **Description**: Renders the live people count homepage.

### 2. `POST /upload`
- **Description**: Accepts an image file and updates the people counter
- **Request**:
  - Form data with the key `image` containing the uploaded image file.
- **Response**:
  - Success: `200` with JSON `{ "faces_detected": <count> }`
  - Error: `400` or `500` with appropriate error message.

### 3. `POST /update`
- **Description**: Updates the people count manually.
- **Request**:
  - JSON body: `{ "count": <new_count> }`
- **Response**:
  - Success: `200` with JSON `{ "message": "Count updated successfully", "count": <updated_count> }`
  - Error: `400`

## License
This project is licensed under the Creative Commons License.