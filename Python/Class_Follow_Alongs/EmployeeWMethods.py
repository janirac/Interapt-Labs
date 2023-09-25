class EmployeeWMethods:
    def __init__(self, empID, empName, empDept, empSalary):
        self._emp_ID = empID
        self._emp_name = empName
        self._emp_dept = empDept
        self._emp_salary = empSalary
        
    @property
    def emp_salary(self):
        return self._emp_salary
    
    @emp_salary.setter
    def emp_salary(self, new_emp_salary):
        if 30_000 <= new_emp_salary <= 200_000:
            self._emp_salary = new_emp_salary
        else:
            print(f'Passed value of {new_emp_salary} not in range. Salary set to None')
            self._emp_salary = None
            
    def print_me(self):
        print(f'{self._emp_ID = }\t{self._emp_name = }\t{self._emp_dept = }\t{self._emp_salary = }')
        
    def give_emp_pct_raise(self, pct_raise):
        if pct_raise < 10 or pct_raise > 20:
            print(f'Raise percentage {pct_raise} out of range - no chnage made')
        elif self._emp_salary is None:
            print(f'Employee with ID = {self._emp_ID} has no valid salary - no change made')
        else:
            self._emp_salary = self._emp_salary * (1 + pct_raise/100)
            
    