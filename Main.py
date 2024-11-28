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

    def give_feedback(self,Student,feedback):
        print (f"Feedback for {Student.name}: {feedback}")
    
    def increase_salary(self):
        self.salary=self.salary*(1.1)

    def get_professor_summary(self):
        print(f"Staff ID: {self.staff_id}  Department: {self.department}  Salary:{self.salary} ")






class administrator (person):
    def __init__(self,name,age,gender, admin_id,office,years_of_service):
        super().__init__(name,age,gender)
        self.admin_id=admin_id
        self.office=office
        self.years_of_service=years_of_service
    
    def set_admin_details(self, admin_id, office, years_of_service):
        self.admin_id=admin_id
        self.office=office
        self.years_of_service=years_of_service

    def increment_service_years(self):
        self.years_of_service += 1

    def get_admin_summary(self ):
        print(f" Admin ID: {self.admin_id}  Office: {self.office}  Years of service: {self.years_of_service} ")


Professor=professor("Dr. Imran",99,"Female","Fathima1234", "Econ", 1000)

Fathima = student("Fathima Williams", 3, "Female", "1am0thered", "CS")
Fathima.add_grade(89)
Fathima.add_grade(79)
Fathima.add_grade(99)
Fathima.calculate_average_grade()
Fathima.get_student_summary()


Professor.give_feedback(Fathima, "Great work on your assignment!")
Professor.increase_salary()
Professor.get_professor_summary()


Marli=administrator ("Marli", 39, "Female", "TToTT", "U38, Teacher Block", 5)
Marli.increment_service_years()
Marli.get_admin_summary()