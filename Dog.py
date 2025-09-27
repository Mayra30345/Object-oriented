class Dog:
    animal='dog'
    def __init__(self,breed,colour):
     self.breed=breed
     self.colour=colour


Rodger= Dog( "Pug" , "Brown" )
Bruzo= Dog( "Bulldog" , "Black" )
print("Rodger details:  ")
print("Rodger is a ",Rodger.animal)
print("Breed: ",Rodger.breed)
print("Colour:",Rodger.colour)

print("\n Bruzo details:  ")
print("Bruzo is a ",Bruzo.animal)
print("Breed: ",Bruzo.breed)
print("Colour:",Bruzo.colour)
