
from tkinter import *
import pyperclip

retorno = 0
share_word = ""

def programa(z):
    global retorno
    global share_word
    share_word = ""
    retorno = z
    resultado_text["text"] = "Resultado:"
    resultado_text["width"] = 20

    palavra = Inserir_palavra.get().strip().lower()#Entry da palavra
    palpite = Inserir_palpite.get().strip().lower()#Entry do palpite

    if(len(palavra) == len(palpite)):
        print("O amigão está funcionando")

        if(retorno >0):
            #Vai deletar as imagens
            for y in range(retorno):
                Imagem[y].pack_forget()

            #Teste for em uma linha:
            #Imagem[for y in range(retorno)].pack_forget()
            Imagem.clear()

        palpite_count = 0
        for x in range(len(palavra)):#adiciona vermelho pra tudo

            Imagem.append(Label(canvas1, height = 30, width = 30))
            Imagem[x]["image"] = red_square #vermelho por padrão
            share_word += "🟥"



# em casos de letras repetidas nos palpites, está indicando como amarelo ainda
#Exemplo:
#Palavra = Verda
#Palpite = Veraa
#Resultado esperado = GGGRG (G = Verde, Y = Amarelo, R= Vermelho)
#Resultado = GGGYG (G = Verde, Y = Amarelo, R= Vermelho)
#ver um jeito de indicar as ocorrências de letras repetidas nas palavras e palpites


        for c in range(len(palpite)): #range pode passar só o len(palpite)
            if(palavra[c] == palpite[c]):#se as letras corresponderem na posição lá
                Imagem[palpite_count]["image"] = green_square
                share_word = share_word[:palpite_count] + "🟩" + share_word[palpite_count+1:]#deu green
            else:
                for d in range (0, len(palpite)):# repete o processo pra verificar o amarelo
                    if(palavra[d] == palpite[c]):

                        Imagem[palpite_count]["image"] = yellow_square
                        share_word = share_word[:palpite_count] + "🟨" + share_word[palpite_count+1:]#deu yellow
            canvas1.pack()
            Imagem[palpite_count].pack(padx = 2, pady = 2, side=LEFT)
            Imagem[palpite_count].pack_propagate(flag=1)
            palpite_count += 1
        else:

            if(len(palavra)>0):
                retorno = x+1
            return retorno


    else:
        print("Verifique a quantidade de letras das palavras")
        resultado_text["text"] = "Erro! Verifique a quantidade de letras das palavras"
        resultado_text["width"] = 40


def compartilhar():
    pyperclip.copy(share_word)

    #🟥 = Vermelho
    #🟨 = Amarelo
    #🟩 = Verde
    #⬛ = Preto (Se necessário)


Termo = Tk()
#Termo.geometry("250x250")
Termo.title("Termo ZAP Version - v2.0")

#Frames e canvas
frame1 = Frame(Termo)
frame2 = Frame(Termo)
frame3 = Frame(Termo)

frame1.pack(expand=True)#pady = 5)
frame2.pack(expand=True)#pady = 5)
frame3.pack(expand=True)#pady = 5)
canvas1 = Canvas(Termo)

#Label
Palavra_text = Label(frame1, text ="Insira a palavra a ser adivinhada", width = 25)
Palavra_text.pack()

#Entrada palavra
Inserir_palavra = Entry(frame1)
Inserir_palavra.pack()

#Label
Palpite_text = Label(frame2, text = "Insira o palpite", width = 20)
Palpite_text.pack()

#Entrada palpite
Inserir_palpite = Entry(frame2)
Inserir_palpite.pack()


#Botões
Butaun = Button(frame3, text="Verificar", command= lambda:programa(retorno), width = 10)
Butaun.pack()

Butaun2 = Button(frame3, text="Compartilhar", command= compartilhar, width = 10)
Butaun2.pack()#side=LEFT)


resultado_text = Label(frame3, text= "Resultado:", width = 20)
resultado_text.pack()

#imagens
red_square = PhotoImage(file = "Imagens/red_square.png")
green_square = PhotoImage(file = "Imagens/green_square.png")
yellow_square = PhotoImage(file = "Imagens/yellow_square.png")
black_square = PhotoImage(file = "Imagens/black_square.png")#fundo

#Lista de imagens para criar o esquema da sequência
Imagem = []
#quadrado vermelho = Letra errada
#quadrado amarelo = letra certa, lugar errado
#quadrado verde = letra certa, lugar certo

Termo.mainloop()
