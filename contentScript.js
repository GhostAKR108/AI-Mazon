// const script = document.createElement("script");
// script.src = chrome.runtime.getURL("dialogue.js");
// document.body.appendChild(script);

document.addEventListener("mouseover", function(event) {
    let hoveredElement = event.target;
    // Send hovered element details to the popup or background script
    if(hoveredElement.parentNode.parentNode.nodeName === "A"){
        console.log("Hovered over a link:", hoveredElement.parentNode.parentNode.getAttribute('href'));
        // chrome.runtime.sendMessage({ target: "popup", action: "show", element: hoveredElement.parentNode.parentNode.getAttribute('href') });
        console.log("Popup msg sent...");
        chrome.runtime.sendMessage({target: "background", action: "scrape", element: "https://www.amazon.in" + hoveredElement.parentNode.parentNode.getAttribute('href')});
        console.log("Scrape msg sent...");
    }
    else{
        chrome.runtime.sendMessage({target: "popupno"});
    }
    console.log("Message sent...");
});
