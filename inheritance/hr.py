class PayrollSystem:

    def calculate_payroll(self, employees):
        print("=" * 50)
        for employee in employees:
            print(f"payroll for: {employee.id_} - {employee.name}")
            print(f"- check amount: {employee.calculate_payroll()}")
        print("=" * 50)