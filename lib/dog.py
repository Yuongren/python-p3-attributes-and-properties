#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name=None, breed=None):
        self._name = None
        self._breed = None
        self._initializing = True
        
        # Only set if provided
        if name is not None:
            self.name = name  # Will call set_name
        if breed is not None:
            self.breed = breed  # Will call set_breed
            
        self._initializing = False

    # Getter and setter for name
    def get_name(self):
        return self._name

    def set_name(self, name):
        if not isinstance(name, str) or not (1 <= len(name) <= 25):
            print("Name must be string between 1 and 25 characters.")
        else:
            if not self._initializing:
                print(f"Setting name to {name}")
            self._name = name

    name = property(get_name, set_name)

    # Getter and setter for breed
    def get_breed(self):
        return self._breed

    def set_breed(self, breed):
        if breed in APPROVED_BREEDS:
            if not self._initializing:
                print(f"Setting breed to {breed}")
            self._breed = breed
        else:
            print("Breed must be in list of approved breeds.")

    breed = property(get_breed, set_breed)