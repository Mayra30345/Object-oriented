class Parrot:
    species="bird"
    def __init__(self,name,age):
        self.name=name
        self.age=age
blue=Parrot("blue",10)
wool=Parrot("wool",13)
print(f"Blue is a {(blue.species)}")
print("Wool is also a {}".format(wool.species))
print("{} is {} years old".format(blue.name,blue.age))
print("{} is {} years old".format(wool.name,wool.age))