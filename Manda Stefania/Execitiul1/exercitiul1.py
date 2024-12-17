class Employee:
    """Common base class for all employees"""
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.tasks = {}
        Employee.empCount += 1

    def display_emp_count(self):
        "Displays the number of employees"
        print(f"Total number of employee(s) is {Employee.empCount}")

    def display_employee(self):
        print("Name :", self.name, ", Salary:", self.salary)

    def __del__(self):
        Employee.empCount -= 1

    def update_salary(self, new_salary):
        self.salary = new_salary

    def modify_task(self, task_name, status="New"):
        self.tasks[task_name] = status

    def display_task(self, status):
        print(f"Taskuri cu statusul {status}")
        for name in self.tasks.keys():
            if self.tasks[name] == status:
                print(name)

class Manager(Employee):
    mgr_count = 0  

    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        Nume_Echipa="F33 "
        self.department=Nume_Echipa+department

        Manager.mgr_count += 1

  
    def display_employee(self):
        print(f"Department:{self.department}")

    


manager1=Manager("Stefania",3900,"HR")
manager2=Manager("Diana",3950,"IT")
manager3=Manager("Amalia",3800,"Marketing")
manager4=Manager("Tudor",3500,"Finance")
manager5=Manager("Vlad",4000,"Sales")




manager1.display_employee()
manager2.display_employee()
manager3.display_employee()
manager4.display_employee()
manager5.display_employee()


employee1=Employee("Stefan",4300)
employee2=Employee("Rares",2256)




employee1.display_employee()
employee2.display_employee()




print(f"Număr total angajați (Employee.empCount): {Employee.empCount}")
print(f"Număr total manageri (Manager.mgr_count): {Manager.mgr_count}")
