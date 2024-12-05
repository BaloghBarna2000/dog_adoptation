class DogAdoption:
    def __init__(self):
        self.available_dogs = []
    
    def add_dog(self, name, age, breed):
        dog = {
            'name': name,
            'age': age,
            'breed': breed,
            'adopted': False
        }
        self.available_dogs.append(dog)
        return True
    
    def adopt_dog(self, name):
        for dog in self.available_dogs:
            if dog['name'] == name and not dog['adopted']:
                dog['adopted'] = True
                return True
        return False
    
    def list_available_dogs(self):
        return [dog for dog in self.available_dogs if not dog['adopted']]