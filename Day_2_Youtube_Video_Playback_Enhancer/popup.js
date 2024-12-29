document.addEventListener("DOMContentLoaded", () => {
    const slider = document.getElementById("speedSlider");
    const speedValue = document.getElementById("speedValue");
    const resetButton = document.getElementById("resetSpeed");
  
    // Update speed value display
    slider.addEventListener("input", () => {
      const speed = slider.value;
      speedValue.textContent = `${speed}x`;
      sendSpeedToContentScript(speed);
    });
  
    // Reset speed to normal
    resetButton.addEventListener("click", () => {
      slider.value = 1;
      speedValue.textContent = "1.0x";
      sendSpeedToContentScript(1);
    });
  
    // Function to send speed to content.js
    function sendSpeedToContentScript(speed) {
      chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
        chrome.scripting.executeScript({
          target: { tabId: tabs[0].id },
          func: (speed) => {
            const video = document.querySelector("video");
            if (video) video.playbackRate = speed;
          },
          args: [parseFloat(speed)]
        });
      });
    }
  });
  