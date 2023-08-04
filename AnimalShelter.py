class AnimalShelter:
    def __init__(self):
        self.cats = []
        self.dogs = []

    def enqueue(self, animal, typeAnimal):
        if typeAnimal == "Cat":
            self.cats.append(animal)
        else:
            self.dogs.append(animal)

    def dequeueCat(self):
        if len(self.cats) == 0:
            return None
        else:
            cat = self.cats.pop(0)
            return cat

    def dequeueDog(self):
        if len(self.dogs) == 0:
            return None
        else:
            dog = self.dogs.pop(0)
            return dog

    def dequeueAny(self):
        if len(self.cats) == 0 or len(self.dogs) == 0:
            return None
        else:
            result = self.dogs.pop(0)
        return result