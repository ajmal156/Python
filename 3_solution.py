score=(int)(input("ENTER THE SCORE PERSENT:"))
if score >=101:
    print("Sorry this value is no define.")
    exit()

if score>=90:
    grade="A"
elif score>=80:
    grade="B"
elif score>=70:
    grade="C"
elif score>=60:
    grade="D"
else:
    grade="F"

print("GRADE:",grade)            