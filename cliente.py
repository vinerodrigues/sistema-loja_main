from tkinter import*
import tkinter as tk
from tkinter import filedialog
from PIL import Image
import dbclientes
from functools import partial
import os.path
import os
import shutil
import cv2
import tirar_foto_cliente
import janeladetalhada_tatuagens
import random
import historicoDeInvestimento


class cliente(object):
	def __init__(self, app, feed_rodape, footer, menu, feed, left_main, ladoDireito):

		self.criarFramesDaJanelaCliente(left_main, ladoDireito)
		self.gerenciarBotoesDoJanelaCliente(footer, menu, feed, feed_rodape, ladoDireito)
		self.criarFormulario(app)			# Onde ficam os campos para amazenamentos de informações dos clientes e foto.
		self.carregarListaDeClientes(ladoDireito, ordem = None)

	def criarFramesDaJanelaCliente(self, left_main, ladoDireito):
		self.menuDoLadoEsquerdo = Frame(left_main, bg = 'black')
		self.menuDoLadoEsquerdo.pack()
		self.corpoDoLadoEsquerdo = Frame(left_main, bg = 'black')
		self.corpoDoLadoEsquerdo.pack()

		#frame super especial
		self.frameParaOsBotoesDeOrdenacao = Frame(ladoDireito, bg = 'black')
		self.frameParaOsBotoesDeOrdenacao.pack()


		self.rodaPeDoScrollbarParaMostrarONumeroDeCliente = Frame(ladoDireito)
		self.rodaPeDoScrollbarParaMostrarONumeroDeCliente.pack(side = BOTTOM)

	def gerenciarBotoesDoJanelaCliente(self, footer, menu, feed, feed_rodape, ladoDireito):
		
		def criarBotoesDaJanelaCliente(footer, menu, feed, feed_rodape, ladoDireito):
			self.botaoAdicionarCliente = Button(self.menuDoLadoEsquerdo, text = "Adicionar", command = partial(adicionarCliente, ladoDireito), height = 2, width = 28,  activebackground = "#353839", activeforeground = 'white', bg = 'black', fg = 'white', font = ('Franklin Gothic Medium', 10) )
			self.botaoAdicionarCliente.pack(side= LEFT)
			self.botaoRemoverCliente = Button(self.menuDoLadoEsquerdo, text = "Remover", command = removerCliente,  height = 2, width = 28, activebackground = "#353839", activeforeground = 'white', bg = 'black', fg = 'white', font = ('Franklin Gothic Medium', 10) )
			self.botaoRemoverCliente.pack(side= LEFT)
			self.botaoPesquisarCliente = Button(self.menuDoLadoEsquerdo, text = "Pesquisar ", command = pesquisarCliente , height = 2,width = 28,  activebackground = "#353839", activeforeground = 'white', bg = 'black', fg = 'white', font = ('Franklin Gothic Medium', 10) )
			self.botaoPesquisarCliente.pack(side= LEFT)		                            
			self.botaoVoltarMenuAnterior = Button(footer, text = 'Voltar', command = partial(voltarAoMenuAnterior, menu, feed, feed_rodape), pady = 10, width = 30,  activebackground = "#353839", activeforeground = 'white', bg = 'black', fg = 'white', font = ('Franklin Gothic Medium', 10))
			self.botaoVoltarMenuAnterior.pack(pady =20)

			self.botaoSortearCliente = Button(self.frameParaOsBotoesDeOrdenacao, text = "Sortear Cliente", command = sortearCliente,  height = 2, width = 14, activebackground = "#353839", activeforeground = 'white', bg = 'black', fg = 'white', font = ('Franklin Gothic Medium', 10) )
			self.botaoSortearCliente.pack(side= LEFT)

			self.botaoOrdenarCrescenteCliente = Button(self.frameParaOsBotoesDeOrdenacao, text = "A.. Z", command = partial(ordenarCrescente, ladoDireito),  height = 2, width = 4, activebackground = "#353839", activeforeground = 'white', bg = 'black', fg = 'white', font = ('Franklin Gothic Medium', 10) )
			self.botaoOrdenarCrescenteCliente.pack(side= LEFT)

			self.botaoOrdenarDecrescenteCliente = Button(self.frameParaOsBotoesDeOrdenacao, text = "Z.. A", command = partial(ordenarDecrescente, ladoDireito),  height = 2, width = 4, activebackground = "#353839", activeforeground = 'white', bg = 'black', fg = 'white', font = ('Franklin Gothic Medium', 10) )
			self.botaoOrdenarDecrescenteCliente.pack(side= LEFT)

			self.botaoPrimeirosClientes = Button(self.frameParaOsBotoesDeOrdenacao, text = "Primeiros Cliente", command = partial(primeirosClientes, ladoDireito),  height = 2, width = 14, activebackground = "#353839", activeforeground = 'white', bg = 'black', fg = 'white', font = ('Franklin Gothic Medium', 10) )
			self.botaoPrimeirosClientes.pack(side= LEFT)

			self.botaoUltimosClientes = Button(self.frameParaOsBotoesDeOrdenacao, text = "Ultimos Cliente", command = partial(ultimosClientes, ladoDireito),  height = 2, width = 14, activebackground = "#353839", activeforeground = 'white', bg = 'black', fg = 'white', font = ('Franklin Gothic Medium', 10) )
			self.botaoUltimosClientes.pack(side= LEFT)
		
		def recarregarScrollBarsParaAtualizarClientesCadastrados(ladoDireito):
			self.carregarListaDeClientes(ladoDireito, None)
		
		def adicionarCliente(ladoDireito):
			def tratarDadosInseridos(ladoDireito):
				nome = obterNomeTratado()
				verificarSeTodosOsCamposForamPreenchidos()
				dados = empacotarDadosRecebidos()
				inserirDadosNoBanco(nome, dados)
				criarUmDiretorioParaArmazenarAsTatuagensJaFeitasPeloCliente(nome)
				recarregarScrollBarsParaAtualizarClientesCadastrados(ladoDireito)
				
			def obterNomeTratado():
				return self.entry_nome.get()
			
			def verificarSeTodosOsCamposForamPreenchidos():				
				if self.entry_tel.get() == '':
					messagebox.showwarning("CAMPO IMCOMPLETO", "O campo telefone não está preenchido corretamente") 
				if self.entry_nascimento.get() == '':
					messagebox.showwarning("CAMPO IMCOMPLETO", "O campo nascimento não está preenchido corretamente")				
				if self.entry_email.get()=='':
					messagebox.showwarning("CAMPO IMCOMPLETO", "O campo email não está preenchido corretamente")			
				if self.entry_end.get()== '':
					messagebox.showwarning("CAMPO IMCOMPLETO", "O campo  endereço não está preenchido corretamente")				
				if self.entry_age_data.get()== '':
					messagebox.showwarning("CAMPO IMCOMPLETO", "O campo data não está preenchido corretamente")				
				if self.entry_age_hora.get()=='':
					messagebox.showwarning("CAMPO IMCOMPLETO", "O campo hora não está preenchido corretamente")				
				if self.entry_comentarios.get()=='':
					messagebox.showwarning("CAMPO IMCOMPLETO", "O campo comentarios telefone não está preenchido corretamente")
			
			def empacotarDadosRecebidos():
				return self.entry_tel.get()+"¹"+self.entry_nascimento.get()+"¹"+self.entry_email.get()+"¹"+self.entry_end.get()+"¹"+self.entry_age_data.get()+"¹"+self.entry_age_hora.get()+'¹'+self.entry_comentarios.get()+'¹'+"²"	
			
			def inserirDadosNoBanco(nome, dados):
				dbclientes.add_clientes(nome, dados)

			def criarUmDiretorioParaArmazenarAsTatuagensJaFeitasPeloCliente(nome):
				diretorio = "C:/sistema_loja-main/Tatuagens/"+nome
				if os.path.isdir(diretorio): 
					pass
				else:
					os.mkdir(diretorio)

			tratarDadosInseridos(ladoDireito)	

		def removerCliente(ladoDireito):
			def tratarDadosParaRemocaoDeCliente():
				nome = obterNomeTratado()
				removerCliente(nome)
				recarregarScrollBarsParaAtualizarClientesCadastrados(ladoDireito)
				removerPastaDosCliente(nome)

			def obterNomeTratado():
				return self.entry_nome.get()
			
			def removerCliente(nome):
				dbclientes.rem_clientes(nome)

			def removerPastaDosCliente(nome):
				os.rmdir("C:/sistema_loja-main/Tatuagens/"+nome)
			
			tratarDadosParaRemocaoDeCliente(ladoDireito)
		
		def pesquisarCliente():
			def tradarDadosParaPesquisaDeCliente():
				nome = obterNomeTratado()
				self.tratarDadosParaExibirNasCaixasDeTexto(nome)

			def obterNomeTratado():
				return self.entry_nome.get()	
			
			tradarDadosParaPesquisaDeCliente()

		def sortearCliente():
			clientesCadastrados = list(dbclientes.clientes.keys())
			clienteSorteado = clientesCadastrados[random.randint(0, len(clientesCadastrados))].decode()
			self.nome_tatuagem = clienteSorteado
			self.entry_nome.delete(0,END)
			self.entry_nome.insert(END, clienteSorteado)
			self.tratarDadosParaExibirNasCaixasDeTexto(clienteSorteado)

		def ordenarCrescente(ladoDireito):
			self.carregarListaDeClientes(ladoDireito, 'Ordem alfabetica crescente')

		def ordenarDecrescente(ladoDireito):
			self.carregarListaDeClientes(ladoDireito, 'Ordem alfabetica decrescente')

		def primeirosClientes(ladoDireito):
			self.carregarListaDeClientes(ladoDireito, 'Primeiros clientes')

		def ultimosClientes(ladoDireito):
			self.carregarListaDeClientes(ladoDireito, 'Ultimo clientes')	

		def voltarAoMenuAnterior(menu, feed, rodape): # - Responsavel por voltar ao menu anterio - #
			def reconstruirPacotes(menu, feed, rodape):
				menu.place(x =0, y = 0 , width = 850, height = 500)
				feed.place(x =0, y = 0 , width = 490, height = 500)
				feed_rodape.pack()
			
			def destruirPacotes():
				self.menuDoLadoEsquerdo.destroy()
				self.corpoDoLadoEsquerdo.destroy()
				self.botaoVoltarMenuAnterior.destroy()
				self.botaoRemoverCliente.destroy()
				self.botaoAdicionarCliente.destroy()
				self.botaoPesquisarCliente.destroy()	
				self.my_canvas.destroy()
				self.my_scrollsbars.destroy()
				self.frame_top.destroy()
				self.frame_bottom.destroy()
				self.entry_comentarios.destroy()
				self.frame_top_bottom.destroy()
				self.label_comentarios.destroy()
				self.frameParaOScrollbars.destroy()
				self.frameParaOsBotoesDeOrdenacao.destroy()
				self.botaoSortearCliente.destroy()
				self.botaoOrdenarCrescenteCliente.destroy()
				self.botaoOrdenarDecrescenteCliente.destroy()
				self.botaoPrimeirosClientes.destroy()
				self.botaoUltimosClientes.destroy()
				self.rodaPeDoScrollbarParaMostrarONumeroDeCliente.destroy()
			reconstruirPacotes(menu, feed, rodape)
			destruirPacotes()	
		#

		criarBotoesDaJanelaCliente(footer, menu, feed, feed_rodape, ladoDireito)
	
	def criarFormulario(self, app):	
		
		def criarFramesDoFormularios(app):	
			
			def criarFramesQueDividemOladoEsquerdoAoMeioHorizontalmente():
				### FRAMES RPRINCIPAIS
				self.frame_top = Frame(self.corpoDoLadoEsquerdo, bg = 'black')
				self.frame_top.pack(pady = 15)
				self.frame_bottom = Frame(self.corpoDoLadoEsquerdo, bg = 'black') # o bottom vai ser o proprio roda pé
				self.frame_bottom.pack()
			
			def criarFramesFilhasDaParteSuperior(app):
				### SUB FRAMES TOP 
				self.frame_top_left = Frame(self.frame_top, bg = 'black')
				self.frame_top_left.pack(side = LEFT, padx = 20 )
				self.frame_top_right = Frame(self.frame_top, bg = 'black')
				self.frame_top_right.pack(side = RIGHT)
				
				self.frame_top_bottom = Frame(app, bg = 'black')
				self.frame_top_bottom.place(y = 440	, x = 182)
			
			def criarFramesDosDadosInseridos():
				### SUB FRAMES YOP RIGHT
				self.frame_top_right_name = Frame(self.frame_top_right, bg = 'black')
				self.frame_top_right_name.pack()
				self.frame_top_right_born = Frame(self.frame_top_right, bg = 'black')
				self.frame_top_right_born.pack()
				self.frame_top_right_tel = Frame(self.frame_top_right, bg = 'black')
				self.frame_top_right_tel.pack()
				self.frame_top_right_email = Frame(self.frame_top_right, bg = 'black')
				self.frame_top_right_email.pack()
				self.frame_top_right_end = Frame(self.frame_top_right, bg = 'black')
				self.frame_top_right_end.pack()
				self.frame_top_right_age = Frame(self.frame_top_right, bg = 'black')
				self.frame_top_right_age.pack()
				### sub frame de agendamento
				self.frame_top_right_age_header = Frame(self.frame_top_right, bg = 'black')
				self.frame_top_right_age_header.pack()
				self.frame_top_right_age_body = Frame(self.frame_top_right, bg = 'black')
				self.frame_top_right_age_body.pack()

				self.frame_top_right_tattoo = Frame(self.frame_top_right, bg = 'black')
				self.frame_top_right_tattoo.pack()
			
			def criarCampoDeCaptacaoDeDados(app):		
				self.label_nome = Label(self.frame_top_right_name, text = "NOME:      ", justify = 'left', anchor = 'w', width = 12 , bg = 'black' , fg = 'white', font = ('Franklin Gothic Medium', 12))
				self.label_nome.pack(side = LEFT, pady = 2)#, fill = X, expand = YES,  )
				self.entry_nome = Entry(self.frame_top_right_name, bg = 'black', fg = 'white')
				self.entry_nome.pack( pady = 2 )#, side = RIGHT, expand = YES, fill = X)
		
				############ DATA DE NASCIMENTO		
				self.label_nascimento = Label(self.frame_top_right_born, text = "NASCIMENTO:      ", justify = 'left', anchor = 'w', width = 12 , bg = 'black' , fg = 'white', font = ('Franklin Gothic Medium', 12))
				self.label_nascimento.pack(side = LEFT, pady = 2, fill = X, expand = YES,  )
				self.entry_nascimento = Entry(self.frame_top_right_born, bg = 'black', fg = 'white')
				self.entry_nascimento.pack( pady = 2 , side = RIGHT, expand = YES, fill = X)
				
				############ TELEFONE		
				self.label_tel = Label(self.frame_top_right_tel, text =   "TELEFONE:  ", justify = 'left', anchor = 'w', width = 12, bg = 'black' , fg = 'white', font = ('Franklin Gothic Medium', 12))
				self.label_tel.pack(side = LEFT, pady = 2)
				self.entry_tel = Entry(self.frame_top_right_tel, bg = 'black', fg = 'white')
				self.entry_tel.pack(pady = 2, side = RIGHT, expand = YES, fill = X)
				
				############ EMAIL	
				self.label_email = Label(self.frame_top_right_email,text ="EMAIL:     ", justify = 'left', anchor = 'w', width = 12 ,bg = 'black' , fg = 'white', font = ('Franklin Gothic Medium', 12))
				self.label_email.pack(side = LEFT, pady = 2)
				self.entry_email = Entry(self.frame_top_right_email, bg = 'black', fg = 'white')
				self.entry_email.pack(pady = 2, side = RIGHT, expand = YES, fill = X)
				
				############ ENDEREÇO		
				self.label_end = Label(self.frame_top_right_end, text =   "ENDEREÇO:  ", justify = 'left', anchor = 'w', width = 12, bg = 'black' , fg = 'white', font = ('Franklin Gothic Medium', 12))
				self.label_end.pack(side = LEFT, pady = 2)
				self.entry_end = Entry(self.frame_top_right_end, bg = 'black', fg = 'white')
				self.entry_end.pack( pady = 2, side = RIGHT, expand = YES, fill = X)
				
				############ AGENDAMENTO		
				self.label_age = Label(self.frame_top_right_age_header, text =   "AGENDAR:", justify = 'left', anchor = 'w', width = 8, bg = 'black' , fg = 'white', font = ('Franklin Gothic Medium', 12))
				self.label_age.pack(side = LEFT,fill = X, expand = YES, pady = 2)
				self.label_age_aux = Label(self.frame_top_right_age_header, text =   ".", bg = 'black', font = ('Franklin Gothic Medium', 12))
				self.label_age_aux.pack(side = LEFT,fill = X, expand = YES, pady = 2, padx = 70)
				
				########### DATA
				self.label_age_data = Label(self.frame_top_right_age_body, text =   "DATA:", bg = 'black' , fg = 'white', font = ('Franklin Gothic Medium', 12))
				self.label_age_data.pack(side = LEFT, pady = 2)
				self.entry_age_data = Entry(self.frame_top_right_age_body, bg = 'black', fg = 'white', width = 10)
				self.entry_age_data.pack( pady = 2,side = LEFT, expand = YES, fill = X)
				
				########### HORA
				self.label_age_hora = Label(self.frame_top_right_age_body, text =   "  HORA:", bg = 'black' , fg = 'white', font = ('Franklin Gothic Medium', 12))
				self.label_age_hora.pack(side = LEFT, pady = 2)
				self.entry_age_hora = Entry(self.frame_top_right_age_body, bg = 'black', fg = 'white', width = 10)
				self.entry_age_hora.pack(side = LEFT, pady = 2, expand = YES, fill = X)

				########### Comentarios ##########################		
				self.label_comentarios = Label(app, width = 15 , justify = 'left', anchor = 'w', text = "COMENTARIOS: ", bg = 'black' , fg = 'white', font = ('Franklin Gothic Medium', 11))
				self.label_comentarios.place(y = 560, x = 70)			
			
			def criarCampoDeCaptacaoDeTatuagens(app):	

				self.frameTatuagens = Frame(self.frame_top_bottom, bg = 'black', width = 900)
				self.frameTatuagens.pack(side = BOTTOM, pady = 3, padx = 3)	

				self.framesMenuTatuagensDoHistoricoDeInvestimento = Frame(self.frameTatuagens, bg = 'black', width = 60)
				self.framesMenuTatuagensDoHistoricoDeInvestimento.pack(padx = 2, pady = 2, side = RIGHT)

				self.botaoMostarTatuagens = Button(self.frameTatuagens, border = '2', width = 31, height = 1, command = partial(mostrarTatuagensFeitasPeloCliente, self.entry_nome.get(), app),  text = "TATUAGENS", bg = 'black' , fg = 'white', font = ('Franklin Gothic Medium', 11))
				self.botaoMostarTatuagens.pack(side = LEFT, pady = 3, padx = 3)
				
			def criarCampoParaComentarioDeClientes(app):
				self.entry_comentarios = Entry(app, bg = 'black', fg = 'white', width = 60)
				self.entry_comentarios.place(y = 550, x = 188, width= 515, height=50) 		
			
			def carregarFotoDosClientesPadrao():
				self.logo2 = PhotoImage(file=("C:/sistema_loja-main/imagens_clientes/seg_2.gif"))
				self.add_users = Button(self.frame_top_left, bg = 'black', command = tirarFotoParaCadastroDeCliente)
				self.add_users['image'] = self.logo2
				self.add_users.image = self.logo2
				self.add_users.pack(side = LEFT, pady = 15)
			
			def tirarFotoParaCadastroDeCliente():
				a = tirar_foto_cliente.carregar_foto(self.entry_nome.get())
				self.logo2 = PhotoImage(file=("C:/sistema_loja-main/imagens_clientes/"+self.entry_nome.get()+".gif"))
				self.add_users['image'] = self.logo2
				self.add_users.image = self.logo2
			
			criarFramesQueDividemOladoEsquerdoAoMeioHorizontalmente()
			criarFramesFilhasDaParteSuperior(app)
			criarFramesDosDadosInseridos()
			criarCampoDeCaptacaoDeDados(app)
			criarCampoDeCaptacaoDeTatuagens(app)
			criarCampoParaComentarioDeClientes(app)
			carregarFotoDosClientesPadrao()

		def mostrarTatuagensFeitasPeloCliente(nome, app):

			def feedDoHistoricoDeTatuagensFeitasPeloCliente(nome, app):
				
				def gerenciarJanelaTatuagens(nome, app):
					
					def main (nome, app):
						self.app = app
						nomeDoClienteComTatuagensFeitas = obterNomeDoClienteParaMostrarAsTatuagens()
						self.cliente = historicoDeInvestimento.historicoDeInvestimento(self.entry_nome.get())
						#Assim que souber o nome do cliente tem que carregar o banco de dados
						#O nome vai ser parametro para classe do banco de dados do historico de investimento

						if verificarSeONomeEhInvalido(nomeDoClienteComTatuagensFeitas):
							messagebox.showerror("ERRO GRAVISSIMO", "Usuario não selecionado")
							return None
						else:
							#Esse comando tem que vir depois do banco de dados carregado pq ele precisa mostrar o valor total
							#de tatuagens feitas pelo cliente
							modificarCaracteristicasDoBotaoMostrarTatuagens(app)
					
						diretorioDoUsuario = gerarDiretorioDoUsuario(nomeDoClienteComTatuagensFeitas)
						listaDeArquivosDoClienteFormatada = formatarTodosOsArquivosContidosNaPastaDoCliente(diretorioDoUsuario, nomeDoClienteComTatuagensFeitas)															
						gerenciarMenusComLoops(listaDeArquivosDoClienteFormatada, nomeDoClienteComTatuagensFeitas, app )

					def obterNomeDoClienteParaMostrarAsTatuagens():
						return self.entry_nome.get()
					
					def verificarSeONomeEhInvalido(nome):
						return nome == ''
					
					def modificarCaracteristicasDoBotaoMostrarTatuagens(app):
						valor = 20.35
						self.botaoMostarTatuagens['width'] = 20
						self.botaoMostarTatuagens['height'] = 2
						self.botaoMostarTatuagens['command'] = partial(desfazerAJanelaDeTatuagens, app)
						self.botaoMostarTatuagens['text'] = f'Historico de investimento\n\n {self.cliente.valorDeTodasAsTatuagens}0 R$'
						self.botaoMostarTatuagens['border'] = '0'
						self.botaoMostarTatuagens['font'] = ('Franklin Gothic Medium', 10)
					
					def gerarDiretorioDoUsuario(nomeDoClienteComTatuagensFeitas):
					
						def verificarSeODiretorioExiste(diretorioDoUsuario):
							return os.path.isdir(diretorioDoUsuario)
						
						def criarDiretorio(diretorioDoUsuario):
							os.mkdir(diretorioDoUsuario)	

						diretorioDoUsuario = "C:/sistema_loja-main/Tatuagens/"+nomeDoClienteComTatuagensFeitas
						
						if not verificarSeODiretorioExiste(diretorioDoUsuario):
							criarDiretorio(diretorioDoUsuario)
						return diretorioDoUsuario
					
					def formatarTodosOsArquivosContidosNaPastaDoCliente(diretorioDoUsuario, nomeDoUsuario):
					
						shutil.copy( "C:/sistema_loja-main/Tatuagens/imagemDefaultParaTatuagens/~~~~~.gif", "C:/sistema_loja-main/Tatuagens/"+nomeDoUsuario )
						converterFotosEnviadasPorClientes (os.listdir(diretorioDoUsuario), diretorioDoUsuario)
						listaDeArquivos = os.listdir(diretorioDoUsuario)
						return listaDeArquivos
					
					main(nome, app)

				def criarFrameDasFotosDasTatuagens():					
					try:
						self.framesDasFotosDasTatuagens = Frame(self.framesMenuTatuagensDoHistoricoDeInvestimento, bg = 'black', width = 60)
						self.framesDasFotosDasTatuagens.pack(padx = 2, pady = 2, side = RIGHT)
					except:
						pass

				def criarBotaoDeAdicaoDeNovasTatuagens(): #Função especial 

					def criarFrameQueAdicionaAFoto():
						try:
							self.frameMenuQueAdicionaAFoto = Frame(self.framesDasFotosDasTatuagens, width = 10, height = 6,  bg = 'black')
							self.frameMenuQueAdicionaAFoto.pack(padx = 2, pady = 2, side = RIGHT)
						except:
							pass
		
					def criarBotaoQueAdicionaAFoto():
						
						try:
							self.botaoQueAdicionaAFoto = Button(self.frameMenuQueAdicionaAFoto, command = adicionarFotoDaTatuagemNaPastaCliente , border = '0', text = '+', width = 10, height = 4,  bg = 'black' , fg = 'white', font = ('Franklin Gothic Medium', 12))
							self.botaoQueAdicionaAFoto.pack()
						except:
							pass

					def adicionarFotoDaTatuagemNaPastaCliente():
						valorDaTatuagem = self.entryMenuFotoValorDaTatuagem.get()
					
					criarFrameQueAdicionaAFoto()
					criarBotaoQueAdicionaAFoto()
				
				def converterFotosEnviadasPorClientes(lista_de_arquivo, diretorio): 
					
					for i in lista_de_arquivo:
						if ".jpg" in i:
							imagens = Image.open(diretorio+'/'+i)
							imagens = imagens.resize((400,400))
							nome_sem_ext = os.path.splitext(i)[0]
							imagens.save(os.path.join(diretorio,nome_sem_ext+'.png'))
							os.remove(diretorio+'/'+i)
							
							
						if ".gif" in i:
							imagens = Image.open(diretorio+'/'+i)
							imagens = imagens.resize((400,400))
							nome_sem_ext = os.path.splitext(i)[0]
							imagens.save(os.path.join(diretorio,nome_sem_ext+'.png'))
							os.remove(diretorio+'/'+i)
							
						if ".jpeg" in i:
							imagens = Image.open(diretorio+'/'+ i)
							imagens = imagens.resize((400,400))
							nome_sem_ext = os.path.splitext(i)[0]
							imagens.save(os.path.join(diretorio,nome_sem_ext+'.png'))
							os.remove(diretorio+'/'+i)

						if ".png" in i:
							imagens = Image.open(diretorio+'/'+ i)
							imagens = imagens.resize((400,400))
							nome_sem_ext = os.path.splitext(i)[0]
							imagens.save(os.path.join(diretorio,nome_sem_ext+'.png'))		
				
				def gerenciarMenusComLoops(listaDeArquivosDoClienteFormatada, nomeDoClienteComTatuagensFeitas, app):
					
					def definirQuantidadeDeArquivosNoDiretorio(listaDeArquivosDoClienteFormatada):
							return len(listaDeArquivosDoClienteFormatada)
					
					
					numeroDeArquivosNoDiretorio = definirQuantidadeDeArquivosNoDiretorio(listaDeArquivosDoClienteFormatada)
					
	
					listaInicial = []
					listaFinal = []

					if numeroDeArquivosNoDiretorio == 0 :
						criarFrameDasFotosDasTatuagens()
						#criarBotaoDeAdicaoDeNovasTatuagens()
					else:
						for i in range(numeroDeArquivosNoDiretorio):
							if i < 4:
								listaInicial.append(listaDeArquivosDoClienteFormatada[i])
							else:
								listaFinal.append(listaDeArquivosDoClienteFormatada[i])
					

					organizarFeedsDasTatuagens(listaInicial, listaFinal, nomeDoClienteComTatuagensFeitas)
			
				def organizarFeedsDasTatuagens(listaInicial, listaFinal, nomeDoClienteComTatuagensFeitas):

					self.contatorDeVezDaListaNoFeed = 0					
										
					if listaFinal != []:
						
						self.AFTER = None
						def feedDeTatuagensDoCliente():
							
							if self.contatorDeVezDaListaNoFeed % 2 == 0:
								try:
									excluirFeedDasFotosDasTatuagens()
									try:
										excluirBotaoDeAdicaoDeNovasTatuagens()
									except:
										pass
									criarFrameDasFotosDasTatuagens()
									mostrarTatuagensNoFeed(nomeDoClienteComTatuagensFeitas, listaInicial)
								except:
									criarFrameDasFotosDasTatuagens()
									mostrarTatuagensNoFeed(nomeDoClienteComTatuagensFeitas, listaInicial)
							else:

								excluirFeedDasFotosDasTatuagens()
								try:
									excluirBotaoDeAdicaoDeNovasTatuagens()
								except:
									pass
								criarFrameDasFotosDasTatuagens()
								mostrarTatuagensNoFeed(nomeDoClienteComTatuagensFeitas, listaFinal)

							self.contatorDeVezDaListaNoFeed += 1
							self.AFTER							
							self.AFTER = app.after(5000, feedDeTatuagensDoCliente)

						feedDeTatuagensDoCliente()			
						
					else:
						criarFrameDasFotosDasTatuagens()	
						mostrarTatuagensNoFeed(nomeDoClienteComTatuagensFeitas, listaInicial)
				
				def mostrarTatuagensNoFeed(nomeDoClienteComTatuagensFeitas, listaDeTatuagens):
					
					numeroDeArquivosNaLista = len(listaDeTatuagens)

					for indiceDoArquivoNaLista in range(numeroDeArquivosNaLista):
						
						if indiceDoArquivoNaLista == 0:
							gerenciarMenuComBotoesEEntryDasFotosDasTatuagens(nomeDoClienteComTatuagensFeitas, listaDeTatuagens[indiceDoArquivoNaLista] )
							#criarBotaoDeAdicaoDeNovasTatuagens()

						elif indiceDoArquivoNaLista == 1:
							gerenciarMenuComBotoesEEntryDasFotosDasTatuagens(nomeDoClienteComTatuagensFeitas, listaDeTatuagens[indiceDoArquivoNaLista])
							excluirBotaoDeAdicaoDeNovasTatuagens()
							#criarBotaoDeAdicaoDeNovasTatuagens()
						elif indiceDoArquivoNaLista == 2:
							gerenciarMenuComBotoesEEntryDasFotosDasTatuagens(nomeDoClienteComTatuagensFeitas, listaDeTatuagens[indiceDoArquivoNaLista])
							excluirBotaoDeAdicaoDeNovasTatuagens()
							#criarBotaoDeAdicaoDeNovasTatuagens()
						elif indiceDoArquivoNaLista == 3:
							gerenciarMenuComBotoesEEntryDasFotosDasTatuagens(nomeDoClienteComTatuagensFeitas, listaDeTatuagens[indiceDoArquivoNaLista])
							excluirBotaoDeAdicaoDeNovasTatuagens()

				def gerenciarMenuComBotoesEEntryDasFotosDasTatuagens(nomeDoCliente = '', nomeDaTatuagem = ''):
		
					def criarFrameQueCarregaAFoto():
						try:
							self.frameMenuFotoEEntry = Frame(self.framesDasFotosDasTatuagens, width = 10, height = 6,  bg = 'black')
							self.frameMenuFotoEEntry.pack(padx = 2, pady = 2, side = LEFT)
						except:
							pass
		
					def criarBotaoQueCarregaAFoto(nomeDoCliente, nomeDaTatuagem):
							
						imagemPadraoParaAdicao = PhotoImage(file=(f'C:/sistema_loja-main/Tatuagens/{nomeDoCliente}/{nomeDaTatuagem}'))
						imagemPadraoParaAdicao = imagemPadraoParaAdicao.zoom(4)													#
						imagemPadraoParaAdicao = imagemPadraoParaAdicao.subsample(30)	
						
						diretorio = f'C:/sistema_loja-main/Tatuagens/{nomeDoCliente}/{nomeDaTatuagem}'
						
						try:
							self.botaoMenuFoto = Button(self.frameMenuFotoEEntry,  bg = 'black', command = partial ( ampliar , diretorio))
							self.botaoMenuFoto['image'] = imagemPadraoParaAdicao
							self.botaoMenuFoto.image = imagemPadraoParaAdicao
							self.botaoMenuFoto.pack()	
						except:
							pass

						if nomeDaTatuagem  == '~~~~~.png':
							self.botaoMenuFoto['command'] = adicionarFotoAoBotao
				
					def criarEntryQueCarregaAFoto(nomeDaTatuagem, nomeDoCliente):
						
						if nomeDaTatuagem == '~~~~~.png':
							try:
								self.entryMenuFotoValorDaTatuagem = Entry(self.frameMenuFotoEEntry, width = 13 , bg = 'black', fg = 'white')
								self.entryMenuFotoValorDaTatuagem.pack(pady = 2)
							except:
								pass
							
							return None

						valorDaTatuagem = obterValorDaTatuagem(nomeDaTatuagem)
						
						if '.' in valorDaTatuagem:
							pass
						else:
							valorDaTatuagem = f'{valorDaTatuagem}.00'

						if valorDaTatuagem == '':
							try:
								self.entryMenuFotoValorDaTatuagem = Entry(self.frameMenuFotoEEntry, width = 13 , bg = 'black', fg = 'white')
								self.entryMenuFotoValorDaTatuagem.pack(pady = 2)
							except:
								pass
						else:
							try:
								self.botaoMenuFotoValorDaTatuagem = Button(self.frameMenuFotoEEntry, border = '0', text = f'{valorDaTatuagem} R$', command = partial(excluirTatuagemEValor, nomeDaTatuagem, nomeDoCliente), width = 13 , bg = 'black', fg = 'white')
								self.botaoMenuFotoValorDaTatuagem.pack(pady = 2)
							except:
								pass
					
					def adicionarFotoAoBotao():
						
						valorDaTatuagem = obterValorDaTatuagemParaAdcionarNoBancoDeDados()

						if valorDaTatuagem != '':
							diretorioDaTatuagemDoCliente = obterDiretorioDaTatuagemEnviadoPeloCliente()
						else:
							messagebox.showerror("ERRO GRAVISSIMO", "Valor não selecionado")
							return None

						diretorioDeDestino = gerarDiretorioDeDestino()
						copiarFotoParaODiretorio(diretorioDeDestino, diretorioDaTatuagemDoCliente)
						converterFotosEnviadasPorClientes(os.listdir(diretorioDeDestino), diretorioDeDestino)
						
						nomeDaTatuagem = obterNomeDaTatuagem(diretorioDaTatuagemDoCliente)
						
						self.cliente.adicionarNomeEValorDaTatuagem(nomeDaTatuagem, valorDaTatuagem )
						
						desfazerAJanelaDeTatuagens(self.app)
						mostrarTatuagensFeitasPeloCliente(nomeDoCliente, self.app)
					
					def obterDiretorioDaTatuagemEnviadoPeloCliente():
						diretorioDaTatuagemDoCliente = filedialog.askopenfilenames()
						return diretorioDaTatuagemDoCliente[0]
					
					def obterNomeDaTatuagem(diretorioDaTatuagemDoCliente):
						TAMANHO_DO_DIRETORIO = len(diretorioDaTatuagemDoCliente)
						nome_aux = []
						nomeDaTatuagem = ''
						for i in range(0,TAMANHO_DO_DIRETORIO):
							if diretorioDaTatuagemDoCliente[TAMANHO_DO_DIRETORIO - 1 - i] != '/':
								nome_aux.append(diretorioDaTatuagemDoCliente[TAMANHO_DO_DIRETORIO - 1 - i])
							else:
								break

						for i in range(len(nome_aux)):
							if nome_aux[i] == '.':

								nome_aux = nome_aux[i+1:]
								break

						for i in range(len(nome_aux)):
							nomeDaTatuagem += nome_aux.pop()		
						nomeDaTatuagem = f'{nomeDaTatuagem}.png'
						return nomeDaTatuagem

					def gerarDiretorioDeDestino():
						return  "C:/sistema_loja-main/Tatuagens/"+self.entry_nome.get()

					def copiarFotoParaODiretorio(diretorioDeDestino, diretorioDaTatuagemDoCliente):
						shutil.copy(diretorioDaTatuagemDoCliente, diretorioDeDestino)
						
					def renomearArquivo(diretorioDeDestino, nomeDaTatuagem):
						old_file = os.path.join(diretorioDeDestino, nomeDaTatuagem)
						new_file = os.path.join(diretorioDeDestino, str(len(os.listdir(diretorioDeDestino)))+'.png')
						os.rename(old_file, new_file)
						return new_file
					
					def obterValorDaTatuagemParaAdcionarNoBancoDeDados():
						return self.entryMenuFotoValorDaTatuagem.get()

					def obterValorDaTatuagem(nomeDaTatuagem):
						return self.cliente.clienteDoBancoDeDados[nomeDaTatuagem.encode()].decode()
					
					def excluirTatuagemEValor(nomeDaTatuagem, nomeDoCliente):
						chave = messagebox.askquestion(title= 'Excluir Tatuagem', message='Deseja excluir a tatuagem?')
										
						if chave == 'yes':
							del self.cliente.clienteDoBancoDeDados[nomeDaTatuagem.encode()]
							os.remove(f'C:/sistema_loja-main/Tatuagens/{nomeDoCliente}/{nomeDaTatuagem}')
							desfazerAJanelaDeTatuagens(self.app)
							mostrarTatuagensFeitasPeloCliente(nomeDoCliente, self.app)
						else:
							pass
					
					criarFrameQueCarregaAFoto()
					criarBotaoQueCarregaAFoto(nomeDoCliente, nomeDaTatuagem)
					criarEntryQueCarregaAFoto(nomeDaTatuagem, nomeDoCliente)
				
				def ampliar(diretorio):
					imagem = cv2.imread(diretorio)
					cv2.imshow("Original", imagem) 
					cv2.waitKey(0)
					
				gerenciarJanelaTatuagens(nome, app)
			
			def excluirHistoricoDeInvestimento(): #TODO - VERIFICAR SE AINDA É UTIL
				try:
					self.frameMenuFotoEEntry.destroy()
				except:
					pass
				try:
					self.botaoMenuFoto.destroy()
				except:
					pass
				try:
					self.entryMenuFotoValorDaTatuagem.destroy()
				except:
					pass
				try:
					self.framesDasFotosDasTatuagens.destroy()	
				except:
					pass
				try:
					self.framesMenuTatuagensDoHistoricoDeInvestimento.destroy()
				except:
					pass
			
			def excluirBotaoDeAdicaoDeNovasTatuagens():
					try:
						self.frameMenuQueAdicionaAFoto.destroy()
					except:
						pass
					try:
						self.botaoQueAdicionaAFoto.destroy()
					except:
						pass

			def excluirFeedDasFotosDasTatuagens():

				try:
					self.framesDasFotosDasTatuagens.destroy()
				except:
					pass

			def desfazerAJanelaDeTatuagens(app):
				try:
					app.after_cancel(self.AFTER)
				except:
					pass 

				excluirFeedDasFotosDasTatuagens()
				excluirBotaoDeAdicaoDeNovasTatuagens()

				self.botaoMostarTatuagens['command'] = partial(mostrarTatuagensFeitasPeloCliente, self.nome_tatuagem, app)
				self.botaoMostarTatuagens['width'] = 27
				self.botaoMostarTatuagens['height'] = 1
				self.botaoMostarTatuagens['text'] = f'TATUAGENS'
				self.botaoMostarTatuagens['border'] = '2'
				self.botaoMostarTatuagens['font'] = ('Franklin Gothic Medium', 11)

			feedDoHistoricoDeTatuagensFeitasPeloCliente(nome, app)	

		criarFramesDoFormularios(app)		 

	def carregarListaDeClientes(self, ladoDireito, ordem):
		
		def gerenciarListaDeClientes(ladoDireito, ordem):
			try:
				excluirScrollbars(ladoDireito)	
			except:			
				criarScrollbarsParaExibirOsClientes(ladoDireito)
				exibirListaDeClienteOrdemDeEntrada(ladoDireito, ordem)
			
			exibirNumeroDeClientesNoRadaPeDoScrollbars()	
		
		def criarScrollbarsParaExibirOsClientes(ladoDireito):
			#frame super especial
			self.frameParaOScrollbars = Frame(ladoDireito)
			self.frameParaOScrollbars.pack(pady = 20)	

			self.my_canvas = Canvas(self.frameParaOScrollbars, bg = 'black', height = 600)
			self.my_canvas.pack(side= LEFT, fill = BOTH)

			self.my_scrollsbars = Scrollbar(self.frameParaOScrollbars, orient = VERTICAL, command = self.my_canvas.yview)
			self.my_scrollsbars.pack(side = LEFT, fill= Y)

			self.my_canvas.configure( yscrollcommand = self.my_scrollsbars.set, bg = 'black')
			self.my_canvas.bind('<Configure>', lambda e: self.my_canvas.configure(scrollregion = self.my_canvas.bbox("all") ))

			self.frame_scrollbar = Frame(self.my_canvas)
			self.my_canvas.create_window((0,0), window=self.frame_scrollbar, anchor = "nw")
		 
			self.frame_auxiliar_scrollbar = Frame(self.frame_scrollbar)
			self.frame_auxiliar_scrollbar.pack()

		def exibirListaDeClienteOrdemDeEntrada(ladoDireito, ordem):
			def criarListaEmOrdemAlfabetica():
				alfabeto = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
				listaEmOrdemAlfabetica = []
				listaDeClientes =  list(dbclientes.clientes.keys())
				for letra in alfabeto:
					for cliente in listaDeClientes:	
						nomeDoCliente = cliente.decode()
						if nomeDoCliente == '':
							pass
						else:
							primeiraLetraDoNoNome = nomeDoCliente[0]
							if letra == primeiraLetraDoNoNome:
								listaEmOrdemAlfabetica.append(nomeDoCliente)
				
				return listaEmOrdemAlfabetica
			
			def inverterLista(lista):
				listaInvertida = []
				for i in range(len(lista)):
					nomeDoCliente = lista.pop()
					listaInvertida.append(nomeDoCliente)
				return listaInvertida

			if ordem == 'Ordem alfabetica crescente':

				listaEmOrdemAlfabetica = criarListaEmOrdemAlfabetica()
				excluirScrollbarsParaRearranjo(ladoDireito)
				for cliente in listaEmOrdemAlfabetica:
					self.but_cliente = Button(self.frame_scrollbar, text = cliente, command = partial(inserirDadosDoClienteAoClicarNoBotaoDoScrolBars, cliente),  height = 2, width = 45,  activebackground = "#353839", activeforeground = 'white', bg = 'black', fg = 'white', font = ('Franklin Gothic Medium', 12))
					self.but_cliente.pack()
	
			elif ordem == 'Ordem alfabetica decrescente':
				listaEmOrdemAlfabetica = criarListaEmOrdemAlfabetica()
				listaEmOrdemAlfabeticaDescrescente = inverterLista(listaEmOrdemAlfabetica)
				excluirScrollbarsParaRearranjo(ladoDireito)
				for cliente in listaEmOrdemAlfabeticaDescrescente:
					self.but_cliente = Button(self.frame_scrollbar, text = cliente, command = partial(inserirDadosDoClienteAoClicarNoBotaoDoScrolBars, cliente),  height = 2, width = 45,  activebackground = "#353839", activeforeground = 'white', bg = 'black', fg = 'white', font = ('Franklin Gothic Medium', 12))
					self.but_cliente.pack()				

			elif ordem == 'Primeiros clientes':

				listaDeClientes =  list(dbclientes.clientes.keys())
				excluirScrollbarsParaRearranjo(ladoDireito)
				for cliente in listaDeClientes:
					self.but_cliente = Button(self.frame_scrollbar, text = cliente, command = partial(inserirDadosDoClienteAoClicarNoBotaoDoScrolBars, cliente.decode()),  height = 2, width = 45,  activebackground = "#353839", activeforeground = 'white', bg = 'black', fg = 'white', font = ('Franklin Gothic Medium', 12))
					self.but_cliente.pack()	

			elif ordem == 'Ultimo clientes':
				listaDeClientes =  list(dbclientes.clientes.keys())
				listaDeClientesInvertida = inverterLista(listaDeClientes)
				excluirScrollbarsParaRearranjo(ladoDireito)
				for cliente in listaDeClientesInvertida:
					self.but_cliente = Button(self.frame_scrollbar, text = cliente, command = partial(inserirDadosDoClienteAoClicarNoBotaoDoScrolBars, cliente.decode()),  height = 2, width = 45,  activebackground = "#353839", activeforeground = 'white', bg = 'black', fg = 'white', font = ('Franklin Gothic Medium', 12))
					self.but_cliente.pack()	

			else:
				clientesCadastrados = dbclientes.clientes.keys()	
				for cliente in clientesCadastrados:
					self.but_cliente = Button(self.frame_scrollbar, text = cliente.decode(), command = partial(inserirDadosDoClienteAoClicarNoBotaoDoScrolBars, cliente.decode()),  height = 2, width = 45,  activebackground = "#353839", activeforeground = 'white', bg = 'black', fg = 'white', font = ('Franklin Gothic Medium', 12))
					self.but_cliente.pack()

		def inserirDadosDoClienteAoClicarNoBotaoDoScrolBars(nome):
			self.nome_tatuagem = nome
			self.entry_nome.delete(0,END)
			self.entry_nome.insert(END, nome)	
			self.tratarDadosParaExibirNasCaixasDeTexto(nome)		
		
		def excluirScrollbars(ladoDireito):
			self.my_canvas.destroy()
			self.my_scrollsbars.destroy()
			self.frameParaOScrollbars.destroy()
			destruirNumeroDeClientesNoRadaPeDoScrollbars()
			criarScrollbarsParaExibirOsClientes(ladoDireito)
			exibirListaDeClienteOrdemDeEntrada(ladoDireito, ordem)

		def excluirScrollbarsParaRearranjo(ladoDireito):
			self.my_canvas.destroy()
			self.my_scrollsbars.destroy()
			self.frameParaOScrollbars.destroy()
			destruirNumeroDeClientesNoRadaPeDoScrollbars()
			criarScrollbarsParaExibirOsClientes(ladoDireito)
			#exibirListaDeClienteOrdemDeEntrada(ladoDireito, ordem)

		def exibirNumeroDeClientesNoRadaPeDoScrollbars():	
			clientesCadastrados = dbclientes.clientes.keys()
			self.numeroDeClientesCadastrado = Label(self.rodaPeDoScrollbarParaMostrarONumeroDeCliente, text = f'{len(clientesCadastrados)} clientes',  height = 2, width = 55	,  justify = 'left', anchor = 'w', bg = 'black', fg = 'gray', font = ('Franklin Gothic Medium', 10) )
			self.numeroDeClientesCadastrado.pack()

		def destruirNumeroDeClientesNoRadaPeDoScrollbars():
			self.numeroDeClientesCadastrado.destroy()

		gerenciarListaDeClientes(ladoDireito, ordem)		

	def tratarDadosParaExibirNasCaixasDeTexto(self, nome):
		def gerenciarTratamentoDeDados(nome):
			verificarSeOClienteTemFoto(nome)
			exibirDadosNaCaixaDeEntrada(nome)
			
		def verificarSeOClienteTemFoto(nome):
			if nome+".gif" in os.listdir("C:/sistema_loja-main/imagens_clientes"):
				self.logo2 = PhotoImage(file=("C:/sistema_loja-main/imagens_clientes/"+nome+".gif"))
				self.add_users['image'] = self.logo2
				self.add_users.image = self.logo2
			else:
				self.logo2 = PhotoImage(file=("C:/sistema_loja-main/imagens_clientes/seg_2.gif"))
				self.add_users['image'] = self.logo2
				self.add_users.image = self.logo2
			
		def exibirDadosNaCaixaDeEntrada(nome):	
			nomeDoCliente  = dbclientes.clientes[nome].decode() #¬ | ! £ ¢ § 
			aux = ''
			telefone = ''
			data_de_nascimento=''
			email=''
			endereco = ''
			data=''
			hora=''
			comentarios =''

			for caracter in nomeDoCliente:
					
				if caracter == '¹' and telefone == '':
					if aux == '':
						telefone = ('021')
					else:	
						telefone = aux
					self.entry_tel.delete(0,END)
					self.entry_tel.insert(END, telefone)
					aux = ''
					
				elif caracter == '¹' and data_de_nascimento == '':
					if aux == '':
						data_de_nascimento = ('00/00/0000')
					else:	
						data_de_nascimento = aux
					self.entry_nascimento.delete(0,END)
					self.entry_nascimento.insert(END, data_de_nascimento)
					aux = ''

				elif caracter == '¹' and email == '':
						
					if aux == '':
						email = "Vazio"
					else:	
						email = aux

					self.entry_email.delete(0,END)
					self.entry_email.insert(END, email)
					aux = ''
					
				elif caracter == '¹' and endereco == '':
					if aux == '':
						endereco = "Rio de Janeiro - RJ"
					else:	
						endereco = aux

					self.entry_end.delete(0,END)
					self.entry_end.insert(END, endereco)
					aux = ''
					
				elif caracter == '¹' and data == '':
					if aux == '':
						data = ('00/00/0000')
					else:	
						data = aux
					self.entry_age_data.delete(0,END)
					self.entry_age_data.insert(END, data)

					aux = ''

				elif caracter == '¹' and hora == '':
						
					if aux == '':
						hora = ('00:00')
					else:	
						hora = aux

					self.entry_age_hora.delete(0,END)
					self.entry_age_hora.insert(END, hora)	
					aux = ''

				elif caracter == '¹' and comentarios == '':
					if aux == '':
						comentarios = ('Vazio')
					else:	
						comentarios = aux

					self.entry_comentarios.delete(0,END)
					self.entry_comentarios.insert(END, comentarios)
					aux = ''
					
				elif caracter == '²':
					break;
				else:
					aux += caracter

		gerenciarTratamentoDeDados(nome)
	
