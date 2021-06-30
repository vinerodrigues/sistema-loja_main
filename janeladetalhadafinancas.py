from tkinter import*
import tkinter as tk
from functools import partial
from datetime import datetime
import time
import main_menu
import dbmfinancas

class abrir_janela_detalhada(object):
	def __init__(self, i):
		self.carregar_scrollbars(i)
		self.listar_financas(i)
		
	def listar_financas(self, i):
		a = dbmfinancas.financas.keys()
		##print("Janela nova",a)
		aux = ''
		nome = ''
		cont = 0
		sinal = ''
		for j in a:
			aux = ''
			##print("Aux", aux)
			nome = ''
			##print("Nome", aux)
			cont = 0
			##print("Cont", cont)
			sinal = ''
			##print("Sinal", sinal)
			##print("Imprimindo o J",j)
			x = j.decode()
			##print("Verificar o que esta havendo", x)
			y = dbmfinancas.financas[x]
			y = y.decode()
			##print("Valores: ",y)
			#cont = 0
			
			for k in y:
				##print(k)
				cont += 1
				##print("Imprimindo o K", k)
				if k ==  '¹':
					nome = aux
			#		#print("Nome: ",nome)
					aux = ''
				elif k ==  '²':
					
					valor = aux
					sinal = valor[len(valor)-1:len(valor):1 ]
					valor = valor[0:len(valor) -1:1]
					aux = ''
			#		#print("valor: ",valor)
				
				elif k ==  '¢':
					comentario = aux
			#		#print("Comentario: ",comentario)
					aux = ''
					
					if sinal == "+":
						fg = 'green'
						self.frame_tabela_1 = Frame(self.frame_auxiliar_scrollbar, width = 10, height = 5, relief = RIDGE, borderwidth = '3', bg = 'black')
						self.frame_tabela_1.pack(pady = 10)
						self.label_teste = Label(self.frame_tabela_1, text="Nome do produto: "+ nome, bg = 'black', fg = fg, font = ('Franklin Gothic Medium', 15), relief = RIDGE, borderwidth = '1', width = 51, height = 1 )
						self.label_teste.pack()
						self.label_teste = Label(self.frame_tabela_1, text="Valor recebido no produto: "+ valor+",00 R$" , bg = 'black', fg = fg, font = ('Franklin Gothic Medium', 15), relief = RIDGE, borderwidth = '1', width = 51, height = 1, justify = 'left', anchor = 'w', )
						self.label_teste.pack()
						self.label_teste = Label(self.frame_tabela_1, text="Data: "+x , bg = 'black', fg = fg, font = ('Franklin Gothic Medium', 15), relief = RIDGE, borderwidth = '1', width = 51, height = 1, justify = 'left', anchor = 'w', )
						self.label_teste.pack()
						self.label_teste = Label(self.frame_tabela_1, text="Comentarios: "+ comentario, bg = 'black', fg = fg, font = ('Franklin Gothic Medium', 15), relief = RIDGE, borderwidth = '1', width = 51, height = 1, justify = 'left', anchor = 'w', )
						self.label_teste.pack()
						aux = ''
						
					else:
						fg = 'red'
						self.frame_tabela_1 = Frame(self.frame_auxiliar_scrollbar, width = 10, height = 5, relief = RIDGE, borderwidth = '3', bg = 'black')
						self.frame_tabela_1.pack(pady = 10)
						self.label_teste = Label(self.frame_tabela_1, text="Nome do produto: "+ nome, bg = 'black', fg = fg, font = ('Franklin Gothic Medium', 15), relief = RIDGE, borderwidth = '1', width = 51, height = 1 )
						self.label_teste.pack()
						self.label_teste = Label(self.frame_tabela_1, text="Valor gasto no produto: "+ valor+",00 R$" , bg = 'black', fg = fg, font = ('Franklin Gothic Medium', 15), relief = RIDGE, borderwidth = '1', width = 51, height = 1, justify = 'left', anchor = 'w', )
						self.label_teste.pack()
						self.label_teste = Label(self.frame_tabela_1, text="Data: "+x , bg = 'black', fg = fg, font = ('Franklin Gothic Medium', 15), relief = RIDGE, borderwidth = '1', width = 51, height = 1, justify = 'left', anchor = 'w', )
						self.label_teste.pack()
						self.label_teste = Label(self.frame_tabela_1, text="Comentarios: "+ comentario, bg = 'black', fg = fg, font = ('Franklin Gothic Medium', 15), relief = RIDGE, borderwidth = '1', width = 51, height = 1, justify = 'left', anchor = 'w', )
						self.label_teste.pack()
						aux = ''
						

				elif k == '§':
					
					aux = ''
					pass
					
				else:
					aux = aux + str(k)
	def carregar_scrollbars(self, i):
		self.my_canvas = Canvas(i, width = 480)
		self.my_canvas.pack(side= LEFT, fill = BOTH)

		self.my_scrollsbars = Scrollbar(i, orient = VERTICAL, command = self.my_canvas.yview)
		self.my_scrollsbars.pack(side = LEFT, fill= Y)

		self.my_canvas.configure( yscrollcommand = self.my_scrollsbars.set, bg = 'black')
		self.my_canvas.bind('<Configure>', lambda e: self.my_canvas.configure(scrollregion = self.my_canvas.bbox("all") ))

		self.frame_scrollbar = Frame(self.my_canvas)
		self.my_canvas.create_window((0,0),window=self.frame_scrollbar, anchor = "nw")
 
		self.frame_auxiliar_scrollbar = Frame(self.frame_scrollbar, bg = 'black')#FRAME ESPECIAL AUXILIAR PARA A EXCLUSÃO E CONSTRUÇÃO DOS BOTÕES
		self.frame_auxiliar_scrollbar.pack()


class abrir_janela_detalhada_diaria(object):
	def __init__(self, i, data):
		self.data = data
		self.carregar_scrollbars(i)
		self.listar_financas(i)
		
	def listar_financas(self, i):
		a = dbmfinancas.financas.keys()
		##print("Janela nova",a)
		aux = ''
		nome = ''
		cont = 0
		sinal = ''
		for j in a:
			aux = ''
			##print("Aux", aux)
			nome = ''
			##print("Nome", aux)
			cont = 0
			##print("Cont", cont)
			sinal = ''
			##print("Sinal", sinal)
			##print("Imprimindo o J",j)
			x = j.decode()
			if (x == self.data):	
				##print("Verificar o que esta havendo", x)
				y = dbmfinancas.financas[x]
				y = y.decode()
				##print("Valores: ",y)
				#cont = 0
				
				for k in y:
					##print(k)
					cont += 1
					##print("Imprimindo o K", k)
					if k ==  '¹':
						nome = aux
				#		#print("Nome: ",nome)
						aux = ''
					elif k ==  '²':
						
						valor = aux
						sinal = valor[len(valor)-1:len(valor):1 ]
						valor = valor[0:len(valor) -1:1]
						aux = ''
				#		#print("valor: ",valor)
					
					elif k ==  '¢':
						comentario = aux
				#		#print("Comentario: ",comentario)
						aux = ''
						
						if sinal == "+":
							fg = 'green'
							self.frame_tabela_1 = Frame(self.frame_auxiliar_scrollbar, width = 10, height = 5, relief = RIDGE, borderwidth = '3', bg = 'black')
							self.frame_tabela_1.pack(pady = 10)
							self.label_teste = Label(self.frame_tabela_1, text="Nome do produto: "+ nome, bg = 'black', fg = fg, font = ('Franklin Gothic Medium', 15), relief = RIDGE, borderwidth = '1', width = 51, height = 1 )
							self.label_teste.pack()
							self.label_teste = Label(self.frame_tabela_1, text="Valor recebido no produto: "+ valor+",00 R$" , bg = 'black', fg = fg, font = ('Franklin Gothic Medium', 15), relief = RIDGE, borderwidth = '1', width = 51, height = 1, justify = 'left', anchor = 'w', )
							self.label_teste.pack()
							self.label_teste = Label(self.frame_tabela_1, text="Data: "+x , bg = 'black', fg = fg, font = ('Franklin Gothic Medium', 15), relief = RIDGE, borderwidth = '1', width = 51, height = 1, justify = 'left', anchor = 'w', )
							self.label_teste.pack()
							self.label_teste = Label(self.frame_tabela_1, text="Comentarios: "+ comentario, bg = 'black', fg = fg, font = ('Franklin Gothic Medium', 15), relief = RIDGE, borderwidth = '1', width = 51, height = 1, justify = 'left', anchor = 'w', )
							self.label_teste.pack()
							aux = ''
							
						else:
							fg = 'red'
							self.frame_tabela_1 = Frame(self.frame_auxiliar_scrollbar, width = 10, height = 5, relief = RIDGE, borderwidth = '3', bg = 'black')
							self.frame_tabela_1.pack(pady = 10)
							self.label_teste = Label(self.frame_tabela_1, text="Nome do produto: "+ nome, bg = 'black', fg = fg, font = ('Franklin Gothic Medium', 15), relief = RIDGE, borderwidth = '1', width = 51, height = 1 )
							self.label_teste.pack()
							self.label_teste = Label(self.frame_tabela_1, text="Valor gasto no produto: "+ valor+",00 R$" , bg = 'black', fg = fg, font = ('Franklin Gothic Medium', 15), relief = RIDGE, borderwidth = '1', width = 51, height = 1, justify = 'left', anchor = 'w', )
							self.label_teste.pack()
							self.label_teste = Label(self.frame_tabela_1, text="Data: "+x , bg = 'black', fg = fg, font = ('Franklin Gothic Medium', 15), relief = RIDGE, borderwidth = '1', width = 51, height = 1, justify = 'left', anchor = 'w', )
							self.label_teste.pack()
							self.label_teste = Label(self.frame_tabela_1, text="Comentarios: "+ comentario, bg = 'black', fg = fg, font = ('Franklin Gothic Medium', 15), relief = RIDGE, borderwidth = '1', width = 51, height = 1, justify = 'left', anchor = 'w', )
							self.label_teste.pack()
							aux = ''
							

					elif k == '§':
						
						aux = ''
						pass
						
					else:
						aux = aux + str(k) 



	def carregar_scrollbars(self, i):
		self.my_canvas = Canvas(i, width = 480)
		self.my_canvas.pack(side= LEFT, fill = BOTH)
		self.my_scrollsbars = Scrollbar(i, orient = VERTICAL, command = self.my_canvas.yview)
		self.my_scrollsbars.pack(side = LEFT, fill= Y)

		self.my_canvas.configure( yscrollcommand = self.my_scrollsbars.set, bg = 'black')
		self.my_canvas.bind('<Configure>', lambda e: self.my_canvas.configure(scrollregion = self.my_canvas.bbox("all") ))

		self.frame_scrollbar = Frame(self.my_canvas)
		self.my_canvas.create_window((0,0),window=self.frame_scrollbar, anchor = "nw")
	 
		self.frame_auxiliar_scrollbar = Frame(self.frame_scrollbar, bg = 'black')#FRAME ESPECIAL AUXILIAR PARA A EXCLUSÃO E CONSTRUÇÃO DOS BOTÕES
		self.frame_auxiliar_scrollbar.pack()


class abrir_janela_detalhada_mensal(object):
	def __init__(self, i, data):
		self.data = data
		self.carregar_scrollbars(i)
		self.listar_financas(i)
		
	def listar_financas(self, i):
		a = dbmfinancas.financas.keys()
		##print("Janela nova",a)
		aux = ''
		nome = ''
		cont = 0
		sinal = ''
		for j in a:
			aux = ''
			##print("Aux", aux)
			nome = ''
			##print("Nome", aux)
			cont = 0
			##print("Cont", cont)
			sinal = ''
			##print("Sinal", sinal)
			##print("Imprimindo o J",j)
			x = j.decode()
			#print("Do mês com X", x)
			do_mes = x[2::]
			mes_requerido = self.data[2::]
			#print("Do mês tratado ", do_mes)
			#print("Do mês requerido", mes_requerido)
			if (do_mes == mes_requerido):	
				##print("Verificar o que esta havendo", x)
				y = dbmfinancas.financas[x]
				y = y.decode()
				##print("Valores: ",y)
				#cont = 0
				
				for k in y:
					##print(k)
					cont += 1
					##print("Imprimindo o K", k)
					if k ==  '¹':
						nome = aux
				#		#print("Nome: ",nome)
						aux = ''
					elif k ==  '²':
						
						valor = aux
						sinal = valor[len(valor)-1:len(valor):1 ]
						valor = valor[0:len(valor) -1:1]
						aux = ''
				#		#print("valor: ",valor)
					
					elif k ==  '¢':
						comentario = aux
				#		#print("Comentario: ",comentario)
						aux = ''
						
						if sinal == "+":
							fg = 'green'
							self.frame_tabela_1 = Frame(self.frame_auxiliar_scrollbar, width = 10, height = 5, relief = RIDGE, borderwidth = '3', bg = 'black')
							self.frame_tabela_1.pack(pady = 10)
							self.label_teste = Label(self.frame_tabela_1, text="Nome do produto: "+ nome, bg = 'black', fg = fg, font = ('Franklin Gothic Medium', 15), relief = RIDGE, borderwidth = '1', width = 51, height = 1 )
							self.label_teste.pack()
							self.label_teste = Label(self.frame_tabela_1, text="Valor recebido no produto: "+ valor+",00 R$" , bg = 'black', fg = fg, font = ('Franklin Gothic Medium', 15), relief = RIDGE, borderwidth = '1', width = 51, height = 1, justify = 'left', anchor = 'w', )
							self.label_teste.pack()
							self.label_teste = Label(self.frame_tabela_1, text="Data: "+x , bg = 'black', fg = fg, font = ('Franklin Gothic Medium', 15), relief = RIDGE, borderwidth = '1', width = 51, height = 1, justify = 'left', anchor = 'w', )
							self.label_teste.pack()
							self.label_teste = Label(self.frame_tabela_1, text="Comentarios: "+ comentario, bg = 'black', fg = fg, font = ('Franklin Gothic Medium', 15), relief = RIDGE, borderwidth = '1', width = 51, height = 1, justify = 'left', anchor = 'w', )
							self.label_teste.pack()
							aux = ''
							
						else:
							fg = 'red'
							self.frame_tabela_1 = Frame(self.frame_auxiliar_scrollbar, width = 10, height = 5, relief = RIDGE, borderwidth = '3', bg = 'black')
							self.frame_tabela_1.pack(pady = 10)
							self.label_teste = Label(self.frame_tabela_1, text="Nome do produto: "+ nome, bg = 'black', fg = fg, font = ('Franklin Gothic Medium', 15), relief = RIDGE, borderwidth = '1', width = 51, height = 1 )
							self.label_teste.pack()
							self.label_teste = Label(self.frame_tabela_1, text="Valor gasto no produto: "+ valor+",00 R$" , bg = 'black', fg = fg, font = ('Franklin Gothic Medium', 15), relief = RIDGE, borderwidth = '1', width = 51, height = 1, justify = 'left', anchor = 'w', )
							self.label_teste.pack()
							self.label_teste = Label(self.frame_tabela_1, text="Data: "+x , bg = 'black', fg = fg, font = ('Franklin Gothic Medium', 15), relief = RIDGE, borderwidth = '1', width = 51, height = 1, justify = 'left', anchor = 'w', )
							self.label_teste.pack()
							self.label_teste = Label(self.frame_tabela_1, text="Comentarios: "+ comentario, bg = 'black', fg = fg, font = ('Franklin Gothic Medium', 15), relief = RIDGE, borderwidth = '1', width = 51, height = 1, justify = 'left', anchor = 'w', )
							self.label_teste.pack()
							aux = ''
							

					elif k == '§':
						
						aux = ''
						pass
						
					else:
						aux = aux + str(k) 



	def carregar_scrollbars(self, i):
		self.my_canvas = Canvas(i, width = 480)
		self.my_canvas.pack(side= LEFT, fill = BOTH)
		self.my_scrollsbars = Scrollbar(i, orient = VERTICAL, command = self.my_canvas.yview)
		self.my_scrollsbars.pack(side = LEFT, fill= Y)

		self.my_canvas.configure( yscrollcommand = self.my_scrollsbars.set, bg = 'black')
		self.my_canvas.bind('<Configure>', lambda e: self.my_canvas.configure(scrollregion = self.my_canvas.bbox("all") ))

		self.frame_scrollbar = Frame(self.my_canvas)
		self.my_canvas.create_window((0,0),window=self.frame_scrollbar, anchor = "nw")
	 
		self.frame_auxiliar_scrollbar = Frame(self.frame_scrollbar, bg = 'black')#FRAME ESPECIAL AUXILIAR PARA A EXCLUSÃO E CONSTRUÇÃO DOS BOTÕES
		self.frame_auxiliar_scrollbar.pack()
		
		
def abrir_janela_detalhada_fc():
	janela_detalhada = tk.Tk()
	abrir_janela_detalhada(janela_detalhada)
	janela_detalhada.title("Finanças Completa")
	width = 500
	height = 800
	x = 850
	y = 0
 	#TAKE THE WINDOW SIZE AND PUT IN GEOMETRY
	##print(aux)
	janela_detalhada.geometry(f'{width}x{height}+{x}+{y}')
	#janela_detalhada.geometry(("600x700"))
	janela_detalhada.wm_iconbitmap('imagens/lou.ico')

	janela_detalhada.mainloop()


def abrir_janela_detalhada_fc_diaria(data):
	janela_detalhada_diaria = tk.Tk()
	abrir_janela_detalhada_diaria(janela_detalhada_diaria, data)
	janela_detalhada_diaria.title("Finanças Completa")
	width = 500
	height = 800
	x = 850
	y = 0
 	#TAKE THE WINDOW SIZE AND PUT IN GEOMETRY
	##print(aux)
	janela_detalhada_diaria.geometry(f'{width}x{height}+{x}+{y}')
	#janela_detalhada.geometry(("600x700"))
	janela_detalhada_diaria.wm_iconbitmap('imagens/lou.ico')
	janela_detalhada_diaria.mainloop()

def abrir_janela_detalhada_fc_mensal(data):
	janela_detalhada_mensal = tk.Tk()
	abrir_janela_detalhada_mensal(janela_detalhada_mensal, data)
	janela_detalhada_mensal.title("Finanças Mensal")
	width = 500
	height = 800
	x = 850
	y = 0
 	#TAKE THE WINDOW SIZE AND PUT IN GEOMETRY
	##print(aux)
	janela_detalhada_mensal.geometry(f'{width}x{height}+{x}+{y}')
	#janela_detalhada.geometry(("600x700"))
	janela_detalhada_mensal.wm_iconbitmap('imagens/lou.ico')

	janela_detalhada_mensal.mainloop()