from finances import FinanceManager

def main():
    """
    Função principal que gerencia a execução do sistema de controle financeiro.
    Apresenta um menu ao usuário e executa as ações conforme a escolha.
    """
    manager = FinanceManager()  # Cria uma instância do gerenciador financeiro

    while True:
        # Exibe o menu de opções para o usuário
        print("\nControle de Finanças Pessoais")
        print("1. Adicionar Receita/Despesa")
        print("2. Visualizar Transações")
        print("3. Visualizar Saldo")
        print("4. Gerar Relatório Mensal")
        print("5. Sair")

        choice = input("Escolha uma opção: ")  # Solicita a escolha do usuário

        if choice == '1':
            # Adicionar uma nova transação
            description = input("Descrição: ")
            amount = float(input("Valor: "))
            category = input("Categoria: ")
            manager.add_transaction(description, amount, category)
        elif choice == '2':
            # Visualizar todas as transações
            transactions = manager.get_transactions()
            for t in transactions:
                print(t)
        elif choice == '3':
            # Visualizar o saldo atual
            balance = manager.get_balance()
            print(f"Saldo atual: {balance}")
        elif choice == '4':
            # Gerar um relatório mensal
            month = int(input("Mês (1-12): "))
            year = int(input("Ano (YYYY): "))
            report = manager.generate_monthly_report(month, year)
            for t in report:
                print(t)
        elif choice == '5':
            # Sair do sistema
            break
        else:
            # Opção inválida
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
