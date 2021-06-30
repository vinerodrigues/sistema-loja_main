from tkinter import*
import tkinter as tk
import databaseproduto
from functools import partial
import dbmfinancas
from datetime import datetime
import time


'''
O controle do estoque irá previnir:
gasto superfluo, falta de material
Ele irá fornecer 
controle de material gasto, fazer projeções de quando o material irá acabar.
A idéia é sempre deixar o programa inteligente.
Todo final de dia terá que dá baixa no sistema do material gasto. Ou em um dia na semana, isso vai depender do fluxo de material gasto.

Uma projeção: 
O programa irá te dizer quando comprar, a quantidade e onde é mais barato.
Terá que fazer um cadastro dos produtos e dos lugares onde vende. 
(preçoxquantidadexfrete=valorunitario e comparar com outros valores unitários)
Editar empresa e tudo mais.
So poderá ser implementado depois de saber a quantidade suportavel por estoque.; 
'''

class estoque(object):
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
		self.cont = 0 
		self.aux_nome_global = ''
		self.valor_global = 0
		self.valor_global_total = 0 
########################## começo do código ##############################################
########################## FRAMES #######################################################
		self.criar_frames()
		self.criar_botao_menu()
		self.criando_scrollbars()
		self.lista_produto()
		self.criar_labels_menu()
		self.datando()



#		#                               ##### BOTÃO VOLTAR #####
		self.but_back = Button(self.footer, text = 'Voltar', command = self.voltar_menu, pady = 10, width = 30,  activebackground = "#353839", activeforeground = 'white', bg = 'black', fg = 'white', font = ('Franklin Gothic Medium', 10))
		self.but_back.pack(pady =20)
	def voltar_menu(self): ####### BOTÃO VOLTAR ##############
		self.menu.place(x =0, y = 0 , width = 850, height = 500)
		self.feed_.place(x =0, y = 0 , width = 490, height = 500) #####
		self.feed_rodape.pack()
		#self.frame_botoes_calendiarios.destroy()
		self.resultado_valor_compra.place_forget()
		self.add_produto.place_forget()
		self.resultado.destroy()
		
		self.but_back.destroy()
		self.aux_left_main.destroy()
		self.aux_right_main.destroy()
		self.excluindo_scrollbars()
		#self.frame_addrem_botoes.place_forget()
	
	def datando(self):
		now = datetime.now()
		self.datahora['text'] = '  -  '+ now.strftime('%H:%M:%S') + '  -  ' + now.strftime('%d/%m/%Y')
		self.hora = now.strftime('%H')
		self.dia = now.strftime('%d')
		self.mes = now.strftime('%m')
		self.ano = now.strftime('%Y')
		self.data_hoje = now.strftime('%d/%m/%Y')
		self.i.after(1000, self.datando)	

	def criar_frames(self):
		#self.frame_addrem_botoes = Frame(self.i, bg = 'white')
		#self.frame_addrem_botoes.place(x = 290, y = 125)
		
		self.frame_addrem_botoes_2 = Frame(self.aux_left_main, bg = 'black')
		self.frame_addrem_botoes_2.pack()
		
		self.frame_lista_produtos = Frame(self.aux_left_main, bg = 'black')
		self.frame_lista_produtos.pack()
	
	def exclui_frames(self):
		self.frame_lista_produtos.pack_forget()
		self.frame_addrem_botoes_2.pack_forget()

	def criar_labels_menu(self):
		self.lista_de_compras = Label(self.aux_right_main, text = "LISTA DE COMPRAS", pady = 20, bg = 'black', fg = 'white', font = ('Franklin Gothic Medium', 20))
		self.lista_de_compras.pack()
		self.aux = Label(self.frame_addrem_botoes_2, text = "dcnjsdkbcds", bg = 'black', fg = 'black')
		self.aux.pack(pady = 50)
		self.resultado_valor_compra = Label(self.i, text = " ",padx = 20, pady = 10, width = 8,   activebackground = "#353839", activeforeground = 'white', bg = 'black', fg = 'white', font = ('Franklin Gothic Medium', 40))
		self.resultado_valor_compra.place(x = 550, y = 125)
		self.resultado = Label(self.aux_right_main, text = '',pady = 20, bg = 'black', fg = 'white', font = ('Franklin Gothic Medium', 20))
		self.resultado.pack(side=BOTTOM)

	def criar_botao_menu(self):
		self.add_produto = Button(self.i, text="Produtos", command = self.nomevalor, pady = 10, width = 8,   activebackground = "#353839", activeforeground = 'white', bg = 'black', fg = 'white', font = ('Franklin Gothic Medium', 30))
		self.add_produto.place(x = 60, y = 125)

	def nomevalor(self):
		
		def add_produto():
			"Adiciona produto no data base e empacota tudo"
			if self.entry_nome_produto.get() == '':
				self.frame_addrem_botoes.destroy()
				self.excluindo_scrollbars()
				self.criando_scrollbars()
				self.lista_produto()
			else:	
				databaseproduto.add_produto_db(self.entry_nome_produto.get(), self.entry_valor_produto.get(), self.entry_quantidade_produto.get())
				self.frame_addrem_botoes.destroy()
				self.excluindo_scrollbars()
				self.criando_scrollbars()
				self.lista_produto()


		def rem_produto():
			"Remove produto no data base e empacota tudo"
			if self.entry_nome_produto.get() == '':
				self.frame_addrem_botoes.destroy()
				self.excluindo_scrollbars()
				self.criando_scrollbars()
				self.lista_produto()
			else:	
				databaseproduto.rem_produto_db(self.entry_nome_produto.get())
				self.frame_addrem_botoes.destroy()
				self.excluindo_scrollbars()
				self.criando_scrollbars()
				self.lista_produto()

		self.frame_addrem_botoes = Frame(self.i, bg = 'white')	
		self.frame_addrem_botoes.place(x = 290, y = 100)
		self.frame_addrem_botoes_interno = Frame(self.frame_addrem_botoes, bg = 'black')
		self.frame_addrem_botoes_interno.pack()
		self.frame_addrem_botoes_interno_top = Frame(self.frame_addrem_botoes_interno, bg = 'black')
		self.frame_addrem_botoes_interno_top.pack()
		self.frame_addrem_botoes_interno_center = Frame(self.frame_addrem_botoes_interno, bg = 'black')
		self.frame_addrem_botoes_interno_center.pack()
		self.frame_addrem_botoes_interno_center_2 = Frame(self.frame_addrem_botoes_interno, bg = 'black')
		self.frame_addrem_botoes_interno_center_2.pack()
		self.frame_addrem_botoes_interno_bottom = Frame(self.frame_addrem_botoes_interno, bg = 'black')
		self.frame_addrem_botoes_interno_bottom.pack()
		
		self.label_nome_produto = Label(self.frame_addrem_botoes_interno_top, text = "Nome: ", bg = 'black' , fg = 'white', font = ('Franklin Gothic Medium', 15))
		self.label_nome_produto.pack(side = LEFT)
		self.entry_nome_produto = Entry (self.frame_addrem_botoes_interno_top, bg = 'black', fg = 'white')
		self.entry_nome_produto.pack()
		self.label_valor_produto = Label(self.frame_addrem_botoes_interno_center, text = "Valor: ", bg = 'black' , fg = 'white', font = ('Franklin Gothic Medium', 15))
		self.label_valor_produto.pack(side = LEFT)
		self.entry_valor_produto = Entry (self.frame_addrem_botoes_interno_center, bg = 'black', fg = 'white')
		self.entry_valor_produto.pack()
		self.label_quantidade_produto = Label(self.frame_addrem_botoes_interno_center_2, text = "Estoque: ", bg = 'black' , fg = 'white', font = ('Franklin Gothic Medium', 15))
		self.label_quantidade_produto.pack(side = LEFT)
		self.entry_quantidade_produto = Entry (self.frame_addrem_botoes_interno_center_2, bg = 'black', fg = 'white')
		self.entry_quantidade_produto.pack()
		self.botao_add_produto = Button(self.frame_addrem_botoes_interno_bottom, text = "Adicionar", command = add_produto, bg = 'black', fg = 'white',  activebackground = "#353839", activeforeground = 'white', font = ('Franklin Gothic Medium', 10))
		self.botao_add_produto.pack(side = LEFT)
		self.botao_rem_produto = Button (self.frame_addrem_botoes_interno_bottom,text="Remover", command = rem_produto, bg = 'black', fg = 'white',  activebackground = "#353839", activeforeground = 'white', font = ('Franklin Gothic Medium', 10))
		self.botao_rem_produto.pack()#AQUI CRIAMOS AS OPÇÕES DA LISTA DE BOTÕES COM O VALOR E O NOME. AQUI TA O SUBMENU DE PRODUTO

	def criando_scrollbars(self):
		####################################Criando scrollbars##########################################################################################
		#create canvas

		self.my_canvas = Canvas(self.frame_lista_produtos, width = 800, bg = 'black')
		self.my_canvas.pack(side= LEFT, fill = BOTH)

		self.my_scrollsbars = Scrollbar(self.frame_lista_produtos, orient = VERTICAL, command = self.my_canvas.yview)
		self.my_scrollsbars.pack(side = LEFT, fill= Y)

		self.my_canvas.configure( yscrollcommand = self.my_scrollsbars.set, bg = 'black')
		self.my_canvas.bind('<Configure>', lambda e: self.my_canvas.configure(scrollregion = self.my_canvas.bbox("all") ))

		self.frame_scrollbar = Frame(self.my_canvas, bg = 'black')
		self.my_canvas.create_window((0,0),window=self.frame_scrollbar, anchor = "nw")
 
		self.frame_auxiliar_scrollbar = Frame(self.frame_scrollbar, bg = 'black')#FRAME ESPECIAL AUXILIAR PARA A EXCLUSÃO E CONSTRUÇÃO DOS BOTÕES
		self.frame_auxiliar_scrollbar.pack()
	
	def excluindo_scrollbars(self):
		self.my_canvas.destroy()
		self.my_scrollsbars.destroy()

	def lista_produto(self):
		#fazer um for do tamanho da lista de produto
		#percorrer a lista de produto
		#criar uma label com os respctivos nomes e valor
		##print(len(databaseproduto.produtos))
		a = databaseproduto.produtos.keys()
		##print(a)
		
		for key in a:
			#criando a frames individuas de cada produto
			self.frame_aux_produto = Frame(self.frame_scrollbar, bg = 'black')
			self.frame_aux_produto.pack()
			#pegando dados
			##print("testttttttttttttttttt1",key)
			valores = databaseproduto.produtos[key].decode()
			nome = key.decode()
			##print(nome)
			aux = '' 

			for j in valores:
				##print("AQUIIIIIIIII",j,key)
				if j == "¹":
					valor = aux
					aux = ''
					##print("valor dentro do for ", valor)
				elif j == "²":
					quantidade_estoque = aux
					aux = ''
					##print("qnt dentro do for",quantidade_estoque)
				elif j == "§":
					quantidade_atual = aux
					aux = ''
					##print("qnt dentro do for",quantidade_atual)
				else:
					aux += j

						
			#valor = databaseproduto.produtos[nome].decode()
			#criando botão 
			self.label_nome_produto_na_lista = Label(self.frame_aux_produto, text = " "+nome+" " + valor+",00 R$"+"	", justify = 'left', anchor = 'w', width = 20 , bg = 'black' , fg = 'white', font = ('Franklin Gothic Medium', 15))
			self.label_nome_produto_na_lista.pack(side = LEFT)
			self.label_estoque_lista = Label(self.frame_aux_produto, text = " Quantidade "+quantidade_atual+" de "+quantidade_estoque+"	 ", justify = 'left', anchor = 'w', width = 20 , bg = 'black' , fg = 'white', font = ('Franklin Gothic Medium', 15))
			self.label_estoque_lista.pack(side = LEFT)
			self.botao_incrementa_produto_na_lista = Button(self.frame_aux_produto, command = partial(self.add_valor_resultado, valor, nome, quantidade_estoque, quantidade_atual), text = '+', width = 3, height = 1, bg = 'black' , fg = 'white', font = ('Franklin Gothic Medium', 15))
			self.botao_incrementa_produto_na_lista.pack(side = LEFT)
			self.botao_decrementa_produto_na_lista = Button(self.frame_aux_produto,command = partial(self.rem_valor_resultado, valor, nome, quantidade_estoque, quantidade_atual),	 text = '-', width = 3, height = 1, bg = 'black' , fg = 'white', font = ('Franklin Gothic Medium', 15))
			self.botao_decrementa_produto_na_lista.pack(side = LEFT)
			self.espaco = Label(self.frame_aux_produto, text = '.', bg = 'black' , fg = 'black', font = ('Franklin Gothic Medium', 15))
			self.espaco.pack(side = LEFT)
			self.botao_comprar = Button(self.frame_aux_produto, text = 'Comprar', command = partial(self.comprar, nome, valor), bg = 'black' , fg = 'white', font = ('Franklin Gothic Medium', 15))
			self.botao_comprar.pack(side=LEFT, padx = 30)
	
	def excluir_lista_produto(self):
		self.frame_aux_produto.destroy()
		pass

	def add_valor_resultado(self, valor, nome, quantidade_estoque, quantidade_atual):
		#AQUI NADA SERA FEITO POR QUE AINDA NÃO FIZ O DATA BASE FINAÇAS
		#variavel auxiliar de reconhecimento
		valor_aux = valor
		##print("~~~~~~~~~~~ ",quantidade_estoque)
		##print("[[[[[[[[[[[[[[[[",quantidade_atual)
		aux_quantidade_atual = 0
		if self.aux_nome_global != nome:
			self.cont = 0

		self.cont +=1	
		valor = int(valor)*self.cont
		self.resultado_valor_compra['text'] = str(valor)+ ",00 R$"
		self.valor_global = valor
		
		aux_quantidade_atual = int(quantidade_atual)
		aux_quantidade_atual += self.cont
		quantidade_atual = str(aux_quantidade_atual)
		databaseproduto.add_produto_db(nome,valor_aux, quantidade_estoque, quantidade_atual)
		self.aux_nome_global = nome

	def rem_valor_resultado(self, valor, nome, quantidade_estoque, quantidade_atual):
		valor_aux = valor
		aux_quantidade_atual = 0
		
		if self.aux_nome_global != nome:
			self.cont = 0
		
		valor = int(valor)*self.cont - int(valor)
		self.resultado_valor_compra['text'] = str(valor)+ ",00 R$"
		
		self.cont = self.cont - 1
		self.valor_global -= valor
		
		aux_quantidade_atual = int(quantidade_atual)
		aux_quantidade_atual += self.cont		
		quantidade_atual = str(aux_quantidade_atual)
		databaseproduto.add_produto_db(nome,valor_aux, quantidade_estoque, quantidade_atual)
		self.aux_nome_global = nome

	def comprar(self, nome, valor):
			
		self.label_lista_de_compra = Label(self.aux_right_main, text= str(self.cont)+"x"+ nome + '	' +str((self.cont )*int(valor))+ ',00 R$', bg = 'black', fg = 'white', font = ('Franklin Gothic Medium', 20))
		self.label_lista_de_compra.pack()
		self.valor_global_total += self.valor_global
		self.resultado['text'] ="TOTAL: " +str(self.valor_global_total)+ ",00 R$"
		
		###### dentro do database das finanças do mês 
		if (self.cont )*int(valor) > 0:#funcionou
			valor = str((self.cont )*int(valor))+"-"+"²"
		else:
			valor = str(-1*(self.cont )*int(valor))+"+"+"²"

		nome = nome+"¹"
		data = self.data_hoje
		comentario = "Produto cadastrado no estoque"+"¢"
		##print(nome)
		##print(valor)
		##print(data)
		dbmfinancas.add_financas(nome,valor,data,comentario)
		#######
		self.cont = 0
		self.excluindo_scrollbars()
		self.criando_scrollbars()
		self.excluir_lista_produto()
		self.lista_produto()
