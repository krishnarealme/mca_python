def check_number(value):
    if value>100:
        return "congrats"
    else:
        return "have a nice day"
user_input=int(input("Enter a number: "))
result=check_number(user_input)
print(result)





