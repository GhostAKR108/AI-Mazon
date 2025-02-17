// var dialogueBox = document.querySelector('.dialogue-box');

// function showDialogue(x, y, content) {
//     dialogueBox.style.left = `${x}px`;
//     dialogueBox.style.top = `${y}px`;
//     dialogueBox.innerHTML = content; // Set content dynamically
//     dialogueBox.classList.add('show');
// }

// function hideDialogue() {
//     dialogueBox.classList.remove('show');
// }

// chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
//     if (message.action === "show") {
//         console.log("Received message in popup");
//         if (message.element) {
//             const content = "https://www.amazon.in" + message.element;
//             document.addEventListener("mousemove", (event) => {
//                 showDialogue(event.pageX + 10, event.pageY + 10, content);
//             })

//         }
//     }
//     else {
//         hideDialogue();

//     }
// });




// // Example usage (move with cursor)
// // document.addEventListener("mouseleave", hideDialogue);
