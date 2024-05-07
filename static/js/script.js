function startGame() {
    // Récupération de l'élément canvas existant
    var canvas = document.getElementById("canvas");
    // Initialisation de Pygame.js
    var game = new PygameGame(canvas);
    // Démarrage du jeu
    game.start();
}