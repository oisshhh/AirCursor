# AirCursor – Head and Eye Controlled Virtual Mouse

## Overview

AirCursor is a computer vision-based virtual mouse that enables hands-free interaction with a computer using head movements and eye blinks. The project uses MediaPipe Face Mesh to detect facial landmarks in real time, allowing users to control the mouse pointer by moving their head and perform mouse clicks through intentional eye blinks.

To demonstrate its practical application, the project also includes a Streamlit-based railway ticket booking interface with large, accessible buttons that can be operated entirely without a physical mouse or keyboard.

---

## Features

- Real-time face landmark detection using MediaPipe Face Mesh
- Cursor movement using nose position tracking
- Blink-based left mouse click using Eye Aspect Ratio (EAR)
- Cursor smoothing for stable movement
- Click cooldown to prevent accidental multiple clicks
- Live visualization of facial landmarks and nose position
- Accessible Streamlit GUI for railway ticket booking
- Hands-free interaction suitable for users with limited hand mobility

---

## Technologies Used

- Python
- OpenCV
- MediaPipe
- PyAutoGUI
- NumPy
- Streamlit

---

## Project Structure

```
├── head_tracking.py          # Head tracking and blink detection
├── bigButtons_frontend.py    # Streamlit railway ticket booking interface
└── README.md
```

---

## How It Works

1. The webcam captures the user's face in real time.
2. MediaPipe Face Mesh detects facial landmarks.
3. The nose tip landmark is mapped to screen coordinates to move the cursor.
4. Cursor movement is smoothed using an exponential moving average to reduce jitter.
5. The Eye Aspect Ratio (EAR) is calculated using eye landmarks.
6. When the EAR falls below a predefined threshold, a mouse click is triggered after a short cooldown period.
7. The virtual mouse can be used to navigate and interact with the railway ticket booking interface.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/AirCursor.git
cd AirCursor
```

Install the required packages:

```bash
pip install opencv-python mediapipe pyautogui numpy streamlit
```

---

## Running the Project

Start the Streamlit interface:

```bash
streamlit run bigButtons_frontend.py
```

Run the head-tracking module:

```bash
python head_tracking.py
```

Ensure that your webcam is connected and accessible.

---

## Future Improvements

- Right-click and double-click support
- Scroll functionality using facial gestures
- Eye-gaze-based cursor control
- Multi-monitor compatibility
- Voice command integration
- Customizable sensitivity and blink thresholds

---

## Applications

- Assistive technology for individuals with motor impairments
- Hands-free human-computer interaction
- Smart kiosks and public information systems
- Contactless computer control
- Accessibility research and educational projects

---

## License

This project is intended for educational and research purposes.
