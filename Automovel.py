from Veiculo import Veiculo

class Automovel(Veiculo):
    def __init__(self, marca, qtd_Rodas, modelo,potenciaMotor, velocidade = 0):
        Veiculo.__init__(self, marca, qtd_Rodas, modelo, velocidade)
        self.potenciaMotor = potenciaMotor

    def imprimir_informacoes(self):
            print ("Marca: ", self.marca)
            print ("Modelo: : ", self.modelo)
            print ("Velocidade: ", self.velocidade)
            print ("Rodas: ", self.qtdRodas)
            print ("Potência do motor: ", self.potenciaMotor, " cavalos.")