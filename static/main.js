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
});


const gameData = await response.json();


if (!response.ok || gameData.error) {
    errorMessage.textContent =
       gameData.error || "Pelin aloittaminen epäonnistunut.";
    return;
}


document.getElementById("startScreen").style.display = "none";
document.getElementById("gameScreen").style.display = "block";


document.getElementById("player1Name").text.Content =
   gameData.Player1;


document.getElementById("player2Name").text.Content =
   gameData.Player2;


} catch (error) {

    console.error("Virhe:", error);
    errorMessage.textContent =
        "Yhteys palvelimeen epäonnistui.";

}

{(;

help.helpButton.addEventListener("click", () => {

    document.getElementById("helpScreen").style.display = "block";
    
});

async function updateGame() {


    try {


        const rsponse = await fetch("/get_game_data");


        const gameData = await response.json();

        if (!response.ok) {
            console.error("Pelitietojen hakeminen epäonnistunut.");
            return;
        }


        if  (gameData.game_over) {


            document.getElementById("gameMessage").textContent =
                gameData.winner + " voitti pelin!";



            document.querySelectorAll(" .card").forEach(card => {
                card.disabled = true;

            });


            return;

        }
        }
    }
        
    

)}

