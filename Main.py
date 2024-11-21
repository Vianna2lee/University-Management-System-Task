class person:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    
    def set_details(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender

        print(f"Name: {self.name}, Age: {self.age},Gender: {self.gender}")



class student(person):
    def __init__(self, name,age,gender, student_id, course):
        super().__init__(name,age,gender)
        self.student_id=student_id
        self.course= course
        self.grades=[]

    def set_student_details(self,student_id,course):
        self.student_id=student_id
        self.course= course
    
    def add_grade(self,grade):
        (self.grades).append(grade)
    
    def calculate_average_grade(self):
        if self.grades==[]:
            self.avg_grade=0
        else:
            self.avg_grade= sum(self.grades)/len(self.grades)

    def get_student_summary(self):
        print(f"student ID: {self.student_id} Course: {self.course} Avg grade: {self.avg_grade}")


class professor(person):
    def __init__(self,name,age,gender,staff_id,department,salary):
        super().__init__(name,age,gender)
        self.staff_id=staff_id
        self.department=department
        self.salary=salary

    def set_professor_details(self,staff_id, department, salary):
        self.staff_id=staff_id
        self.department=department
        self.salary=salary

    def give_feedback(self,student,feedback):
        print ("Feedback for {student.name} ")









Fathima=person("Fathima",18,"Male")


Fathima= student("Fathima",18,"Male","S5462","CS")
Fathima.set_details("Fathima",17,"Female")

Fathima.add_grade(89)
Fathima.add_grade(22)
Fathima.add_grade(78)
Fathima.add_grade(88)
Fathima.add_grade(72)

Fathima.calculate_average_grade()

Fathima.get_student_summary()