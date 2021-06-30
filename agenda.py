from tkinter import*
import tkinter as tk
from PIL import Image
import dbclientes
from functools import partial
from datetime import datetime
import time
import cliente
import main_menu
import janeladetalhadaagenda
import janelaAniversariantesDoMes

class agenda(object):
	def __init__(self, i,feed_rodape, footer, menu, feed, left_main, right_main, datahora, aux_right_main, aux_left_main):

		self.i = i
		self.menu = menu
		self.footer = footer
		self.feed_ = feed
		self.feed_rodape = feed_rodape 
		self.left_main = left_main #vai ser excluidos 
		self.right_main = right_main # vao ser excluidos
		self.datahora = datahora
		self.aux_right_main = aux_right_main
		self.aux_left_main = aux_left_main
		
		#---- Metodos ------#
		self.coletarDataEHora()	##CRIA OS PARAMETROS DE DATA E HORA
		self.criarPrincipaisFramesDaJanelaAgenda()
		self.gerenciarBotoesDaJanelaAgenda(footer)
		self.gerenciarLabelsDaJanelaAgenda()

		
		self.detalhar_mes() ## ESSA FUNÇÃO SÓ CRIA BOTÕES RELATORIOS
		self.news()			##AQUI MOSTRA O MURAL DE INFORMAÇÃO E DEFINE OS ANIVERSARIANTES DE HOJE
		self.criarCalendarioNaJanelaAgenda()
	def coletarDataEHora(self):
		now = datetime.now()
		self.hora = now.strftime('%H')
		self.dia = now.strftime('%d')
		self.mes = now.strftime('%m')
		self.ano = now.strftime('%Y')
		self.dataDeHoje = now.strftime('%d/%m/%Y')

	def criarPrincipaisFramesDaJanelaAgenda(self):

		self.frame_aux_dias_calendario = Frame(self.aux_left_main, bg = 'black')
		self.frame_aux_dias_calendario.pack(side = BOTTOM, pady = 20)

		self.frame_label_news_tatuagens_hoje_header = Frame(self.aux_right_main, bg = 'black')
		self.frame_label_news_tatuagens_hoje_header.pack(pady = 20)
		
		self.frame_label_news_niver_hoje_header = Frame(self.aux_right_main, bg = 'black')
		self.frame_label_news_niver_hoje_header.pack(pady = 20)

		#criar Labels dos clientes para melhor apresentação
		
		self.frame_label_news_agendados_hoje_header = Frame(self.aux_right_main, bg = 'black')
		self.frame_label_news_agendados_hoje_header.pack(pady = 20)

	def gerenciarBotoesDaJanelaAgenda(self, footer):
		def criarBotoesDaJanelaAgenda(footer):

			self.but_back = Button(footer, text = 'Voltar', command = voltarMenuPrincipal, pady = 10, width = 30,  activebackground = "#353839", activeforeground = 'white', bg = 'black', fg = 'white', font = ('Franklin Gothic Medium', 10))
			self.but_back.pack(pady =20)
		
		def voltarMenuPrincipal(): ####### BOTÃO VOLTAR ##############
			self.menu.place(x =0, y = 0 , width = 850, height = 500)
			self.feed_.place(x =0, y = 0 , width = 490, height = 500) #####
			self.feed_rodape.pack()
			self.label_news_niver_hoje.destroy()
			self.frame_botoes_calendiarios.destroy()
			self.but_back.destroy()
			self.aux_left_main.destroy()
			self.aux_right_main.destroy()

		criarBotoesDaJanelaAgenda(footer)

	def gerenciarLabelsDaJanelaAgenda(self):
		self.label_news_tatuagens_hoje_header = Label(self.frame_label_news_tatuagens_hoje_header,text = 'CLIENTE PARA HOJE', bg = 'black' , fg = 'white', font = ('Franklin Gothic Medium', 20))
		self.label_news_tatuagens_hoje_header.pack(pady = 5)
		
		self.label_news_tatuagens_hoje = Label(self.frame_label_news_tatuagens_hoje_header, text = 'Hoje não há clientes marcados', bg = 'black' , fg = 'white', font = ('Franklin Gothic Medium', 12))
		self.label_news_tatuagens_hoje.pack(pady = 2)

		self.label_news_agendados_hoje_header = Label(self.frame_label_news_agendados_hoje_header, text = 'CLIENTES AGENDADOS', bg = 'black' , fg = 'white', font = ('Franklin Gothic Medium', 20))
		self.label_news_agendados_hoje_header.pack(pady = 5)

	def criarCalendarioNaJanelaAgenda(self):	

		def gerenciarCalendario():
			carregarCalendarioComOsDiasComClientesVerde()

		def carregarCalendarioComOsDiasComClientesVerde():
			
			def gerenciarDatasECalendario():
				mesEAnoFormatado = formatarDataParaPesquisarSeHaClienteMarcado()
				criarBotoesDoCalendario(mesEAnoFormatado)
			
			def formatarDataParaPesquisarSeHaClienteMarcado():
				
				if verificarSeOMesEhDe31Dias():
					self.len_mes = 31
					datando = self.mes+"/"+self.ano

				elif verificarSeOMesEhDe30Dias():
					self.len_mes =30
					datando = self.mes+"/"+self.ano
				else:
					self.len_mes = 28
					datando = self.mes+"/"+self.ano	
				return datando
			
			def criarBotoesDoCalendario(mesEAnoFormatado):	
				aniversariantes = {}
				for j in range(self.len_mes):
					if j%7==0:
						self.frame_botoes_calendiarios = Frame(self.frame_aux_dias_calendario, bg ='black') 	
						self.frame_botoes_calendiarios.pack(pady=1,padx=1)

					dataFormatada = formatarDataParaCalendario(j+1, mesEAnoFormatado)		
					
					valor = carregarDadosDoCalendario(dataFormatada, aniversariantes)
				
					if valor == None:
						self.botoes_dia = Button(self.frame_botoes_calendiarios, text ="Dia "+str(j+1),command = partial(self.detalhar_dia, j+1) , width = 15, height = 2, activebackground = "#353839", activeforeground = 'white',bg = 'black', fg = 'white', font = ('Franklin Gothic Medium', 10) )
						self.botoes_dia.pack(side = LEFT)
					else:

						self.botoes_dia = Button(self.frame_botoes_calendiarios, text ="Dia "+str(j+1),command = partial(self.detalhar_dia, j+1) , width = 15, height = 2, activebackground = "#353839", activeforeground = 'white',bg = 'black', fg = valor, font = ('Franklin Gothic Medium', 10) )
						self.botoes_dia.pack(side = LEFT)
				
				mostrarAniversariantes(aniversariantes)

			def formatarDataParaCalendario(dia, mesEAnoFormatado):
				if dia <= 9:
					aux_datando = str(0)+str(dia)+"/"+mesEAnoFormatado
				else:
					aux_datando =str(dia)+"/"+mesEAnoFormatado
				return aux_datando				

			def verificarSeOMesEhDe31Dias():
				return self.mes == '01' or self.mes == '03' or self.mes == '05' or self.mes == '07' or self.mes == '08' or self.mes == '10' or self.mes == '11'

			def verificarSeOMesEhDe30Dias():
				return self.mes == '04' or self.mes == '09' or self.mes == '06' or self.mes == '11'
			
			gerenciarDatasECalendario()
			
		def mostrarAniversariantes(aniversariantes):
				
			def criarBotoesDosAniversariantes():
				self.botao_news_niver_hoje_header = Button(self.frame_label_news_niver_hoje_header, command = partial(mostrarJanelaComAniversarariantes, aniversariantes), text = 'ANIVERSARIANTES DO MÊS', bg = 'black' , fg = 'white', font = ('Franklin Gothic Medium', 20), border = '0')
				self.botao_news_niver_hoje_header.pack(pady = 5)

				self.label_news_niver_hoje = Label(self.frame_label_news_niver_hoje_header, text = 'Hoje não há aniversariantes', bg = 'black' , fg = 'white', font = ('Franklin Gothic Medium', 12))
				self.label_news_niver_hoje.pack(pady = 2)					

			def mostrarJanelaComAniversarariantes(aniversariantes):
				janelaAniversariantesDoMes.abrirJanelaDosAniversariantesDoMes(aniversariantes)
				
			def mostrarAniversariantes(aniversariantes, listaDeAniversariantes):
					
				if self.contatorDeAniversariantesDoMes == len(listaDeAniversariantes):
					self.contatorDeAniversariantesDoMes = -1
				else:
					nomeDoAniversariante = listaDeAniversariantes[self.contatorDeAniversariantesDoMes]
					dataDeAniversario = aniversariantes[nomeDoAniversariante]
					idadeQueEleEstaCompletando = int(self.ano) - int(dataDeAniversario[6::])
					self.label_news_niver_hoje['text'] = f'{dataDeAniversario[0:5:]}/2021\n Nome: {nomeDoAniversariante}, {idadeQueEleEstaCompletando} anos'
				
			criarBotoesDosAniversariantes()

			listaDeAniversariantes = list(aniversariantes)
			self.contatorDeAniversariantesDoMes = 0
				
			def feedDeAniversariantesDoMes():
				mostrarAniversariantes(aniversariantes, listaDeAniversariantes)
				self.contatorDeAniversariantesDoMes += 1
				self.i.after(2000, feedDeAniversariantesDoMes)
			
			feedDeAniversariantesDoMes()	
		
		def carregarDadosDoCalendario(data, aniversariantes):
			self.cont_niver = 0
			
			listaDeClientes  = dbclientes.clientes 
		
			for cliente in listaDeClientes:
				dadosDosClientesBruto = dbclientes.clientes[cliente.decode()].decode()
				aux = ''
				telefone = ''
				data_de_nascimento=''
				email=''
				endereco = ''
				data_aux=''
				hora_aux=''
				comentarios =''

				for caracter in dadosDosClientesBruto:
					if caracter == '¹' and telefone == '':
						if aux == '':
							telefone = ('021')
						else:	
							telefone = aux
						aux = ''
						
					elif caracter == '¹' and data_de_nascimento == '':
						if aux == '':
							data_de_nascimento = ('00/00/0000')
						else:	
							data_de_nascimento = aux

						aux = ''

					elif caracter == '¹' and email == '':
						if aux == '':
							email = "Vazio"
						else:	
							email = aux
						aux = ''
						
					elif caracter == '¹' and endereco == '':
						if aux == '':
							endereco = "Rio de Janeiro - RJ"
						else:	
							endereco = aux
						aux = ''
						
					elif caracter == '¹' and data_aux == '':
						if aux == '':
							data_aux = ('00/00/0000')
						else:	
							data_aux = aux
						aux = ''

					elif caracter == '¹' and hora_aux == '':
						if aux == '':
							hora_aux = ('00:00')
						else:	
							hora_aux = aux	
						aux = ''

					elif caracter == '¹' and comentarios == '':
						if aux == '':
							comentarios = ('Vazio')
						else:	
							comentarios = aux
						aux = ''
					elif caracter == '²':
						break;
					else:
						aux += caracter

				data_de_nascimento_aux = data_de_nascimento[0:5:]
				mesDeNascimento = data_de_nascimento[3:5:]

				if self.mes == mesDeNascimento:
					aniversariantes[cliente.decode()] = f'{data_de_nascimento}'

				if data_aux == data:
					fg = "green"
					return fg
				
		gerenciarCalendario()

	def carregar_calendario(self, data):  # FUNÇÃO CHAMADA PRA O CARREGAR DIA -- PARA OS PARAMETROS DIARIOS ## AQUI MOSTRA OS CLIENTES HOJE

		listaDeClientes  = dbclientes.clientes 
		for cliente in listaDeClientes:
			dadosDosClientesBruto = dbclientes.clientes[cliente.decode()].decode()
			
			aux = ''
			telefone = ''
			data_de_nascimento=''
			email=''
			endereco = ''
			data_aux=''
			hora_aux=''
			comentarios =''

			for caracter in dadosDosClientesBruto:
				if caracter == '¹' and telefone == '':
					if aux == '':
						telefone = ('021')
					else:	
						telefone = aux
					aux = ''
					
				elif caracter == '¹' and data_de_nascimento == '':
					if aux == '':
						data_de_nascimento = ('00/00/0000')
					else:	
						data_de_nascimento = aux

					aux = ''

				elif caracter == '¹' and email == '':
					if aux == '':
						email = "Vazio"
					else:	
						email = aux
					aux = ''
					
				elif caracter == '¹' and endereco == '':
					if aux == '':
						endereco = "Rio de Janeiro - RJ"
					else:	
						endereco = aux
					aux = ''
					
				elif caracter == '¹' and data_aux == '':
					if aux == '':
						data_aux = ('00/00/0000')
					else:	
						data_aux = aux
					aux = ''

				elif caracter == '¹' and hora_aux == '':
					if aux == '':
						hora_aux = ('00:00')
					else:	
						hora_aux = aux	
					aux = ''

				elif caracter == '¹' and comentarios == '':
					if aux == '':
						comentarios = ('Vazio')
					else:	
						comentarios = aux
					aux = ''
				elif caracter == '²':
					break;
				else:
					aux += caracter

			if data_aux == data: 
				self.label_expansao_data(cliente.decode(), data_aux, hora_aux)
				
	def detalhar_dia(self, dia):
		
		self.cont_exp_data = 0
		
		if int(dia) > 9:
			data = str(dia)+'/'+self.mes+'/'+self.ano
			self.carregar_calendario(data)
		else:
			data = '0'+str(dia)+'/'+self.mes+'/'+self.ano
			self.carregar_calendario(data)
	
	def label_expansao_data(self, nome, data, hora): ##aqui esta definido os aniversariantes de hoje. FUNCIONANDO PERFEITAMENTE.		
		
		if data == self.dataDeHoje:
			
			if self.cont_exp_data == 0:
				self.cont_exp_data =+ 1
				self.label_news_tatuagens_hoje['text'] = "Nome: "+nome+", Hora: "+hora 	
			
			elif(self.cont_exp_data == 1 or self.cont_exp_data == 2 or self.cont_exp_data == 3):
				self.label_news_tatuagens_hoje['text'] += "\n"+ "Nome: "+nome+", Hora: "+hora 	#Label(self.aux_right_main, text = "Nome: "+nome+", Hora: "+hora, bg = 'black' , fg = 'white', font = ('Franklin Gothic Medium', 25))
				self.label_news_tatuagens_hoje.pack(pady = 10)
			else:
				self.label_news_tatuagens_hoje['text'] += 'E mais.'

		else:
			try:
				if self.cont_exp_data == 0:
					self.cont_exp_data =+ 1
					##print(self.cont_exp_data)
					self.label_agendados.destroy()                      
					self.label_agendados = Label(self.frame_label_news_agendados_hoje_header, text = "Nome: "+nome+", Hora: "+hora, bg = 'black' , fg = 'white', font = ('Franklin Gothic Medium', 12))
					self.label_agendados.pack(pady = 2)
				elif(self.cont_exp_data == 1 or self.cont_exp_data ==2 or self.cont_exp_data == 3):
					self.label_agendados['text'] += "\n"+ "Nome: "+nome+", Hora: "+hora 	#Label(self.aux_right_main, text = "Nome: "+nome+", Hora: "+hora, bg = 'black' , fg = 'white', font = ('Franklin Gothic Medium', 25))
					#self.label_agendados.pack(pady = 10)
				else:
					self.label_agendados['text'] += 'E mais.'


			except:
				self.label_agendados = Label(self.frame_label_news_agendados_hoje_header, text = "Nome: "+nome+", Hora: "+hora, bg = 'black' , fg = 'white', font = ('Franklin Gothic Medium', 12))
				self.label_agendados.pack(pady = 10)

	def detalhar_mes(self): ## ESSA FUNÇÃO SÓ CRIA BOTÕES RELATORIOS

		self.frame_detalhar_dia = Frame(self.aux_left_main, bg = 'black')
		self.frame_detalhar_dia.pack(side=TOP, pady = 50)
		
		self.botao_detalhar_dia = Button(self.frame_detalhar_dia, text = "Relatório Completo", command = self.janela_detalhada,  activebackground = "#353839", activeforeground = 'white', bg = 'black', fg = 'white', font = ('Franklin Gothic Medium', 20))
		self.botao_detalhar_dia.pack(side = LEFT)

		self.botao_detalhar_mes = Button(self.frame_detalhar_dia, text = "Relatório Mensal", command = self.janela_detalhada_mes,  activebackground = "#353839", activeforeground = 'white', bg = 'black', fg = 'white', font = ('Franklin Gothic Medium', 20))
		self.botao_detalhar_mes.pack(padx = 5)

	def janela_detalhada(self): ##MOSTRA TODOS OS CLIENTE JÁ INSERIDOS

		janeladetalhadaagenda.abrir_janela_detalhada_cl()
		pass
		
	def janela_detalhada_mes(self): ##MOSTRA SOMENTE OS CLIENTES DO MES 
		dia = self.dia

		data = str(dia)+'/'+self.mes+'/'+self.ano

		janeladetalhadaagenda.abrir_janela_detalhada_cl_mes(data)

	def news(self):
		self.detalhar_dia(self.dia)
		
		