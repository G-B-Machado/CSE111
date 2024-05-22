import csv

def read_dictionary(filename):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.
    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    dictionary = {}

    with open(filename, "r") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)

        for student in reader:
            if len(student) != 0:
                dictionary[student[0]] = student[1]

    return dictionary

def search_students(dictionary, id_student):
    if id_student in dictionary:
        print(dictionary[id_student])
    else:
        print("No such student")
def main():
    students = read_dictionary("week5/students.csv")
    student_id = input("Please, insert the student id: ")
    search_students(students, student_id)
   
if __name__ == "__main__":
    main()