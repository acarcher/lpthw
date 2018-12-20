from sys import exit, stdout
from time import sleep
from random import random, randrange


class character():
    def __init__(self, conscious="asleep", timeleft=3, money=0, loc="home", day=1, str=0, int=0, cha=0, mod=1, str_diff=0, int_diff=0, cha_diff=0):
        self.conscious = conscious
        self.timeleft = timeleft
        self.money = money
        self.loc = loc
        self.day = day
        self.str = str
        self.int = int
        self.cha = cha
        self.mod = mod
        self.str_diff = str_diff
        self.int_diff = int_diff
        self.cha_diff = cha_diff

    def increase(self, trait, amount):
        setattr(self, trait, getattr(self, trait) + amount)

    def decrease(self, trait, amount):
        setattr(self, trait, getattr(self, trait) - amount)

    def moveTo(self, location):
        setattr(self, "loc", location)

    def hasTime(self):
        return self.timeleft > 0

    def isAt(self, location):
        return self.loc == location

    def checkStats(self):
        return ((self.str >= 50 and self.int >= 50 and self.cha >= 50 and self.money >= 100) or
                ((self.str >= 100 or self.int >= 100 or self.cha >= 100) and self.money >= 100))

    def stats(self):
        chat("It is day " + str(self.day) + ".", self)
        chat("You are at " + self.loc + ".", self)
        chat("You have " + str(self.timeleft) + " actions left.", self)
        chat("You have " + str(self.money) + " dollars.", self)
        chat("Your stats are:", self)
        chat("str: " + str(self.str), self)
        chat("int: " + str(self.int), self)
        chat("cha: " + str(self.cha), self)

    def state(self):
        return self.conscious

    def wakeUp(self):
        setattr(self, "conscious", "awake")


def home(player):
    arrival = "You arrive at your house, you have " + str(player.timeleft) + " actions left."
    chat(arrival, player)

    player.moveTo("home")

    choices = "While at home, you may (sleep) to restore your actions."
    chat(choices, player)


def bar(player):
    arrival = "You arrive at the bar, you have " + str(player.timeleft) + " actions left."
    chat(arrival, player)

    player.moveTo("bar")
    player.cha_diff = int(randrange(10, 100) * player.mod)
    player.str_diff = int(randrange(10, 100) * player.mod)

    choices = (
        "While at the bar you may (drink), (hit on)[" +
        str(player.cha) + "/" + str(player.cha_diff) + "] girls, " +
        "and get into a fist (fight)[" +
        str(player.str) + "/" + str(player.str_diff) + "].")

    chat(choices, player)


def school(player):
    arrival = "You arrive at school, you have " + str(player.timeleft) + " actions left."
    chat(arrival, player)

    player.moveTo("school")
    player.int_diff = int(randrange(10, 100) * player.mod)
    choices = (
        "While at school you may (study) or take a (test)[" +
        str(player.int) + "/" + str(player.int_diff) + "].")
    chat(choices, player)


def gym(player):
    arrival = "You arrive at the gym, you have " + str(player.timeleft) + " actions left."
    chat(arrival, player)

    player.moveTo("gym")
    player.str_diff = int(randrange(10, 100) * player.mod)
    choices = (
        "While at the gym you may (exercise) or play a (pickup) game[" +
        str(player.str) + "/" + str(player.str_diff) + "].")
    chat(choices, player)


def job(player):
    arrival = "You arrive at your job, you have " + str(player.timeleft) + " actions left."
    chat(arrival, player)

    player.moveTo("job")

    choices = "While at your job you may (work)."
    chat(choices, player)


def mall(player):
    arrival = "You arrive at the mall, you have " + str(player.timeleft) + " actions left."
    chat(arrival, player)

    player.moveTo("mall")

    intro = "While at the mall you see the girl you've been looking for."
    chat(intro, player)
    choices = (
        "You may approach[" + str(player.cha)  "] her, " +
        "make her laugh with a joke, " +
        "talk with her, " +
        "or try to get her number. +
        "Good luck!")
    # approach
    # joke
    # talk
    # number


def chatspeed(player):

    if player.state() == "asleep":
        speed = random() / (5 * 4)
    elif player.state() == "awake":
        speed = random() / (10 * 2)
    else:
        speed = 0

    return speed


def chat(words, player):

    for letter in words:
        stdout.write(letter)
        stdout.flush()
        sleep(chatspeed(player))
    print("")


def action_success(stat, requirement):
    modifier = randrange(0, 25) / 100
    if random() > .5:
        modifier = -modifier
    chance = stat / requirement + modifier

    return chance >= 1, chance


def action(command, player):
    if "sleep" in command and player.isAt("home"):
        player.timeleft = 3
        player.day += 1
        chat("It's a new day." + " Day " + str(player.day) + " to be exact.", player)

    elif "drink" in command and player.isAt("bar") and player.hasTime():
        player.decrease("timeleft", 1)
        player.increase("cha", 5)
        chat("Whew, that's the good stuff. Charisma increased by 5.", player)

    elif "hit" in command and player.isAt("bar") and player.hasTime():
        player.decrease("timeleft", 1)
        success, chance = action_success(player.cha, player.cha_diff)
        if success:
            player.increase("cha", 15)
            chat("Success! [" + str(int(chance * 100)) + "/100] You flirt flawlessly. Charisma increased by 15!", player)
            player.mod += .05
            player.cha_diff = int(randrange(10, 100) * player.mod)
        else:
            player.decrease("cha", 5)
            chat("Failure. [" + str(int(chance * 100)) + "/100] She looks at you weirdly. Charisma decreased by 5.", player)
            player.cha_diff = int(randrange(10, 100) * player.mod)

    elif "fight" in command and player.isAt("bar") and player.hasTime():
        player.decrease("timeleft", 1)
        success, chance = action_success(player.str, player.str_diff)
        if success:
            player.increase("str", 15)
            player.increase("money", 10)
            chat("Success! [" + str(int(chance * 100)) + "/100] You fuck him up. Strength increased by 15, Wealth by 10!", player)
            player.mod += .05
            player.str_diff = int(randrange(10, 100) * player.mod)
        else:
            player.decrease("str", 5)
            chat("Failure. [" + str(int(chance * 100)) + "/100] You get your shit kicked in. Strength decreased by 5, Wealth by 20.", player)
            player.str_diff = int(randrange(10, 100) * player.mod)

    elif "study" in command and player.isAt("school") and player.hasTime():
        player.decrease("timeleft", 1)
        player.increase("int", 5)
        chat("That was a lot of studying. Intellect increased by 5.", player)

    elif "test" in command and player.isAt("school") and player.hasTime():
        player.decrease("timeleft", 1)
        success, chance = action_success(player.int, player.int_diff)
        if success:
            player.increase("int", 15)
            chat("Success! [" + str(int(chance * 100)) + "/100] You pass your test with flying colors! Intellect increased by 15.", player)
            player.mod += .05
            player.int_diff = int(randrange(10, 100) * player.mod)
        else:
            player.decrease("int", 5)
            chat("Failure. [" + str(int(chance * 100)) + "/100] Your test returns a flag. Intellect decreased by 5.", player)
            player.int_diff = int(randrange(10, 100) * player.mod)

    elif "exercise" in command and player.isAt("gym") and player.hasTime():
        player.decrease("timeleft", 1)
        player.increase("str", 5)
        chat("Got a good pump! Strength increased by 5.", player)

    elif "pickup" in command and player.isAt("gym") and player.hasTime():
        player.decrease("timeleft", 1)
        success, chance = action_success(player.str, player.str_diff)
        if success:
            player.increase("str", 15)
            chat("Success! [" + str(int(chance * 100)) + "/100] You dominate the field. Strength increased by 15!", player)
            player.mod += .05
            player.str_diff = int(randrange(10, 100) * player.mod)
        else:
            player.decrease("str", 5)
            chat("Failure. [" + str(int(chance * 100)) + "/100] You flop badly. Strength decreased by 5.", player)
            player.str_diff = int(randrange(10, 100) * player.mod)

    elif "work" in command and player.isAt("job") and player.hasTime():
        player.decrease("timeleft", 1)
        player.increase("money", 20)
        chat("You work like a dog. Wealth increased by 20.", player)

    elif "approach" in command and player.isAt("mall") and player.hasTime():
        pass

    elif "joke" in command and player.isAt("mall") and player.hasTime():
        pass

    elif "talk" in command and player.isAt("mall") and player.hasTime():
        pass

    elif "number" in command and player.isAt("mall") and player.hasTime():
        pass

    elif not player.hasTime():
        chat("You must return home, you are out of actions.", player)
    else:
        print("Unrecognized command")


def movement(command, player):

    if "home" in command:
        home(player)
    elif "bar" in command and player.hasTime():
        bar(player)
    elif "school" in command and player.hasTime():
        school(player)
    elif "gym" in command and player.hasTime():
        gym(player)
    elif "job" in command and player.hasTime():
        job(player)
    elif "mall" in command and player.hasTime() and player.checkStats():
        mall(player)
    elif not player.hasTime():
        chat("You must return home, you are out of actions.", player)
    elif not player.checkStats() and "mall" in command:
        chat("You are not worthy enough to get into the mall yet, try increasing your stats.", player)
    else:
        print("Unrecognized command")


def help():
    print("Valid commands are:")
    print("goto [location]")
    print("do [action]")
    print("stats")
    print("help")


def repl(player):
    prompt = "> "
    question = "What would you like to do?"

    while True:

        print(question)
        command = input(prompt)

        if "goto" in command:
            movement(command, player)

        elif "do" in command:
            action(command, player)

        elif "stats" in command:
            player.stats()

        elif "cheat" in command:
            player.str = 50
            player.int = 50
            player.cha = 50
            player.money = 100

        elif "quit" in command:
            exit(0)

        elif "help" in command:
            help()

        else:
            print("Unrecognized command")


def start():
    the_hero = character()

    chat("== A white light surrounds you, you feel comforted. ==", the_hero)
    chat("Hello ......", the_hero)
    chat("Yes, you are dreaming ......", the_hero)
    chat("It is time for your life to change ......", the_hero)
    chat("From now on, each day you will work toward improving yourself ......", the_hero)
    chat("Your goal is to be worthy of the girl of your dreams ......", the_hero)
    chat("Work ... School ... Gym ... Bar ......", the_hero)
    chat("Each of these are your training grounds ......", the_hero)
    chat("Increase your wealth, intellect, strength, and charisma ......", the_hero)
    chat("Each of these presents unique opportunities, some good, some bad ......", the_hero)
    chat("Perservere ......", the_hero)
    chat("Until you are capable of meeting her at the mall and getting her number ......", the_hero)
    chat("Good luck! ......", the_hero)

    the_hero.wakeUp()

    chat("== The alarm goes off. ==", the_hero)
    chat("'What a strange dream', you say to yourself.", the_hero)
    chat("'If I get stuck, I can type [help] into the terminal?'", the_hero)
    chat("What the hell does that mean?", the_hero)

    repl(the_hero)


start()
