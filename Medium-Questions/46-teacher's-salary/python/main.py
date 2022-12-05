import os, sys


class Teacher:

    def __init__(self, salary):
        try:
            salary = float(salary)
        except ValueError:
            raise ValueError("Salary must be Number")
        else:
            self.salary = salary

    def calculate_salary(self):
        if self.salary < 4_000_000:
            return f"Teacher Salary: {4_000_000 + 0.5 * self.salary / 100}\n 0.5% of \33[32m {self.salary} \33[0m => {0.5 * self.salary / 100}"
        if self.salary >= 4_000_000 or self.salary < 7_000_000:
            return f"Teacher Salary: {self.salary + 12 * self.salary / 100}\n 12% of \33[32m {self.salary} \33[0m => {12 * self.salary / 100}"
        if self.salary > 7_000_000:
            return f"Teacher Salary: {self.salary + 10 * self.salary / 100}\n 10% of \33[32m {self.salary} \33[0m => {10 * self.salary / 100}"


def main():
    teacher = Teacher(58040000)
    print(teacher.calculate_salary())



if __name__ == '__main__':
    main()