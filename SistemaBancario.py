class ContaBancaria:
    def __init__(self, nome, saldo_inicial=0):
        self.nome = nome
        self.saldo = saldo_inicial

    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f'Depósito de {valor} realizado. Saldo atual: {self.saldo}')
        else:
            print('Valor de depósito inválido.')

    def saque(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            print(f'Saque de {valor} realizado. Saldo atual: {self.saldo}')
        else:
            print('Saque não permitido. Saldo insuficiente ou valor inválido.')

    def consultar_saldo(self):
        print(f'Saldo atual da conta de {self.nome}: {self.saldo}')


def main():
    print("Bem-vindo ao Sistema Bancário Simples!")
    nome_cliente = input("Digite seu nome: ")
    conta = ContaBancaria(nome_cliente)

    while True:
        print("\nEscolha uma opção:")
        print("1. Consultar saldo")
        print("2. Fazer depósito")
        print("3. Fazer saque")
        print("4. Sair")
        
        opcao = input("Digite o número da opção desejada: ")

        if opcao == '1':
            conta.consultar_saldo()
        elif opcao == '2':
            valor_deposito = float(input("Digite o valor do depósito: "))
            conta.deposito(valor_deposito)
        elif opcao == '3':
            valor_saque = float(input("Digite o valor do saque: "))
            conta.saque(valor_saque)
        elif opcao == '4':
            print("Obrigado por usar nosso sistema bancário!")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")


if __name__ == "__main__":
    main()
