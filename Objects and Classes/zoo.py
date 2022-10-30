class Zoo:

    def __init__(self, name_of_the_zoo):
        self.name_of_the_zoo = name_of_the_zoo
        self.mammals = []
        self.fish = []
        self.birds = []

    __animals = 0

    def add_animals(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fish.append(name)
        elif species == "bird":
            self.birds.append(name)

        Zoo.__animals += 1

    def get_info(self, species):

        result = ""

        if species == "mammal":
            result += f"Mammals in {name_of_the_zoo}: {', '.join(self.mammals)}\n"
        elif species == "fish":
            result += f"Fishes in {name_of_the_zoo}: {', '.join(self.fish)}\n"
        elif species == "bird":
            result += f"Birds in {name_of_the_zoo}: {', '.join(self.birds)}\n"

        result += f"Total animals: {Zoo.__animals}"
        return result


name_of_the_zoo = input()
zoo = Zoo(name_of_the_zoo)

number = int(input())

for i in range(number):
    animal = input().split(" ")

    species = animal[0]
    name = animal[1]

    zoo.add_animals(species, name)

specie = input()
print(zoo.get_info(specie))
