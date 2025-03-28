def greet():
    print("Hello, dear world!")
    print("End of the greet function.")

greet()
name1 = "Thor"
name2 = "Joel"
list_of_names = ["Katja", "Olga","Tim"]

for name in list_of_names:
    print("Hello, ", name)

def greet_person(name):
    print("Hello, ", name)
    print("End of the greet_person function.")

greet_person(name=name1)
greet_person(name1)
greet_person(name2)

greet_person(name="Najat")
greet_person(name="Zito")

greet_person("Hanno")

for name in list_of_names:
    greet_person(name)