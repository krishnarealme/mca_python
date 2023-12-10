count_10=0
for i in range(5):
    value=int(input(f"Enter value {i+1}: "))
    if value>10:
        count_10+=1
print(f"Number of values greater than 10 is: {count_10}")
