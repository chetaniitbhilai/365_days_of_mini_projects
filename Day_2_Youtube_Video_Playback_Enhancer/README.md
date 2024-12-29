# YouTube Speed Controller Chrome Extension

This Chrome extension allows users to control the playback speed of YouTube videos with an easy-to-use interface. Users can increase or decrease the playback speed using a slider and reset the speed back to normal.

## Features

- **Speed Control**: Adjust YouTube video playback speed between 0.5x to 3x.
- **Reset to Normal**: One-click reset to the default playback speed (1x).
- **Intuitive UI**: Simple, user-friendly interface with a slider to control the speed and a reset button.

## Prerequisites

- Google Chrome (latest version)
- Basic understanding of how Chrome extensions work
- A YouTube account (optional, but necessary to test the extension)

## Installation

### 1. Clone the repository or download the source code
If you have the source code in a GitHub repository, you can clone it or download it as a ZIP file. If not, create the necessary files manually.

### 2. Load the extension in Chrome

1. Open **Chrome** and navigate to `chrome://extensions/`.
2. Enable **Developer mode** in the top right corner.
3. Click **Load unpacked** and select the folder where the project is located (the folder containing `manifest.json`, `popup.html`, `popup.js`, `content.js`, `styles.css`, and `icon.png`).
4. Once loaded, you should see the extension icon in the top-right corner of your Chrome browser.

### 3. Use the extension

1. Navigate to **YouTube** in your browser.
2. Click on the extension icon to open the popup.
3. Adjust the playback speed using the slider or reset it to 1x using the reset button.
4. The playback speed will immediately apply to the active YouTube video.


### Fun fact 
**This extenstion not only increases the speed of video but also the speed of the advertisements that comes on the youtube videos.**

## File Breakdown

- **`manifest.json`**: Metadata file that defines the extension settings, permissions, and popup.
- **`popup.html`**: Contains the HTML structure for the popup interface (slider and reset button).
- **`popup.js`**: Contains the JavaScript logic for interacting with the UI elements (slider and reset button) and sending commands to YouTube videos.
- **`content.js`**: Contains the code for interacting with the YouTube video element on the page and changing the playback speed.
- **`styles.css`**: Basic styling for the popup UI, including the slider and button.
- **`icon.png`**: Icon image displayed in the Chrome toolbar.

## Code Explanation

### `manifest.json`
The `manifest.json` file defines the extension's metadata, permissions, and settings. It specifies that the extension will work on YouTube and has access to scripting APIs to interact with the page content.

### `popup.html`
This HTML file is the structure of the popup that appears when you click the extension icon. It includes:
- A slider to adjust playback speed.
- A text element to display the current speed.
- A reset button to set the playback speed back to the default value of 1x.

### `popup.js`
This JavaScript file handles the logic of interacting with the popup:
- It listens for user input on the slider to update the playback speed.
- It sends the selected speed to the `content.js` script to adjust the video speed on the page.

### `styles.css`
This CSS file provides basic styling for the popup, including the layout of the slider and button, making the UI clean and easy to use.

### `icon.png`
An icon image that appears in the Chrome toolbar to represent the extension. You can replace it with your own icon if needed.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
