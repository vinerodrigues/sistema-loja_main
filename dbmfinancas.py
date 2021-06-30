
import semidbm
financas = semidbm.open("C:/sistema_loja-main/financas.db", "c")

a = financas.keys()
#print("Datas dentro de finanças",a)
#for i in a:
#	del financas[i]
def add_financas(nome, valor, data, comentario):
	##print(data)
	if data.encode() in financas: #####Adicionando os dados no data base
		aux_1 = financas[data]
		aux_2 =aux_1.decode()+"§"+nome+valor+comentario
		financas[data] = aux_2
		#print("Dentro do in/segundo loop---",financas[data].decode())
		
	else:
		financas[data]=nome+valor+comentario
		#print("Fora do in, no else primeiro loop ",financas[data])
		#print(financas.keys())

def rem_financas(nome, valor, data, comentario):
	##print(data)
	if data.encode() in financas: #####Adicionando os dados no data base
		aux_1 = financas[data]
		aux_2 = "-"+aux_1.decode()+"§"+nome+valor+comentario
		financas[data] = aux_2
		##print("Dentro do in/segundo loop---",financas[data].decode())
		a = financas.keys()
		##print(a)
		#for i in a:
		#	del financas[i]
	else:
		financas[data]=nome+valor+comentario
		##print("Fora do in, no else primeiro loop ",financas[data])
		##print(financas.keys())
