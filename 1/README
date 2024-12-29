# Use Your Phone as a Touchpad

This project allows you to use your phone as a touchpad for your computer. You can control the mouse pointer and perform clicks using a simple client-server architecture. The program uses Python for the server and an HTML/JavaScript-based client that runs in your phone's web browser.

---

## Features
- *Mouse Movement:* Move the mouse pointer by dragging your finger across the phone screen.
- *Left-Click:* Tap on the phone screen to perform a left mouse click.

---

## Requirements
1. Python 3 installed on your computer.
2. pynput Python library:
   bash
   pip install pynput
   
3. A modern web browser on your phone (e.g., Chrome, Safari).
4. Both your phone and computer connected to the same network (Wi-Fi).

---

## Setup Instructions

### 1. Clone the Repository
1. Open a terminal or command prompt and run the following command to clone the repository:
   bash
   git clone <repository_url>
   
   Replace <repository_url> with the actual URL of your repository.

2. Navigate to the cloned repository directory:
   bash
   cd <repository_directory>
   

### 2. Server Setup (Computer)
1. *Run the server code:*
   In the terminal, run:
   bash
   python server.py
   

2. The server will display a message like:
   
   Server listening on 0.0.0.0:5000
   

### 3. Client Setup (Phone)
1. *Host the HTML client:*
   - In the terminal, run:
     bash
     python -m http.server 8000
     
   - This will serve the index.html file on port 8000.

2. *Access the webpage on your phone:*
   - Open your phone’s browser (e.g., Chrome, Safari).
   - Enter the URL: http://<YOUR_COMPUTER_IP>:8000/index.html
     For example, if your computer’s IP is 192.168.1.10, enter:
     
     http://192.168.1.10:8000/index.html
     

3. **Replace YOUR_SERVER_IP:**
   - Find your computer’s IP address.
     - On Windows: Open Command Prompt and type ipconfig.
     - On macOS/Linux: Open Terminal and type ifconfig.
   - Replace YOUR_SERVER_IP in the index.html file with your computer's IP address (e.g., 192.168.1.10).

---

## Usage
1. Drag your finger on the phone screen to move the mouse pointer on your computer.
2. Tap the screen to perform a left mouse click.

---

## Troubleshooting
- *Server not starting:* Ensure Python is installed correctly and that the pynput library is installed.
- *Phone can’t connect to the webpage:* Ensure your computer’s firewall isn’t blocking connections.
- *Mouse not moving:* Double-check the IP address and ensure your devices are on the same network.

---

## Future Enhancements
- *Right-Click:* Add a two-finger tap for right-click functionality.
- *Scrolling:* Add swipe gestures to simulate scroll events.
- *Double-Click:* Add support for double-tap to perform double-click actions.

Feel free to extend the code as needed!