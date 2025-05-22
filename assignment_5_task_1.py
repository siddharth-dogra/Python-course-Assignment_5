records={'john':85,'jacob':80,'rohan':90,'siddharth':90}
name=input("Enter the student's name: ")
value=name in records
if value== False:
    print("student not found")
else:
    print("{}'s marks:".format(name), records[name])
