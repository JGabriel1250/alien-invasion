from tkinter import *
from consatantes import *
from calculo_par_impar import *
import random
import sys
import os
import tkinter.messagebox as mbox

def restart_programa():
    python = sys.executable
    os.execl(python, python, *sys.argv)

raiz = Tk()

class janela():
    """Construtor da janela do jogo"""

    def __init__(self, raiz):
        self.fr1 = Frame(raiz, bg=cinza1)
        self.fr1.pack()

        self.fr_result = Frame(raiz, bg=cinza1)
        self.fr_result.pack()

        self.fr2 = Frame(raiz, bg=cinza1)
        self.fr2.pack()

        self.fr3 = Frame(raiz, bg=cinza1)
        self.fr3.pack()

        self.fr4 = Frame(raiz, bg=cinza1)
        self.fr4.pack()

        self.fr5 = Frame(raiz, bg=cinza1)
        self.fr5.pack()

        self.fr6 = Frame(raiz, bg=cinza1)
        self.fr6.pack()


        self.img_player = PhotoImage(file='par_ou_ímpar_shinobi/imagens/ninja.png')
        self.img_pc = PhotoImage(file='par_ou_ímpar_shinobi/imagens/robo.png')
        self.img0 = PhotoImage(file='par_ou_ímpar_shinobi/imagens/numero_0.png')
        self.img1 = PhotoImage(file='par_ou_ímpar_shinobi/imagens/numero_1.png')
        self.img2 = PhotoImage(file='par_ou_ímpar_shinobi/imagens/numero_2.png')
        self.img3 = PhotoImage(file='par_ou_ímpar_shinobi/imagens/numero_3.png')
        self.img4 = PhotoImage(file='par_ou_ímpar_shinobi/imagens/numero_4.png')
        self.img5 = PhotoImage(file='par_ou_ímpar_shinobi/imagens/numero_5.png')
        self.img6 = PhotoImage(file='par_ou_ímpar_shinobi/imagens/numero_6.png')
        self.img7 = PhotoImage(file='par_ou_ímpar_shinobi/imagens/numero_7.png')
        self.img8 = PhotoImage(file='par_ou_ímpar_shinobi/imagens/numero_8.png')
        self.img9 = PhotoImage(file='par_ou_ímpar_shinobi/imagens/numero_9.png')
        self.img10 = PhotoImage(file='par_ou_ímpar_shinobi/imagens/numero_10.png')


        self.lb1 = Label(self.fr1, text= 'BATALHA SHINOBI', bg=cinza1, font=fonte1, fg=azul2 ,padx=35)
        self.lb1.pack(side=LEFT)

        self.botao_restart = Button(self.fr1, text='Restart', font=fonte4, relief=RAISED, command=self.resetar)
        self.botao_restart.bind('<Return>', self.resetar2)
        self.botao_restart.pack(side=LEFT)

        self.lb_result = Label(self.fr_result, text='', bg=cinza1, font=fonte1, fg='green')
        self.lb_result.pack()


        self.placar1 = 0
        self.placar2 = 0
        self.lb2 = Label(self.fr2, text=f'    JOGADOR         {self.placar1}    X    {self.placar2}     COMPUTADOR',
                          bg=cinza1, font=fonte2, fg=azul2, pady=10.)
        self.lb2.pack()

        self.lb_img1 = Label(self.fr3, image=self.img_player, bg=cinza1)
        self.lb_img1.pack(side=LEFT, padx=25)

        self.lb_img2 = Label(self.fr3, image=self.img_pc, bg=cinza1)
        self.lb_img2.pack(side=LEFT, padx=25)

        self.escolha = StringVar()

        self.rb_par = Radiobutton(self.fr4, text='Par', value='par', variable=self.escolha, bg=cinza1,
                                  fg=azul2, font=fonte2, pady=20)
        self.rb_par.pack(side=LEFT)

        self.rb_impar = Radiobutton(self.fr4, text='Ímpar', value='impar', variable=self.escolha, bg=cinza1,
                                    fg=azul2, font=fonte2, pady=20)
        self.rb_impar.pack(side=LEFT)

        self.lb3 = Label(self.fr5, text='Número de 0 a 10', bg=cinza1, fg=azul2, font=fonte3, width=15, pady=20)
        self.lb3.pack(side=LEFT)

        self.num = Entry(self.fr5, width=3, font=fonte3)
        self.num.pack(side=LEFT)

        self.bt_jogar = Button(self.fr6, text='ENTER', font=fonte1, bg=cinza2, relief=RAISED, border=8, command=self.jogar)
        self.bt_jogar.bind('<Return>', self.jogar2)
        self.bt_jogar.focus_force()
        self.bt_jogar.pack()

        self.lb_erro = Label(self.fr6, text='', font=fonte4, bg=cinza1, fg=vermelho)
        self.lb_erro.pack()

    def jogar(self):
        try:
            num = int(self.num.get())
            escolha = self.escolha.get()
            num_robo = random.randrange(0,10)


            if escolha == 'par' or escolha == 'impar':
                if num >= 0 and num <= 10:
                    if num == 0:
                        self.lb_img1['image'] = self.img0
                        self.lb_erro['text'] = ''
                    elif num == 1:
                        self.lb_img1['image'] = self.img1
                        self.lb_erro['text'] = ''
                    elif num == 2:
                        self.lb_img1['image'] = self.img2
                        self.lb_erro['text'] = ''
                    elif num == 3:
                        self.lb_img1['image'] = self.img3
                        self.lb_erro['text'] = ''
                    elif num == 4:
                        self.lb_img1['image'] = self.img4
                        self.lb_erro['text'] = ''
                    elif num == 5:
                        self.lb_img1['image'] = self.img5
                        self.lb_erro['text'] = ''
                    elif num == 6:
                        self.lb_img1['image'] = self.img6
                        self.lb_erro['text'] = ''
                    elif num == 7:
                        self.lb_img1['image'] = self.img7
                        self.lb_erro['text'] = ''
                    elif num == 8:
                        self.lb_img1['image'] = self.img8
                        self.lb_erro['text'] = ''
                    elif num == 9:
                        self.lb_img1['image'] = self.img9
                        self.lb_erro['text'] = ''
                    elif num == 10:
                        self.lb_img1['image'] = self.img10
                        self.lb_erro['text'] = ''
                    

                    if num_robo == 0:
                        self.lb_img2['image'] = self.img0
                    elif num_robo == 1:
                        self.lb_img2['image'] = self.img1
                    elif num_robo == 2:
                        self.lb_img2['image'] = self.img2
                    elif num_robo == 3:
                        self.lb_img2['image'] = self.img3
                    elif num_robo == 4:
                        self.lb_img2['image'] = self.img4
                    elif num_robo == 5:
                        self.lb_img2['image'] = self.img5
                    elif num_robo == 6:
                        self.lb_img2['image'] = self.img6
                    elif num_robo == 7:
                        self.lb_img2['image'] = self.img7
                    elif num_robo == 8:
                        self.lb_img2['image'] = self.img8
                    elif num_robo == 9:
                        self.lb_img2['image'] = self.img9
                    elif num_robo == 10:
                        self.lb_img2['image'] = self.img10


                
                    par_impar = calcular_par_impar(num, num_robo)
                    if par_impar == 'Par':
                        self.lb_result['text'] = 'DEU PAR'
                    elif par_impar == 'Ímpar':
                        self.lb_result['text'] = 'DEU ÍMPAR'

                    if par_impar == 'Par' and escolha == 'par':
                        self.placar1 += 1
                        self.lb2['text'] = f'    JOGADOR         {self.placar1}    X    {self.placar2}     COMPUTADOR'

                    elif par_impar == 'Par' and escolha == 'impar':
                        self.placar2 += 1
                        self.lb2['text'] = f'    JOGADOR         {self.placar1}    X    {self.placar2}     COMPUTADOR'

                    elif par_impar == 'Ímpar' and escolha == 'impar':
                        self.placar1 += 1
                        self.lb2['text'] = f'    JOGADOR         {self.placar1}    X    {self.placar2}     COMPUTADOR'

                    elif par_impar == 'Ímpar' and escolha == 'par':
                        self.placar2 += 1
                        self.lb2['text'] = f'    JOGADOR         {self.placar1}    X    {self.placar2}     COMPUTADOR'



                else:
                    self.lb_erro['text'] = 'ERRO! ESCOLHA PAR OU ÍMPAR E DIGITE ENTRE 0 A 10'

            else:
                self.lb_erro['text'] = 'ERRO! ESCOLHA PAR OU ÍMPAR E DIGITE ENTRE 0 A 10'


        except:
            self.lb_erro['text'] = 'ERRO! ESCOLHA PAR OU ÍMPAR E DIGITE ENTRE 0 A 10'
                
            

    def jogar2(self, event):
        try:
            num = int(self.num.get())
            escolha = self.escolha.get()
            num_robo = random.randrange(0,10)


            if escolha == 'par' or escolha == 'impar':
                if num >= 0 and num <= 10:
                    if num == 0:
                        self.lb_img1['image'] = self.img0
                        self.lb_erro['text'] = ''
                    elif num == 1:
                        self.lb_img1['image'] = self.img1
                        self.lb_erro['text'] = ''
                    elif num == 2:
                        self.lb_img1['image'] = self.img2
                        self.lb_erro['text'] = ''
                    elif num == 3:
                        self.lb_img1['image'] = self.img3
                        self.lb_erro['text'] = ''
                    elif num == 4:
                        self.lb_img1['image'] = self.img4
                        self.lb_erro['text'] = ''
                    elif num == 5:
                        self.lb_img1['image'] = self.img5
                        self.lb_erro['text'] = ''
                    elif num == 6:
                        self.lb_img1['image'] = self.img6
                        self.lb_erro['text'] = ''
                    elif num == 7:
                        self.lb_img1['image'] = self.img7
                        self.lb_erro['text'] = ''
                    elif num == 8:
                        self.lb_img1['image'] = self.img8
                        self.lb_erro['text'] = ''
                    elif num == 9:
                        self.lb_img1['image'] = self.img9
                        self.lb_erro['text'] = ''
                    elif num == 10:
                        self.lb_img1['image'] = self.img10
                        self.lb_erro['text'] = ''
                    

                    if num_robo == 0:
                        self.lb_img2['image'] = self.img0
                    elif num_robo == 1:
                        self.lb_img2['image'] = self.img1
                    elif num_robo == 2:
                        self.lb_img2['image'] = self.img2
                    elif num_robo == 3:
                        self.lb_img2['image'] = self.img3
                    elif num_robo == 4:
                        self.lb_img2['image'] = self.img4
                    elif num_robo == 5:
                        self.lb_img2['image'] = self.img5
                    elif num_robo == 6:
                        self.lb_img2['image'] = self.img6
                    elif num_robo == 7:
                        self.lb_img2['image'] = self.img7
                    elif num_robo == 8:
                        self.lb_img2['image'] = self.img8
                    elif num_robo == 9:
                        self.lb_img2['image'] = self.img9
                    elif num_robo == 10:
                        self.lb_img2['image'] = self.img10


                
                    par_impar = calcular_par_impar(num, num_robo)
                    if par_impar == 'Par':
                        self.lb_result['text'] = 'DEU PAR'
                    elif par_impar == 'Ímpar':
                        self.lb_result['text'] = 'DEU ÍMPAR'

                    if par_impar == 'Par' and escolha == 'par':
                        self.placar1 += 1
                        self.lb2['text'] = f'    JOGADOR         {self.placar1}    X    {self.placar2}     COMPUTADOR'

                    elif par_impar == 'Par' and escolha == 'impar':
                        self.placar2 += 1
                        self.lb2['text'] = f'    JOGADOR         {self.placar1}    X    {self.placar2}     COMPUTADOR'

                    elif par_impar == 'Ímpar' and escolha == 'impar':
                        self.placar1 += 1
                        self.lb2['text'] = f'    JOGADOR         {self.placar1}    X    {self.placar2}     COMPUTADOR'

                    elif par_impar == 'Ímpar' and escolha == 'par':
                        self.placar2 += 1
                        self.lb2['text'] = f'    JOGADOR         {self.placar1}    X    {self.placar2}     COMPUTADOR'



                else:
                    self.lb_erro['text'] = 'ERRO! ESCOLHA PAR OU ÍMPAR E DIGITE ENTRE 0 A 10'

            else:
                self.lb_erro['text'] = 'ERRO! ESCOLHA PAR OU ÍMPAR E DIGITE ENTRE 0 A 10'


        except:
            self.lb_erro['text'] = 'ERRO! ESCOLHA PAR OU ÍMPAR E DIGITE ENTRE 0 A 10'


    def resetar(self):
        resposta = mbox.askquestion('RESTART', 'DESEJA REINICIAR?')
        if resposta == 'yes':
            restart_programa()

    def resetar2(self, event):
        resposta = mbox.askquestion('RESTART', 'DESEJA REINICIAR?')
        if resposta == 'yes':
            restart_programa()



raiz.geometry('840x650+300+30')
raiz.iconbitmap('par_ou_ímpar_shinobi/imagens/ninjaa.ico')
raiz.title('Shinobi par ou ímpar')
raiz['bg'] = cinza1


janela = janela(raiz)

raiz.mainloop()