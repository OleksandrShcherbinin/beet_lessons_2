from hr2 import (
    SalaryPolicy,
    CommissionPolicy,
    HourlyPolicy
)
from productivity2 import (
    ManagerRole,
    SecretaryRole,
    SalesPersonRole,
    FactoryWorkerRole
)


class Employee:
    def __init__(self, id_, name):
        self.id_ = id_
        self.name = name


class Manager(Employee, ManagerRole, SalaryPolicy):
    def __init__(self, id_, name, weekly_salary):
        SalaryPolicy.__init__(self, weekly_salary)
        super().__init__(id_, name)


class Secretary(Employee, SecretaryRole, SalaryPolicy):
    def __init__(self, id_, name, weekly_salary):
        SalaryPolicy.__init__(self, weekly_salary)
        super().__init__(id_, name)


class SalesPerson(Employee, SalesPersonRole, CommissionPolicy):
    def __init__(self, id_, name, weekly_salary, commission):
        CommissionPolicy.__init__(self, weekly_salary, commission)
        super(SalesPerson, self).__init__(id_, name)


class FactoryWorker(Employee, FactoryWorkerRole, HourlyPolicy):
    def __init__(self, id_, name, hours_worked, hour_rate):
        HourlyPolicy.__init__(self, hours_worked, hour_rate)
        super().__init__(id_, name)


class TemporarySecretary(Employee, SecretaryRole, HourlyPolicy):
    def __init__(self, id_, name, hours_worked, hour_rate):
        HourlyPolicy.__init__(self, hours_worked, hour_rate)
        super().__init__(id_, name)

