import customtkinter
import tkinter as tk
from tkinter import ttk, font
from tkinter import messagebox
from tkinter import *

class Tela_Principal():
    def __init__(self, windows):
        self.janela = windows
        self.janela.title('SNAC - Login')
        self.janela.geometry('1000x600+750+150')
        self.janela.resizable(width=False, height=False)
        self.logo = PhotoImage(file ='imagens/Fundo_PrimeiraTela.png')
        self.seta_branca2 = PhotoImage(file='imagens/Seta2_Branca.png')
        self.logo_imagem = Label(self.janela, image= self.logo, borderwidth= 0)
        self.logo_imagem.place(x=400, y=0)


# ---------------------- Tela de Login --------------------

        #---------- Frame -------

        self.frame = customtkinter.CTkFrame(self.janela, fg_color='white', corner_radius=0, width=400, height=600)
        self.frame.place(x=0, y=0)

        # labels

        self.label_login = customtkinter.CTkLabel(self.frame,
                                                 text='Insira sua conta',
                                                 font=('Arial', 26, 'bold'), text_color='black', fg_color='white')
        self.label_login.place(x=70, y=150)

        self.label_cadastre_se = customtkinter.CTkLabel(self.frame,
                                                        text='Não tem uma conta?', font=('Arial', 12),
                                                        text_color='gray')
        self.label_cadastre_se.place(x=85, y=470)

        # caixas

        self.caixa_usuario = customtkinter.CTkEntry(self.frame,
                                                 placeholder_text='E-mail ou usuário',
                                                 width=250, height=50, border_width=0, corner_radius=12, bg_color='white', text_color='black')
        self.caixa_usuario.place(x=70, y=220)

        self.caixa_senha = customtkinter.CTkEntry(self.frame,
                                                placeholder_text='Senha',
                                                width=250, height=50, border_width=0, corner_radius=12, bg_color='white', text_color='black')
        self.caixa_senha.place(x=70, y=300)

        # Checkbox de manter login

        def funcao_chechkbok():
            if self.caixa_selecao.get() == 'on':
                mensagem['text'] = f' O checkbox foi ativado: {self.caixa_selecao.get()}'
            else:
                mensagem['text'] = f'O checkbox foi desativado: {self.caixa_selecao.get()}'

        self.conf = customtkinter.StringVar(value='off')
        self.caixa_selecao = customtkinter.CTkCheckBox(self.frame, variable=self.conf, onvalue='on', offvalue='off',
                                                  text='Manter login', font=('Arial', 15),
                                                  command=funcao_chechkbok, checkbox_width=20, checkbox_height=20, border_width=2,
                                                  checkmark_color='#315a2e', fg_color='lightgray', bg_color='white', corner_radius=5,
                                                  hover=True, hover_color='lightgray', border_color='lightgray')
        self.caixa_selecao.place(x=75, y=370)
        mensagem = Label(self.frame, fg='white', bg='white', font=('Arial', 15, 'bold'))
        mensagem.place(x=0, y=0)

        # botões

        self.botao_cadastrar = customtkinter.CTkButton(self.janela,
                                                       text='',
                                                       text_color='black', fg_color='#316dbc', hover_color='#7ccaf4',
                                                       border_color='black', bg_color='white',
                                                       font=('Arial', 15), command=self.janela_lobby, width=50, height=50,
                                                       image=self.seta_branca2, anchor='center')
        self.botao_cadastrar.place(x=170, y=410)

        self.funcao_cadastrar = customtkinter.CTkButton(self.frame,
                                                        text='Cadastre-se', font=('Arial', 12), text_color='gray', bg_color='transparent',
                                                        fg_color='transparent', hover_color='white', width=25, height=15, command=self.janela_cadastro)
        self.funcao_cadastrar.place(x=200, y=473)
        self.funcao_cadastrar.bind('<Enter>', self.trocar_cor)
        self.funcao_cadastrar.bind('<Leave>', self.trocar_cor2)
        self.funcao_cadastrar.bind('<Button-1>')



# ---------------------------Métodos-----------------------------


    def trocar_cor(self, event):
        self.funcao_cadastrar.configure(text_color='#316dbc')

    def trocar_cor2(self, event):
        self.funcao_cadastrar.configure(text_color='gray')

    def voltar1(self):
        self.janela2.withdraw()
        self.janela.deiconify()

    def voltar2(self):
        self.janela4.withdraw()
        self.janela3.deiconify()


#-------------Tela Cadastro / Janela Auxiliar--------------

    def janela_cadastro(self):
        self.janela.withdraw()
        self.janela2 = customtkinter.CTkToplevel()
        self.janela2.title('SNAC - Cadastro')
        self.janela2.geometry('1000x600+750+150')
        self.janela2.resizable(width=False, height=False)
        self.seta_voltar = PhotoImage(file='imagens/Seta_voltar.png')
        self.logo_imagem2 = Label(self.janela2, image=self.logo, borderwidth=0)
        self.logo_imagem2.place(x=400, y=0)

        # ---------------------- Cadastro/Segunda Tela --------------------

        self.frame2 = customtkinter.CTkFrame(self.janela2, fg_color='white', corner_radius=0, width=400, height=600)
        self.frame2.place(x=0, y=0)

        # -----------Labels---------------

        self.label_cadastrar = customtkinter.CTkLabel(self.frame2,
                                                      text='Cadastre-se',
                                                      font=('Arial', 26, 'bold'), text_color='black', fg_color='white')
        self.label_cadastrar.place(x=70, y=50)

        self.label_nome = customtkinter.CTkLabel(self.frame2,
                                                 text='Nome de usuário',
                                                 font=('Arial', 17, 'bold'), text_color='black', fg_color='white')
        self.label_nome.place(x=70, y=105)

        self.label_email = customtkinter.CTkLabel(self.frame2,
                                                  text='E-mail',
                                                  font=('Arial', 17, 'bold'), text_color='black', fg_color='white')
        self.label_email.place(x=70, y=200)

        self.label_senha = customtkinter.CTkLabel(self.frame2,
                                                  text='Senha',
                                                  font=('Arial', 17, 'bold'), text_color='black', fg_color='white')
        self.label_senha.place(x=68, y=295)

        self.label_confirmar_senha = customtkinter.CTkLabel(self.frame2,
                                                            text='Confirmar senha',
                                                            font=('Arial', 17, 'bold'), text_color='black',
                                                            fg_color='white')
        self.label_confirmar_senha.place(x=65, y=390)

        # -------------caixas-----------

        self.caixa_nome = customtkinter.CTkEntry(self.frame2,
                                                 placeholder_text='Nome de usuário',
                                                 width=250, height=50, border_width=0, corner_radius=12,
                                                 bg_color='white', text_color='black')
        self.caixa_nome.place(x=65, y=140)

        self.caixa_email = customtkinter.CTkEntry(self.frame2,
                                                  placeholder_text='E-mail',
                                                  width=250, height=50, border_width=0, corner_radius=12,
                                                  bg_color='white', text_color='black')
        self.caixa_email.place(x=65, y=235)

        self.caixa_senha = customtkinter.CTkEntry(self.frame2,
                                                  placeholder_text='Senha',
                                                  width=250, height=50, border_width=0, corner_radius=12,
                                                  bg_color='white', text_color='black')
        self.caixa_senha.place(x=65, y=330)

        self.caixa_confirmar_senha = customtkinter.CTkEntry(self.frame2,
                                                            placeholder_text='Senha',
                                                            width=250, height=50, border_width=0, corner_radius=12,
                                                            bg_color='white', text_color='black')
        self.caixa_confirmar_senha.place(x=65, y=425)

        # ------------Botôes------------

        self.botao_cadastrar = customtkinter.CTkButton(self.frame2,
                                                       text='Cadastrar',
                                                       text_color='white', fg_color='#316dbc', hover_color='#7ccaf4',
                                                       border_color='black', bg_color='white', corner_radius=5,
                                                       font=('Arial', 15, 'bold'), width=55, height=30)
        self.botao_cadastrar.place(x=140, y=500)

        self.botao_voltar = customtkinter.CTkButton(self.frame2,
                                                    text='',
                                                    text_color='black', fg_color='#316dbc', hover_color='#7ccaf4',
                                                    border_color='black', bg_color='white', command=self.voltar1,
                                                    font=('Arial', 15), width=50, height=50,
                                                    image=self.seta_voltar, anchor='center')
        self.botao_voltar.place(x=5, y=5)


#------------Tela de Lobby / Segunda tela------------

    def janela_lobby(self):
        self.janela.withdraw()
        self.janela3 = customtkinter.CTkToplevel()
        self.janela3.title('SNAC - Lobby')
        self.janela3.geometry('1000x600+750+150')
        self.janela['bg'] = '#242424'
        self.janela3.resizable(width=False, height=False)

        self.imagem1 = PhotoImage(file='imagens/teams.png')
        self.imagem2 = PhotoImage(file='imagens/py2.png')
        self.tela1 = PhotoImage(file='imagens/anuncio1.png')
        self.tela2 = PhotoImage(file='imagens/anuncio2.png')
        self.tela3 = PhotoImage(file='imagens/anuncio3.png')

        self.fundo = Label(self.janela3, image=self.imagem2, width=1000, height=600)
        self.fundo.place(x=-2, y=53)

        # Botões inferiores
        self.frame_1 = customtkinter.CTkButton(self.janela3, width=160, height=130, corner_radius= 20, bg_color='#126F94', image= self.tela1, text='', fg_color='#126F94')
        self.frame_1.place(x= 15, y=450)

        self.frame_2 = customtkinter.CTkButton(self.janela3, width=160, height=130, corner_radius= 20, bg_color= '#126F94', text= '', image=self.tela2,fg_color='#126F94' )
        self.frame_2.place(x=400, y=450)

        self.frame_3 = customtkinter.CTkButton(self.janela3, width=160, height=130, corner_radius= 20, bg_color='#126F94', text='', fg_color='#126F94', image=self.tela3)
        self.frame_3.place(x=780, y=450)

        # frame principal black
        self.frame_4 = customtkinter.CTkFrame(self.janela3, width=1000, height=110, fg_color='#3B3538', corner_radius=0)
        self.frame_4.place(x=0, y=0)

        self.jogar = customtkinter.CTkButton(self.frame_4, text='Jogar', text_color='white', font=('Bold', 25),
                                             corner_radius=18, width=150, command=self.janela_jogar,
                                             height=40, bg_color='#3B3538', fg_color='#7CCAF4', hover_color='#F2CB05')
        self.jogar.place(x=105, y=40)


        self.bot3 = customtkinter.CTkButton(self.frame_4, text='Loja', text_color='white', font=('Bold', 19),
                                            corner_radius=18, width=150,
                                            height=40, bg_color='#3B3538', fg_color='#7CCAF4', hover_color='#F2CB05')
        self.bot3.place(x=455, y=40)

        self.bot4 = customtkinter.CTkButton(self.frame_4, text='Perfil', text_color='white', font=('Bold', 19),
                                            corner_radius=18, width=150,
                                            height=40, bg_color='#3B3538', fg_color='#7CCAF4', hover_color='#F2CB05')
        self.bot4.place(x=625, y=40)

        self.bot5 = customtkinter.CTkButton(self.frame_4, text='', width=40,
                                            height=40, bg_color='#3B3538', fg_color='#3B3538',
                                            hover_color='#F2CB05', image=self.imagem1, anchor='center',
                                            compound='left')
        self.bot5.place(x=890, y=40)

        self.combobox = customtkinter.CTkOptionMenu(self.janela3, values=['PYTHON', 'JAVA', 'PORTUGOL'],
                                                    corner_radius=18, fg_color='#7CCAF4',
                                                    bg_color='#3B3538', text_color='white', width=150, height=40,
                                                    font=('Bold', 17))
        self.combobox.set('Modos')
        self.combobox.place(x=280, y=40)

#---------Tela para Jogar / Terceira tela---------

    def janela_jogar(self):
        self.janela3.withdraw()
        self.janela4 = Toplevel()
        self.janela4.title('SNAC - Jogar')
        self.janela4['bg']= '#306D92'
        self.janela4.geometry('1500x800+550+150')
        self.janela4.resizable(width=False, height=False)

        # Imagens
        self.img2 = PhotoImage(file='imagens/Engrenagem.png')
        self.img3 = PhotoImage(file='imagens/thumb1.png')
        self.img4 = PhotoImage(file='imagens/thumb2.png')
        self.img5 = PhotoImage(file='imagens/thumb3.png')
        self.img6 = PhotoImage(file='imagens/thumb4.png')
        self.img7 = PhotoImage(file='imagens/thumb5.png')
        self.img8 = PhotoImage(file='imagens/thumb6.png')
        self.img9 = PhotoImage(file='imagens/thumb7.png')
        self.img10 = PhotoImage(file='imagens/thumb8.png')

        self.frame3 = customtkinter.CTkFrame(self.janela4, fg_color='#3B3538', corner_radius=0, width=2000, height=150)
        self.frame3.place(x=0, y=0)

        # -----------------------------BOTÕES-------------------------------------------

        self.bot_voltar = customtkinter.CTkButton(self.janela4,
                                                       text='VOLTAR',
                                                       text_color='white', fg_color='#7CCAF4', bg_color='#3B3538',
                                                       hover_color='#F2CB05', command=self.voltar2,
                                                       font=('Arial', 20, 'bold'),
                                                       width=200, height=50, corner_radius=18)
        self.bot_voltar.place(x=65, y=55)

        self.bot_loja = customtkinter.CTkButton(self.janela4,
                                                        text='Loja',
                                                        text_color='white', fg_color='#7CCAF4', bg_color='#3B3538',
                                                        hover_color='#F2CB05',
                                                        font=('Arial', 20, 'bold'),
                                                        width=150,
                                                        height=40, corner_radius=18)
        self.bot_loja.place(x=320, y=60)

        self.bot_perfil = customtkinter.CTkButton(self.janela4,
                                                        text='Perfil',
                                                        text_color='white', fg_color='#7CCAF4', bg_color='#3B3538',
                                                        hover_color='#F2CB05',
                                                        font=('Arial', 20, 'bold'),
                                                        width=150,
                                                        height=40, corner_radius=18)
        self.bot_perfil.place(x=520, y=60)

        self.botao_config = customtkinter.CTkButton(self.janela4, text='', image=self.img2, compound='left', width=10,
                                                    height=10, anchor='center', fg_color='#3B3538', bg_color='#3B3538',
                                                    hover_color='#F2CB05')
        self.botao_config.place(x=1400, y=60)

        self.imagem_1 = customtkinter.CTkButton(self.janela4, text='', image=self.img3, compound='left', width=10,
                                               height=10, anchor='center', fg_color='#306D92', bg_color='#3B3538',
                                               hover_color='#306D92', corner_radius=100)
        self.imagem_1.place(x=55, y=190)

        self.imagem_2 = customtkinter.CTkButton(self.janela4, text='', image=self.img4, compound='left', width=10,
                                               height=10, anchor='center', fg_color='#306D92', bg_color='#3B3538',
                                               hover_color='#306D92', corner_radius=100)
        self.imagem_2.place(x=60, y=500)

        self.imagem_3 = customtkinter.CTkButton(self.janela4, text='', image=self.img5, compound='left', width=10,
                                               height=10, anchor='center', fg_color='#306D92', bg_color='#3B3538',
                                               hover_color='#306D92', corner_radius=100)
        self.imagem_3.place(x=450, y=500)

        self.imagem_4 = customtkinter.CTkButton(self.janela4, text='', image=self.img6, compound='left', width=10,
                                               height=10, anchor='center', fg_color='#306D92', bg_color='#3B3538',
                                               hover_color='#306D92', corner_radius=100)
        self.imagem_4.place(x=1200, y=500)

        self.imagem_5 = customtkinter.CTkButton(self.janela4, text='', image=self.img7, compound='left', width=10,
                                               height=10, anchor='center', fg_color='#306D92', bg_color='#3B3538',
                                               hover_color='#306D92', corner_radius=100)
        self.imagem_5.place(x=450, y=190)

        self.imagem_6 = customtkinter.CTkButton(self.janela4, text='', image=self.img8, compound='left', width=10,
                                               height=10, anchor='center', fg_color='#306D92', bg_color='#3B3538',
                                               hover_color='#306D92', corner_radius=100)
        self.imagem_6.place(x=850, y=190)

        self.imagem_7 = customtkinter.CTkButton(self.janela4, text='', image=self.img9, compound='left', width=10,
                                               height=10, anchor='center', fg_color='#306D92', bg_color='#3B3538',
                                               hover_color='#306D92', corner_radius=100)
        self.imagem_7.place(x=850, y=500)

        self.imagem_8 = customtkinter.CTkButton(self.janela4, text='', image=self.img10, compound='left', width=10,
                                               height=10, anchor='center', fg_color='#306D92', bg_color='#3B3538',
                                               hover_color='#306D92', corner_radius=100)
        self.imagem_8.place(x=1200, y=190)

        self.bot_thumb1 = customtkinter.CTkButton(self.janela4,
                                                        text='Variavel',
                                                        text_color='white', fg_color='black', bg_color='#306D92',
                                                        hover_color='#F2CB05',
                                                        font=('Arial', 20, 'bold'),
                                                        width=150,
                                                        height=45, corner_radius=18)
        self.bot_thumb1.place(x=100, y=400)

        self.bot_thumb2 = customtkinter.CTkButton(self.janela4,
                                                        text='Função',
                                                        text_color='white', fg_color='black', bg_color='#306D92',
                                                        hover_color='#F2CB05',
                                                        font=('Arial', 20, 'bold'),
                                                        width=150,
                                                        height=45, corner_radius=50)
        self.bot_thumb2.place(x=490, y=400)

        self.bot_thumb3 = customtkinter.CTkButton(self.janela4,
                                                        text='Lista',
                                                        text_color='white', fg_color='black', bg_color='#306D92',
                                                        hover_color='#F2CB05',
                                                        font=('Arial', 20, 'bold'),
                                                        width=150,
                                                        height=45, corner_radius=50)
        self.bot_thumb3.place(x=890, y=400)

        self.bot_thumb4 = customtkinter.CTkButton(self.janela4,
                                                         text='Tkinter',
                                                         text_color='white', fg_color='black', bg_color='#306D92',
                                                         hover_color='#F2CB05',
                                                         font=('Arial', 20, 'bold'),
                                                         width=150,
                                                         height=45, corner_radius=50)
        self.bot_thumb4.place(x=1250, y=400)

        self.bot_thumb5 = customtkinter.CTkButton(self.janela4,
                                                         text='Dash',
                                                         text_color='white', fg_color='black', bg_color='#306D92',
                                                         hover_color='#F2CB05',
                                                         font=('Arial', 20, 'bold'),
                                                         width=150,
                                                         height=45, corner_radius=50)
        self.bot_thumb5.place(x=1250, y=700)

        self.bot_thumb6 = customtkinter.CTkButton(self.janela4,
                                                         text='ReportLab',
                                                         text_color='white', fg_color='black', bg_color='#306D92',
                                                         hover_color='#F2CB05',
                                                         font=('Arial', 20, 'bold'),
                                                         width=150,
                                                         height=45, corner_radius=50)
        self.bot_thumb6.place(x=890, y=700)

        self.bot_thumb7 = customtkinter.CTkButton(self.janela4,
                                                         text='Calculadora',
                                                         text_color='white', fg_color='black', bg_color='#306D92',
                                                         hover_color='#F2CB05',
                                                         font=('Arial', 20, 'bold'),
                                                         width=150,
                                                         height=45, corner_radius=50)
        self.bot_thumb7.place(x=490, y=700)

        self.bot_thumb8 = customtkinter.CTkButton(self.janela4,
                                                         text='Dados',
                                                         text_color='white', fg_color='black', bg_color='#306D92',
                                                         hover_color='#F2CB05',
                                                         font=('Arial', 20, 'bold'),
                                                         width=150,
                                                         height=45, corner_radius=50)
        self.bot_thumb8.place(x=100, y=700)


# ----------------------- Chamando a classe ModeloSistema -----------------
windows = Tk()
objeto = Tela_Principal(windows)
windows.mainloop()