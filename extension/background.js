// Set up an object to store the logged text field values
let loggedValues = {};

// Listen for messages from the popup
chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  // If the message is for the startLogging function
  if (message.function === 'startLogging') {
    // Call the startLogging function
    startLogging();
  }
});
    
// Start logging text field values
function startLogging() {
  // Get all the text fields on the page
  const textFields = document.querySelectorAll('input[type=text]');

  // For each text field
  textFields.forEach(textField => {
    // Get the text field's name and value
    const name = textField.name;
    const value = textField.value;

    // If the text field doesn't already have a logged value
    if (!loggedValues[name]) {
      // Add the text field's name and value to the logged values object
      loggedValues[name] = value;
    }

    // Add an input event listener to the text field
    textField.addEventListener('input', () => {
      // Update the logged value for the text field
      loggedValues[name] = textField.value;
    });
  });
}

// Listen for the user to click the browser action
chrome.browserAction.onClicked.addListener(() => {
  // Create a file with the logged values
  const data = new Blob([JSON.stringify(loggedValues)], {type: 'application/json'});
  const fileName = 'logged-values.json';
  chrome.downloads.download({url: URL.createObjectURL(data), filename: fileName});
});
