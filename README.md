🔗 https://smart-parking-system-nu.vercel.app/

🚘 Smart Parking System — Intelligent Parking Detection & Dashboard 🅿️

Welcome to Smart Parking System, an AI-powered real-time car parking detection and visualization system.
Simple to use. Powerful behind the scenes. 📡

🎯 Motto
“Smart cities need smart solutions.”
This system automates parking monitoring using computer vision, providing instant updates to a cloud database and displaying it on a clean web dashboard. Ideal for malls, IT parks, or any urban parking infrastructure.

🚀 Features

🧠 Real-time YOLOv8 Car Detection
📹 Supports Static & Live Video Feed
🔲 Custom Parking Area Zones via JSON
🔥 Firebase Realtime Database Integration
🗺️ Google Maps Integration (View Parking Location)
📊 Dynamic Web Dashboard: Live Table, Map, and Video
🎨 Clean UI with Pastel Gradients and Emoji Feedback
📝 Auto Logging of Status in CSV
⚡ Optimized for Vercel or Local Deployment

🧑‍💻 Tech Stack Used
Tool / Library	Purpose
YOLOv8 (Ultralytics)	Object detection for identifying cars
OpenCV	Video frame capture and image processing
Firebase RTDB	Cloud storage of parking availability data
HTML, CSS, JS	Frontend dashboard
Google Maps API	Display real-world parking locations
Vercel (optional)	Frontend hosting (blazing fast ⚡)


🧾 How It Works

🎯 Detect Cars:
The Python script reads each video frame and detects cars using YOLOv8.

📍 Match Zones:
Each car's center is compared against defined polygon zones (from parking_areas.json) using OpenCV.

🔄 Update Firebase:
The script sends real-time status (1 = Free, 0 = Occupied) to Firebase RTDB under /parking.

🖥️ Web Dashboard:
The frontend fetches the latest data from Firebase and shows:

A status table

A Google Map marker

A video demo stream

📝 CSV Logging:
Each detection frame is timestamped and saved to parking_log.csv.

