password= input("ENTER THE PASSWORD:")
password_length=len(password)
if password_length<8:
    string="Wake"
elif password_length<11:
    string="Normal"
else:
    password_length="Strong"

print("PASSWORD STRINGTH IS:" ,string)            