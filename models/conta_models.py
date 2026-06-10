usuario_cadastrado = [{'nome': 'carlos daniel','cpf': '149', 'data_nascimento': '23042003', 'senha': '9828'},{'nome': 'daniel','cpf': '145', 'data_nascimento': '23042003', 'senha': '9829'}]

conta = [{'agencia': '0001','numero_da_conta': 1, 'cpf': '149', 'saldo': 1500 , 'extrato':''},{'agencia': '0001','numero_da_conta': 2, 'cpf': '145', 'saldo': 3000 , 'extrato':''}]

def cadastrar_conta_corrente(cpf,numero_conta):
    conta = {
        'agencia': '0001',
        'numero_da_conta':numero_conta,
        'cpf':cpf,
        'saldo': 0,
        'extrato':''
    }
    return conta

def sacar(*,saldo,valor,extrato):
    if valor <= saldo:
        saldo -= valor
        extrato += f'sacou R${valor:.2f}\n'
        return  saldo , extrato
    return f'Saldo insuficente seu saldo atual: {saldo}'

def depositar(saldo,valor,extrato,/):
        
        deposito = saldo + valor
        extrato += f'Depositou R${valor:.2f}\n'
        return deposito , extrato
    

