from tkinter import*
import tkinter as tk
from functools import partial
from datetime import datetime
import time
import main_menu
import dbclientes
import cv2

class abrir_janela_detalhada(object):
	def __init__(self, i):
		self.carregar_scrollbars(i)
		self.listar_financas(i)
		
	def listar_financas(self, i):
		def mostrar_foto(nome):
			diretorio = "C:/sistema_loja-main/imagens_clientes/"+nome+".png"
			imagem = cv2.imread(diretorio)
			cv2.imshow("Original", imagem) 
			cv2.waitKey(0)
			pass

		x  = dbclientes.clientes.keys() #¬ | ! £ ¢ § 
		#print("Lista: ",x)
		for k in x:
			#print('Nome:',k)
			aux = ""
			y = dbclientes.clientes[k.decode()].decode()
			#print('Valor: ',y)
			#self.data_aux = ''
			#self.hora_aux = ''
			nome = k.decode()
			aux = ''
			telefone = ''
			data_de_nascimento=''
			email=''
			endereco = ''
			self.data_aux=''
			self.hora_aux=''
			comentarios =''

			for i in y:
				##print("Correndo o data base - ",i)
				if i == '¹' and telefone == '':
					if aux == '':
						telefone = ('021')
					else:	
						telefone = aux
					#self.entry_tel.delete(0,END)
					#self.entry_tel.insert(END, telefone)
					##print("Telefone: ",telefone)
					aux = ''
					
				elif i == '¹' and data_de_nascimento == '':
					if aux == '':
						data_de_nascimento = ('00/00/0000')
					elif aux == ' ':
						data_de_nascimento = ('00/00/0000')
					elif aux == '  ':
						data_de_nascimento = ('00/00/0000')
					elif aux == '    ':
						data_de_nascimento = ('00/00/0000')
					elif aux == '	':
						data_de_nascimento = ('00/00/0000')
					else:	
						data_de_nascimento = aux
					#self.entry_nascimento.delete(0,END)
					#self.entry_nascimento.insert(END, data_de_nascimento)
					##print("data_de_nascimento: ", data_de_nascimento)
					#data_de_nascimento = aux
					##print(aux)
					aux = ''

				elif i == '¹' and email == '':
					if aux == '':
						email = "Vazio"
					elif aux == ' ':
						email = "Vazio"
					elif email == '   ':
						email = "Vazio"
					elif email == "	":
						email="Vazio"
					else:	
						email = aux
					#self.entry_email.delete(0,END)
					#self.entry_email.insert(END, email)
					aux = ''
					##print("EMAIL: ", email)
					
				elif i == '¹' and endereco == '':
					if aux == '':
						endereco = "1 - Rio de Janeiro - RJ"
					elif aux == ' ':
						endereco = "2 - Rio de Janeiro - RJ"
					elif aux == '  ':
						endereco = "3 - Rio de Janeiro - RJ"
					elif aux == '    ':
						endereco = "4 - Rio de Janeiro - RJ"
					elif aux == '	':
						endereco = "tab -Rio de Janeiro - RJ"
					else:	
						endereco = aux
						#endereco = aux
						##print("Endereço: ", aux)
						##print("Endereço: ", endereco)
					aux = ''
					
				elif i == '¹' and self.data_aux == '':
					if aux == '':
						self.data_aux = ('00/00/0000')
					else:	
						self.data_aux = aux
					#data = aux
					##print(" Data: ", self.data_aux)
					aux = ''

				elif i == '¹' and self.hora_aux == '':
					if aux == '':
						self.hora_aux = ('00:00')
					else:	
						self.hora_aux = aux	
					#hora = aux
					##print("Hora: ",self.hora_aux)
					aux = ''

				elif i == '¹' and comentarios == '':
					if aux == '':
						comentarios = ('1 -Vazio')
					elif aux == ' ':
						comentarios = ('2 - Vazio')
					elif aux == '  ':
						comentarios = ('2 - Vazio')
					elif aux == '   ':
						comentarios = ('2 - Vazio')
					elif aux == '	':
						comentarios = ('2 - Vazio')
					elif aux == '	 ':
						comentarios = ('2 - Vazio')
					elif aux == '	  ':
						comentarios = ('2 - Vazio')
					else:	
						comentarios = aux
					##print("Comentarios: ", comentarios)
					aux = ''
				elif i == '²':
					break;
				else:
					aux += i
			if self.data_aux != '':

				self.frame_tabela = Frame(self.frame_auxiliar_scrollbar, width = 10, height = 5, relief = RIDGE, borderwidth = '3', bg = 'black')
				self.frame_tabela.pack(pady = 10)

				self.label_teste = Button(self.frame_tabela, text="Nome: "+ nome, bg = 'black', fg = 'white', font = ('Franklin Gothic Medium', 12), relief = RIDGE, borderwidth = '1', width = 51, height = 1, command = partial(mostrar_foto, nome ))
				self.label_teste.pack()
				self.label_teste = Label(self.frame_tabela, text="Telefone: "+ telefone, bg = 'black', fg = 'white', font = ('Franklin Gothic Medium', 12), relief = RIDGE, borderwidth = '1', width = 51, height = 1, justify = 'left', anchor = 'w', )
				self.label_teste.pack()
				self.label_teste = Label(self.frame_tabela, text="Data de Nascimento: "+ data_de_nascimento, bg = 'black', fg = 'white', font = ('Franklin Gothic Medium', 12), relief = RIDGE, borderwidth = '1', width = 51, height = 1, justify = 'left', anchor = 'w')
				self.label_teste.pack()
				self.label_teste = Label(self.frame_tabela, text="Email: "+email, bg = 'black', fg = 'white', font = ('Franklin Gothic Medium', 12), relief = RIDGE, borderwidth = '1', width = 51, height = 1, justify = 'left', anchor = 'w')
				self.label_teste.pack()
				self.label_teste = Label(self.frame_tabela, text="Endereço: "+ endereco, bg = 'black', fg = 'white', font = ('Franklin Gothic Medium', 12), relief = RIDGE, borderwidth = '1', width = 51, height = 1, justify = 'left', anchor = 'w')
				self.label_teste.pack()
				self.label_teste = Label(self.frame_tabela, text="Data: "+ self.data_aux, bg = 'black', fg = 'white', font = ('Franklin Gothic Medium', 12), relief = RIDGE, borderwidth = '1', width = 51, height = 1, justify = 'left', anchor = 'w')
				self.label_teste.pack()
				self.label_teste = Label(self.frame_tabela, text="Hora: "+ self.hora_aux, bg = 'black', fg = 'white', font = ('Franklin Gothic Medium', 12), relief = RIDGE, borderwidth = '1', width = 51, height = 1, justify = 'left', anchor = 'w')
				self.label_teste.pack()
				self.label_teste = Label(self.frame_tabela, text="Comentario: "+ comentarios, bg = 'black', fg = 'white', font = ('Franklin Gothic Medium', 12), relief = RIDGE, borderwidth = '1', width = 51, height = 1, justify = 'left', anchor = 'w')
				self.label_teste.pack()


			
	def carregar_scrollbars(self, i):
		self.my_canvas = Canvas(i, width = 480)
		self.my_canvas.pack(side= LEFT, fill = BOTH)

		self.my_scrollsbars = Scrollbar(i, orient = VERTICAL, command = self.my_canvas.yview)
		self.my_scrollsbars.pack(side = LEFT, fill= Y)

		self.my_canvas.configure( yscrollcommand = self.my_scrollsbars.set, bg = 'black')
		self.my_canvas.bind('<Configure>', lambda e: self.my_canvas.configure(scrollregion = self.my_canvas.bbox("all") ))

		self.frame_scrollbar = Frame(self.my_canvas)
		self.my_canvas.create_window((0,0),window=self.frame_scrollbar, anchor = "nw")
 
		self.frame_auxiliar_scrollbar = Frame(self.frame_scrollbar, bg = 'black')#, relief = RIDGE, borderwidth = '3', width = 20, height = 6)#FRAME ESPECIAL AUXILIAR PARA A EXCLUSÃO E CONSTRUÇÃO DOS BOTÕES
		self.frame_auxiliar_scrollbar.pack()

class abrir_janela_detalhada_mes(object):
	def __init__(self, i, data):
		self.data_recebida = data
		self.carregar_scrollbars(i)
		self.listar_financas(i)
		
	def listar_financas(self, i):
		def mostrar_foto(nome):
			diretorio = "C:/sistema_loja-main/imagens_clientes/"+nome+".png"
			imagem = cv2.imread(diretorio)
			cv2.imshow("Original", imagem) 
			cv2.waitKey(0)
			pass

		x  = dbclientes.clientes.keys() #¬ | ! £ ¢ § 
		#print("Lista: ",x)
		for k in x:
			##print('Nome:',k)
			aux = ""
			y = dbclientes.clientes[k.decode()].decode()
			##print('Valor: ',y)
			#self.data_aux = ''
			#self.hora_aux = ''
			nome = k.decode()
			aux = ''
			telefone = ''
			data_de_nascimento=''
			email=''
			endereco = ''
			self.data_aux=''
			self.hora_aux=''
			comentarios =''

			for i in y:
				##print("Correndo o data base - ",i)
				if i == '¹' and telefone == '':
					if aux == '':
						telefone = ('021')
					else:	
						telefone = aux
					#self.entry_tel.delete(0,END)
					#self.entry_tel.insert(END, telefone)
					##print("Telefone: ",telefone)
					aux = ''
					
				elif i == '¹' and data_de_nascimento == '':
					if aux == '':
						data_de_nascimento = ('00/00/0000')
					elif aux == ' ':
						data_de_nascimento = ('00/00/0000')
					elif aux == '  ':
						data_de_nascimento = ('00/00/0000')
					elif aux == '    ':
						data_de_nascimento = ('00/00/0000')
					elif aux == '	':
						data_de_nascimento = ('00/00/0000')
					else:	
						data_de_nascimento = aux
					#self.entry_nascimento.delete(0,END)
					#self.entry_nascimento.insert(END, data_de_nascimento)
					##print("data_de_nascimento: ", data_de_nascimento)
					#data_de_nascimento = aux
					##print(aux)
					aux = ''

				elif i == '¹' and email == '':
					if aux == '':
						email = "Vazio"
					elif aux == ' ':
						email = "Vazio"
					elif email == '   ':
						email = "Vazio"
					elif email == "	":
						email="Vazio"
					else:	
						email = aux
					#self.entry_email.delete(0,END)
					#self.entry_email.insert(END, email)
					aux = ''
					##print("EMAIL: ", email)
					
				elif i == '¹' and endereco == '':
					if aux == '':
						endereco = "1 - Rio de Janeiro - RJ"
					elif aux == ' ':
						endereco = "2 - Rio de Janeiro - RJ"
					elif aux == '  ':
						endereco = "3 - Rio de Janeiro - RJ"
					elif aux == '    ':
						endereco = "4 - Rio de Janeiro - RJ"
					elif aux == '	':
						endereco = "tab -Rio de Janeiro - RJ"
					else:	
						endereco = aux
						#endereco = aux
						##print("Endereço: ", aux)
						##print("Endereço: ", endereco)
					aux = ''
					
				elif i == '¹' and self.data_aux == '':
					if aux == '':
						self.data_aux = ('00/00/0000')
					else:	
						self.data_aux = aux
					#data = aux
					##print(" Data: ", self.data_aux)
					aux = ''

				elif i == '¹' and self.hora_aux == '':
					if aux == '':
						self.hora_aux = ('00:00')
					else:	
						self.hora_aux = aux	
					#hora = aux
					##print("Hora: ",self.hora_aux)
					aux = ''

				elif i == '¹' and comentarios == '':
					if aux == '':
						comentarios = ('1 -Vazio')
					elif aux == ' ':
						comentarios = ('2 - Vazio')
					elif aux == '  ':
						comentarios = ('2 - Vazio')
					elif aux == '   ':
						comentarios = ('2 - Vazio')
					elif aux == '	':
						comentarios = ('2 - Vazio')
					elif aux == '	 ':
						comentarios = ('2 - Vazio')
					elif aux == '	  ':
						comentarios = ('2 - Vazio')
					else:	
						comentarios = aux
					##print("Comentarios: ", comentarios)
					aux = ''
				elif i == '²':
					break;
				else:
					aux += i
			
			#print("Data do cliente marcado",	self.data_aux)
			#print("Data recebida do sistema",self.data_recebida)

			a = self.data_aux[3::]
			b = self.data_recebida[3::]
			#print("Formato final data do cleinte",a)
			#print("Formato final do sistema ",b)

			if a == b : 

				self.frame_tabela = Frame(self.frame_auxiliar_scrollbar, width = 10, height = 5, relief = RIDGE, borderwidth = '3', bg = 'black')
				self.frame_tabela.pack(pady = 10)

				self.label_teste = Button(self.frame_tabela, text="Nome: "+ nome, bg = 'black', fg = 'white', font = ('Franklin Gothic Medium', 12), relief = RIDGE, borderwidth = '1', width = 51, height = 1, command = partial(mostrar_foto, nome ))
				self.label_teste.pack()
				self.label_teste = Label(self.frame_tabela, text="Telefone: "+ telefone, bg = 'black', fg = 'white', font = ('Franklin Gothic Medium', 12), relief = RIDGE, borderwidth = '1', width = 51, height = 1, justify = 'left', anchor = 'w', )
				self.label_teste.pack()
				self.label_teste = Label(self.frame_tabela, text="Data de Nascimento: "+ data_de_nascimento, bg = 'black', fg = 'white', font = ('Franklin Gothic Medium', 12), relief = RIDGE, borderwidth = '1', width = 51, height = 1, justify = 'left', anchor = 'w')
				self.label_teste.pack()
				self.label_teste = Label(self.frame_tabela, text="Email: "+email, bg = 'black', fg = 'white', font = ('Franklin Gothic Medium', 12), relief = RIDGE, borderwidth = '1', width = 51, height = 1, justify = 'left', anchor = 'w')
				self.label_teste.pack()
				self.label_teste = Label(self.frame_tabela, text="Endereço: "+ endereco, bg = 'black', fg = 'white', font = ('Franklin Gothic Medium', 12), relief = RIDGE, borderwidth = '1', width = 51, height = 1, justify = 'left', anchor = 'w')
				self.label_teste.pack()
				self.label_teste = Label(self.frame_tabela, text="Data: "+ self.data_aux, bg = 'black', fg = 'white', font = ('Franklin Gothic Medium', 12), relief = RIDGE, borderwidth = '1', width = 51, height = 1, justify = 'left', anchor = 'w')
				self.label_teste.pack()
				self.label_teste = Label(self.frame_tabela, text="Hora: "+ self.hora_aux, bg = 'black', fg = 'white', font = ('Franklin Gothic Medium', 12), relief = RIDGE, borderwidth = '1', width = 51, height = 1, justify = 'left', anchor = 'w')
				self.label_teste.pack()
				self.label_teste = Label(self.frame_tabela, text="Comentario: "+ comentarios, bg = 'black', fg = 'white', font = ('Franklin Gothic Medium', 12), relief = RIDGE, borderwidth = '1', width = 51, height = 1, justify = 'left', anchor = 'w')
				self.label_teste.pack()

			
	def carregar_scrollbars(self, i):
		self.my_canvas = Canvas(i, width = 480)
		self.my_canvas.pack(side= LEFT, fill = BOTH)

		self.my_scrollsbars = Scrollbar(i, orient = VERTICAL, command = self.my_canvas.yview)
		self.my_scrollsbars.pack(side = LEFT, fill= Y)

		self.my_canvas.configure( yscrollcommand = self.my_scrollsbars.set, bg = 'black')
		self.my_canvas.bind('<Configure>', lambda e: self.my_canvas.configure(scrollregion = self.my_canvas.bbox("all") ))

		self.frame_scrollbar = Frame(self.my_canvas)
		self.my_canvas.create_window((0,0),window=self.frame_scrollbar, anchor = "nw")
 
		self.frame_auxiliar_scrollbar = Frame(self.frame_scrollbar, bg = 'black')#, relief = RIDGE, borderwidth = '3', width = 20, height = 6)#FRAME ESPECIAL AUXILIAR PARA A EXCLUSÃO E CONSTRUÇÃO DOS BOTÕES
		self.frame_auxiliar_scrollbar.pack()

		
		
def abrir_janela_detalhada_cl():
	janela_detalhada = tk.Tk()
	abrir_janela_detalhada(janela_detalhada)
	janela_detalhada['bg'] = 'black'
	janela_detalhada.title("Agenda Completa")
	width = 500
	height = 800
	x = 850
	y = 0
 	#TAKE THE WINDOW SIZE AND PUT IN GEOMETRY
	##print(aux)
	janela_detalhada.geometry(f'{width}x{height}+{x}+{y}')
	#janela_detalhada.geometry(("600x700"))
	janela_detalhada.wm_iconbitmap('imagens/lou.ico')
	janela_detalhada.mainloop

def abrir_janela_detalhada_cl_mes(data):
	janela_detalhada_mes = tk.Tk()
	abrir_janela_detalhada_mes(janela_detalhada_mes, data)
	janela_detalhada_mes['bg'] = 'black'
	janela_detalhada_mes.title("Agenda Completa")
	width = 500
	height = 800
	x = 850
	y = 0
 	#TAKE THE WINDOW SIZE AND PUT IN GEOMETRY
	##print(aux)
	janela_detalhada_mes.geometry(f'{width}x{height}+{x}+{y}')
	#janela_detalhada.geometry(("600x700"))
	janela_detalhada_mes.wm_iconbitmap('imagens/lou.ico')
	janela_detalhada_mes.mainloop()