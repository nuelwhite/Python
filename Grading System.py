marks = int(input("Enter your marks: "))        # takes input from user

if marks >= 90:         # if marks is greater than or equal to 90, print Grade A
    print("Grade: A")   # ...
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
elif marks >= 60:
    print("Grade: D")
else:
    print("Grade: F")   # ...