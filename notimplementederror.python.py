class Animal:
    def __init__(self,name):
        self.name=name
    def sound(self):
        return NotImplementedError('you have to define this method in your subclasses')
class Dog(Animal):
     def __init__(self,name,breed):
          super().__init__(name)
          self.breed=breed
     def sound(self):
        return 'bhow bhow'
class Cat(Animal):
      def __init__(self,name,breed):
          super().__init__(name) 
          self.breed=breed
      def sound(self):
        return 'meao meao'
doggy=Dog('tipu','normal')
print(doggy.sound())        
