from flask import Flask, render_template
from templates.tictac import TicTacToe 

app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/score')
def score():
    return render_template('score.html')

@app.route('/play')
def play():
    game = TicTacToe()  # Instancier la classe TicTacToe
    game.mainloop()     # Exécuter le jeu
    return "Game Over"  # Retourner un message une fois que le jeu est terminé

if __name__ == '__main__':
    app.run(debug=True)
