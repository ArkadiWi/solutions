import sys


class Critter(object):
    def __init__(self, name='no name', hunger=0, boredom=0):
        self.__name = name
        self.__hunger = hunger
        self.__boredom = boredom
        print(
            f'It\'s your lucky day - you\'ve created new animal: {self.__name}. Good for you!!!!')

    def __pass_time(self):
        self.__hunger += 2
        self.__boredom += 2

    def __str__(self):
        return f'I\'m Critter object. My name is: {self.__name}. And I\'m {self.mood}'

    @property
    def mood(self):
        mood = self.__boredom + self.__hunger
        if mood < 5:
            m = 'I\'m happy'
        elif 5 <= mood <= 10:
            m = 'I\'m glad'
        elif 10 <= mood <= 15:
            m = 'I\'m angry'
        else:
            m = 'I\m furious'
        return m

    def talk(self):
        print(f'My name is {self.__name} And I\'m {self.mood}')

    def name(self):
        return self.__name

    def eat(self, food=2):
        print(f'{self.__name} - Yummy yummy, delicious food!!!!')
        self.__hunger -= food
        if self.__hunger < 0:
            self.__hunger = 0
        self.__pass_time()

    def play(self, fun=2):
        print(f'{self.__name} - Hurray - great fun')
        self.__boredom -= fun
        if self.__boredom < 0:
            self.__boredom = 0
        self.__pass_time()


farmAnimals = {}
pet = None
whitchAnimal = None


def makeLife():

    name = input('What is the name of the new creature?... ')
    if name not in farmAnimals.values():
        name = Critter(name)
        farmAnimals[len(farmAnimals) + 1] = name

    else:
        print(f'The creature {name} already exist, make a new choice')
        menu1()


def showLife():
    print(f'There are {len(farmAnimals)} animals on the farm already\n')
    if len(farmAnimals) > 0:
        for number, name in farmAnimals.items():
            print(f'{number})....{name.name()}')
        menu2()
    else:
        print('You have to create one')
        menu1()


def oneAnimalInnerLoop():
    print(f'''\n\t Menu:
            0) Return to main menu
            1) Return to other Pets
            2) Feed {pet.name()}
            3) Play with {pet.name()}
            4) Listen to {pet.name()}
            5) Kill {pet.name()}
            ''')
    choose = input('Make your decision...')

    if choose == '0':
        menu1()

    elif choose == '1':
        showLife()

    elif choose == '2':
        pet.eat()

    elif choose == '3':
        pet.play()

    elif choose == '4':
        pet.talk()

    elif choose == '5':
        print(
            f':-(  A {pet.name()} will be killed\n\t.....Good bye cruel world....')
        del farmAnimals[whichAnimal]
        showLife()
    else:
        print('Bad choice, try again')
        oneAnimal()
    oneAnimalInnerLoop()


def oneAnimal():
    global pet, whichAnimal

    if len(farmAnimals) > 0:
        try:
            whichAnimal = int(input(
                'Choose which number of pets you want to take care of:'))
        except ValueError:
            print(
                'Bad choice. Try again.')
            showLife()

        if whichAnimal not in farmAnimals:
            print('Bad choice, try again')
            showLife()
        else:
            pet = farmAnimals[whichAnimal]
            oneAnimalInnerLoop()

    else:
        print('You have to create one')
        menu1()


def allAnimals():
    if len(farmAnimals) > 0:
        print('''\n\t Menu:
        0) Return to main menu
        1) Feed all animals
        2) Play with all animals
        3) Listen to your animals
        4) Kill all animals
        ''')
        choose = input('Make your decision...')

        if choose == '0':
            menu1()
        elif choose == '1':
            for number, name in farmAnimals.items():
                name.eat()

        elif choose == '2':
            for number, name in farmAnimals.items():
                name.play()

        elif choose == '3':
            for number, name in farmAnimals.items():
                name.talk()

        elif choose == '4':
            print(':-(  All animals will be killed\n.....Good bye cruel world....')
            farmAnimals.clear()
            showLife()
        else:
            print('Bad choice, try again')
            allAnimals()

        allAnimals()
    else:
        print('You have to create one')
        menu1()


def menu1():

    choice = None
    while choice != 0:
        print('''\n\t Menu:
        0) Finish the program
        1) Create a new life
        2) Show: what animals are on the farm \n\t\t and other instructions.
        ''')

        choice = input('Choose an option: ')

        if choice == '0':
            print('Good bye')
            sys.exit(0)
        elif choice == '1':
            makeLife()
        elif choice == '2':
            showLife()
        else:
            print('Bad choice, try again')
            menu1()


def menu2():
    print('''\n\t Here you can choose what to do:
    0) Back to main menu
    1) Pick one animal
    2) Pick all animals
    ''')
    choose = input('Make your decision...')
    if choose == '0':
        menu1()
    elif choose == '1':
        oneAnimal()
    elif choose == '2':
        allAnimals()
    else:
        print('Bad choice, try again')
        menu2()


def main():

    menu1()


main()

input('Press Enter to finish')
