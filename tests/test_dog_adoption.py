import unittest
from dog_adoption import DogAdoption

class TestDogAdoption(unittest.TestCase):

    def setUp(self):
        self.shelter = DogAdoption()

    # Unit Test: Kutya hozzáadása
    def test_add_dog(self):
        result = self.shelter.add_dog("Buddy", 2, "Golden Retriever")
        self.assertTrue(result)
        self.assertEqual(len(self.shelter.available_dogs), 1)

    # Unit Test: Örökbefogadás
    def test_adopt_dog_success(self):
        self.shelter.add_dog("Buddy", 2, "Golden Retriever")
        result = self.shelter.adopt_dog("Buddy")
        self.assertTrue(result)

    # Unit Test: Sikertelen örökbefogadás
    def test_adopt_dog_failure(self):
        result = self.shelter.adopt_dog("Buddy")
        self.assertFalse(result)

    # Integration Test: Kutyalista örökbefogadás után
    def test_list_available_dogs(self):
        self.shelter.add_dog("Buddy", 2, "Golden Retriever")
        self.shelter.add_dog("Bubuka", 3, "Labrador")
        self.shelter.adopt_dog("Buddy")
        available_dogs = self.shelter.list_available_dogs()
        self.assertEqual(len(available_dogs), 1)
        self.assertEqual(available_dogs[0]['name'], "Charlie")

if __name__ == "__main__":
    unittest.main()
