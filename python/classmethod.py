class Animal:

    totalAnimals = 0

    @classmethod
    def tellMeHowManyAnimalsThereAre(cls):
        print('There are {} animals'.format(cls.totalAnimals))

    def __init__(self, weight):
        self.weight = weight
        Animal.totalAnimals += 1

    def speed(self):
        return 10/self.weight


anAnimal = Animal(10)
anAnimal.speed()


import pdb; pdb.set_trace()

