from main import StudentsInMLOps

def test_StudentsInMLOps():
    mlops_class = StudentsInMLOps()

    # Test enrollStudents method
    mlops_class.enrollStudents(20)
    assert mlops_class.getTotalStrength() == 20

    # Test dropStudents method
    mlops_class.dropStudents(5)
    assert mlops_class.getTotalStrength() == 15

    # Test getClassName method
    assert mlops_class.getClassName() == "MLOps"

    print("All tests passed successfully.")

if __name__ == "__main__":
    test_StudentsInMLOps()
