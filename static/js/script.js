function startGame() {
    var canvas = document.getElementById("canvas");
    var ctx = canvas.getContext("2d");
    var currentPlayer = "X";
    var board = [["", "", ""], ["", "", ""], ["", "", ""]];
    var gameOver = false;

    // Dessiner la grille de jeu
    function drawBoard() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        ctx.beginPath();
        ctx.moveTo(100, 0);
        ctx.lineTo(100, 300);
        ctx.moveTo(200, 0);
        ctx.lineTo(200, 300);
        ctx.moveTo(0, 100);
        ctx.lineTo(300, 100);
        ctx.moveTo(0, 200);
        ctx.lineTo(300, 200);
        ctx.stroke();
    }

    // Afficher le résultat de la partie dans la div
    function showResult(message) {
        var resultDiv = document.getElementById("resultDiv");
        resultDiv.innerHTML = message;
        resultDiv.style.display = "block";
    }

    // Gérer les clics sur le canvas
    canvas.addEventListener("click", function(event) {
        if (gameOver) return;
        var rect = canvas.getBoundingClientRect();
        var x = event.clientX - rect.left;
        var y = event.clientY - rect.top;
        var row = Math.floor(y / 100);
        var col = Math.floor(x / 100);
        if (board[row][col] === "") {
            board[row][col] = currentPlayer;
            drawSymbol(row, col, currentPlayer);
            if (checkWinner()) {
                showResult("Le joueur " + currentPlayer + " a gagné!");
                gameOver = true;
            } else if (checkTie()) {
                showResult("C'est un égalité");
                gameOver = true;
            } else {
                currentPlayer = currentPlayer === "X" ? "O" : "X";
            }
        }
    });

    // Dessiner le symbole sur le canvas
    function drawSymbol(row, col, player) {
        ctx.font = "60px Arial";
        ctx.fillText(player, col * 100 + 30, row * 100 + 80);
    }

    // Vérifier s'il y a un vainqueur
    function checkWinner() {
        for (var i = 0; i < 3; i++) {
            if (board[i][0] === board[i][1] && board[i][1] === board[i][2] && board[i][0] !== "") return true;
            if (board[0][i] === board[1][i] && board[1][i] === board[2][i] && board[0][i] !== "") return true;
        }
        if (board[0][0] === board[1][1] && board[1][1] === board[2][2] && board[0][0] !== "") return true;
        if (board[0][2] === board[1][1] && board[1][1] === board[2][0] && board[0][2] !== "") return true;
        return false;
    }

    // Vérifier s'il y a égalité
    function checkTie() {
        for (var i = 0; i < 3; i++) {
            for (var j = 0; j < 3; j++) {
                if (board[i][j] === "") return false;
            }
        }
        return true;
    }

    // Démarrer le jeu en dessinant la grille de jeu
    drawBoard();
}
