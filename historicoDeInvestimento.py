import semidbm

class historicoDeInvestimento (object):
	def __init__(self, nomeDoCliente): #, nomeDaTatuagem = None, valorDaTatuagem = None  ):
		self.criarBancoDeDados(nomeDoCliente)
		self.valorDeTodasAsTatuagens = ''
		self.somarValorDeTodasAsTatuagens(nomeDoCliente)
	
	def criarBancoDeDados(self, nomeDoCliente):
		self.clienteDoBancoDeDados = semidbm.open(f'C:/sistema_loja-main/Tatuagens/BancoDeDadosDosCleintes/bancoDeDados{nomeDoCliente}', 'c') 

	def adicionarNomeEValorDaTatuagem(self, nomeDaTatuagem, valorDaTatuagem):#, nomeDaTatuagem = None, valorDaTatuagem = None):
		self.clienteDoBancoDeDados[nomeDaTatuagem] = valorDaTatuagem

	def somarValorDeTodasAsTatuagens(self, nomeDoCliente):
		somatorioDeValores = 0
		for tatuagens in self.clienteDoBancoDeDados:
			somatorioDeValores += float(self.clienteDoBancoDeDados[tatuagens].decode())
		self.valorDeTodasAsTatuagens = str(somatorioDeValores)


		
