document.addEventListener("DOMContentLoaded", () => {

    const startButton = document.getElementById("startButton");
    const helpButton = document.getElementById("helpButton");

    const player1Input = document.getElementById("player1");
    const player2Input = document.getElementById("player2");

    const errorMessage = document.getElementById("errorMessage");


    startButton.addEventListener("click", async () => {


        const player1Name = player1Input.Value.trim();
        const player2Name = player1Input.Value.trim();

        
        errornMessage.textContent = "";

        if (player1Name == "" || player2Name === "") {
            
            errorMessage.textContent = "Anna molempien pelaajien nimet!";
            return;

    }

try {

    const response = await fetch("/start_game", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
    })
}
    
}

