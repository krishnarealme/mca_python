names={'K':'Krishna','R':'Raja','A':'Arun'}
word=input("Enter the first letter of your friends name: ").upper()
friend_name=names.get(word,"Try another letter")
print(friend_name)
