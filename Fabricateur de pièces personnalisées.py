import tkinter as tk

def custom_piece():
    """
    Créé une fenêtre composée d'une grille et de 3 bouttons pour créer une pièce
    personnalisée pour le Tétris (dans la même dossier)
    """
    global x_can,y_can,c,can,fra_bot
    x_can=10 #Nombre de cases en largeur et en hauteur de la grille
    y_can=10
    c=300//greater(y_can,x_can) #Taille en pixels de chaque case de la grille

    fen=tk.Tk()
    fen.title('Créer une pièce')

    can=tk.Canvas(fen,width=c*x_can,height=c*y_can,bg='black',bd=2,
        relief=tk.SOLID)
    can.grid(column=0,row=0)

    can.bind('<Button-1>',click)

    fra_bot=tk.Frame(fen,width=c*x_can,height=50,bg='black',bd=2,
        relief=tk.SOLID)
    fra_bot.grid(column=0,row=1)

    but_add_row=tk.Button(fra_bot,text='Ajouter une ligne',font='Verdanna 12',
        command=add_row)
    but_add_row.grid(column=0,row=0)

    but_done=tk.Button(fra_bot,text='Valider',font='Verdanna 12',
        command=done)
    but_done.grid(column=1,row=0)

    but_add_col=tk.Button(fra_bot,text='Ajouter une colonne',font='Verdanna 12',
        command=add_col)
    but_add_col.grid(column=2,row=0)

    #Liste de l'état de la grille
    list_state=[[0 for x  in range(x_can)] for y in range(y_can)]

    can_maj()

    fen.mainloop()

def add_col():
    """
    Ajoute une colonne à la grille
    """
    global x_can,y_can,can,fra_bot,c
    list_state.append([0 for a in range(y_can)])
    x_can+=1
    can.configure(width=c*x_can)
    fra_bot.configure(width=c*x_can)
    can_maj()


def add_row():
    """
    Ajoute une ligne à la grille
    """
    global x_can,y_can,can,c
    for col in list_state:
        col.append(0)
    y_can+=1
    can.configure(height=c*y_can)
    can_maj()

def dim_piece(piece,xy):
    """Renvoie la dimention du carré ou du rectangle contenant la pièce
    Arguments:
    ----------
        piece:list de tuples

        xy:bool
        True pour retourner les longueurs des cotés du rectangle
        contenant la pièce

        False pour la longeur du carré contenant la pièce"""
    list_ext=[[piece[0][0],piece[0][0]],[piece[0][1],piece[0][1]]]
    for pix in piece:
        list_ext=[[smaller(list_ext[0][0],pix[0]),
            greater(list_ext[0][1],pix[0])],[smaller(list_ext[1][0],pix[1]),
            greater(list_ext[1][1],pix[1])]]
    if xy:
        return list_ext[0][1]-list_ext[0][0]+1,list_ext[1][1]-list_ext[1][0]+1
    else:
        return greater(list_ext[0][1]-list_ext[0][0],
                       list_ext[1][1]-list_ext[1][0])+1


def comp(piece):
    sx=piece[0][0]
    sy=piece[0][1]
    for pix in piece:
        sx=smaller(sx,pix[0])
        sy=smaller(sy,pix[1])
    return [(pixe[0]-sx,pixe[1]-sy) for pixe in piece]

def done():
    """
    Affiche dans la console la liste des coordonnées de la pièce personnalisée
    """
    piece_temp=comp([(x,y) for x in range(x_can) for y in range(y_can) if list_state[x][y]==1])
    n=dim_piece(piece_temp,False)
    n_x,n_y=dim_piece(piece_temp,True)
    #Centre la pièce dans le plus petit carré pouvant la contenir
    print([(pix[0]+((n-n_x)+abs(n-n_x))//4,pix[1]+((n-n_y)+abs(n-n_y))//4) for pix in piece_temp])



def click(event):
    """
    Change l'état de la case sur laquelle l'utilisat.eur.rice clique de activée
    à désactivée ou inversement
    """
    global c
    x_click=event.x//c
    y_click=event.y//c
    list_state[x_click][y_click]=abs(list_state[x_click][y_click]-1)
    can_maj()


def smaller(a,b):
    """
    Fonction qui renvoie le plus petit élément entre a et b

    Arguments:
        a : type=int or float
        b : type=int or float

    Returns:
        small : type=int or float
            Le plus petit élément entre a et b

    """
    if a>b:
        return b
    else:
        return a

def greater(a,b):
    """
    Fonction qui renvoie le plus grand élément entre a et b

    Arguments:
        a : type=int or float
        b : type=int or float

    Returns:
        great : type=int or float
            Le plus grand élément entre a et b

    """
    if a<b:
        return b
    else:
        return a

def can_maj():
    """
    Met à joue la grille selon l'état de la liste
    """
    global can,list_state,x_can,y_can
    can.delete(tk.ALL)
    for x in range(x_can):
        for y in range(y_can):
            if list_state[x][y]==0:
                can.create_rectangle(x*c,y*c,(x+1)*c,(y+1)*c,fill='grey',
                    outline='black',width=2)


custom_piece()