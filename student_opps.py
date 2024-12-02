class student:
    def __init__(self ,Name ,Rollnmuber  ,Marks):
        self.Name =Name
        self.Rollnmuber =Rollnmuber 
        self.Marks =Marks

    def display_details(self):
        return f"Name: {self.Name} ,RollNumber: {self.Rollnmuber} ,Marks: {self.Marks}"

def main():

    student_1 = student("Ajmal" ,204, 48.9)
    student_2 = student("Hamad" ,306, 48.9)

    print("Details the student_1")
    print(student_1.display_details())

    print("\nDetails the student_2")
    print(student_2.display_details())


if __name__ =="__main__":
    main()


