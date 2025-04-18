class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5  # starting at middle value
        self.energy = 5  # starting at middle value
        self.happiness = 5  # starting at middle value
        self.tricks = []  # list to store learned tricks
    
    def eat(self):
        self.hunger = max(0, self.hunger - 3)  # reduce hunger by 3, but not below 0
        self.happiness += 1  # increase happiness by 1
        if self.happiness > 10:
            self.happiness = 10  # cap happiness at 10
        print(f"{self.name} ate some food! Yum!")
    
    def sleep(self):
        self.energy = min(10, self.energy + 5)  # increase energy by 5, but not above 10
        print(f"{self.name} took a nap and feels refreshed!")
    
    def play(self):
        self.energy = max(0, self.energy - 2)  # decrease energy by 2, but not below 0
        self.happiness = min(10, self.happiness + 2)  # increase happiness by 2, but not above 10
        self.hunger = min(10, self.hunger + 1)  # increase hunger by 1, but not above 10
        print(f"{self.name} played and had fun!")
    
    def get_status(self):
        print(f"\n--- {self.name}'s Status ---")
        print(f"Hunger: {self.hunger}/10 {'🍽️' if self.hunger > 7 else ''}")
        print(f"Energy: {self.energy}/10 {'😴' if self.energy < 3 else ''}")
        print(f"Happiness: {self.happiness}/10 {'😀' if self.happiness > 7 else '😢' if self.happiness < 3 else ''}")
        
    def train(self, trick):
        if trick not in self.tricks:
            self.tricks.append(trick)
            self.energy = max(0, self.energy - 1)  # training takes some energy
            self.hunger = min(10, self.hunger + 1)  # training makes pet hungry
            print(f"{self.name} learned how to {trick}!")
        else:
            print(f"{self.name} already knows how to {trick}!")
    
    def show_tricks(self):
        if not self.tricks:
            print(f"{self.name} doesn't know any tricks yet.")
        else:
            print(f"\n--- {self.name}'s Tricks ---")
            for i, trick in enumerate(self.tricks, 1):
                print(f"{i}. {trick}")