import semidbm

usuarios = semidbm.open('C:/sistema_loja-main/usuarios.dat', 'c')

def validarEntrada(usuario,senha):
	nomeCodificado = usuario.encode()
	senha_encode = senha.encode()
	if nomeCodificado in usuarios:
		if senha_encode == usuarios[nomeCodificado.decode()]:
			return 1
		else:
			return 2
		 	
	
def adicionarUsuario(usuario, senha):
	nomeCodificado = usuario.encode()
	if nomeCodificado in usuarios:
		#print("usuario já existe")
		pass
	else:
		usuarios[nomeCodificado] = senha.encode()
		#print('Usuario criado')

def removerUsuario(usuario,senha):
	del usuarios[usuario]
	#print("usuario removidos")
	#print(usuarios.keys())
#usuarios['a'] = 'a'
#usuarios.close()	


	
