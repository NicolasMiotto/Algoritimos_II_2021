class Aluno():
    def __init__(self, nome, codigo, matricula):
        self.nome = nome
        self.codigo = codigo
        self.matricula = matricula

    def get_matricula(self):
        return self.matricula
             
    def get_nome(self):
        return self.nome

    def get_codigo(self):
        return self.codigo
    
    def mostra_aluno(self):
        print("Nome: ",self.nome,"<->","Código: ", self.codigo ,"<->", "matricula: ", self.matricula)


lista_alunos = [Aluno("Nicolas", 1999, 25268)]

def cadastrar_aluno():
    aluno = Aluno(input("Digite o nome do(a) aluno(a): "), input("Digite o código do(a) aluno(a): "), input("Digite a matrícula do(a) aluno(a): "))
    lista_alunos.append(aluno)

def relatorio_aluno():
    print("=-=-=-=-=-=RELATORIO ALUNOS=-=-=-=-=-=")
    for a in lista_alunos:
        a.mostra_aluno()

while True:
    escolha = input("""
MENU
1- Cadastrar Alunos
2- Relatório de Alunos
Escolha:
""")


    if escolha == '1':
        cadastrar_aluno()

    if escolha == '2':
        relatorio_aluno()

        
