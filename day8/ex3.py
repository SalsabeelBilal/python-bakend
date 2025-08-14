class Person:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.__email = email

    def display_info(self):
        print(f"ID: {self.id}, Name: {self.name}, Email: {self.__email}")

    def get_email(self):
        return self.__email


class Student(Person):
    def __init__(self, id, name, email, major, gpa):
        super().__init__(id, name, email)
        self.major = major
        self.gpa = gpa
        self.courses_enrolled = []

    def enroll(self, course):
        if course not in self.courses_enrolled:
            self.courses_enrolled.append(course)
            print(f"{self.name} enrolled in {course}")
        else:
            print(f"{self.name} is already enrolled in {course}")

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.gpa < other.gpa
        return NotImplemented

    def __repr__(self):
        return f"Student(id={self.id}, name='{self.name}', gpa={self.gpa})"


class Professor(Person):
    def __init__(self, id, name, email, department):
        super().__init__(id, name, email)
        self.department = department
        self.courses_teaching = []

    def add_course(self, course):
        if course not in self.courses_teaching:
            self.courses_teaching.append(course)
            print(f"Professor {self.name} now teaches {course}")
        else:
            print(f"Professor {self.name} already teaches {course}")


if __name__ == "__main__":
    s1 = Student(1, "Alice", "alice@example.com", "Computer Science", 3.8)
    s2 = Student(2, "Bob", "bob@example.com", "Mathematics", 3.5)
    p1 = Professor(101, "Dr. Smith", "smith@example.com", "Engineering")

    s1.display_info()
    p1.display_info()

    s1.enroll("Python 101")
    s1.enroll("Algorithms")
    s1.enroll("Python 101")

    p1.add_course("Data Structures")
    p1.add_course("Algorithms")
    p1.add_course("Data Structures")

    print(f"Is {s1.name}'s GPA less than {s2.name}'s? {s1 < s2}")

    print(s1)
    print(s2)
