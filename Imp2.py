class Var:
    def __init__(self,id,name,sal,dept):
        self.id=id
        self.name=name
        self.sal=sal
        self.dept=dept
    def display_emp(self):
        print(f"emp ID:{self.id}          |")
        print(f"emp NAME:{self.name}       |")
        print(f"emp SALARY:{self.sal}   |")
        print(f"emp DEPARTMENT:{self.dept}  |")
id=int(input("enter ID..:"))
print(":_________________________________________________:")
name=input("enter NAME..:")
print(":_________________________________________________:")
sal=float(input("enter SALARY..:"))
print(":_________________________________________________:")
dept=input("enter which depart emp work..:")
print(":_________________________________________________:")
emp=Var(id,name,sal,dept)
print("DISPAY DETAILS...:")
emp.display_emp()
print(":_______________________________________________________:")
