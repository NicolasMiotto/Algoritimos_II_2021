class Veiculo():
    def __init__(self, marca,  qtdRodas , modelo, velocidade =0):
        self.marca = marca
        self.qtdRodas = qtdRodas
        self.modelo = modelo
        self.velocidade = velocidade
      
       
    def imprimir_informacoes(self):
        print ("Marca: ", self.marca)
        print ("Modelo: : ", self.modelo)
        print ("Velocidade: ", self.velocidade)
        print ("Rodas: ", self.qtdRodas)

    def imprimir_velocidade(self): 
        print ("Velocidade: ", self.velocidade)
        
    def acelerar(self, valor):
        self.velocidade += valor
        return self.velocidade
    
    def frear(self):
        self.velocidade -= valor
        return self.velocidade
    


