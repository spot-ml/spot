chrome.runtime.onMessage.addListener(
    function(request, sender, sendResponse) {
        if (request.getText) {
            chrome.tabs.executeScript({
                file: 'contentScript.js'
            });
        }
        if(request.texts) {
            console.log(request.texts);
        }
    });
