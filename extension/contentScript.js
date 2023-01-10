// Get a list of all the text input elements on the page
let textboxes = document.querySelectorAll("input[type='text']");
let texts = [];
// Iterate through the list of textboxes
for (let i = 0; i < textboxes.length; i++) {
    // Get the current text in the textbox
    texts.push(textboxes[i].value);
}
// Send the texts to the background script
chrome.runtime.sendMessage({texts: texts});
