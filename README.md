# UV Therapy Skin Monitor (Skin Tone Detection)

This is a Python-based demo system that uses your webcam to monitor skin tone in real-time. It classifies the skin as **"Normal"** or **"Abnormal (Reddish Skin)"** based on average skin color within a selected region. This can be used to visually monitor the effects of UV therapy and assist in adjusting exposure levels.

---

## 📷 Features

- Real-time webcam video streaming
- Basic skin color analysis using OpenCV
- Detects reddish (possibly overexposed) skin tones inside the Green Square
- Displays "Normal" or "Abnormal" status on screen inside the Green Square

---
## 🔁 Clone the Project

```bash
git clone https://github.com/MwarandusLab/UV_Skin_Monitoring.git
```
Then:
```bash
cd UV_Skin_Monitoring
```
## 🔧 Setup Instructions

### ✅ Prerequisites

- Python 3.10+
- Webcam or External USB Camera

### 🐍 Create Virtual Environment
Navigate to your project folder
```bash
python -m venv venv
```
Activate it:
**Windows(Powershell):**
```bash
.\venv\Scripts\Activate.ps1
```
**macOS/Linux:**
source venv/bin/activate
### 📦 Install Dependencies
Install required libraries using the provided requirements.txt:
```bash
pip install -r requirements.txt
```
Or manually:
```bash
pip install opencv-python numpy
```
### 🚀 Running the Application
```bash
python app.py
```

