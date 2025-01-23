from game import Person, bcolors
from magic import Spell
from inventory import Item
import random

# Create Magic
fire = Spell("Fire", 25, 600)
thunder = Spell("Thunder", 25, 600)
blizzard = Spell("Blizzard", 25, 600)
meteor = Spell("Meteor", 40, 1200)

# Create Items
potion = Item("Potion", "potion", "Heals 50 HP", 50)
elixer = Item("Elixer", "elixer", "Fully restores HP/MP of player", 9999)
grenade = Item("Grenade", "attack", "Deals 500 damage", 500)

player_spells = [fire, thunder, blizzard, meteor]
player_items = [{"item": potion, "quantity": 15},
                {"item": elixer, "quantity": 5}, {"item": grenade, "quantity": 5}]

# Instantiate People
player_1 = Person("Fighter", 3260, 200, 250, player_spells, player_items)
player_2 = Person("Ninja  ", 3260, 200, 250, player_spells, player_items)
player_3 = Person("Wizard ", 15, 600, 0, player_spells, player_items)
player_4 = Person("Tank   ", 6, 1, 125, player_spells, player_items)
enemy_1 = Person("Wolf   ", 5000, 701, 525, [], [])
enemy_2 = Person("Wolf   ", 5000, 701, 525, [], [])
enemy_3 = Person("Orc    ", 6000, 701, 400, [], [])
enemy_4 = Person("Boss   ", 11200, 701, 750, [], [])
player = [player_1, player_2, player_3, player_4]
enemy = [enemy_1, enemy_2, enemy_3, enemy_4]
player_count = 4
enemy_count = 4

running = True
i = 0
player_target = 0 
enemy_choice = 0

print(bcolors.FAIL + bcolors.BOLD + "YOUR PARTY HAS ENCOUNTERD A GROUP OF MONSTERS!" + bcolors.ENDC)

while running:
    for n in range(0,4):
      if player[n].get_hp() == 0: continue
      print("=============================")

      print("\n\n")
      print("NAME                     HP                                      MP")

      player_1.get_stats()
      player_2.get_stats()
      player_3.get_stats()
      player_4.get_stats()

      print("\n")

      enemy_1.get_enemy_stats()
      enemy_2.get_enemy_stats()
      enemy_3.get_enemy_stats()
      enemy_4.get_enemy_stats()
    
      player[n].choose_action()
      choice = input("    Choose action: ")
      index = int(choice) - 1

      if index > 2 or index < 0:
              raise ValueError("Invalid action! Choose a correct value   for action (from 1 to 3).")
    
      if index == 0:
          dmg = player[n].generate_damage()
          enemy_choice = player[n].choose_target(enemy)
          enemy[enemy_choice].take_damage(dmg)
          print("You attacked for", dmg, "points of damage.")
      elif index == 1:
          player[n].choose_magic()
          magic_choice = int(input("    Choose magic: ")) - 1

          if magic_choice > 3 or magic_choice < 0:
              raise ValueError("Invalid magic! Choose a correct value for magic (from 1 to 4).")

          spell = player[n].magic[magic_choice]
          magic_dmg = spell.generate_damage()

          current_mp = player[n].get_mp()

          if spell.cost > current_mp:
              print(bcolors.FAIL + "\nNot enough MP\n" + bcolors.ENDC)
              continue
        
          player[n].reduce_mp(spell.cost)
          
          enemy_choice = player[n].choose_target(enemy)

          enemy[enemy_choice].take_damage(magic_dmg)
          print(bcolors.OKBLUE + "\n" + spell.name + " deals", str(magic_dmg), "points of damage" + bcolors.ENDC)
    
      elif index == 2:
          player[n].choose_item()
          item_choice = int(input("    Choose item: ")) - 1

          if item_choice > 2 or index < 0:
              raise ValueError("Invalid item! Choose a correct value for item (from 1 to 3).")
        
          item = player[n].items[item_choice]["item"]

          if player[n].items[item_choice]["quantity"] == 0:
              print(bcolors.FAIL + "\n" + "None left..." + bcolors.ENDC)
              continue

          player[n].items[item_choice]["quantity"] -= 1
        
          if item.type == "potion":
              player[n].heal(item.prop)
              print(bcolors.OKGREEN + "\n" + item.name + " heals for", str(item.prop), "HP" + bcolors.ENDC)
        
          elif item.type == "elixer":
              player[n].hp = player[n].maxhp
              player[n].mp = player[n].maxmp

              print(bcolors.OKGREEN + "\n" + item.name + " fully restores HP/MP" + bcolors.ENDC)
          elif item.type == "attack":
              enemy_choice = player[n].choose_target(enemy)
              enemy[enemy_choice].take_damage(item.prop)
              print(bcolors.FAIL + "\n" + item.name + " deals", str(item.prop), "points of damage" + bcolors.ENDC)
      if enemy[enemy_choice].get_hp() == 0:
        print("Enemy Slained!!!")
        enemy_count = enemy_count - 1
              
      if enemy_count <= 2:
          print(bcolors.OKGREEN + "You win!" + bcolors.ENDC)
          running = False
      elif player_count <= 2:
          print(bcolors.FAIL + "Your enemy has defeated you!" + bcolors.ENDC)
          running = False
      if running == False: break
    if running == False: break
    for n in range(0,4):
      enemy_dmg = enemy[n].generate_damage()
      
      player_target = random.randrange(0,4)
      while 1:
        player_target = random.randrange(0,4)
        if player[player_target].get_hp(): break
      player_name = player[player_target].get_name()
      player[player_target].take_damage(enemy_dmg)
      print(f"Enemy attacks {player_name} for", enemy_dmg)
      if player[player_target].get_hp() == 0:
        print(f"{player_name} has been slained!!!")
        player_count = player_count - 1
      if enemy_count <= 2:

          print(bcolors.OKGREEN + "You win!" + bcolors.ENDC)

          running = False
      elif player_count <= 2:
          print(bcolors.FAIL + "Your enemy has defeated you!" + bcolors.ENDC)
          running = False
    if running == False: break   
      