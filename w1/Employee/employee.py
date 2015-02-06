class HourlyEmployee():
    def __init__(self, name, hourly_wage):
        self.name = name
        self.hourly_wage = hourly_wage

    def getName(self):
        return self.name

    def weeklyPay(self, hours):
        payA = 0
        if hours > 40:
            payA = 40*self.hourly_wage 
            rest_h = hours - 40
            rest_pay = rest_h*self.hourly_wage*(1.5)
            pay = payA + rest_pay
        else:
            pay = hours*self.hourly_wage


        return float(payA)

class SalariedEmployee():
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary    

    def weeklyPay(self, hours):
        return self.salary/52


    def getName(self):
        return self.name


class Manager(SalariedEmployee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def weeklyPay(self, hours):
        pay = super().weeklyPay(hours) + self.bonus

        return pay


    def getName(self):
        return self.name


if __name__ == '__main__':
    staff = []
    staff.append(HourlyEmployee("Morgan, Harry", 30.0))
    staff.append(SalariedEmployee("Lin, Sally", 52000.0))
    staff.append(Manager("Smith, Mary", 104000.0, 50.0))
    for employee in staff :
        hours = int(input("Hours worked by " + employee.getName() + ": "))
        pay = employee.weeklyPay(hours)
        print("Salary: %.2f" % pay)


