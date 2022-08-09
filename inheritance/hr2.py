class PayrollSystem:

    def calculate_payroll(self, employees):
        print("=" * 50)
        for employee in employees:
            print(f"payroll for: {employee.id_} - {employee.name}")
            print(f"- check amount: {employee.calculate_payroll()}")
        print("=" * 50)


class SalaryPolicy:
    def __init__(self, weekly_salary):
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary


class HourlyPolicy:
    def __init__(self, worked_hours, hour_rate):
        self.worked_hours = worked_hours
        self.hour_rate = hour_rate

    def calculate_payroll(self):
        return self.worked_hours * self.hour_rate


class CommissionPolicy(SalaryPolicy):
    def __init__(self, weekly_salary, commission):
        super().__init__(weekly_salary)
        self.commission = commission

    def calculate_payroll(self):
        fixed = super().calculate_payroll()
        return fixed + self.commission

