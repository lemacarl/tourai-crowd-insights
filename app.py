from flask import Flask, request, jsonify, render_template
from ultralytics import YOLO
from PIL import Image
import io

app = Flask(__name__)

model = YOLO('yolo11x.pt')

data = {'count': 0}

@app.route('/')
def map_view():
    return render_template('map.html', count=data['count']) 

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify({"error": "No image file found in the request"}), 400

    file = request.files['image']
    if file.filename == '':
        return jsonify({"error": "No image selected for uploading"}), 400

    try:
        image = Image.open(io.BytesIO(file.read()))

        results = model(image)
        face_count = 0

        for box in results[0].boxes:  
            label = box.cls  
            if label == 0:  
                face_count += 1
        
        data['count'] = face_count

        return jsonify({"faces_detected": face_count}), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route('/update', methods=['POST'])
def update_count():
    try:
        content = request.get_json()
        if not content or 'count' not in content:
            return jsonify({"error": "Invalid input, 'count' is required"}), 400

        new_count = content['count']
        if not isinstance(new_count, int) or new_count < 0:
            return jsonify({"error": "Invalid value for 'count', must be a non-negative integer"}), 400

        data['count'] = new_count

        return jsonify({"message": "Count updated successfully", "count": data['count']}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
