class Employee:
      def __init__(self,name,loss,gain,text):
        self.name=name
        self.gain=gain
        self.loss=loss
        self.text=text
        
      def show_emp(self):
             print(f"COMPANY NAME:{self.name}|")
             print(f"PROFIT $:{self.gain}    |")
             print(f"LOSS $:{self.loss}      |")
             print(f"TEXT PAY :{self.text}   |")
             
name=input("COMPANY NAME =...:")
print(":__________________________________:")
gain=input("PROFIT =..:")
print(":__________________________________:")
loss=input("LOSS =..:")
print(":__________________________________:")
text=float(input("TEXT PAY =...:"))
emp=Employee(name,gain, loss,text)
print("DISPLAY DETAILS...:")
emp.show_emp()
print(":__________________________________:")
