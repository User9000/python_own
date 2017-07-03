

###Clases ....objects
class Animal():
    name = 'amy'
    noise = "Grunt"
    size = "large"
    color = "brown"
    hair = "Covers body"
    def get_color(self):
        return self.color
    def make_noise(self):
        return self.noise

class Dog(Animal):
    name = 'Jon'
   # color = 'brown'

  #  def get_color(self):
     #   return self.color
   
jon = Dog()

print(jon.name)
print(jon.color)
print(jon.size)

         

