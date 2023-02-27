class Animal:
    def __init__(self, nome, idade, especie, cor, som):
        self.nome = nome
        self.idade = idade
        self.especie = especie
        self.cor = cor
        self.som = som

    def emitir_som(self):
        print(self.som)

    def mudar_cor(self, nova_cor):
        self.cor = nova_cor


class Elefante(Animal):
    def __init__(self, nome, idade, especie, cor, som, tamanho):
        super().__init__(nome, idade, especie, cor, som)
        self.tamanho = tamanho

    def trombar(self):
        print(self.som)

    def mudar_tamanho(self, novo_tamanho):
        self.tamanho = novo_tamanho

nome = input("Entre com o nome do elefante: ")
idade = input("Entre com a idade do elefante: ")
especie = input("Entre com a especie do elefante: ")
cor = input("Entre com a cor do elefante: ")
tamanho = input("Entre com o tamanho do elefante: ")
som = "Fuuhh"

elefante1 = Elefante(nome, idade, especie, cor, som, tamanho)

if especie == "Africano":
    if int(idade) < 10:
        elefante1.mudar_tamanho("Pequeno")
        elefante1.som = "Paaah"

    else:
        elefante1.mudar_tamanho("Grande")
        elefante1.som = "PAHHHHHH"


elefante1.emitir_som()
print("Tamanho do elefante:", elefante1.tamanho)




