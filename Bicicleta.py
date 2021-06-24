from Veiculo import Veiculo

class Bicicleta(Veiculo):
    def __init__(self, marca, qtdRodas, modelo, numero_marchas, bagageiro, velocidade = 0):
        Veiculo.__init__(self, marca, qtdRodas, modelo, velocidade)
        self.numero_marchas = numero_marchas
        self.bagageiro = bagageiro
    
    def imprimir_informacoes(self):  
            print ("Marca: ", self.marca)
            print ("Modelo: : ", self.modelo)
            print ("Velocidade: ", self.velocidade)
            print ("Rodas: ", self.qtdRodas)
            print ("Numero de marchas: ", self.numero_marchas)
            print ("Tem bagageiro: ", self.bagageiro)


            