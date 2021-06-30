from tkinter import*
import tkinter as tk
from functools import partial
from datetime import datetime
import time
import main_menu
import dbmfinancas
import janeladetalhadafinancas
'''
Controlará as finanças da empresa:
- Mostrará quanto deve (Fixo e os variaveis).
- Mostrará os gastos individuais.
- Arrecadação Mensal/semanal/diaria.
'''
'''
Projeção do programa inteligente:
O ganho por hora/trabalho.
O programa irá projetar a arrecadação e os gastos, ou seja, a projeção de lucro.

#Quanto maior o numero de dados e variedade de dados. Maior e melhor será as projeções.
'''
class financas(object):
	def __init__(self, i,feed_rodape, footer, menu, feed, left_main, right_main, datahora, aux_right_main, aux_left_main):
############################ INSTANCIAS ############################################
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
		self.datando()
		self.datando_3()
		self.detalhar_mes()
		self.calendario()
		self.menu_entradasaida()
		self.carregar_dados()

#		#                               ##### BOTÃO VOLTAR #####
		self.but_back = Button(self.footer, text = 'Voltar', command = self.voltar_menu, pady = 10, width = 30,  activebackground = "#353839", activeforeground = 'white', bg = 'black', fg = 'white', font = ('Franklin Gothic Medium', 10))
		self.but_back.pack(pady =20)

	def datando(self):
		now = datetime.now()
		self.datahora['text'] = '  -  '+ now.strftime('%H:%M:%S') + '  -  ' + now.strftime('%d/%m/%Y')
		self.hora = now.strftime('%H')
		self.dia = now.strftime('%d')
		self.mes = now.strftime('%m')
		self.ano = now.strftime('%Y')
		self.data_hoje = now.strftime('%d/%m/%Y')
		self.i.after(1000, self.datando)

	def calendario(self):
		a = dbmfinancas.financas.keys()
		datando = ''
		aux_datando = ''
		valor = 0
		
		self.frame_aux_dias_calendario = Frame(self.aux_left_main, bg = 'black')
		self.frame_aux_dias_calendario.pack(side = BOTTOM, pady = 20)

		if (self.mes == '01' or self.mes == '03' or self.mes == '05' or self.mes == '07' or self.mes == '08' or self.mes == '10' or self.mes == '11'): 
			self.len_mes = 31
			datando = self.mes+"/"+self.ano
		elif (self.mes == '04' or self.mes == '09' or self.mes == '06' or self.mes == '11'):
			self.len_mes =30
			datando = self.mes+"/"+self.ano 
		else:
			self.len_mes = 28	
			datando = self.mes+"/"+self.ano
		
		for j in range(self.len_mes):
			if j%7==0:
				self.frame_botoes_calendiarios = Frame(self.aux_left_main, bg ='black') 	
				self.frame_botoes_calendiarios.pack(pady=1,padx=1)
			
			if j+1 <= 9:
				aux_datando = str(0)+str(j+1)+"/"+datando

			else:
				aux_datando =str(j+1)+"/"+datando
			
			##print(aux_datando)
			##print("Condição calendario")
			##print(len(a))
			##print(j)
			#if len(a)<=j:#linha de codigo retirada pois o len pode ser maior que J impedindo que alguns valores entre	
			if aux_datando.encode() in a:
				valor = self.saldo(aux_datando.encode())
			##print("valor --------", valor)
			
			
			if valor > 0:		
				self.botoes_dia = Button(self.frame_botoes_calendiarios, text = 'Dia '+str(j+1)+'\nSaldo: '+str(valor)+' R$'  , command = partial(self.detalhar_dia, j+1) , width = 15, height = 2, activebackground = "#353839", activeforeground = 'white',bg = 'black', fg = 'green', font = ('Franklin Gothic Medium', 10) )
				self.botoes_dia.pack(side = LEFT)
				valor = 0
			elif valor == 0:		
				self.botoes_dia = Button(self.frame_botoes_calendiarios, text = 'Dia '+str(j+1)+'\nSaldo: '+str(valor)+' R$'  , command = partial(self.detalhar_dia, j+1) , width = 15, height = 2, activebackground = "#353839", activeforeground = 'white',bg = 'black', fg = 'white', font = ('Franklin Gothic Medium', 10) )
				self.botoes_dia.pack(side = LEFT)
			else:		
				self.botoes_dia = Button(self.frame_botoes_calendiarios, text = 'Dia '+str(j+1)+'\nSaldo: '+str(valor)+' R$'  , command = partial(self.detalhar_dia, j+1) , width = 15, height = 2, activebackground = "#353839", activeforeground = 'white',bg = 'black', fg = 'red', font = ('Franklin Gothic Medium', 10) )
				self.botoes_dia.pack(side = LEFT)
				valor = 0 
					
	def detalhar_mes(self):
		self.frame_detalhar_dia = Frame(self.aux_left_main, bg = 'black')
		self.frame_detalhar_dia.pack(side=TOP, pady = 50)
		self.botao_detalhar_finan = Button(self.frame_detalhar_dia, text = "Relatório Completo", command = self.janela_detalhada,  activebackground = "#353839", activeforeground = 'white', bg = 'black', fg = 'white', font = ('Franklin Gothic Medium', 20))
		self.botao_detalhar_finan.pack(side= LEFT)
		self.botao_detalhar_mes = Button(self.frame_detalhar_dia, text = "Relatório Mensal", command = self.janela_detalhada_mes,  activebackground = "#353839", activeforeground = 'white', bg = 'black', fg = 'white', font = ('Franklin Gothic Medium', 20))
		self.botao_detalhar_mes.pack(padx = 5, side = LEFT)

	def detalhar_dia(self, dia): # - Formata a data e a hora - #
		#------ Responsavel por receber o dia e botar no formato da data tradicional ------#
		'''
		Aqui ele pega o dia e bota ele no formato de data tradicional para ser comparado com os clientes agendados.
		o if verifica se o numero tem uma ou duas casas decimais, se houver uma, ele acrescenta o 0.
		self.detalhar_dia chama self.carregar_calendario -> self.carregar_calendario chama self.label_expansao_feed. 
		'''
		if int(dia) > 9: # Se for maior que 9, formata e envia para a função self.carregar_calendario 
			data = str(dia)+'/'+self.mes+'/'+self.ano
			#self.carregar_calendario(data, dia)
		else:			 # Se não, ele acrescenta o 0 na frente para que fique com duas casas decimais, formata e envia para self.carregar_calendario
			data = '0'+str(dia)+'/'+self.mes+'/'+self.ano
			#self.carregar_calendario(data, dia)

		#data = '0'+str(dia)+'/'+self.mes+'/'+self.ano
		#self.carregar_calendario(data, dia)
		#----------------------------------------------------------------------------------#	
		janeladetalhadafinancas.abrir_janela_detalhada_fc_diaria(data)
	
	def janela_detalhada(self):
		janeladetalhadafinancas.abrir_janela_detalhada_fc()

	def janela_detalhada_mes(self):
		#------ Responsavel por receber o dia e botar no formato da data tradicional ------#
		'''
		Aqui ele pega o dia e bota ele no formato de data tradicional para ser comparado com os clientes agendados.
		o if verifica se o numero tem uma ou duas casas decimais, se houver uma, ele acrescenta o 0.
		self.detalhar_dia chama self.carregar_calendario -> self.carregar_calendario chama self.label_expansao_feed. 
		'''
		dia = self.dia
		#print("Verificando o dia", dia)
		#print("Verificando o dia", dia)
		#print("Verificando o dia", dia)
		#print("Verificando o dia", dia)
		if len(dia) == 1:
			if int(dia) > 9 : # Se for maior que 9, formata e envia para a função self.carregar_calendario 
				data = str(dia)+'/'+self.mes+'/'+self.ano
				#self.carregar_calendario(data, dia)
			else:			 # Se não, ele acrescenta o 0 na frente para que fique com duas casas decimais, formata e envia para self.carregar_calendario
				data = '0'+str(dia)+'/'+self.mes+'/'+self.ano
				#self.carregar_calendario(data, dia)
		elif len(dia) ==2:
			data = str(dia)+'/'+self.mes+'/'+self.ano
		else:
			#print("ERRADO")
			pass

		#data = '0'+str(dia)+'/'+self.mes+'/'+self.ano
		#self.carregar_calendario(data, dia)
		#print(data)
		janeladetalhadafinancas.abrir_janela_detalhada_fc_mensal(data)
		
	def datando_3(self):
		now = datetime.now()
		#self.datahora['text'] = '  -  '+ now.strftime('%H:%M:%S') + '  -  ' + now.strftime('%d/%m/%Y')
		self.hora = now.strftime('%H')
		self.dia = now.strftime('%d')
		self.mes = now.strftime('%m')
		self.ano = now.strftime('%Y')

		self.i.after(1000, self.datando_3)
			
	def voltar_menu(self): ####### BOTÃO VOLTAR ##############
		self.menu.place(x =0, y = 0 , width = 850, height = 500)
		self.feed_.place(x =0, y = 0 , width = 490, height = 500) #####
		self.feed_rodape.pack()
		#self.frame_botoes_calendiarios.destroy()
		self.but_back.destroy()
		self.aux_left_main.destroy()
		self.aux_right_main.destroy()
		self.entry_comentario.place_forget()

	def menu_entradasaida(self):
		## FRAMES
		self.frame_header = Frame(self.aux_right_main, bg = 'black')
		self.frame_header.pack(side = TOP)
		self.frame_nome = Frame(self.aux_right_main, bg = 'black')
		self.frame_nome.pack()
		self.frame_valor = Frame(self.aux_right_main, bg = 'black')
		self.frame_valor.pack()
		self.frame_data = Frame(self.aux_right_main, bg = 'black')
		self.frame_data.pack()
		self.frame_comentario = Frame(self.aux_right_main, bg = 'black')
		self.frame_comentario.pack()
		self.frame_footer = Frame(self.aux_right_main, bg = 'black')
		self.frame_footer.pack(side = BOTTOM, pady = 120)
		### LABELS E ENTRY E BOTÃOS
		###LABELS CABEÇALHO
		self.label_header = Label(self.frame_header, text = "CABEÇALHO",pady = 20, bg = 'black', fg = 'white', font = ('Franklin Gothic Medium', 20))
		self.label_header.pack()
		#### label e entry nome
		self.label_nome = Label(self.frame_nome, text = "Nome: ", bg = 'black' , fg = 'white', font = ('Franklin Gothic Medium', 15))
		self.label_nome.pack(side = LEFT)
		self.entry_nome = Entry(self.frame_nome, bg = 'black', fg = 'white')
		self.entry_nome.pack(side = LEFT)
		#### label e entry valor
		self.label_valor = Label(self.frame_valor, text = "Valor: ", bg = 'black' , fg = 'white', font = ('Franklin Gothic Medium', 15))
		self.label_valor.pack(side = LEFT)
		self.entry_valor = Entry(self.frame_valor, bg = 'black', fg = 'white')
		self.entry_valor.pack(side = LEFT)
		#### label e entry valor
		self.label_data = Label(self.frame_data, text = "Data: ", bg = 'black' , fg = 'white', font = ('Franklin Gothic Medium', 15))
		self.label_data.pack(side = LEFT)
		self.entry_data = Entry(self.frame_data, bg = 'black', fg = 'white')
		self.entry_data.pack(side = LEFT)
		#### label e entry comentario
		self.label_comentario = Label(self.frame_comentario, text = "Comentario: ", bg = 'black' , fg = 'white', font = ('Franklin Gothic Medium', 15))
		self.label_comentario.pack(side = LEFT)
		#### label especial de comentario pq vou usar place
		self.entry_comentario = Entry(self.i, bg = 'black', fg = 'white')
		self.entry_comentario.place(y = 320, x = 960, width= 300, height=100)
		#### label e botão valor
		self.botao_entrada = Button(self.frame_footer, text = "Entrada ", command = self.entrada_financas, bg = 'black', fg = 'white',  activebackground = "#353839", activeforeground = 'white', font = ('Franklin Gothic Medium', 10) )
		self.botao_entrada.pack(side = LEFT)
		self.botao_saida = Button(self.frame_footer, text = "Saida", command = self.saida_financas, bg = 'black', fg = 'white',  activebackground = "#353839", activeforeground = 'white', font = ('Franklin Gothic Medium', 10))
		self.botao_saida.pack(side = LEFT)

	def entrada_financas(self):
		nome = self.entry_nome.get()+"¹"
		valor = self.entry_valor.get()+"+"+"²"
		
		#a data vai ter um trabalho isolado
		if self.entry_data.get() == '':
			data = self.data_hoje
			##print("TESTANDO DATA ::::::::", data)
		else:
			data = self.entry_data.get()
			##print("TESTANDO DATA ::::::::", data)
		
		comentario = self.entry_comentario.get()+"¢"
		dbmfinancas.add_financas(nome,valor,data,comentario)
		self.entry_nome.delete(0,END)
		self.entry_valor.delete(0,END)
		self.entry_comentario.delete(0,END)
		self.entry_data.delete(0,END)
	
	def saida_financas(self):
		nome = self.entry_nome.get()+"¹"
		valor = self.entry_valor.get()+"-"+"²"
		
		#a data vai ter um trabalho isolado
		if self.entry_data.get() == '':
			data = self.data_hoje
		else:
			data = self.entry_data.get()
		
		comentario = self.entry_comentario.get()+"¢"
		dbmfinancas.rem_financas(nome,valor,data,comentario)
		self.entry_nome.delete(0,END)
		self.entry_valor.delete(0,END)
		self.entry_comentario.delete(0,END)
		self.entry_data.delete(0,END)

	def carregar_dados(self):
		a = dbmfinancas.financas.keys()
		##print(a)
		#atribuir valor positivo e negativo
		#carregar o calendario de conta

		#lista detalhada de contas

	def saldo(self, chave):
	
		a = dbmfinancas.financas[chave.decode()].decode()
		##print("Dentro de saldo",chave)
		##print("Dentro de saldo",a)
		b = ''
		c = ''
		var1 = ''		
		var2 = ''
		var3 = ''
		var4 = ''
		cont = 0
		pega_valor_positivo = 0
		pega_valor_negativo = 0
		valor = 0 
		for i in a:
			##print(i)
			if i =='¹':
				var1 = b
				b = '' 
			elif i == '²':
				var2 = b
				b = '' 
				for j in var2:
					##print("jjjjjjjjjjjjjjj",j)
					if j == "+":
						##print("aquiiii",c)
						pega_valor_positivo += int(c)
						c = ''
					
					elif j == "-":
						pega_valor_negativo -= int(c)
						c = ''
					else:
						c += j

			elif i == '³':
				var3 = b
				b = '' 
			elif i == '¢':
				var4 = b
				b = '' 
			elif i == '§':
				cont += 1
			else:
				b += str(i)
		##print("iouopppppppppppppppppppppppppppppppppppppppppppppp",pega_valor_positivo)
		##print("difhconubcd", pega_valor_negativo)
		valor = pega_valor_positivo + pega_valor_negativo + valor
		return valor
