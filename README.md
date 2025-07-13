🔗 **Live Demo**: [smart-parking-system.vercel.app](https://smart-parking-system-nu.vercel.app)

# 🚘 Smart Parking System — Intelligent Parking Detection & Dashboard 🅿️  


Welcome to **Smart Parking System**, an AI-powered real-time vehicle detection and visualization platform.  
Built to bring intelligence to modern parking spaces using Computer Vision + Cloud.  
**Simple to use. Powerful behind the scenes.** 📡

---

## 🎯 Motto  
> “Smart cities need smart solutions.”  
This system automates parking management by detecting vehicles in real time and updating their availability to the cloud, while providing a user-friendly, responsive dashboard.

---

## 🚀 Features

- 🧠 Real-time **YOLOv8** Car Detection  
- 📹 Supports Static & Live **Video Feed**  
- 🔲 Custom **Parking Area Zones** via JSON  
- 🔥 **Firebase Realtime Database** Integration  
- 🗺️ Embedded **Google Maps** to Locate Parking  
- 📊 Dynamic Web Dashboard: **Table + Video + Map**  
- 🎨 **Pastel UI** with Emoji Feedback  
- 📝 Automatic **CSV Logging** with Timestamps  
- ⚡ Deployed on **Vercel** for Fast & Secure Hosting  

---

## 🧑‍💻 Tech Stack

| Tool / Library         | Purpose                                       |
|------------------------|-----------------------------------------------|
| YOLOv8 (Ultralytics)   | Object detection (cars in parking video)      |
| OpenCV                 | Frame processing and centroid-based matching  |
| Firebase Realtime DB   | Cloud database for parking status (free/busy) |
| HTML, CSS, JavaScript  | Frontend dashboard (map, table, video)        |
| Google Maps API        | Map integration for location visualization    |
| Vercel                 | Hosting the frontend web app                  |

---

## 🧾 How It Works

### 1️⃣ Detect Cars
- The Python script reads each frame of a video using OpenCV and runs YOLOv8 to detect vehicles.

### 2️⃣ Match Zones
- For each car detected, it checks if the center point lies inside a predefined polygon (from `parking_areas.json`).

### 3️⃣ Update Firebase
- It updates Firebase with:
  - `1` = Free
  - `0` = Occupied

