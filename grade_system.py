def grade_calculate(score):
    if score > 1100 or score < 0:
        return "Invalid Score"  # Invalid if score is beyond the range
    if score >= 985:
        return 'A1+'
    if score >= 880:
      return 'A1'
    if score >= 785:
        return 'A'
    if score >= 670:
        return 'B'
    if score >= 585:
        return 'C'
    if score >= 500:
        return 'D'
    if score >= 300:
        return 'E'  # Below D but passing
    else:
        return 'Fail'  

def grade_calculate_student():
    while True:
        try:
            student_name =input("Enter the student name:")
            score =int(input(f"Enter the score {student_name} scored  is: "))

            if score > 1100 or score <0 :
                print("sorry ,Please enter the number between 0 to 1100.")
                continue
            
            grade =grade_calculate(score)
            print(f"{student_name} scored {score} and received by grade in {grade}")
    
            
            another_student =input("Do you want to another student ('Yes'\'No'): ").lower()
            if another_student != 'yes':
             print("Exiting the student grading system!. GoodBy!")
             break
        except ValueError:
            print("Sorry , invalid please enter the numeric number.")

 
grade_calculate_student()
    










    

    

