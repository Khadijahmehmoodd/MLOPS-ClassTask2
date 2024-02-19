
class StudentsInMLOps:
    def __init__(self):
        self.total_strength = 0
        self.class_name = "MLOps"

    def enrollStudents(self, num_students):
        if num_students > 0:
            self.total_strength += num_students
            print(f"{num_students} Students Enrolled Successfully.")
        else:
            print("No of Students to enroll should be greater than 0.")

    def dropStudents(self, num_students):
        if num_students > 0 and num_students <= self.total_strength:
            self.total_strength -= num_students
            print(f"{num_students} Students dropped successfully.")
        elif num_students <= 0:
            print("Number of students to drop should be greater than 0.")
        else:
            print("Invalid no of students to drop.")

    def getTotalStrength(self):
        return self.total_strength

    def getClassName(self):
        return self.class_name

# Example usage:
if __name__ == "__main__":
    mlops_class = StudentsInMLOps()
    mlops_class.enrollStudents(20)
    mlops_class.enrollStudents(10)
    print("Total Strength:", mlops_class.getTotalStrength())
    print("Class Name:", mlops_class.getClassName())
    mlops_class.dropStudents(5)
    print("Total Strength After Dropping Students:", mlops_class.getTotalStrength())
