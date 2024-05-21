from finances import FinanceManager

def main():
    manager = FinanceManager()

    while True:
        print("\nControle de Finanças Pessoais")
        print("1. Adicionar Receita/Despesa")
        print("2. Visualizar Transações")
        print("3. Visualizar Saldo")
        print("4. Gerar Relatório Mensal")
        print("5. Sair")

        choice = input("Escolha uma opção: ")

        if choice == '1':
            description = input("Descrição: ")
            amount = float(input("Valor: "))
            category = input("Categoria: ")
            manager.add_transaction(description, amount, category)
        elif choice == '2':
            transactions = manager.get_transactions()
            for t in transactions:
                print(t)
        elif choice == '3':
            balance = manager.get_balance()
            print(f"Saldo atual: {balance}")
        elif choice == '4':
            month = int(input("Mês (1-12): "))
            year = int(input("Ano (YYYY): "))
            report = manager.generate_monthly_report(month, year)
            for t in report:
                print(t)
        elif choice == '5':
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()

