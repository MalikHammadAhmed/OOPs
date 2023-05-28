class Employee:
    def __init__(self, emp_id, name, salary):
        self.__emp_id = emp_id
        self.__name = name
        self.__salary = salary

    def get_emp_id(self):
        return self.__emp_id

    def get_name(self):
        return self.__name

    def get_salary(self):
        return self.__salary

    def set_salary(self, new_salary):
        if new_salary > 0:
            self.__salary = new_salary
        else:
            print("invalid Salary")

#Creating an employee object
emp = Employee(101, "Hamid", 5000)

#Accessing employee information using getter methods
print(emp.get_emp_id())
print(emp.get_name())
print(emp.get_salary())

# Trying to access the attribute directly (without encapsulation)
print(emp.__salary)        # Throws an AttributeError

# Trying to modify the salary directly (without encapsulation)
emp.__salary = -1000       # Does not affect the actual salary

# Modifying the salary using the setter method (encapsulated access)
emp.set_salary(6000)       # Updates the employee salary

# Accessing the updated salary using the getter method
print(emp.get_salary())    # Prints the updated salary