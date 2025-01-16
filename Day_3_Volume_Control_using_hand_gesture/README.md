# Volume Control Using Hand Gestures

This project provides a Python-based implementation for controlling system volume using hand gestures. It leverages computer vision techniques and libraries to detect hand movements and map them to volume controls.

## Project Structure

- **`hand_tracking.ipynb`**: A Jupyter Notebook for testing and experimenting with hand-tracking techniques.
- **`hand_tracking.py`**: Python script for hand tracking functionality, likely used as a helper module.
- **`volume_gesture_control_ubuntu.py`**: Volume control implementation tailored for Ubuntu operating systems.
- **`volume_gesture_control_wnds.py`**: Volume control implementation tailored for Windows operating systems.
- **`requirements.txt`**: Contains the list of Python dependencies required to run the project.
- **`README.md`**: Documentation for the project (this file).

## Prerequisites

- Python 3.x
- Ensure the required Python packages are installed using `requirements.txt`.

```bash
pip install -r requirements.txt
```

## Usage

1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd volume_control-main
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the volume control script:
   - For Ubuntu:
     ```bash
     python volume_gesture_control_ubuntu.py
     ```
   - For Windows:
     ```bash
     python volume_gesture_control_wnds.py
     ```

4. Optionally, use `hand_tracking.py` or `hand_tracking.ipynb` for testing hand-tracking functionalities.

## Features

- Platform-specific implementation for volume control (Ubuntu and Windows).
- Uses hand gestures detected via a webcam to adjust system volume.

## Dependencies

- OpenCV
- Mediapipe
- Other packages listed in `requirements.txt`.

## Contribution

Feel free to fork the repository, raise issues, or submit pull requests for enhancements or bug fixes.

## License

This project is licensed under Apache License 2.0.
