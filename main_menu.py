from tkinter import* 			#LIBRARY RESPONSIBLE TO INTERFACES
import tkinter as tk 			#LIBRARY RESPONSIBLE TO INTERFACES
from PIL import Image 			#LIBRARY RESPONSIBLE TO WORK WITH IMAGES
from datetime import datetime	#LIBRARY RESPONSIBLE TO WORK WITH TIMES AND DATES
import time 					#LIBRARY RESPONSIBLE TO CALL TIME OF THE SYSTEM
import users    				#MANAGER DB USERS
import cliente 					#WINDOW CLIENT - INTERFACE ABOUT CONTROL OF CLIENT
import estoque 					#WINDOW STOCK  - INTERFACE ABOUT CONTROL OF STOCK
import finanças 				#WINDOW FINANCES - INTERFACE ABOUT CONTROL OF FINANCES
import agenda 					#WINDOW SCHEDULE - INTERFACE ABOUT CONTROL OF SCHEDULE
import dbclientes               #MANAGER DB CLIENTS
import databaseproduto          #MANAGER DB PROTUCTS
from functools import partial
import cv2
import os.path
import os
import webbrowser

class menuPrincipal(object):
	def __init__(self, i, usuario):

		#------ ATRIBUIÇÕES ------#
		self.i = i 				# instanciando
		self.usuario = usuario
		#-------------------------# 
		
		#------- CHAMANDO METODOS ------#
		self.gerenciarFramesDoMenuPrincipal()
		self.configurarCabecalho()					
		self.adicionarOuRemoverUsuarios()					
		self.botoesDoMenuPrincipal()				
		self.converterImagens()
		self.gerarFeedDeMateriaisPendentes() # Função responsavel pelo feed do material
		self.formatarDataHora()						# Função responsavel pela data e a hora do programa
		self.carregarFeedDaAgenda()			# Carrega o feed e a agenda. //Chama self.detalhar_dia (Chama self.carregar_calendario).
		#----------------------------------------------------------------------------------------------# 
	#-------- MÉTODOS --------#

	def gerenciarFramesDoMenuPrincipal(self):

		def gerarFramesDoMenuPrincipal(): # - Organiza as frames do main_menu - #

			self.principal = Frame (self.i, bg = 'black')					   	#Frame main, mãe de todas as frames

			#------ FRAMES PRINCIPAL ------#
			self.cabecalho = Frame (self.principal, bg = 'black')				#Frame header, onde ficam os itens do cabeçalho
			self.metadeDireitaDoPrincipal = Frame (self.principal , bg = 'black')			#Frame right_main, o lado direito do programa
			self.metadeEsquerdaDoPrincipal = Frame (self.principal, bg = 'black')				#Frame left_main, o lado esquerdo do programa
			self.rodape = Frame (self.principal, bg = 'black')				#Frame footer, o rodapé 

		    #------ SUB FRAMES ------#
			self.dataHoraDoCabecalho = Frame(self.cabecalho, bg = 'black')			#Frame hour_date; filha de header, onde ficam data e hora empacotado.
			self.menu = Frame (self.metadeEsquerdaDoPrincipal, bg = 'black')				#Frame menu, filha de left_main, onde ficam os menus			
			self.feed = Frame (self.metadeDireitaDoPrincipal, bg = 'black')			#Frame feed,  filha de right_main, onde ficam os feeds e resultados do programa.
			
			#------ EMPACOTAMENTO ----------#
			self.principal.place (x = 10, y =10 , width = 1340, height = 1090)
			self.cabecalho.place (x = 0, y = 0 , width = 1340, height = 100)
			self.metadeDireitaDoPrincipal.place (x = 850, y = 100 , width = 490 , height = 500)
			self.metadeEsquerdaDoPrincipal.place (x = 0, y = 100 , width = 850, height = 500)
			self.dataHoraDoCabecalho.place (x = 0, y = 0 , width = 1340, height = 100)
			self.menu.place (x =0, y = 0 , width = 850, height = 500)
			self.feed.place (x =0, y = 0 , width = 490, height = 500)
			self.rodape.place (x = 0, y = 600 , width = 1340, height = 110)
		
		def gerarFramesDoFeed():
			
			self.titulo_feed = Frame (self.feed, bg = 'black')
			self.titulo_feed.pack()
			self.primeiroDoFeed = Frame (self.feed, bg = 'black')
			self.primeiroDoFeed.pack (pady = 5)
			self.segundoDoFeed = Frame (self.feed, bg = 'black')
			self.segundoDoFeed.pack (pady = 5)
			self.terceiroDoFeed = Frame (self.feed, bg = 'black')
			self.terceiroDoFeed.pack (pady = 5)
			self.quartoDoFeed = Frame (self.feed, bg = 'black')
			self.quartoDoFeed.pack (pady = 5)

		gerarFramesDoMenuPrincipal()
		gerarFramesDoFeed()
	
	def configurarCabecalho(self):  # - Organiza o cabeçalho - #

		self.usuarioAtivo = Label(self.dataHoraDoCabecalho, text = '@' + self.usuario , bg = 'black', fg = 'white', pady = 15, font = ('Franklin Gothic Medium', 15))
		self.usuarioAtivo.grid(row = 0, column = 2 )
		self.datahora = Label(self.dataHoraDoCabecalho,  bg = 'black', fg = 'white', pady = 15, font=('Arial', 15) )
		self.datahora.grid(row = 0, column = 3)

	def adicionarOuRemoverUsuarios(self): # - Botão responsável por chamar a função que cria um menu para add e remover usuarios - #
		
		def mostrarBotaoParaAdicionarOuRemoverNovoUsuario():
			self.imagemDaLogo = PhotoImage(file=("C:/sistema_loja-main/imagens/lou.gif"))			
			self.imagemDaLogo = self.imagemDaLogo.zoom(7)													
			self.imagemDaLogo = self.imagemDaLogo.subsample(30)												
			self.adicionarOuRemover = Button(self.dataHoraDoCabecalho, bg = 'black', command = gerenciarUsuarios, border ="0")	#
			self.adicionarOuRemover['image'] = self.imagemDaLogo											
			self.adicionarOuRemover.image = self.imagemDaLogo												
			self.adicionarOuRemover.grid(row = 0 , column = 0, padx = 10)

		def gerenciarUsuarios():
			
			def gerenciarLayoutParaPreenchimentoDeUsuarioESenha():
				self.frameDoGerenciadorDeUsuarios = Frame(self.dataHoraDoCabecalho, bg = 'black')
				self.frameDoGerenciadorDeUsuarios.grid(row = 0, column = 1, padx =10)
		
				self.textoIndicativoParaNomeDoUsuario = Label(self.frameDoGerenciadorDeUsuarios, text = "Usuario", bg = 'black', fg = 'white')
				self.textoIndicativoParaNomeDoUsuario.grid(row = 0, column = 0  )
				self.caixaDeEntradaParaNomeDoUsuario = Entry(self.frameDoGerenciadorDeUsuarios, bg ='black', fg = 'white')
				self.caixaDeEntradaParaNomeDoUsuario.grid(row = 0, column = 1  )

				self.textoInidicativoParaEntradaDesenha = Label(self.frameDoGerenciadorDeUsuarios, text = "Senha", bg = 'black', fg = 'white')
				self.textoInidicativoParaEntradaDesenha.grid(row = 1, column = 0  )
				self.caixaParaEntradaDeSenha = Entry(self.frameDoGerenciadorDeUsuarios, show = '*', bg = 'black', fg = 'white')
				self.caixaParaEntradaDeSenha.bind ("<Return>", adicionarUsuario)
				self.caixaParaEntradaDeSenha.grid(row = 1, column = 1  )

				self.botaoDeConfirmacaodeEntrada = Button(self.frameDoGerenciadorDeUsuarios, command = adicionarUsuario , text = "Add", bg = 'black', fg = 'white', activebackground = "#353839", activeforeground = 'white')
				self.botaoDeConfirmacaodeEntrada.bind ("<Return>", adicionarUsuario)
				self.botaoDeConfirmacaodeEntrada.grid(row = 2, column = 1, sticky=W, ipadx = 20  )
				
				self.botaoDeRemocaodeDeUsuario = Button(self.frameDoGerenciadorDeUsuarios, command = removerUsuario, text = "Rem", bg = 'black', fg = 'white', activebackground = "#353839", activeforeground = 'white')
				self.botaoDeRemocaodeDeUsuario.grid(row = 2, column = 1, sticky=E, ipadx = 15  )

			def adicionarUsuario(event = None): # - Adicionar usuarios - #
				nomeDoUsuario = self.caixaDeEntradaParaNomeDoUsuario.get()
				senhaDoUsuario = self.caixaParaEntradaDeSenha.get()
				if nomeDoUsuario == '':
					self.frameDoGerenciadorDeUsuarios.grid_forget()
				else:	
					users.adicionarUsuario (nomeDoUsuario, senhaDoUsuario)
					self.frameDoGerenciadorDeUsuarios.grid_forget()
		
			def removerUsuario(): # - Remover usuarios - #
				nomeDoUsuario = self.caixaDeEntradaParaNomeDoUsuario.get()
				senhaDoUsuario = self.caixaParaEntradaDeSenha.get()
			
				if nomeDoUsuario == '':
					self.frameDoGerenciadorDeUsuarios.grid_forget()
				else:	
					users.removerUsuario (nomeDoUsuario, senhaDoUsuario)
					self.frameDoGerenciadorDeUsuarios.grid_forget()

			gerenciarLayoutParaPreenchimentoDeUsuarioESenha()		

		mostrarBotaoParaAdicionarOuRemoverNovoUsuario()
									
	def formatarDataHora(self): # - Formata a data e a hora de acordo com a hora do sistema - #		
		now = datetime.now()

		self.datahora['text'] = f' - {now.strftime("%H:%M:%S")} - {now.strftime("%d/%m/%Y")}' # Formata a data e a hora
		self.hora = now.strftime('%H') 			# Pega a hora individualmente
		self.dia = now.strftime('%d')			# Pega a dia individualmente
		self.mes = now.strftime('%m')			# Pega a mês individualmente
		self.ano = now.strftime('%Y') 			# Pega a ano individualmente
		self.dataDoSistema = now.strftime('%d/%m/%Y')
		self.i.after(1000, self.formatarDataHora) 		#Chama a função novamente depois de 1 segundo

	def converterImagens(self):

		def converterParaPNG(lista_de_arquivo, diretorio):
			for i in lista_de_arquivo:

				if ".jpg" in i:
					imagens = Image.open(diretorio+'/'+i)
					imagens = imagens.resize((225,225))
					nome_sem_ext = os.path.splitext(i)[0]
					imagens.save(os.path.join(diretorio,nome_sem_ext+'.png'))
					imagens.save(os.path.join(diretorio,nome_sem_ext+'.gif'))
					os.remove(diretorio+'/'+i)
		
				if ".jpeg" in i:
					imagens = Image.open(diretorio+'/'+ i)
					imagens = imagens.resize((225,225))
					nome_sem_ext = os.path.splitext(i)[0]
					imagens.save(os.path.join(diretorio,nome_sem_ext+'.png'))
					imagens.save(os.path.join(diretorio,nome_sem_ext+'.gif'))
					os.remove(diretorio+'/'+i)

		diretorio = "C:/sistema_loja-main/imagens_clientes"
		lista_de_arquivo = os.listdir (diretorio)
		converterParaPNG (lista_de_arquivo, diretorio)

	def carregarFeedDaAgenda(self): # - Carrega o feed dos clientes -	#
		
		def carregarTituloDoFeed(): # - Cria as labels para o feed clientes default - #
			self.titulo_feed_label = Label(self.titulo_feed, text = "Próximos clientes", justify = 'center', width = 20 , bg = 'black' , fg = 'white', font = ('Franklin Gothic Medium', 20))
			self.titulo_feed_label.pack()
		
		def verificarProximasDatasDaAgenda(data):
		    
		    def gerenciarDadosDosClientesParaPorFeed(data):
			    #Esse dia posso colocar ele um global dentro desse escopo pois terei que manipulalo em dias que terão menos que 31 dias.
			    dia = int(data[0:2:])
			    mes = int(data[3:5:])
			    ano = int(data[6::])
			    contadorInfinito = 0
			    contadorDeDatasComClientesAgendados = 0    		
			    
			    while ano < 2023:
	        		dataFormatada = formatarDiaMesAno(str(dia), mes, ano)
	        		chaveParaIncrementarNumeroDeFrames = verificarSeTemClienteAgendadoParaProximasDatasDaAgenda(dataFormatada,  contadorDeDatasComClientesAgendados)
	        		dia += 1
	        		
	        		if chaveParaIncrementarNumeroDeFrames == None:
	        			chaveParaIncrementarNumeroDeFrames = 0
	        		elif chaveParaIncrementarNumeroDeFrames > 0:
	        			contadorDeDatasComClientesAgendados += 1

	        		if verificarSeJaAchouOsQuatroProximosClientes(contadorDeDatasComClientesAgendados):
	        			break

	        		if verificarSeEhOUltimoDiaDoMes(dia):
	        			mes += 1
	        			dia = 1
	        		elif verificarSeEhOUltimoMesDoAno(mes):
	        			ano +=1
	        			dia = 0
	        			mes = 1

		    def formatarDiaMesAno(dia, mes, ano):
		    	
		    	if mes < 10:
		    		aux_mes = f'{0}{str(mes)}'
		    	else:
		    		aux_mes = f'{str(mes)}'

		    	if int(dia) > 9:
		    		return f'{str(dia)}/{aux_mes}/{ano}'
		    	else:
		    		return f'{0}{str(dia)}/{aux_mes}/{ano}'

		    def verificarSeJaAchouOsQuatroProximosClientes(contadorDeDatasComClientesAgendados):
		    	return contadorDeDatasComClientesAgendados == 4

		    def verificarSeEhOUltimoDiaDoMes(dia):
		    	return dia == 32

		    def verificarSeEhOUltimoMesDoAno(mes):
		    	return mes == 13

		    def verificarSeEhOAnoLimite(ano):
		    	return ano == 2022

		    gerenciarDadosDosClientesParaPorFeed(data)		    	
        					
		def verificarSeTemClienteAgendadoParaProximasDatasDaAgenda(data, contadorDeDatasComClientesAgendados): # - Quest 1 - Carrega o calendario e determina se há ou não clientes naquele dia - # 

			def coletarDadosDaBaseDosClientesCadastrados(data, contadorDeDatasComClientesAgendados):
				contadorDeClientesAgendados = 0
				CLIENTES_CADASTRADOS = coletarDadosBrutosDaBaseDeDadosDoCliente()  
				
				for cliente in CLIENTES_CADASTRADOS:
					
					dadosDoClienteBruto = fornecerDadosDosClientes(CLIENTES_CADASTRADOS, cliente)
					
					dados = ''
					telefone = ''
					data_de_nascimento=''
					email=''
					endereco = ''
					data_aux=''
					hora_aux=''
					comentarios =''

					for caracterer in dadosDoClienteBruto:
						if caracterer == '¹' and telefone == '':
							if dados == '':
								telefone = ('021')
							else:	
								telefone = dados
							dados = ''
							
						elif caracterer == '¹' and data_de_nascimento == '':
							if dados == '':
								data_de_nascimento = ('00/00/0000')
							else:	
								data_de_nascimento = dados
							dados = ''

						elif caracterer == '¹' and email == '':
							if dados == '':
								email = "Vazio"
							else:	
								email = dados
							dados = ''
							
						elif caracterer == '¹' and endereco == '':
							if dados == '':
								endereco = "Rio de Janeiro - RJ"
							else:	
								endereco = dados
							dados = ''
							
						elif caracterer == '¹' and data_aux == '':
							if dados == '':
								data_aux = ('00/00/0000')
							else:	
								data_aux = dados
							dados = ''

						elif caracterer == '¹' and hora_aux == '':
							if dados == '':
								hora_aux = ('00:00')
							else:	
								hora_aux = dados	
							dados = ''

						elif caracterer == '¹' and comentarios == '':
							if dados == '':
								comentarios = ('Vazio')
							else:	
								comentarios = dados
							dados = ''
						elif caracterer == '²':
							break;
						else:
							dados += caracterer
						
					if verificarSeTemClienteNessaData(data_aux, data):
						contadorDeClientesAgendados = inserirClienteAgendadoNoFeed(cliente.decode(), data_aux, hora_aux, telefone, contadorDeClientesAgendados, contadorDeDatasComClientesAgendados)
				return contadorDeClientesAgendados
			


			def coletarDadosBrutosDaBaseDeDadosDoCliente():
				return dbclientes.clientes

			def fornecerDadosDosClientes(CLIENTES_CADASTRADOS, cliente):
				return CLIENTES_CADASTRADOS[cliente.decode()].decode()
			
			def verificarSeTemClienteNessaData(data_aux, data):
				return data_aux == data
				
			return coletarDadosDaBaseDosClientesCadastrados(data, contadorDeDatasComClientesAgendados)
		
		def inserirClienteAgendadoNoFeed(cliente, dataAgendada, horaAgendada,telefoneDoCliente, contadorDeClientesAgendados, contadorDeDatasComClientesAgendados):

			def gerenciarLayoutDoFeed(cliente, dataAgendada, horaAgendada,telefoneDoCliente, contadorDeClientesAgendados, contadorDeDatasComClientesAgendados):

				def definirOrdemDeDadosInseridos(cliente, dataAgendada, horaAgendada,telefoneDoCliente, contadorDeClientesAgendados, contadorDeDatasComClientesAgendados):			
										
					if contadorDeDatasComClientesAgendados == 0:
						if contadorDeClientesAgendados == 0:
							datarComoTituloAJanelaQueVaiMostrarOsClientes(dataAgendada, self.primeiroDoFeed)
							exibirDadosDoClienteAgendado(cliente, dataAgendada, horaAgendada, telefoneDoCliente, self.primeiroDoFeed, contadorDeClientesAgendados )
							self.vetorParaTestarOFeedMovel = []
							self.vetorParaTestarOFeedMovel.append(cliente)
							self.vetorParaTestarOFeedMovel.append(horaAgendada)
							self.vetorParaTestarOFeedMovel.append(telefoneDoCliente)
							return (contadorDeClientesAgendados + 1)
						
						#Para testar a idéia eu vou contruir um vetor para armazenar os dados
						elif contadorDeClientesAgendados == 1:
							#------- ideia de mudar os dados dos clientes do feed com o tempo.
							#self.cont = 0
							#def testarAfter():
							#	self.cont+= 1
							#	if self.cont % 2 == 0:
							#		exibirDadosDoClienteAgendado(cliente,dataAgendada, horaAgendada,telefoneDoCliente, self.primeiroDoFeed, contadorDeClientesAgendados)
							#	else:
							#		exibirDadosDoClienteAgendado(self.vetorParaTestarOFeedMovel[0], 0 , self.vetorParaTestarOFeedMovel[1], self.vetorParaTestarOFeedMovel[2],0 ,  contadorDeClientesAgendados)
							#	self.i.after(5000, testarAfter)
							#testarAfter()
							#
							#print(self.vetorParaTestarOFeedMovel)							
							exibirDadosDoClienteAgendado(cliente, dataAgendada, horaAgendada,telefoneDoCliente, self.primeiroDoFeed, contadorDeClientesAgendados)
							return (contadorDeClientesAgendados + 1)
						
						elif contadorDeClientesAgendados == 2:
							pass
						elif contadorDeClientesAgendados == 3:
							pass
						else:
							pass
					
					elif contadorDeDatasComClientesAgendados == 1:

						if contadorDeClientesAgendados == 0:
							datarComoTituloAJanelaQueVaiMostrarOsClientes(dataAgendada, self.segundoDoFeed)
							exibirDadosDoClienteAgendado(cliente, dataAgendada, horaAgendada,telefoneDoCliente, self.segundoDoFeed, contadorDeClientesAgendados)
							return (contadorDeClientesAgendados + 1)
						else:
							exibirDadosDoClienteAgendado(cliente, dataAgendada, horaAgendada,telefoneDoCliente, self.segundoDoFeed, contadorDeClientesAgendados)
							return (contadorDeClientesAgendados + 1)

					elif contadorDeDatasComClientesAgendados == 2:

						if contadorDeClientesAgendados == 0:
							datarComoTituloAJanelaQueVaiMostrarOsClientes(dataAgendada, self.terceiroDoFeed)
							exibirDadosDoClienteAgendado(cliente, dataAgendada, horaAgendada,telefoneDoCliente, self.terceiroDoFeed, contadorDeClientesAgendados)
							return (contadorDeClientesAgendados + 1)
						else:
							exibirDadosDoClienteAgendado(cliente, dataAgendada, horaAgendada,telefoneDoCliente, self.terceiroDoFeed, contadorDeClientesAgendados)
							return (contadorDeClientesAgendados + 1)
					
					elif contadorDeDatasComClientesAgendados == 3:

						if contadorDeClientesAgendados == 0:
							datarComoTituloAJanelaQueVaiMostrarOsClientes(dataAgendada, self.quartoDoFeed)
							exibirDadosDoClienteAgendado(cliente, dataAgendada, horaAgendada,telefoneDoCliente, self.quartoDoFeed, contadorDeClientesAgendados)
							return (contadorDeClientesAgendados + 1)
						else:
							exibirDadosDoClienteAgendado(cliente, dataAgendada, horaAgendada,telefoneDoCliente, self.quartoDoFeed, contadorDeClientesAgendados)
							return (contadorDeClientesAgendados + 1)	
						
				def datarComoTituloAJanelaQueVaiMostrarOsClientes(data, frame):
					dataTituloDosClientesDaqueleDia = Label(frame, text = "Data: "+ data, justify = 'left', anchor = 'w', width = 15 , bg = 'black' , fg = 'white', font = ('Franklin Gothic Medium', 11))
					dataTituloDosClientesDaqueleDia.pack( pady = 3)

				def exibirDadosDoClienteAgendado(cliente, dataAgendada, horaAgendada,telefoneDoCliente, frame, contadorDeClientesAgendados):
					
					def criarFramesParaPrimeiraDataComClienteQueVaiAparecer(frame):
						
						framePrincipalDoFeed = Frame(frame, bg = 'black')
						framePrincipalDoFeed.pack(side = BOTTOM)
						
						ladoDireitoDaframe = Frame(framePrincipalDoFeed, bg = 'black')
						ladoDireitoDaframe.pack(side = RIGHT)

						ladoEsquerdoDaFrame = Frame(framePrincipalDoFeed, bg = 'black')
						ladoEsquerdoDaFrame.pack(side = LEFT)

						frameParaExibirOsDados = Frame(ladoDireitoDaframe, bg = 'black')
						frameParaExibirOsDados.pack(pady = 8)
						
						mostrarFotoDoClienteAgendado(cliente, ladoEsquerdoDaFrame)
						mostrarDadosDoClienteAgendado(cliente, horaAgendada, telefoneDoCliente, frameParaExibirOsDados)

					def ampliarFotoDoCliente(diretorio):
						#print("AQUI")
						imagem = cv2.imread(diretorio)
						cv2.imshow("imagens_clientes", imagem) 
						cv2.waitKey(0)

					def mostrarFotoDoClienteAgendado(nome, ladoEsquerdoDaFrame):
						
						diretorio = "C:/sistema_loja-main/imagens_clientes"	
						fotoDoCliente = PhotoImage(file = (diretorio+'/'+nome+".gif"))
						fotoDoCliente = fotoDoCliente.zoom(9)													#
						fotoDoCliente = fotoDoCliente.subsample(30)
						self.botaoParaAmpliacaoDaFoto = Button(ladoEsquerdoDaFrame, bg = 'black' , command = partial(ampliarFotoDoCliente,diretorio+'/'+nome+".png"))
						self.botaoParaAmpliacaoDaFoto['image'] = fotoDoCliente											#
						self.botaoParaAmpliacaoDaFoto.image = fotoDoCliente												#
						self.botaoParaAmpliacaoDaFoto.pack(pady = 10, padx = 3)

					def mostrarDadosDoClienteAgendado(nome, hora, telefone, frameParaExibirOsDados):
						
						self.nomeDoCliente = Label(frameParaExibirOsDados, text = "Nome: "+ nome, justify = 'left', anchor = 'w', width = 20 , bg = 'black' , fg = 'white', font = ('Franklin Gothic Medium', 10))
						self.nomeDoCliente.pack()

						self.horaAgendada = Label(frameParaExibirOsDados, text ="Hora: " +hora  , justify = 'left', anchor = 'w', width = 20 , bg = 'black' , fg = 'white', font = ('Franklin Gothic Medium', 10))
						self.horaAgendada.pack()

						self.telefoneDoCliente = Button(frameParaExibirOsDados,text ="Telefone: " +telefone,command = partial(self.open_Url, telefone), border ="0", justify = 'left', anchor = 'w', width = 20 , bg = 'black' , fg = 'white', font = ('Franklin Gothic Medium', 10))
						self.telefoneDoCliente.pack()
				
					def trocarDadosDoClienteExibidoNoFeed(nome, hora, telefone ): #TODO - idéia em andamento para implementação de da mudança de cliente de acordo com o feed
						diretorio = "C:/sistema_loja-main/imagens_clientes"	
						fotoDoCliente = PhotoImage(file = (diretorio+'/'+nome+".gif"))
						fotoDoCliente = fotoDoCliente.zoom(9)													#
						fotoDoCliente = fotoDoCliente.subsample(30)
						self.botaoParaAmpliacaoDaFoto['image'] = fotoDoCliente											#
						self.botaoParaAmpliacaoDaFoto.image = fotoDoCliente
						self.nomeDoCliente['text'] = nome
						self.horaAgendada['text'] = hora
						self.telefoneDoCliente['text'] = telefone
					
					if contadorDeClientesAgendados == 0:
						criarFramesParaPrimeiraDataComClienteQueVaiAparecer(frame)
					else:
						criarFramesParaPrimeiraDataComClienteQueVaiAparecer(frame)
						pass
						#trocarDadosDoClienteExibidoNoFeed(cliente, horaAgendada, telefoneDoCliente )		

				chave = definirOrdemDeDadosInseridos(cliente, dataAgendada, horaAgendada,telefoneDoCliente, contadorDeClientesAgendados,contadorDeDatasComClientesAgendados)
				return chave

			chave = gerenciarLayoutDoFeed(cliente, dataAgendada, horaAgendada,telefoneDoCliente, contadorDeClientesAgendados, contadorDeDatasComClientesAgendados)
			return chave		
		
		#Chamada para o inicio da função para gerenciar o feed
		carregarTituloDoFeed()
		verificarProximasDatasDaAgenda(self.dataDoSistema)

	def botoesDoMenuPrincipal(self): # - Menu principal com os botões: Clients, Finanças, Estoque e Agenda - #
		
		def gerenciarLayoutDosBotoesDoMenuPrincipal(): 
			self.botaoCliente = Button(self.menu, text = "Clientes", command = abrirJanelaCliente, width = 30, height = 3, activebackground = "#353839", activeforeground = 'white', bg = 'black', fg = 'white', font = ('Franklin Gothic Medium', 20))
			self.botaoCliente.pack()

			self.botaoMateriais = Button(self.menu, text = "Materiais",command = abrirJanelaEstoque, width = 30, height = 3,  activebackground = "#353839", activeforeground = 'white', bg = 'black', fg = 'white', font = ('Franklin Gothic Medium', 20))
			self.botaoMateriais.pack()
			
			self.botaoFinancas = Button(self.menu, text = "Finanças",command = abrirJanelaFinanca , width = 30, height = 3, activebackground = "#353839", activeforeground = 'white', bg = 'black', fg = 'white', font = ('Franklin Gothic Medium', 20))
			self.botaoFinancas.pack()
			
			self.botaoAgenda = Button(self.menu, text = " Agenda 	",command = abrirJanelaAgenda, width = 30, height = 3, activebackground = "#353839", activeforeground = 'white', bg = 'black', fg = 'white', font = ('Franklin Gothic Medium', 20))
			self.botaoAgenda.pack()		
		
		def abrirJanelaCliente(): 

			self.feed.place_forget()	
			self.menu.place_forget()
			self.feed_rodape.pack_forget()
			cliente.cliente(self.i ,self.feed_rodape,self.rodape,self.menu, self.feed, self.metadeEsquerdaDoPrincipal, self.metadeDireitaDoPrincipal )

		def abrirJanelaEstoque(): 

			self.feed.place_forget()
			self.menu.place_forget()
			self.feed_rodape.pack_forget()
			self.aux_right_main = Frame(self.metadeDireitaDoPrincipal, bg = 'black')
			self.aux_right_main.pack()
			self.aux_left_main = Frame(self.metadeEsquerdaDoPrincipal, bg = 'black')
			self.aux_left_main.pack()
			estoque.estoque(self.i,self.feed_rodape,self.rodape,self.menu, self.feed, self.metadeEsquerdaDoPrincipal, self.metadeDireitaDoPrincipal,  self.datahora, self.aux_right_main, self.aux_left_main)		
		
		def abrirJanelaFinanca():

			self.feed.place_forget()
			self.menu.place_forget()
			self.feed_rodape.pack_forget()
			self.aux_right_main = Frame(self.metadeDireitaDoPrincipal, bg = 'black')
			self.aux_right_main.pack()
			self.aux_left_main = Frame(self.metadeEsquerdaDoPrincipal, bg = 'black')
			self.aux_left_main.pack()
			finanças.financas(self.i,self.feed_rodape,self.rodape,self.menu, self.feed, self.metadeEsquerdaDoPrincipal, self.metadeDireitaDoPrincipal,  self.datahora, self.aux_right_main, self.aux_left_main)		
		
		def abrirJanelaAgenda():

			self.feed.place_forget()
			self.menu.place_forget()
			self.feed_rodape.pack_forget()
			self.aux_right_main = Frame(self.metadeDireitaDoPrincipal, bg = 'black')
			self.aux_right_main.pack()
			self.aux_left_main = Frame(self.metadeEsquerdaDoPrincipal, bg = 'black')
			self.aux_left_main.pack()
			agenda.agenda(self.i,self.feed_rodape,self.rodape,self.menu, self.feed, self.metadeEsquerdaDoPrincipal, self.metadeDireitaDoPrincipal,  self.datahora, self.aux_right_main, self.aux_left_main)
			
		gerenciarLayoutDosBotoesDoMenuPrincipal()

	def gerarFeedDeMateriaisPendentes(self): # - Carrega as opções para o feed de material - #
		
		def gerarMensagemPadrao():
			return f'Não há materiais pendentes'

		def coletarDadosDoBanco(contadorDeMateriaisPendentes):
			produtosCadastrados = databaseproduto.produtos
			
			for produto in produtosCadastrados:
				self.produto = produto.decode()
				aux = '' 
				DADOS_DO_PRODUTO = produtosCadastrados[produto.decode()].decode()
				
				for caracterer in DADOS_DO_PRODUTO:
					
					if caracterer == "¹":
						self.valor = aux
						aux = ''
					elif caracterer == "²":
						self.capacidadeDoEstoque = aux
						aux = ''
					elif caracterer == "§":
						self.quantidadeAtual = aux
						aux = ''
					else:
						aux += caracterer

				contadorDeMateriaisPendentes += compararQuantidadeAtualComACapacidadeDoEstoque(contadorDeMateriaisPendentes)
			
			return contadorDeMateriaisPendentes
			
		def compararQuantidadeAtualComACapacidadeDoEstoque(contadorDeMateriaisPendentes):
			
			if int(self.quantidadeAtual) < (int(self.capacidadeDoEstoque)/3) and contadorDeMateriaisPendentes < 2:
				self.MENSAGEM_DO_FEED = self.MENSAGEM_DO_FEED+"Há apenas"+str(self.quantidadeAtual)+" "+self.produto+ " de "+ str(self.capacidadeDoEstoque)+'\n'
				return 1

			elif int(self.quantidadeAtual) < (int(self.capacidadeDoEstoque)/3) and contadorDeMateriaisPendentes >= 2:
				self.MENSAGEM_DO_FEED = f'Conferir estoque, há {contadorDeMateriaisPendentes} materiais pendentes'
				return 1
			
			else:
				return 0

		def gerarLayoutDeApresentacaoDeDados(contadorDeMateriaisPendentes):
			
			if contadorDeMateriaisPendentes > 0:
				fg = f'red'
			else:
				fg = f'green'

			self.feed_rodape = Label(self.rodape, text = self.MENSAGEM_DO_FEED , bg = 'black', fg = fg, pady = 30, font = ('Franklin Gothic Medium', 20) )
			self.feed_rodape.pack()	
		
		contadorDeMateriaisPendentes = 0											
		self.MENSAGEM_DO_FEED = gerarMensagemPadrao()									
		contadorDeMateriaisPendentes = coletarDadosDoBanco (contadorDeMateriaisPendentes)
		gerarLayoutDeApresentacaoDeDados (contadorDeMateriaisPendentes)

	def open_Url(self, telefone):
		webbrowser.open_new("wa.me/"+"55"+telefone)


	#'''''''''''''''''''''''''''''''''''''''''''''''	