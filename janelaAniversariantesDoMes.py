from tkinter import*
from datetime import datetime
import time
from functools import partial
import cv2

class janelaAniversarianteDoMes(object):
	def __init__(self, app, aniversariantes):

		self.coletarDataEHora()
		self.carregar_scrollbars(app)
		self.mostarAniversariantesNaJanela(aniversariantes)

		
	def mostarAniversariantesNaJanela(self, aniversariantes):
		def mostrar_foto(nome):
			diretorio = "C:/sistema_loja-main/imagens_clientes/"+nome+".png"
			imagem = cv2.imread(diretorio)
			cv2.imshow("Original", imagem) 
			cv2.waitKey(0)		
		
		listaDeAniversariantes = list(aniversariantes)
		
		for nomeDoAniversariante in listaDeAniversariantes:
			dataDeAniversario = aniversariantes[nomeDoAniversariante]
			idadeQueEleEstaCompletando = int(self.ano) - int(dataDeAniversario[6::])

			self.frame_tabela = Frame(self.frame_auxiliar_scrollbar, width = 10, height = 5, relief = RIDGE, borderwidth = '3', bg = 'black')
			self.frame_tabela.pack(pady = 10)

			self.label_teste = Button(self.frame_tabela, text="Nome: "+ nomeDoAniversariante, bg = 'black', fg = 'white', font = ('Franklin Gothic Medium', 12), relief = RIDGE, borderwidth = '1', width = 51, height = 1, command = partial(mostrar_foto, nomeDoAniversariante ))
			self.label_teste.pack()

			self.label_teste = Label(self.frame_tabela, text = f'Data do aniversario: {dataDeAniversario[0:5:]}/2021', bg = 'black', fg = 'white', font = ('Franklin Gothic Medium', 12), relief = RIDGE, borderwidth = '1', width = 51, height = 1, justify = 'left', anchor = 'w')
			self.label_teste.pack()		

			self.label_teste = Label(self.frame_tabela, text= f'Idade que irá completar: {idadeQueEleEstaCompletando} anos', bg = 'black', fg = 'white', font = ('Franklin Gothic Medium', 12), relief = RIDGE, borderwidth = '1', width = 51, height = 1, justify = 'left', anchor = 'w')
			self.label_teste.pack()

	def carregar_scrollbars(self, app):
		self.my_canvas = Canvas(app, width = 480)
		self.my_canvas.pack(side= LEFT, fill = BOTH)

		self.my_scrollsbars = Scrollbar(app, orient = VERTICAL, command = self.my_canvas.yview)
		self.my_scrollsbars.pack(side = LEFT, fill= Y)

		self.my_canvas.configure( yscrollcommand = self.my_scrollsbars.set, bg = 'black')
		self.my_canvas.bind('<Configure>', lambda e: self.my_canvas.configure(scrollregion = self.my_canvas.bbox("all") ))

		self.frame_scrollbar = Frame(self.my_canvas)
		self.my_canvas.create_window((0,0),window=self.frame_scrollbar, anchor = "nw")
 
		self.frame_auxiliar_scrollbar = Frame(self.frame_scrollbar, bg = 'black')#, relief = RIDGE, borderwidth = '3', width = 20, height = 6)#FRAME ESPECIAL AUXILIAR PARA A EXCLUSÃO E CONSTRUÇÃO DOS BOTÕES
		self.frame_auxiliar_scrollbar.pack()

	def coletarDataEHora(self):
		now = datetime.now()
		self.hora = now.strftime('%H')
		self.dia = now.strftime('%d')
		self.mes = now.strftime('%m')
		self.ano = now.strftime('%Y')
		self.dataDeHoje = now.strftime('%d/%m/%Y')

def abrirJanelaDosAniversariantesDoMes(aniversariantes):
	app = Tk()
	app['bg'] = 'black'
	app.geometry (f'{500}x{800}+{850}+{0}')
	app.title('Aniversariantes do mês		')
	janelaAniversarianteDoMes(app, aniversariantes)
	app.mainloop()