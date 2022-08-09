from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, id_, name):
        self.id_ = id_
        self.name = name

    @abstractmethod
    def calculate_payroll(self):
        pass


class SalaryEmployee(Employee):
    def __init__(self, id_, name, weekly_salary):
        super().__init__(id_, name)
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary


class HourlyEmployee(Employee):
    def __init__(self, id_, name, hour_rate, hours_worked):
        super().__init__(id_, name)
        self.hour_rate = hour_rate
        self.hours_worked = hours_worked

    def calculate_payroll(self):
        return self.hour_rate * self.hours_worked


class CommissionEmployee(SalaryEmployee):
    def __init__(self, id_, name, weekly_salary, commission):
        super().__init__(id_, name, weekly_salary)
        self.commission = commission

    def calculate_payroll(self):
        # так сделано для того чтобы расчет зарплаты производился на основании
        # метода SalaryEmployee, если вдруг что-то изменться, то эти изменения
        # повлияют автоматически и на этоот класс
        fixed = super().calculate_payroll()
        return fixed + self.commission


class Manager(SalaryEmployee):
    def work(self, hours):
        print(f"{self.name} yells for {hours} hours")


class Secretary(SalaryEmployee):
    def work(self, hours):
        print(f"{self.name} expends {hours} hours doing paper work")


class SalesPerson(CommissionEmployee):
    def work(self, hours):
        print(f"{self.name} expends {hours} hours on the phone")


class FactoryWorker(HourlyEmployee):
    def work(self, hours):
        print(f"{self.name} manufactures gadgets for {hours} hours")


class TemporarySecretary(Secretary, HourlyEmployee):
    # Diamond problem
    def __init__(self, id_, name, hour_rate, hours_worked):
        HourlyEmployee.__init__(self, id_, name, hour_rate, hours_worked)

    def calculate_payroll(self):
        return HourlyEmployee.calculate_payroll(self)


