import random
from time import sleep 
from os import system, name
from tkinter import *
import tkinter as tk
from tkinter.ttk import *

#variaveis

numjogos=1
vitorias_utilizador=0
vitorias_pc=0
empates=0
opcao=0
opcaopc=0

#ficheiro para guardar resultados
f = open("data.txt", "w")
f.close()


#funcao criar objetos iniciais
# janela com objetos
janela = tk.Tk(className="Jogo")
# adicionar titulo e janela
Label(janela, text = 'Pedra , Papel , Tesoura', font =( 
   'Verdana', 15)).pack(side = TOP, pady = 10) 
moldura1 = tk.Canvas(janela, width = 500, height = 300)
moldura1.pack()

#adicionar textos
textopedra = tk.Label(janela, text= 'Voce escolheu Pedra!', fg='blue', font=('helvetica', 12, 'bold'))
textopapel = tk.Label(janela, text= 'Voce escolheu Papel!', fg='blue', font=('helvetica', 12, 'bold'))
textotesoura = tk.Label(janela, text= 'Voce escolheu Tesoura!', fg='blue', font=('helvetica', 12, 'bold'))
textopedra1 = tk.Label(janela, text= 'O adversário escolheu Pedra!', fg='black', font=('helvetica', 12, 'bold'))
textopapel1 = tk.Label(janela, text= 'O adversário escolheu Papel!', fg='black', font=('helvetica', 12, 'bold'))
textotesoura1 = tk.Label(janela, text= 'O adversário escolheu Tesoura!', fg='black', font=('helvetica', 12, 'bold'))
textoempate = tk.Label(janela, text= 'Ambos escolheram a mesma opção o resultado foi empate!', fg='blue', font=('helvetica', 12, 'bold'))
textowin = tk.Label(janela, text= 'O utilizador ganhou!', fg='green', font=('helvetica', 12, 'bold'))
textolose = tk.Label(janela, text= 'O adversário ganhou!', fg='red', font=('helvetica', 12, 'bold'))
textosep = tk.Label(janela, text= '------------------------------------------------------------------------------------------', fg='green', font=('helvetica', 12, 'bold'))
textosep1 = tk.Label(janela, text= '------------------------------------------------------------------------------------------', fg='green', font=('helvetica', 12, 'bold'))


# adicionar as imagens e redimencionamento
pedra = PhotoImage(file = r".\rock.png")
papel = PhotoImage(file = r".\paper.png") 
tesoura = PhotoImage(file = r".\scissors.png")
imagempedra = pedra.subsample(3, 3) 
imagempapel = papel.subsample(3, 3)
imagemtesoura = tesoura.subsample(3, 3) 


#definicao das açoes dos botões
def acaopedra ():
    opcao=1
    textopedra.place(x=10, y = 160)
    programa(opcao,numjogos,vitorias_utilizador,vitorias_pc,empates)

def acaopapel ():  
    opcao=2
    textopapel.place(x=10, y = 160)
    programa(opcao,numjogos,vitorias_utilizador,vitorias_pc,empates)

def acaotesoura ():  
    opcao=3
    textotesoura.place(x=10, y = 160)
    programa(opcao,numjogos,vitorias_utilizador,vitorias_pc,empates)

def clearFrame():
    textopedra.place_forget()
    textopapel.place_forget()
    textotesoura.place_forget()
    textopedra1.place_forget()
    textopapel1.place_forget()
    textotesoura1.place_forget()
    textoempate.place_forget()
    textowin.place_forget()
    textolose.place_forget()


def programa (opcao,numjogos,vitorias_utilizador,vitorias_pc,empates):
    # criar a opção do computador
    numerorandom=random.randint(0, 12)
    if numerorandom <= 4:
        opcaopc=1
        textopedra1.place(x=10, y = 200)
    
    elif numerorandom > 4 and numerorandom <= 8:
        opcaopc=2
        textopapel1.place(x=10, y = 200)
    
    elif numerorandom > 8 and numerorandom <= 12:
        opcaopc=3
        textotesoura1.place(x=10, y = 200)
    
    # escolher qual dos dois ganhou ou perdeu
    if opcao==opcaopc:
        textosep.place(x=10, y = 240)
        textoempate.place(x=10, y = 260)
        empates=empates+1
    elif opcao == 1 and opcaopc == 2:
        textosep.place(x=10, y = 240)
        textolose.place(x=10, y = 260)
        vitorias_pc=vitorias_pc+1
    elif opcao == 1 and opcaopc == 3:
        textosep.place(x=10, y = 240)
        textowin.place(x=10, y = 260)
        vitorias_utilizador=vitorias_utilizador+1
    elif opcao == 2 and opcaopc == 1:
        textosep.place(x=10, y = 240)
        textowin.place(x=10, y = 260)
        vitorias_utilizador=vitorias_utilizador+1
    elif opcao == 2 and opcaopc == 3:
        textosep.place(x=10, y = 240)
        textolose.place(x=10, y = 260)
        vitorias_pc=vitorias_pc+1
    elif opcao == 3 and opcaopc == 1:
        textosep.place(x=10, y = 240)
        textolose.place(x=10, y = 260)
        vitorias_pc=vitorias_pc+1
    elif opcao == 3 and opcaopc == 2:
        textosep.place(x=10, y = 240)
        textowin.place(x=10, y = 260)
        vitorias_utilizador=vitorias_utilizador+1
    f = open("data.txt", "a")
    f.write("%s %s %s %s %s %s \n" %(numjogos,vitorias_utilizador,vitorias_pc,empates,opcao,opcaopc))
    f.close()
    numjogos=numjogos+1
    bt_play_again = Button(janela, text = 'Jogar Novamente !',command=clearFrame,compound = LEFT).place(x=380,y=180)  

#definir os butoes
botaopedra = Button(janela, text = 'Pedra !',command=acaopedra,image = imagempedra,compound = LEFT).place(x=5,y=50)
botaopapel = Button(janela, text = 'Papel !',command=acaopapel,image = imagempapel,compound = LEFT).place(x=170,y=50)
botaotesoura = Button(janela, text = 'Tesoura !',command=acaotesoura,image = imagemtesoura,compound = LEFT).place(x=335,y=50)
textosep1.place(x=10, y = 280)

#iniciar janela
janela.mainloop()

    

   
    

