class Student:
    def __init__(self,name,scores) -> None:
        self.name = name
        self.scores = scores
    
    def calculate_average(self) -> int:
       if len(self.scores) > 0:
           return sum(self.scores) / len(self.scores)
       return 0
    
    def is_passing(self,passing = 40):
        average = self.calculate_average()
        return average >= passing
    

class Performance_tracker:
    def __init__(self) -> None:
        self.students_record = {}

    def add_students(self):
        while True:
            try:
                student_name = input("\nEnter student name (or type stop to stop) : ").lower().strip()
                if student_name == "stop":
                    break
                grades = input("Enter marks in 3 subjects (math , science and English respectively) Ensure their is space in it :  ").strip()
                student_grades = [int(grade) for grade in grades.split()]
                
                if student_name in self.students_record:
                    self.students_record[student_name].scores = student_grades
                else:
                    self.students_record[student_name] = Student(student_name,student_grades)
                
                print(f"Updated dictionary : {self.get_students_data()}")

            
            except ValueError :
                print("Please enter a Valid Marks")
            except Exception as error : 
                print(error)

    def calculate_class_average(self):
        total_scores = []
        for i in self.students_record.values():
            total_scores.extend(i.scores)
        average = sum(total_scores) / len(total_scores)
        print(f"Class Average : {average:.2f}")

    def display_student_performance(self):
        for student in self.students_record.values():
            average = student.calculate_average()
            passing = f"PASS" if student.is_passing() else "FAIL"
            print(f"{student.name} : Average : {average:.2f} , Status : {passing}")
    
    def get_students_data(self):
        return {name: student.scores for name, student in self.students_record.items()}
    

tracker = Performance_tracker()
tracker.add_students()
tracker.display_student_performance()
tracker.calculate_class_average()
