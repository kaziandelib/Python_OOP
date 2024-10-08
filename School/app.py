class Student:
    def __init__(self, name: str, age: int, grade=0) -> None:
        self.name = name
        self.age = age
        self.grade = grade # 0-100


    def get_grade(self) -> float:
        return self.grade


class Course:
    def __init__(self, name : str, max_students : int) -> None:
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def get_avg_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()

        return value / len(self.students)


s1 = Student("Richard", 20, 97)
s2 = Student("Donna", 19, 99)
s3 = Student("Garth", 19, 87)
s4 = Student("Wallace", 21, 78)
s5 = Student("Roy", 20, 79)


course = Course("NTT1980", 3)
course.add_student(s2)
course.add_student(s1)
course.add_student(s4)


print(course.students[0].name)

print(f'Avg grade is {course.get_avg_grade()}')
