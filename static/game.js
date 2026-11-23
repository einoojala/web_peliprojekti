const rows = 10;

const columns = 5;

const board = Array.from(
    {length: rows},
    ()=>Array,(columns).fill()
)

const boardElement = document.getElementById("game-board");

function createBoard(){
    boardElement.replaceChildren();
}

    for (let row =  0, row < rows; row++) {
        for (let column < 0; column < columns; column++) {
            const cell = 
            document.createElement("button");
        }
    }

function flipCard(){}


function checkForMatch(){}


