#Generating a python code for revision of basics 
class Animal:
    def sound(self,voice):
        print(voice,"\n")
    def eats(self, meat):
        if meat != False:
            print("Carnivore\n")
        else:
            print("Herbivore")
cat = Animal()
cat.sound("meow")
cat.eats(True)
