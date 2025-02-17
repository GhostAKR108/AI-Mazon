chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
    console.log("Sending URL to Flask server");

    if (message.action === "scrape") {
        fetch("http://127.0.0.1:5000/scrape", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ url: message.element })
        })
        .then(response => {
            console.log("Response Status:", response.status);
            if (response.ok) {
                return response.json();
            } else {
                throw new Error("Failed to fetch data from the server.");
            }
        })
        .then(data => {
            console.log("Parsed Response:", data);
            chrome.runtime.sendMessage({target: "popup", action: "updateUI", data: data}); // Send the data back to content script
        })
        .catch(error => {
            console.error("Error while scraping:", error);
            chrome.runtime.sendMessage({tagret: "popup", action: "updateUI", data: {error: error.message}});
            // sendResponse({ error: error.message }); // Send error response
        });

        return true;  // This is crucial for handling async sendResponse
    }
});
