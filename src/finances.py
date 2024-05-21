from datetime import datetime

# Classe que representa uma transação financeira
class Transaction:
    def __init__(self, description, amount, category, date=None):
        """
        Inicializa uma nova transação.
        :param description: Descrição da transação.
        :param amount: Valor da transação (positivo para receitas, 
negativo para despesas).
        :param category: Categoria da transação (ex: Alimentação, 
Transporte).
        :param date: Data da transação (padrão: data e hora atual).
        """
        self.description = description
        self.amount = amount
        self.category = category
        self.date = date if date else datetime.now()

    def __repr__(self):
        """
        Retorna uma representação em string da transação.
        :return: String representando a transação.
        """
        return f"Transaction(description={self.description}, 
amount={self.amount}, category={self.category}, date={self.date})"

# Classe que gerencia as transações financeiras
class FinanceManager:
    def __init__(self):
        """
        Inicializa o gerenciador financeiro com uma lista vazia de 
transações.
        """
        self.transactions = []

    def add_transaction(self, description, amount, category):
        """
        Adiciona uma nova transação à lista de transações.
        :param description: Descrição da transação.
        :param amount: Valor da transação.
        :param category: Categoria da transação.
        """
        transaction = Transaction(description, amount, category)
        self.transactions.append(transaction)

    def get_balance(self):
        """
        Calcula o saldo atual somando os valores de todas as transações.
        :return: Saldo atual.
        """
        balance = sum(t.amount for t in self.transactions)
        return balance

    def get_transactions(self):
        """
        Retorna a lista de todas as transações.
        :return: Lista de transações.
        """
        return self.transactions

    def generate_monthly_report(self, month, year):
        """
        Gera um relatório de transações para um mês e ano específicos.
        :param month: Mês do relatório (1-12).
        :param year: Ano do relatório.
        :return: Lista de transações no mês e ano especificados.
        """
        report = [t for t in self.transactions if t.date.month == month 
and t.date.year == year]
        return report

