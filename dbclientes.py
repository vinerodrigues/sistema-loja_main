import semidbm
###### DATA BASE DE CLIENTES E AGENDAMENTOS #########
clientes = semidbm.open("C:/sistema_loja-main/lista_cliente.db", 'c')

def add_clientes(nome,dados):
	clientes[nome]=dados
	#print(clientes.keys())
	#print('Adicionado')

def rem_clientes(nome):
	del clientes[nome]
	#print(clientes.keys())
	#print("Deletado")