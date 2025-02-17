import {getActiveTabURL} from "./utils.js";

// document.addEventListener("mousemove", function(event) {
//     let hoveredElement = document.elementFromPoint(event.clientX, event.clientY);
//     console.log("Hovered element:", hoveredElement);
// });

chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
    if (message.target === "popup") {
        if (message.action === "updateUI"){
            console.log("Information: ", message.data.productinfo);
            let outputElement = document.getElementById("product-info");
            // Update Title and Price
            
            // document.getElementById("product-info").innerText = info;
            outputElement.innerText = message.data.productinfo;
        }
        
        else {
            document.getElementById("hover-info").innerText = "Nothing to show";
        }
    }
});




document.addEventListener("DOMContentLoaded", async ()=>{
    const activeTab = await getActiveTabURL();

    if(activeTab && activeTab.url.includes("amazon")){
        console.log("Amazon website running...")
    }
    else{
        console.log("Not running any Amazon site...")
        document.getElementById("message").innerHTML = "This is not an Amazon page"
    }
})