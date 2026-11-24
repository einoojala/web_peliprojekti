const ROWS = 10;
const COLUMNS = 5;

const board = Array.from(
    { length: ROWS },
    () => Array(COLUMNS).fill(null)
);

const boardElement = document.getElementById("game-board");

function createBoard() {
    boardElement.replaceChildren();

    for (let row = 0; row < ROWS; row++) {
        for (let column = 0; column < COLUMNS; column++) {
            const cell = document.createElement("button");

            cell.type = "button";
            cell.className = "cell";
            cell.dataset.row = row;
            cell.dataset.column = column;

            cell.setAttribute(
                "aria-label",
                `Row ${row + 1}, column ${column + 1}`
            );

            cell.addEventListener("click", () => {
                console.log("Clicked:", row, column);
            });

            boardElement.appendChild(cell);
        }
    }
}

createBoard();

function flipCard() {}

function checkForMatch() {}