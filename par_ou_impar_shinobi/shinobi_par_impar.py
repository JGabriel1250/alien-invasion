from tkinter import *
from consatantes import *
from calculo_par_impar import *
import random
import tkinter.messagebox as mbox

raiz = Tk()

class janela():
    def __init__(self, raiz):
        self.placar1 = 0
        self.placar2 = 0
        
        # FRAMES
        self.fr1 = Frame(raiz, bg=cinza1); self.fr1.pack()
        self.fr_result = Frame(raiz, bg=cinza1); self.fr_result.pack()
        self.fr2 = Frame(raiz, bg=cinza1); self.fr2.pack()
        self.fr3 = Frame(raiz, bg=cinza1); self.fr3.pack()
        self.fr4 = Frame(raiz, bg=cinza1); self.fr4.pack()
        self.fr5 = Frame(raiz, bg=cinza1); self.fr5.pack()
        self.fr6 = Frame(raiz, bg=cinza1); self.fr6.pack()
        
        # IMAGENS
        self.img_player = PhotoImage(file='par_ou_ímpar_shinobi/imagens/ninja.png')
        self.img_pc = PhotoImage(file='par_ou_ímpar_shinobi/imagens/robo.png')
        
        self.img_nums = [
            PhotoImage(file=f'par_ou_ímpar_shinobi/imagens/numero_{n}.png')
            for n in range(11)
        ]

        # TITULO
        Label(self.fr1, text='BATALHA SHINOBI', bg=cinza1, font=fonte1, fg=azul2, padx=35).pack(side=LEFT)

        # BOTÃO DE RESTART
        Button(self.fr1, text='Restart', font=fonte4, command=self.resetar, ).pack(side=LEFT)

        #RESULTADO
        self.lb_result = Label(self.fr_result, text='', bg=cinza1, font=fonte1, fg='green')
        self.lb_result.pack()

        #PLACAR
        self.lb2 = Label(self.fr2, text=self.get_placar(), bg=cinza1, font=fonte2, fg=azul2, pady=10)
        self.lb2.pack()

        # IMAGENS DOS JOGADORES
        self.lb_img1 = Label(self.fr3, image=self.img_player, bg=cinza1); self.lb_img1.pack(side=LEFT, padx=25)
        self.lb_img2 = Label(self.fr3, image=self.img_pc, bg=cinza1); self.lb_img2.pack(side=LEFT, padx=25)

        # ESCOLHA PAR OU ÍMPAR
        self.escolha = StringVar()
        Radiobutton(self.fr4, text='Par', value='par', variable=self.escolha, bg=cinza1, font=fonte2, fg=azul2).pack(side=LEFT, pady=20)
        Radiobutton(self.fr4, text='Ímpar', value='impar', variable=self.escolha, bg=cinza1, font=fonte2, fg=azul2).pack(side=LEFT, pady=20)

        # ENTRADA DE NÚMERO
        Label(self.fr5, text='Número de 0 a 10', bg=cinza1, font=fonte3, fg=azul2).pack(side=LEFT)
        self.num = Entry(self.fr5, width=3, font=fonte3); self.num.pack(side=LEFT)

        # BOTÃO DE JOGAR
        self.bt_jogar = Button(self.fr6, text='Jogar', bg=cinza2, font=fonte1, relief=RAISED, border=8, command=self.jogar)
        self.bt_jogar.pack(pady=15)

        # --- binds do Enter ---
        # Enter quando estiver dentro da Entry
        self.num.bind('<Return>', lambda event: self.jogar())
        # Enter global na janela (funciona mesmo sem foco na Entry
        raiz.bind('<Return>', lambda event: self.jogar())
        self.lb_erro = Label(self.fr6, text='', bg=cinza1, font=fonte4, fg=vermelho); self.lb_erro.pack()


    # ATUALIZA O TEXTO DO PLACAR
    def get_placar(self):
        return f'   JOGADOR        {self.placar1}    X    {self.placar2}     COMPUTADOR'

    # FUNÇÃO PRINCIPAL DO JOGO
    def jogar(self):
        try:
            num = int(self.num.get())
            escolha = self.escolha.get()
            num_robo = random.randrange(0, 11)

            if escolha in ("par", "impar") and 0 <= num <= 10:
                self.lb_img1['image'] = self.img_nums[num]
                self.lb_img2['image'] = self.img_nums[num_robo]
                self.lb_erro['text'] = ''

                resultado = calcular_par_impar(num, num_robo)
                self.lb_erro['text'] = f'DEU {resultado.upper()}'
                if resultado.lower() == escolha.strip().lower():
                    self.placar1 += 1
                else:
                    self.placar2 += 1

                self.lb2['text'] = self.get_placar()

            else:
                self.lb_erro['text'] = 'ERRO! Escolha Par/Ímpar e número entre 0 a 10'

        except:
            self.lb_erro['text'] = 'ERRO! Digite um número válido'


    # RESET JOGO
    def resetar(self):
        if mbox.askquestion('RESTART', 'Deseja reiniciar?') == 'yes':
            self.lb_result['text'] = ''
            self.lb_img1['image'] = self.img_player
            self.lb_img2['image'] = self.img_pc
            self.placar1 = 0
            self.placar2 = 0
            self.lb2['text'] = self.get_placar()
            self.lb_erro['text'] = ''



raiz.geometry('840x650+300+30')
raiz.iconbitmap('par_ou_ímpar_shinobi/imagens/ninjaa.ico')
raiz.title('Shinobi par ou ímpar')
raiz['bg'] = cinza1


janela(raiz)
raiz.mainloop()