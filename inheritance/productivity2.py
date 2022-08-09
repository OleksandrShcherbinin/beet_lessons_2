class ProductivitySystem:
    def track(self, employees, hours):
        print('Track productivity')
        for employee in employees:
            result = employee.work(hours)
            print(f"{employee.name}: {result}")
            print("-" * 50)


class ManagerRole:
    def work(self, hours):
        return f"yells for {hours} hours"


class SecretaryRole:
    def work(self, hours):
        return f"expends {hours} hours doing paper work"


class SalesPersonRole:
    def work(self, hours):
        return f"expends {hours} hours on the phone"


class FactoryWorkerRole:
    def work(self, hours):
        return f" manufactures gadgets for {hours} hours"

