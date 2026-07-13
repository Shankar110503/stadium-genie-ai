async function sendMessage() {

    const input = document.getElementById("message");
    const message = input.value.trim();

    if (!message) return;

    const chat = document.getElementById("chat");

    chat.innerHTML += `<p class="user">You: ${message}</p>`;

    input.value = "";

    const response = await fetch("/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            message: message
        })
    });

    const data = await response.json();

    chat.innerHTML += `<p class="bot">AI: ${data.reply}</p>`;

    chat.scrollTop = chat.scrollHeight;
}
