window.onload = function() {
   console.log("WebChat is initializing...");
   WebChat.init({
     title: "Chatbot",
     subtitle: "Ρώτησέ με οτιδήποτε!",
     initPayload: "/greet",  // Αρχικό payload
     inputTextFieldHint: "Πληκτρολόγησε εδώ...",
     profileAvatar: "https://your-avatar-url.com/avatar.png",  // Εικόνα του avatar
     openLauncherImage: "https://your-launcher-url.com/launcher.png",  // Εικόνα του launcher
     showMessageDate: true,
     params: { storage: "session" },
     socketUrl: "http://localhost:5005",  // Διεύθυνση του Rasa server
     socketPath: "/socket.io/",
     language: "el",  // Ρύθμιση γλώσσας
     userMessageEvent: "user_uttered",
     botMessageEvent: "bot_uttered",
     customMessageDelay: (message) => {
         return 200 + message.length;  // Καθυστέρηση για τα μηνύματα
     }
   }, document.getElementById("webchat"));
};
