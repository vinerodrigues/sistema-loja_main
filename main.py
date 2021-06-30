from tkinter import* 			#LIBRARY TO GENERATE INTERFACES
import tkinter as tk 			#LIBRARY TO GENERATE INTERFACES
from tkinter import messagebox	# CAIXA DE MENSAGEM
from PIL import Image  			#LIBRARY TO WORK WITH IMAGES 
import users					#MANAGER DB USERS
import main_menu				#NEXT WINDOW OF THE APP

class sistemaDeControleDeLoja(object):
	def __init__(self, loja):
		self.loja = loja 

		self.colocarInconeNaJanelaDoPrograma() 		
		self.gerarFramesDoSistema()	
		self.colocarLogoDoProgramaNaTelaInicial()
		self.gerarMenuInicialParaAutenticacaoDeEntrada()		

	def colocarInconeNaJanelaDoPrograma (self): 
		self.loja.tk.call('wm', 'iconphoto', self.loja._w, tk.PhotoImage(file=("C:/sistema_loja-main/imagens/lou.gif")))

	def gerarFramesDoSistema (self):  # - Organiza as frames do main_menu - 	#
		
		#------ Franes principal ------#		
		self.frameLogoInicial = Frame(self.loja, bg = 'black', pady = 20)	
		self.frameEntradaDeUsuario = Frame(self.loja, bg = 'black', pady = 20) 		# THIS FRAME WILL BE RESPONSIBLE OF THE LOGIN'S LABEL
		self.frameEntradaDeSenha = Frame(self.loja, bg='black', pady = 20)		# THIS FRAME WILL BE RESPONSIBLE OF THE PASSWORD'S BOX
		self.frameBotaoDeConfirmacao = Frame(self.loja, bg = 'black')				# THIS FRAME WILL BE RESPONSIBLE OF THE ENTERBUTTON'S BOX
		#------------------------------#

		#------ PACKING AND SORT INIT FRAMES ------#
		self.frameLogoInicial.pack()
		self.frameEntradaDeUsuario.pack()
		self.frameEntradaDeSenha.pack()
		self.frameBotaoDeConfirmacao.pack()
		#------------------------------------------#

	def colocarLogoDoProgramaNaTelaInicial (self): # - Cria a logo estampada no inicio - 	#
		
		imagemDaLogo = PhotoImage (file = ("C:/sistema_loja-main/imagens/lou.gif"))
		self.labelLogoDoSistema = Label (self.frameLogoInicial, bg = 'black')
		self.labelLogoDoSistema['image'] = imagemDaLogo
		self.labelLogoDoSistema.image = imagemDaLogo
		self.labelLogoDoSistema.pack ()

	def gerarMenuInicialParaAutenticacaoDeEntrada (self): 

		self.textoIndicativoParaNomeDoUsuario = Label (self.frameEntradaDeUsuario, text = "Usuario", bg = 'black' , fg = 'white', font = ('Franklin Gothic Medium', 15))
		self.textoIndicativoParaNomeDoUsuario.pack ()
		
		self.caixaDeEntradaParaNomeDoUsuario = Entry (self.frameEntradaDeUsuario, bg = 'black', fg = 'white')
		self.caixaDeEntradaParaNomeDoUsuario.pack ()

		self.textoInidicativoParaEntradaDesenha = Label (self.frameEntradaDeSenha, text = "Senha", bg = 'black' , fg = 'white', font = ('Franklin Gothic Medium', 15))
		self.textoInidicativoParaEntradaDesenha.pack ()
		self.caixaParaEntradaDeSenha = Entry (self.frameEntradaDeSenha, show = '*', bg = 'black', fg = 'white')
		self.caixaParaEntradaDeSenha.bind ("<Return>", self.validarDadosInseridos)
		self.caixaParaEntradaDeSenha.pack ()

		self.botaoDeConfirmacaodeEntrada = Button (self.frameBotaoDeConfirmacao, text = "Entrar", bg = 'black', fg = 'white', bd = 1, activebackground = "#353839", activeforeground = 'white', command = self.validarDadosInseridos )
		self.botaoDeConfirmacaodeEntrada.bind ("<Return>", self.validarDadosInseridos)
		self.botaoDeConfirmacaodeEntrada.pack ()	

	def validarDadosInseridos(self, event = None): # - FUNCTION REPOSIBLE OF THE GET USERS AND PASSWORD AND TESTING - #

		nomeDoUsuario = self.caixaDeEntradaParaNomeDoUsuario.get()
		senhaDoUsuario = self.caixaParaEntradaDeSenha.get() 
		chaveDeValidacaoDeEntrada = users.validarEntrada(nomeDoUsuario, senhaDoUsuario) 

		if chaveDeValidacaoDeEntrada == 1:
			self.entrarNoSistema(nomeDoUsuario)
		
		elif chaveDeValidacaoDeEntrada == 2:
			messagebox.showwarning("Entrada invalida", "A senha está incorreta")

		else:
			messagebox.showerror("Entrada invalida", "Usuario não existe")

	def entrarNoSistema (self, nomeDoUsuario):
		self.frameLogoInicial.destroy()		
		self.frameEntradaDeUsuario.destroy()	
		self.frameEntradaDeSenha.destroy()		
		self.frameBotaoDeConfirmacao.destroy()
		main_menu.menuPrincipal(self.loja, nomeDoUsuario)

loja = tk.Tk()	
sistemaDeControleDeLoja(loja)	
loja.title ("Lourenço art tattoo") 
loja.geometry (f'{loja.winfo_screenwidth()}x{loja.winfo_screenheight()-60}+{-7}+{0}')
loja ['bg'] = 'black' 
loja.mainloop ()

