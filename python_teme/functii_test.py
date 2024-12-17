import pytest
from ex1 import Employee, Manager

# test pentru crearea unui obiect Employee
def test_employee_creation():
    emp = Employee("Ioana", 5000)
    assert emp.name == "Ioana"
    assert emp.salary == 5000
    assert Employee.empCount == 1

# test pentru crearea unui obiect Manager
def test_manager_creation():
    mgr = Manager("Marin", 7000, "HR")
    assert mgr.name == "Marin"
    assert mgr.salary == 7000
    assert mgr.department == "F33-HR"
    assert Manager.mgr_count == 1

# test pentru verificarea empCount și mgr_count
def test_counts_increment():
    emp1 = Employee("Ana", 4000)
    emp2 = Employee("Maria", 4500)
    mgr1 = Manager("Andrei", 8000, "IT")
    assert Employee.empCount == 3
    assert Manager.mgr_count == 1

if __name__ == "__main__":
    pytest.main()

