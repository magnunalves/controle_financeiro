import unittest
from datetime import datetime
from src.finances import FinanceManager

class TestFinanceManager(unittest.TestCase):
    def test_add_transaction(self):
        manager = FinanceManager()
        manager.add_transaction("Teste", 100, "Receita")
        self.assertEqual(len(manager.get_transactions()), 1)
        self.assertEqual(manager.get_balance(), 100)

    def test_get_balance(self):
        manager = FinanceManager()
        manager.add_transaction("Receita", 200, "Receita")
        manager.add_transaction("Despesa", -50, "Despesa")
        self.assertEqual(manager.get_balance(), 150)

    def test_generate_monthly_report(self):
        manager = FinanceManager()
        manager.add_transaction("Receita de Janeiro", 300, "Receita", 
datetime(2024, 1, 15))
        manager.add_transaction("Despesa de Janeiro", -100, "Despesa", 
datetime(2024, 1, 20))
        report = manager.generate_monthly_report(1, 2024)
        self.assertEqual(len(report), 2)

if __name__ == "__main__":
    unittest.main()

