👁️‍🗨️ Human-Scanning-Application
Real-time human detection using YOLOv8 — no touch, no tags, just fast and accurate AI vision. Ideal for smart surveillance, people counting, and intelligent automation.

🚀 What is This Project?
Human-Scanning-Application is a Python-based, real-time human detection system powered by the YOLOv8 model from Ultralytics. It captures live video input from a webcam and accurately detects the presence of humans using AI and computer vision.

Whether you're building a smart security system, monitoring crowd density, or automating space usage — this tool gives you instant results.

✨ Key Features
🎥 Live Human Detection using YOLOv8.

⚡ Real-Time Processing on webcam input.

📦 Bounding Boxes drawn around detected individuals.

🚀 Optimized for Speed & Accuracy using latest YOLO architecture.

📁 Optional Logging of detection time and human count.

💻 Offline Functionality – works on any Python-enabled system with a webcam.

🔧 Installation
Required Libraries
Install the following Python packages:

bash
Copy
Edit
pip install opencv-python
pip install numpy
pip install ultralytics
Alternatively, use the provided requirements.txt:

requirements.txt

Copy
Edit
opencv-python
numpy
ultralytics
Install all at once:

bash
Copy
Edit
pip install -r requirements.txt
▶️ How to Use
Clone or download this repository.

Make sure your webcam is connected.

Run the main Python file:

bash
Copy
Edit
python human_scanner.py
A window will display your webcam feed with bounding boxes around detected humans.

(Optional) Save detection logs with timestamp and human count.

🔍 How It Works (Step-by-Step)
Activates webcam using cv2.VideoCapture(0).

Loads the YOLOv8 model for inference.

Processes each frame in real-time.

Detects and marks humans with bounding boxes.

Displays live results.

(Optional) Logs detections to a .csv file for later analysis.

🖼️ Example Output
On-screen Output:

yaml
Copy
Edit
🧍 Detected Humans: 3
Sample CSV Log (if enabled):

Timestamp	Count
2025-06-26 10:00 AM	4
2025-06-26 10:05 AM	2

🔄 Comparison With Other Applications
Feature	This Application ✅	Others ❌
Uses latest YOLOv8	✅ Yes	❌ Often outdated
Real-time webcam detection	✅ Yes	✅/❌ Varies
Lightweight and fast	✅ Yes	❌ Slower
Works completely offline	✅ Yes	❌ Often cloud-based
Easy to modify/customize	✅ Yes	❌ Less flexible

🔮 Future Enhancements
🧍‍♂️ Person tracking and heatmaps.

🎯 Intruder detection in restricted zones.

📡 CCTV integration for real-time alerts.

📊 Dashboard for live people counting.

🤖 Gender, age, posture recognition.

🤝 Contributions
Contributions are welcome!
To contribute:

Fork the repository

Create a new branch

Make your changes

Open a pull request

For major features, please open an issue first to discuss the proposed changes.

📬 Contact
Project Owner: Shivam Sorot
📧 Email: shivam29022000@gmail.com
