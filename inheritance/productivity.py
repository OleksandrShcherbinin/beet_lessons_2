class ProductivitySystem:
    def track(self, employees, hours):
        print('Track productivity')
        for employee in employees:
            employee.work(hours)
