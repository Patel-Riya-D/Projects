function toggleChat() {
  const bot = document.getElementById("chatbot-container");
  bot.style.display = (bot.style.display === "none") ? "block" : "none";
}

function handleChat() {
  const input = document.getElementById("chat-input");
  const msg = input.value.toLowerCase();
  const log = document.getElementById("chat-messages");

  const user = document.createElement("p");
  user.innerHTML = "<strong>🧑‍💼 You:</strong> " + msg;
  log.appendChild(user);

  const bot = document.createElement("p");
  bot.innerHTML = "<strong>🤖 AIVi:</strong> Typing...";
  log.appendChild(bot);

  setTimeout(() => {
    let reply = "I'm still learning! Try asking about resume scores.";
    if (msg.includes("score")) reply = "Resumes are scored using AI based on job description similarity.";
    else if (msg.includes("download")) reply = "Click the 'Download Report' button to save CSV.";
    else if (msg.includes("hello") || msg.includes("hi")) reply = "Hello! Ask me anything about resume ranking.";
    else if (msg.includes("developer")) reply = "I'm tailored to help screen Data Scientist resumes currently.";

    bot.innerHTML = `<strong>🤖 AIVi:</strong> ${reply}`;
    log.scrollTop = log.scrollHeight;
  }, 500);

  input.value = "";
}
