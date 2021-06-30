#databaseproduto
import estoque
import semidbm
produtos = semidbm.open("C:/sistema_loja-main/produtos.db", 'c')


def add_produto_db(nome, valor, quantidade_estoque, quantidade_atual = 0):
	#print("Dentro do databaseprodutos")
	#print(nome)
	#print(valor)
	##print(quantidade_estoque)
	#print(quantidade_atual)
	if int(quantidade_atual) <= 9 and int(quantidade_atual) >= 0:
		quantidade_atual = "0"+str(quantidade_atual)
	
	if int(quantidade_estoque) <= 9 and int(quantidade_estoque) >= 0 and "0" not in quantidade_estoque:
		quantidade_estoque = "0"+str(quantidade_estoque)

	produtos[nome] = str(valor)+"¹"+str(quantidade_estoque)+"²"+str(quantidade_atual)+"§" 
	#print(len(produtos))
	#print("fim dbprodutos")

def rem_produto_db(nome):
	#print(nome)
	del produtos[nome]

