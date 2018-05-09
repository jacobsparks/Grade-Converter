#This is a simple program that converts a number grade into a letter grade.





def grade_converter(grade):
    if grade >= 94 and grade <= 100:
        return "A"
    elif grade >= 90 and grade < 94:
        return "A-"
    elif grade >=87 and grade < 90:
        return "B+"
    elif grade >= 84 and grade < 87:
        return "B"
    elif grade >= 80 and grade < 84:
        return "B-"
    elif grade >= 77 and grade < 80:
        return "C+"
    elif grade >= 74 and grade < 77:
        return "C"
    elif grade >= 70 and grade < 74:
        return "C-"
    elif grade >= 67 and grade < 70:
        return "D+"
    elif grade >= 64 and grade < 67:
        return "D"
    elif grade >= 61 and grade < 64:
        return "D-"
    elif grade > 100:
        return "off the charts"
    else:
        return "F"
while True:
    grade = int(input("Please enter what you made on the test here:"))        
    letter_grade = (grade_converter(grade))
    print("Your letter grade is " + str(letter_grade) + "!")




