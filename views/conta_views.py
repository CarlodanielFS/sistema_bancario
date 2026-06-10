def menu_inicial():
    print('SISTEMA BANCÁRIO')
    print('[1] Login')
    print('[2] Cadastrar-se')
    print('[3] Sair')
    entrada = int(input("Escolha uma das opcoes acima: "))
    
    return entrada
def menu(): 
    print(f'\n'+ '=' * 20)
    print('[1] Depositar')
    print('[2] Sacar')
    print('[3] Extrato')
    print('[4] Cadastrar')

def pedir_valor():
    return float(input("Valor: "))

def pegar_dados_usuario():
    dados_usuarios = {
        'nome':input('Vi que voce nao pussui conta preenche a baixo\nNome: '),
        'cpf':input("CPF: "),
        'data_nascimento':input('Data do Nascimento: '),
        'senha':input('Senha: ')
    
    }
    return dados_usuarios
def login():
    print("TELA DE LOGIN")
    cpf = input("Digite seu cpf: ").strip()
    senha = input("digite a senha: ").strip()
    
    return cpf,senha

def mostrar_extrato(saldo,/,*,extrato):
    print("\n" + "=" * 20)
    print("EXTRATO")
    print("=" * 20)
    print(extrato)
    print(f"Saldo Atual: R$ {saldo:.2f}")
    
def mensagem(msg):
    print(msg)