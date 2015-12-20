#python 3
#David Turati
#Metodo de interpolacao na forma de Newtom

# -*- coding:latin 1 -*-
class Newton():
	imagem = []
	dominio = []
	vetor_d = []
	aux = []
	temp = []

	#Construtor
	def __init__(self,tm):
		self.__tamanho = tm
		print("Forma de Newtom")

	#metodos getters
	def get_tamanho(self):
		return self.__tamanho
	
	#metodos setters
	def set_tamanho(self,tm):
		sefl.__tamanho = tm

	#preenche valores do dominio
	def preenche_dominio(self):
		for i in range(self.__tamanho):
			print("digite o elemento do dominio em X",i)
			self.dominio.append(int(input()))

	#preenche valores da imagem
	def preenche_imagem(self):
		for i in range(self.__tamanho):
			print("Digite o valor de fx",i)
			self.imagem.append(int(input()))

	#metodo para calcular numerado F(Xn-1) - F(Xn)
	def calcula_numerador(self,x,y):
		return x-y

	#metodo para calcular denominado (Xn-1) - (Xn)
	def calcula_denominado(self,x,y):
		return x-y

	def calcula_d(self):
		tm = self.__tamanho - 1

		#Encontra o D0 e coloca no vetor com os Dn
		self.vetor_d.append(self.imagem[0])

		#faz uma copia da lista numerado e denominador para duas listas temporarias
		self.temp_imagem = self.imagem[:]
		self.temp_dominio = self.dominio[:]

		ordem = 1 #ordem da tabela, começa em 1 pois ordem 0 o D0 é o primeiro elemento da lista de imagem
		while(tm > 0):
			for i in range(tm):
				im = self.calcula_numerador( self.temp_imagem [i+1], self.temp_imagem [i])
				dm = self.calcula_denominado(self.temp_dominio[ordem], self.temp_dominio[0])
				ax = im/dm
				self.aux.append(ax)
			#adiciona elemetos no final da lista vetor_d
			self.vetor_d.append(self.aux[0])
			
			t = len(self.temp_imagem) - 1

			#remove elementos da lista de temp_imagem
			while(t >= 0):
				del self.temp_imagem[t]
				t = t-1
			self.temp_imagem = self.aux[:]

			t = len(self.aux) - 1
			#remove elementos da lista do aux
			while(t >= 0):
				del self.aux[t]
				t = t - 1

			tm = tm - 1
			ordem = ordem + 1

	#Metodo que orgazina a equação com os Dn encontrado no metodo anterior
	def equacao(self):
		aux = [0]
		self.v_equacao =[str(self.vetor_d[0])]
		tamanho = len(self.vetor_d) - 1
		cont = 1

		while(tamanho > 0):
			tmp = str(["x",-self.dominio[0]])
			for  i in range(1,cont):
				tmp += str(["x",-self.dominio[i]])

			tmp = str(self.vetor_d[cont]) + "*" + tmp

			self.v_equacao.append(tmp)

			tamanho -=  1
			cont = cont + 1

	def imprime_imagem_dominio(self):
		print("Valores do dominio")
		print(self.dominio)
		print("Valores da imagem")
		print(self.imagem)
		print("Vetor d:")
		print(self.vetor_d)
		print(" ")
		print("Equacao:")
		for i in self.v_equacao:
			print(i,"+",end=" ")
		print(" ")

	#property
	tamanho = property(fget = get_tamanho, fset = set_tamanho)

# cria objeto Newton
print("Digite o tamanho do dominio e imagem da função")
n = Newton(int(input()))

#chama os metodos
n.preenche_dominio()

n.preenche_imagem()

n.calcula_d()

n.equacao()

n.imprime_imagem_dominio()