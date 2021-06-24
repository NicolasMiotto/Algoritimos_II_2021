from Veiculo import Veiculo
from Bicicleta import Bicicleta
from Automovel import Automovel
from Moto import Moto
from Carro import Carro

print("----------Veículos----------")
v1 = Veiculo("Volksvagem", 4 , "Tiguan")
v1.imprimir_informacoes()
print(" -->> Acelerando.......... ")
v1.acelerar(20)
v1.imprimir_velocidade()


print("----------Bicicletas----------")
b1 = Bicicleta("GIOS", 2 , "Mountain bike", 18, True)
b1.imprimir_informacoes()
print(" -->> Acelerando.......... ")
b1.acelerar(5)
b1.imprimir_velocidade()

print("----------Automoveis----------")
a1 = Bicicleta("Chevrolet", 4 , "Blazer", 180, True)
a1.imprimir_informacoes()
print(" -->> Acelerando.......... ")
a1.acelerar(550)
a1.imprimir_velocidade()

print("----------Motos----------")
m1 = Bicicleta("Honda", 2 , "Hornet", 600, True)
m1.imprimir_informacoes()
print(" -->> Acelerando.......... ")
m1.acelerar(200)
m1.imprimir_velocidade()

print("----------Carros----------")
c1 = Bicicleta("Kia", 4 , "Sportage", 400, 4) 
c1.imprimir_informacoes()
print(" -->> Acelerando.......... ")
c1.acelerar(80)
c1.imprimir_velocidade()