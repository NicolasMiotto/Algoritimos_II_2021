produtos = [ 'melancia' , 'banana' , 'abacaxi' , 'romã']
preco_produto = [ 1.0 , 14.50 , 55.00 , 3.40]
quandidade_produto = [2 , 45 , 2355 , 23]


def imprime_produto():
    print("Produtos:")
    for produto in produtos:
        print("--->", produto)

def deleta_item():
    produto_excluido = input("Qual produto da lista você quer escolher? :")
    print(produtos)
    if produto_excluido in produtos:
        produtos.remove(produto_excluido)
    else:
        print("Produto não existente na lista ")


while True:
    escolha = input("""
MENU
0-  Finalizar o Programa
1-  Imprimir Produtos
2-  Remover produtos
""")    

    if escolha == '0':
        break
    if escolha == '1':
        imprime_produto()
    if escolha == '2':
        deleta_item()
   
        

