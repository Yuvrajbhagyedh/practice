is_student=input("are u a student ? true or false ?: ").lower()=="true"
age=int(input("enter ur age: "))

if is_student and age<25:
    print("full discount")
elif is_student and age>=25 and age<=100:
    print("half discount")
else:
    print("not eligible")    