# 🚀 CrowdCount-OpenCV: Real-Time People Detection & Counter

A lightweight and efficient Python script powered by **OpenCV** to detect and count people/objects in real-time from pre-recorded gallery videos. The system processes the input video frame-by-frame, overlays dynamic bounding boxes, displays a live person counter, and outputs a high-quality tracked video back to your storage.

---

## 🔥 Features
* 📂 **Gallery Video Stream:** Reads any standard video format (`.mp4`, `.avi`, etc.) from local storage.
* 🤖 **Smart Detection:** Uses Haar Cascade Classifiers (`haarcascade_fullbody.xml`) for reliable person/body detection.
* 📊 **Live Analytics Overlay:** Displays a real-time tracking counter on the top-left corner using smooth Anti-Aliased (`cv2.LINE_AA`) fonts.
* 💾 **Auto-Save Output:** Automatically compiles and writes the processed video back to disk using the optimized `mp4v` codec.

---

## 🛠️ Prerequisites & Installation

Make sure you have Python installed on your system. Then, install the required dependencies:

```bash
pip install opencv-python
Note: Ensure you have the haarcascade_fullbody.xml (or haarcascade_frontalface_default.xml) file downloaded and placed in your working directory or correct path.

🚀 How To Run
Clone this repository:

Bash


git clone [https://github.com/YOUR_USERNAME/CrowdCount-OpenCV.git](https://github.com/YOUR_USERNAME/CrowdCount-OpenCV.git)
Navigate to the project directory and update the test_path in the script with your local video path.

Run the script:

Bash


python people_detector.py
Press 'r' on your keyboard anytime to stop processing and close the video window.

📝 Code Breakdown
cv2.VideoCapture(): Streams the video from your gallery.

detectMultiScale(): Scans the grayscale frames to look for bodies/faces.

len(frames): Calculates the exact number of objects detected per frame dynamically.

cv2.VideoWriter(): Smoothly packages the processed frames into a new .mp4 file.

📈 Next Milestones / Future Scope
[ ] Migrate from Haar Cascades to YOLO (You Only Look Once) for next-level accuracy and multi-class tracking.

[ ] Implement Region of Interest (ROI) selection to count people passing through a specific boundary.

[ ] Add an FPS (Frames Per Second) counter overlay to benchmark performance.

🤝 Contributing
Contributions, issues, and feature requests are welcome! Feel free to check the issues page if you want to contribute.

Give a ⭐️ if this project helped you!
# realtime-people-tracker
track people in real time movement
