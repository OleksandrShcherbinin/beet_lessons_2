import hr2
import employees2
import productivity2


manager = employees2.Manager(1, "Alex", 2000)
secretary = employees2.Secretary(2, "Ivan", 40)
sales = employees2.SalesPerson(3, 'Kevin', 1000, 500)
worker = employees2.FactoryWorker(4, "Anatoliy", 30, 70)
temporary_secretary = employees2.TemporarySecretary(5, "Robin", 40, 9)
print(employees2.TemporarySecretary.__mro__)
employees_list = (manager, secretary, sales, worker, temporary_secretary)

productivity_system = productivity2.ProductivitySystem()
productivity_system.track(employees_list, 40)

payroll_system = hr2.PayrollSystem()
payroll_system.calculate_payroll(employees_list)
