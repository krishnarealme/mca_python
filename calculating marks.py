def marks(m1,m2):
    m1+=10
    m2+=20
    return m1,m2
M1=int(input("Enter the mark 1: "))
M2=int(input("Enter the mark 2: "))
new_M1,new_M2=marks(M1,M2)
print("Modified M1: ",new_M1)
print("Modified M2: ",new_M2)
