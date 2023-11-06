import random
import time

#Declaring different dice
d20dice = range(1, 20)
d12dice = range(1, 12)
d10dice = range(1, 10)
d8dice = range(1, 8)
d6dice = range(1, 6)


# Declare classes
class Character:
    def __init__ (self, name, health, atkbonus, armcla, basedmg, dicedmg, atkdice):
        self.name = name
        self.health = health
        self.atkbonus = atkbonus
        self.armcla = armcla
        self.basedmg = basedmg
        self.dicedmg = dicedmg
        self.atkdice = atkdice
        self.goldvalue = health
    def __repr__(self):
      intro = "{name} has {health} health with an armour class of {armcla}".format(name = self.name, health = self.health, armcla = self.armcla)
      return intro

    def take_damage(self, damage):
      self.health -= damage
      return self.health
    
    def atk_roll(self):
      dice_roll = random.choice(d20dice) + self.atkbonus
      return dice_roll

    def deal_damage(self):
      damage = self.basedmg + (self.dicedmg * (random.choice(self.atkdice)))
      return damage
    
    def gold_value(self):
      value = random.randint(40, self.goldvalue)
      value = value * 3
      return value

class Warrior(Character):
    def __init__(self, name):
      Character.__init__(self, name, 200, 6, 14, 10, 3, d10dice)
      
      self.charges = 2
      
    def special_attack(self):
      if self.charges <= 0:
        return 0
      print("You use RECKLESS STRIKES")
      output = random.choice(d20dice) * 3 + 10
      return output

class Rogue(Character):
    def __init__(self, name):
      Character.__init__(self, name, 120, 8, 16, 5, 5, d6dice)
      
      self.charges = 3
      
    def special_attack(self):
      if self.charges <= 0:
        return 0
      print("You use SNEAK ATTACK")
      output = random.choice(d12dice) * 5 + 8
      return output

class Mage(Character):
    def __init__(self, name):
      Character.__init__(self, name, 80, 10, 16, 10, 3, d12dice)
      
      self.charges = 4
      
    def special_attack(self):
      if self.charges <= 0:
        return 0
      print("You use FIREBALL")
      time.sleep(1)
      output = random.choice(d8dice) * 8 + 6
      return output



def enemy_choice(x):
  if x == 1:
    opponent = Character("Balzog the Cruel",150, 8, 17, 8, 2, d8dice)
    print(opponent)
    return opponent
  elif x == 2:
    opponent = Character("Draygurn the Butcher",120, 6, 16, 5, 8, d6dice)
    print(opponent)
    return opponent
  elif x == 3:
    opponent = Character("Dire Wolf",70, 8, 14, 4, 4, d6dice)
    print(opponent)
    return opponent

def class_choice(x, name):
  if x == 1:
    player = Warrior(name)
    print(player)
    return player
  elif x == 2:
    player = Rogue(name)
    print(player)
    return player
  elif x == 3:
    player = Mage(name)
    print(player)
    return player


def start():
  player_name = input("Choose your characters name...\n")
  class_pick = 0
  choices = [1, 2, 3]
  while class_pick not in choices:
    class_pick = int(input("Pick your class... \n 1. Warrior, 2. Rogue, 3. Mage\n"))
  player = class_choice(class_pick, player_name)
  b_choice = 0
  print("Select opponent - 1. Balzog the Cruel, 2. Dragurn the Butcher, 3. Dire Wolf")
  while b_choice not in choices:
    b_choice = int(input("Input a number between 1, 2 and 3...\n"))
  opponent = enemy_choice(b_choice)
  print("Let's roll for initiative")
  time.sleep(1)
  input("Press Enter to roll...\n")
  player_roll, baddie_roll = 0, 0
  while player_roll == baddie_roll:
    player_roll = random.choice(d20dice)
    baddie_roll = random.choice(d20dice)
    print(f"Player rolled: {player_roll}")
    time.sleep(1)
    print(f"{opponent.name} rolled {baddie_roll}")
  if player_roll > baddie_roll:
      print(f"{player.name} goes first...")
      time.sleep(1)
      return player_turn(player, opponent)
  elif player_roll < baddie_roll:
      print(f"{opponent.name} goes first...")
      time.sleep(1)
      return baddie_turn(player, opponent)


def player_turn(player, opponent):
  print(player, opponent)
  if player.health >= 1:
    print(f"It's your go {player.name}!")
    time.sleep(1)
    print("Time to attack!")
    time.sleep(1)
    if player.charges > 0:
      style = int(input("Type 1 for normal attack, or 2 for Special attack\n"))
      if style == 2:
        player.charges -= 1
        print(f"You have {player.charges} charges remaining of your special attack")
        attackroll = player.atk_roll()
        print(f"You rolled {attackroll} to strike again {opponent.name} armour class of {opponent.armcla}!")
        if attackroll >= opponent.armcla:
          damagedealt = player.special_attack()
          opponent.take_damage(damagedealt)
          print(f"You dealt {damagedealt} to {opponent.name}")
          print(f"{opponent.name} has {opponent.health} HP left")
          time.sleep(1)
          baddie_turn(player, opponent)
        else:
          print("Oh no, you missed!")
          time.sleep(1)
          baddie_turn(player, opponent)
    else:
      if player.charges == 0:
        print("You are out of charges!")
        player.charges -= 1
      input("Press enter to launch a normal attack")
      time.sleep(1)
      attackroll = player.atk_roll()
      print(f"You rolled {attackroll} to strike again {opponent.name} armour class of {opponent.armcla}!")
      if attackroll >= opponent.armcla:
        damagedealt = player.deal_damage()
        opponent.take_damage(damagedealt)
        print(f"You dealt {damagedealt} to {opponent.name}")
        print(f"{opponent.name} has {opponent.health} HP left")
        time.sleep(1)
        baddie_turn(player, opponent)
      else:
        print("Oh no, you missed!")
        time.sleep(1)
        baddie_turn(player, opponent)
  else:
      print("Game over, you lose!")
      time.sleep(2)
      exit()


def baddie_turn(player, opponent):
  if opponent.health >= 1:
    print(f"{opponent.name}'s turn")
    time.sleep(1)
    print("Prepare yourself!")
    time.sleep(1)
    attackroll = opponent.atk_roll()
    print(f"{opponent.name} rolled {attackroll} to strike against {player.name}armour class of {player.armcla}!")
    time.sleep(2)
    if attackroll >= player.armcla:
      damagedealt = opponent.deal_damage()
      player.take_damage(damagedealt)
      print(f"{opponent.name} deals {damagedealt} damage!")
      time.sleep(1)
      print(f"{player.name} has {player.health} HP left")
      time.sleep(1)
      player_turn(player, opponent)
    else:
      print(f"{opponent.name} missed!")
      time.sleep(1)
      player_turn(player, opponent)
  else:
      print(f"{opponent.name} is defeated! Congratulations")
      time.sleep(2)
      gold_won = opponent.gold_value()
      print(f"{opponent.name} has dropped {gold_won} You place it in your coin purse")
      time.sleep(2)
      exit()


start()

