class Person:
    def __init__(self,name,lastname):
        self.name=name
        self.lastname=lastname
    def print_person(self):
        print(f"{self.name} {self.lastname}")


class Employee(Person):
    def __init__(self,name,lastname,employee_id):
        super().__init__(name,lastname)
        self.employee_id=employee_id
    def print_employee(self):
        print(f"My name is: {self.name} {self.lastname}, employee number {self.employee_id}")

steve=Employee("Steve", "Carrell", 1234)
steve.print_employee()
steve.print_person()
