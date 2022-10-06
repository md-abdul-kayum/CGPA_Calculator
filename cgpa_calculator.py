semester=input("Enter Your Semester or Year to calculate Your CGPA: ")
print("You are calculating your"+" "+semester+" "+"semester's result...!")

a=int(input("Enter your total number of courses: "))
credit=0
res=[]
result=0
crdt=[]
r=[]
curs=[]
for gpa in range(a):
    course=input("Enter your course name: ")
    b=float(input("Enter the credit for"+" "+course+" "+"course: "))
    c=float(input("Enter your gpa for"+" "+course+" "+"course: "))
    credit=credit+b
    res.append(b*c)
    crdt.append(b)
    r.append(c)
    curs.append(course)


for i in range(len(res)):
    result=result+res[i]

result=result/credit

print("\n \n \t \t \t \t \t *** Your"+" "+ semester+" "+"semester's Transcript *** \t \t ")
print("\n \t \t \t \t \t \t Your gpa for"+" "+semester+" "+"semester is:",round(result,2))
print("\t \t \t \t Total Credit completed in this"+" "+semester+" "+"semester is:",credit)
print("\n \n \t \t \t \t Course_Name \t-----\t Credit \t-----\t Occupied_GPA \n")

for k in range(a):
    print("\t \t \t \t"+str(curs[k])+"\t-----\t\t"+str(crdt[k])+"\t-----\t\t\t"+str(r[k]))
