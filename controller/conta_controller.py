from models.conta_models import cadastrar_conta_corrente , sacar , depositar, usuario_cadastrado, conta
from views.conta_views import menu , pegar_dados_usuario , login , mostrar_extrato, mensagem,pedir_valor,menu_inicial


def buscar_usuario(cpf,senha):
    
    for usuario in usuario_cadastrado:
        if usuario['cpf'] == cpf and usuario['senha'] == senha:
            
            for contas in conta:
                if contas['cpf'] == cpf:
                    return usuario,contas
    
    return None ,None

def verificar_cpf(cpf):
    for usuario in usuario_cadastrado:
        if usuario['cpf'] == cpf:
            return True
    
    return False

def validaçaoConta():
    cadastro_usuario = pegar_dados_usuario()
    usuarios = verificar_cpf(
        cadastro_usuario['cpf'])
    
    if usuarios:
        mensagem('Conta com esse mesmo cpf esta cadastrato')
        return
    
    usuario_cadastrado.append(cadastro_usuario)
    
    cadastro_ContaCorrente = cadastrar_conta_corrente(
        cadastro_usuario['cpf'] , 
        len(conta) + 1
        )
    
    conta.append(cadastro_ContaCorrente)
    mensagem('Conta cadastrata com sucesso')
    

def iniciar_sistema():
    while True:
        tela_inicial = menu_inicial()
        
        if tela_inicial == 1:
            cpf , senha = login()
            encontrar_usuario , contas = buscar_usuario(cpf,senha)
        
            if encontrar_usuario is None:
                mensagem('CPF ou senha inválidos')
                continue
            
        
            
            while True:
                menu()
                entrada = int(input("Escolha uma das opcoes acima: "))
                
                if entrada == 1:
                    mensagem('Opcao de deposito selecionado')
                    valor = pedir_valor()
                    saldo_atual, extrato = contas['saldo'],contas['extrato']
                    
                    deposito, extrato_deposito= depositar(
                        saldo_atual,
                        valor,
                        extrato
                        )
                    
                    contas['saldo'] , contas['extrato']= deposito, extrato_deposito
                    
                elif entrada == 2 :
                    mensagem('Opcao de saque selecionado')
                    valor = pedir_valor()
                    saldo_atual, extrato = contas['saldo'],contas['extrato']
                    
                    deposito, extrato_saque= sacar(
                        saldo =saldo_atual,
                        valor = valor ,
                        extrato = extrato
                        )
                    
                    contas['saldo'] , contas['extrato'] = deposito, extrato_saque
                    
                elif entrada == 3:
                    mensagem('Opcao de extrato selecionado')
                    mostrar_extrato(contas['saldo'],extrato = contas['extrato'])
                
                elif entrada == 4:
                    mensagem('Voltando ao  menu inicial')
                    break
                
        elif tela_inicial == 2:
            validaçaoConta()
        
        elif tela_inicial == 3:
            mensagem('Saindo')
            break
            
        else:
            mensagem('\nNenhuma das opcoes selecionada.\nPor favor selecione umas das opcoes acima valida\n')
         
            
            
       