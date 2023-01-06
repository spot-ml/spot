// Get the start logging button
const startLoggingButton = document.getElementById('start-logging-button');

// Add a click event listener to the button
startLoggingButton.addEventListener('click', () => {
  // Send a message to the active tab to start logging text field values
  chrome.tabs.query({active: true, currentWindow: true}, tabs => {
    chrome.tabs.sendMessage(tabs[0].id, {function: 'startLogging'});
  });
});
