class Duck:
   def fly(self):
      print("Flap flap flap.")

   def sound(self):
      print("Quack Quack!")


class Airplane:
   def fly(self):
      print("Wroooomm!")


class Dog:
   def sound(self):
      print("Woof woof!")


def flyaway(flyer):
   flyer.fly()

def animal_sounds(animal):
   animal.sound()

if __name__ == '__main__':
   flyables = [Duck(), Airplane()]
   animals = [Duck(), Dog()]

   for flyable in flyables:
      flyaway(flyable)

   for animal in animals:
      animal_sounds(animal)