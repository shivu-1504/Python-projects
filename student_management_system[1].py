"""
2. Student Management System (OOP + File Handling)
Create class Student:

Features:

Add student

Save student to file

Read all students from file

Calculate average marks

Use:

JSON or text file

Exception handling
"""

print("====== Student Management System ======")

class Student:
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    def add_student(self):
        try:
            with open("students.txt", "a") as file:
                file.write(f"{self.name},{self.roll},{self.marks}\n")
            print(f"Student {self.name} added successfully.")
        except Exception as e:
            print(f"Error adding student: {e}")

    @staticmethod
    def read_students():
        students = []
        try:
            with open("students.txt", "r") as file:
                for line in file:
                    name, roll, marks = line.strip().split(",")
                    students.append(Student(name, roll, float(marks)))
            return students
        except FileNotFoundError:
            print("No students found. File does not exist.")
            return []
        except Exception as e:
            print(f"Error reading students: {e}")
            return []
        
    @staticmethod
    def calculate_average(students):
        if not students:
            print("No students to calculate average.")
            return 0
        total_marks = sum(student.marks for student in students)
        average = total_marks / len(students)
        return average

# Example Usage
if __name__ == "__main__":  
    s1 = Student("Alice", "101", 85)
    s2 = Student("Bob", "102", 90)
    s1.add_student()
    s2.add_student()
    students = Student.read_students()
    avg_marks = Student.calculate_average(students)
    print(f"Average Marks: {avg_marks:.2f}")
    