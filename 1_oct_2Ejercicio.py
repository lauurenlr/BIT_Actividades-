edades = [12, 17, 8, 15, 22, 9, 30, 25] #Creating list
for edad in edades: #Creating loop for to iterate on list age
    if (edad == 25): #If the age is 25 years, to print "you found  25 year-old student"
        print(f"La edad del estudiante es {edad}") #To remember to put "f", because "f" find variable declared
        break  # To exit the loop when it find the age 25 year
    else: #If the age is not 25 year, it doesn't imprime nothing
        continue #To pass the next number

print ("¡Encontramos al estudiante de 25 años! Deteniendo el análisis")
print("____________________________________________________________________")

for edad in edades: #Creating loop for to iterate on list age
    if (edad < 10): #If the ages are less than 10, do nothing
        continue
    elif (edad >= 18): #If the ages are greater than or equal to 18, to find this range
        print(f"Adulto: {edad} años")

    elif (10 < edad < 18): #If the ages are greater than 10 but less than 18, find this range
        print(f"Menor: {edad} años")
print("____________________________________________________________________")
print("Second exercise: Students list")
#Second part
students =  ["Juan", "Pedro", "Jorge", "María","Ana"] #Creating list
i = 0 #Creando posición 1
while i < len(students): #Position i must be less than the length of the student list
    student = students[i] #Position i
    i=i+1 #The iterate or position to increase

    if student == "Ana":
        print (f"{student} está en la lista")
        break
    elif student.startswith("J"): #If the name starts with "J", it doesn't print anything.
        continue
    print (student)


