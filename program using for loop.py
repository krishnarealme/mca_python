def calc_square(number):
    return number** 2
values=[]
for i in range(5):
    value=float(input(f"Enter value{i+1}: "))
    values.append(value)
for value in values:
    square=calc_square(value)
    print(f"The square of {value} is:{square}")
