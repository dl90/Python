import random

class mob:
    def __init__(self, name_, weapon_, hp_, ac_lower_range_, ac_upper_range_):
        self.name = name_
        self.weapon = weapon_
        self.hp = hp_
        self.ac_lower = ac_lower_range_
        self.ac_upper = ac_upper_range_
    
    def ac(self):
        ac = random.randrange(self.ac_lower, self.ac_upper)
        return ac
    
    def fight(self, opponent):
        print(f"{self.name} took a swing at {opponent.name}")
        hit = self.ac() - opponent.ac()

        if(hit > 0):
            dmg = hit + wepDmg[self.weapon]
            print(f"You hit the {opponent.name} for " + str(dmg))
            opponent.hp -= dmg
        else:
            print("You missed")
    
    def flight(self, opponent):
        print(f"{self.name} tries to run away from {opponent.name}")
        hit = self.ac() - opponent.ac()

        if(hit > 0):
            print("You escaped")
            return False

        else:
            fight(self, opponent)


wepDmg = {
    "Great Axe": 20,
    "Sword": 10,
    "Bow": 15
}


def encounter(hero, mob):

    print(f"{hero.name} encountered a {mob.name} wielding a {mob.weapon}")
    print("Type the a key and then RETURN to attack.")

    state = True
    while state:
        action = input()

        if action.lower() == "a":
            hero.fight(mob)

        if action.lower() == "e":
            state = hero.flight(mob)

        if mob.hp < 1:
            print("You killed your foe!")
            state = False

        else:
            print(f"The {mob.name}  has {mob.hp} HP remaining")


foe = mob("Troll", "Great Axe", 200, 30, 40)
hero = mob("Hero", "Sword", 100, 35, 45)

# encounter(hero, foe)
