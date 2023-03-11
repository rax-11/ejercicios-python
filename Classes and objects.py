from Student import Student # desde el archivo student quiero importar la clase student

student1 = Student("Jim", "Business", 3.56, False) # La clase es una plantilla de lo que un objeto es
student2 = Student("Pam", "Art", 3.346, True)
print(student1.name)
print(student1.gpa)
print(student2.major)
print(student2.is_on_probation)

print(student1.on_honor_roll())
print(student2.on_honor_roll())