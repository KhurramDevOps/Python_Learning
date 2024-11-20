# Student Performance Tracker

This Python program allows for the management and tracking of student performance through a command-line interface. It enables users to add student information, calculate averages, and determine passing status.

## Classes

### Student

The `Student` class represents a student with a name and their scores in various subjects.

#### Attributes

- `name`: The name of the student (string).
- `scores`: A list of scores (list of integers).

#### Methods

- `__init__(self, name, scores)`: Initializes a student with a name and their scores.
- `calculate_average(self) -> int`: Calculates and returns the average score of the student. Returns `0` if there are no scores.

- `is_passing(self, passing=40)`: Determines if the student is passing based on their average score. The default passing score is `40`.

```python
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
```

### Performance_tracker

The `Performance_tracker` class manages a collection of students and their performance.

#### Attributes

- `students_record`: A dictionary that stores student names as keys and `Student` objects as values.

#### Methods

- `__init__(self)`: Initializes an empty student record.

- `add_students(self)`: Prompts the user to input student names and scores. The input loop continues until the user types "stop". Updates existing student scores if the name already exists.

```python
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
```

- `calculate_class_average(self)`: Calculates and prints the average score of the entire class.

- `display_student_performance(self)`: Displays each student's average score and passing status.

- `get_students_data(self)`: Returns a dictionary of student names and their scores.

```python
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

```

## Usage

1. **Adding Students**:

   - Run the program, and it will prompt you to enter student names and their scores in three subjects (math, science, and English).
   - Enter scores separated by spaces.
   - Type "stop" to finish adding students.

2. **Displaying Performance**:

   - After adding students, the program will display each student's average score and their passing status (PASS/FAIL).

3. **Calculating Class Average**:
   - The program will also calculate and display the average score of the entire class.

## Example

```plaintext
Enter student name (or type stop to stop) : John
Enter marks in 3 subjects (math, science and English respectively): 45 55 65
Updated dictionary : {'john': [45, 55, 65]}

Enter student name (or type stop to stop) : Jane
Enter marks in 3 subjects (math, science and English respectively): 30 40 50
Updated dictionary : {'john': [45, 55, 65], 'jane': [30, 40, 50]}

Enter student name (or type stop to stop) : stop

john : Average : 55.00 , Status : PASS
jane : Average : 40.00 , Status : PASS
Class Average : 47.50
```
