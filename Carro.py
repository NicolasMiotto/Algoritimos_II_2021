from Veiculo import Veiculo
from Automovel import Automovel

class Carro(Automovel):
    def __init__(self, marca, qtd_Rodas, modelo, potenciaMotor, qtdPortas, velocidade = 0):
        Automovel.__init__(self, marca, qtd_Rodas, modelo, velocidade,potenciaMotor)
        self.qtdPortas = qtdPortas

    def imprimir_informacoes(self):
            print ("Marca: ", self.marca)
            print ("Modelo: : ", self.modelo)
            print ("Velocidade: ", self.velocidade)           
            print ("Rodas: ", self.qtdRodas)
            print ("Portas: ", self.qtdPortas)            
            print ("Potência do motor: ", self.potenciaMotor, " cavalos.")