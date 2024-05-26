from datetime import datetime, timedelta

class Employee:
    def __init__(self, name, hours_worked=0, overtime_hours=0):
        self.name = name
        self.hours_worked = hours_worked
        self.overtime_hours = overtime_hours

    def mark_attendance(self, hours):
        self.hours_worked += hours
        if hours > 8:
            self.overtime_hours += hours - 8

    def get_overtime(self):
        return self.overtime_hours

class Attendance:
    def __init__(self):
        self.employees = {}

    def add_employee(self, name):
        self.employees[name] = Employee(name)

    def mark_attendance(self, name, hours):
        if name in self.employees:
            self.employees[name].mark_attendance(hours)
    def get_overtime(self):
        for employee in self.employees.values():
            print(f"{employee.name} has worked {employee.get_overtime()} overtime hours.")

# create an attendance object
attendance = Attendance()

# add employee
attendance.add_employee("Ali Raza Baloch")
attendance.add_employee("Ali Raza Baloch")

# mark attendance for a year
for i in range(365):
    attendance.mark_attendance("Ali Raza Baloch", 8)  # regular 8 hours
    attendance.mark_attendance("Ali Raza Baloch", 9)  # 1 hour overtime per day

# calculate and print overtime hours for all employees
attendance.get_overtime()