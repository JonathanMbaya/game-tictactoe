import tkinter

def check_win( clicked_row, clicked_col):
    #detecter la victoire horizontale
    count = 0
    for i in range(3):
        current_button = buttons[i][clicked_row]
        if current_button['text']== "X":
            count+= 1
    
    if count == 3:
        print("Victoire !")


    #detecter la victoire verticale
    count = 0
    for i in range(3):
        current_button = buttons[i][clicked_row]
        if current_button['text']== "X":
            count+= 1
    
    if count == 3:
        print("Victoire !")

def place_symbol(row, column):
    print('click', row, column)

    clicked_button = buttons[column][row]
    clicked_button.config(text="X")

    check_win(row, column)

def draw_grid():
    for column in range(3):
        buttons_in_cols = []
        for row in range(3):
            button = tkinter.Button(
                root, font=("Arial", 50),
                width=5, height=3,
                command=lambda r=row, c=column: place_symbol(r,c)
            )
            button.grid(row=row, column=column)
            buttons_in_cols.append(button)
        buttons.append(buttons_in_cols)

# stockage
buttons = []

# Créer la fenêtre de jeu 
root = tkinter.Tk()

# Personnalisation de la fenêtre
root.title("Jeu de Morpion")
root.minsize(500,500)

# Dessiner la grille de jeu
draw_grid()

# Lancer la boucle principale
root.mainloop()
