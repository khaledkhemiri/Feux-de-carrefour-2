# mon projet de feux de carrefour
# avec tkinter
from Tkinter import*
#! /usr/bin/env python
# -*- coding: Latin-1 -*-
 

 
import time
# programme principal
# les variables suivantes seront utilisées de manière globale :
x1, y1 =200,20        # coordonnées initiales
x2, y2 =280,570        # coordonnées initiales de la voiture
 
 
# Création du widget principal ("maître") :
root=Tk()# -*- coding: cp1252 -*-
 
root.title("Projet Feux de carrefour")
# création des widgets "esclaves" :
 
# dessiner le fond
 
a = 0
b = 0
 
can1 = Canvas(root, bg='dark grey',height=640,width=480)
feux=can1.create_rectangle(100,100,290,590,width=5,fill='black')
 
 
led1=can1.create_oval(125,125,250,250,width=5,fill='white')
led2=can1.create_oval(125,280,250,400,width=5,fill='white')
led3=can1.create_oval(125,405,250,530,width=5,fill='white')
 
time.sleep(3)
 
# while  a  < 1 : 
    # print a
led1=can1.create_oval(125,125,250,250,width=5,fill='red')
time.sleep(3)
led1=can1.create_oval(125,125,250,250,width=5,fill='white')
led2=can1.create_oval(125,280,250,400,width=5,fill='yellow')   

can1.pack(side=LEFT)
 
 
 
Button(root,text='Quitter',command=root.quit).pack(side=BOTTOM)
 
# Button(fen, text='Start', command =start).pack(side =LEFT, padx =10)
 
 
# démarrage du réceptionnaire d'évènements (boucle principale) :
root.mainloop()

