#
#  biggest project i've done 3/21/22
#  Nathaniel Masson // Naedrae // Razuul
#
from tkinter import *
import random
from player import *
from enemies import *
import time


# window creation
root = Tk()
root.geometry("500x760")
root.title("Dungeon")
root.configure(bg="black")
e = Entry()
e.grid



money = player.money
player_hpp = player.hp
playerhp = player.hp
level = player.level
reqexp = player.reqexp
y = player.reqexp
# Weapons
def give_money():
    global money
    money = money + 500000
def dev_sword1():
    dev_sword = 5000, 5000
    player.dmg = dev_sword
    button_dev_sword.config(text="-Equipped-\nDev")
    root.update(), time.sleep(.5)
    button_dev_sword.config(text='Dev')
def rusty_dagger1():
    global money
    weapon = 2, 3, 4, 5
    if money >= 20:
        money = money - 20
        player.dmg = weapon
        button_rusty_dagger.config(text="-Equipped-\nRusty Dagger\n$20")
        root.update(), time.sleep(.5)
        button_rusty_dagger.config(text='Rusty Dagger\n$20')
    else:
        button_rusty_dagger.config(text="-Not Enough-\n-Money-\nRusty Dagger\n$20")
        root.update(), time.sleep(1)
        button_rusty_dagger.config(text='Rusty Dagger\n$20')
def dagger1():
    global money
    weapon = 10, 11, 12, 13, 14, 15
    if money >= 40:
        money = money - 40
        player.dmg = weapon
        button_dagger.config(text="-Equipped-\nDagger\n$40")
        root.update(), time.sleep(.5)
        button_dagger.config(text='Dagger\n$40')
    else:
        button_dagger.config(text="-Not Enough-\n-Money-\nDagger\n$40")
        root.update(), time.sleep(1)
        button_dagger.config(text='Dagger\n$40')
def sharp_dagger1():
    global money
    weapon = 16, 17, 18, 19, 20
    if money >= 60:
        money = money - 60
        player.dmg = weapon
        button_sharp_dagger.config(text="-Equipped-\nSharp Dagger\n$60")
        root.update(), time.sleep(.5)
        button_sharp_dagger.config(text='Sharp Dagger\n$60')
    else:
        button_sharp_dagger.config(text="-Not Enough-\n-Money-\nSharp Dagger\n$60")
        root.update(), time.sleep(1)
        button_sharp_dagger.config(text='Sharp Dagger\n$60')
def bent_sword1():
    global money
    weapon = 20, 21, 22, 23, 24, 25
    if money >= 80:
        player.dmg = weapon
        button_bent_sword.config(text="-Equipped-\nBent Sword\n$80")
        root.update(), time.sleep(.5)
        button_bent_sword.config(text='Bent Sword\n$80')
    else:
        button_bent_sword.config(text="-Not Enough-\n-Money-\nBent Sword\n$60")
        root.update(), time.sleep(1)
        button_bent_sword.config(text='Bent Sword\n$60')
def sword1():
    global money
    weapon = 26, 27, 28, 29, 30
    if money >= 100:
        player.dmg = weapon
        button_sword.config(text="-Equipped-\nSword\n$100")
        root.update(), time.sleep(.5)
        button_sword.config(text='Sword\n$100')
    else:
        button_sword.config(text="-Not Enough-\n-Money-\nSword\n$100")
        root.update(), time.sleep(1)
        button_sword.config(text='Sword\n$100')
def sharp_sword1():
    global money
    weapon = 31, 32, 33, 34, 35
    if money >= 120:
        player.dmg = weapon
        button_sharp_sword.config(text="-Equipped-\nSharp Sword\n$120")
        root.update(), time.sleep(.5)
        button_sharp_sword.config(text='Sharp Sword\n$120')
    else:
        button_sharp_sword.config(text="-Not Enough-\n-Money-\nSharp Sword\n$120")
        root.update(), time.sleep(1)
        button_sharp_sword.config(text='Sharp Sword\n$120')
def unbalanced_katana1():
    global money
    weapon = 36, 37, 38, 39, 40
    if money >= 140:
        player.dmg = weapon
        button_unbalanced_katana.config(text="-Equipped-\nUnbalanced Katana\n$140")
        root.update(), time.sleep(.5)
        button_unbalanced_katana.config(text='Unbalanaced Katana\n$140')
    else:
        button_unbalanced_katana.config(text="-Not Enough-\n-Money-\nUnbalanced Katana\n$140")
        root.update(), time.sleep(1)
        button_unbalanced_katana.config(text='Unbalanced Katana\n$140')
def katana1():
    global money
    weapon = 41, 42, 43, 44, 45
    if money >= 160:
        player.dmg = weapon
        button_katana.config(text="-Equipped-\nKatana\n$160")
        root.update(), time.sleep(.5)
        button_katana.config(text='Katana\n$160')
    else:
        button_katana.config(text="-Not Enough-\n-Money-\nKatana\n$160")
        root.update(), time.sleep(1)
        button_katana.config(text='Katana\n$160')
def perfected_katana1():
    global money
    weapon = 46, 47, 48, 49, 50
    if money >= 180:
        player.dmg = weapon
        button_perfected_katana.config(text="-Equipped-\nPerfected Katana\n$180")
        root.update(), time.sleep(.5)
        button_perfected_katana.config(text='Perfected Katana\n$180')
    else:
        button_perfected_katana.config(text="-Not Enough-\n-Money-\nPerfected Katana\n$180")
        root.update(), time.sleep(1)
        button_perfected_katana.config(text='Perfected Katana\n$180')
def enchanted_dagger1():
    global money
    weapon = 51, 52, 53, 54, 55
    if money >= 200:
        player.dmg = weapon
        button_enchanted_dagger.config(text="-Equipped-\nEnchanted Dagger\n$200")
        root.update(), time.sleep(.5)
        button_enchanted_dagger.config(text='Enchanted Dagger\n$200')
    else:
        button_enchanted_dagger.config(text="-Not Enough-\n-Money-\nEnchanted Dagger\n$200")
        root.update(), time.sleep(1)
        button_enchanted_dagger.config(text='Enchanted Dagger\n$200')
def enchanted_sword1():
    global money
    weapon = 56, 57, 58, 59, 60
    if money >= 220:
        player.dmg = weapon
        button_enchanted_sword.config(text="-Equipped-\nEnchanted Sword\n$220")
        root.update(), time.sleep(.5)
        button_enchanted_sword.config(text='Enchanted Sword\n$220')
    else:
        button_enchanted_sword.config(text="-Not Enough-\n-Money-\nEnchanted Sword\n$220")
        root.update(), time.sleep(1)
        button_enchanted_sword.config(text='Enchanted Sword\n$220')
def enchanted_katana1():
    global money
    weapon = 61, 62, 63, 64, 65
    if money >= 240:
        player.dmg = weapon
        button_enchanted_katana.config(text="-Equipped-\nEnchanted Katana\n$240")
        root.update(), time.sleep(.5)
        button_enchanted_katana.config(text='Enchanted Katana\n$240')
    else:
        button_enchanted_katana.config(text="-Not Enough-\n-Money-\nEnchanted Katana\n$240")
        root.update(), time.sleep(1)
        button_enchanted_katana.config(text='Enchanted Katana\n$240')
def subtraction(a,b):
    sub=a-b
def restore_health():
    global money
    global playerhp
    reqs = player.level * player.level  #reqs means prerequisites or requirements.
    if reqs <= money:
        playerhp = player.hp
        misc_text.insert(1.0, "\n\nPlayer healed!")
        root.update(), time.sleep(2)
        misc_text.delete(1.0, "end")
        money = money - reqs
    if reqs > money:
        misc_text.insert(1.0, "\n\nNot enough money!")
        root.update(), time.sleep(2)
        misc_text.delete(1.0, "end")
def clear():
    dungeon_text.delete(1.0, "end")
def bank_button():
    misc_text.delete(1.0, "end")
    misc_text.insert(1.0, "           $" + str(money))
    root.update(), time.sleep(2)
    misc_text.delete(1.0, "end")
def button_level():
    global reqexp
    global level
    global y
    if reqexp <= 0:
        sum = player.hp * 0.5
        player.hp = player.hp + sum
        y = y * 0.5
        reqexp = player.reqexp + y
        button_level_up.config(text="Level  \nUp     ")

        print("this worked!\n player.hp = " + str(player.hp))
        print("Y =  " + str(y))
#mobs
def rat_button():
    global money
    global playerhp
    mobhp = rat.hp
    mobname = rat.name
    dungeon_text.insert(1.0, "An infected rat approaches!\n")
    root.update(), time.sleep(1)
    while True:
        mobdmg = random.randint(1, 2)
        playerdmg = random.choice(player.dmg)
        mobdmg = mobdmg
        emoney = rat.emoney
        exp = rat.eexp
        # combat
        mobhp = mobhp - playerdmg
        playerhp = playerhp - mobdmg
        # combat ^
        dungeon_text.insert(1.0, "You dealt " + str(playerdmg) + "!          Rat HP: " + str(mobhp) + "\n")
        dungeon_text.insert(1.0, str(mobname) + " dealt " + str(mobdmg) + "!          Player HP: " + str(
            playerhp) + "\n")
        root.update(), time.sleep(.5)
        dungeon_text.delete(1.0, "end")
        if mobhp <= 0:
            global reqexp
            dungeon_text.delete(1.0, "end")
            money = money + emoney
            reqexp = reqexp - exp
            root.update(), time.sleep(0.2)
            dungeon_text.insert(1.0, mobname + " killed!\nLoot: $" + str(emoney))
            if reqexp <= 0:
                global level
                level = level + 1
                button_level_up.config(text="Level  \nUp+     ")
            break
        if playerhp <= 0:
            dungeon_text.delete(1.0, "end")
            root.update(), time.sleep(1)
            dungeon_text.insert(1.0, "You died! Exiting...")
            root.update(), time.sleep(2)
            exit()
def kobald_button():
    global money
    global playerhp
    mobhp = kobald.hp
    mobname = kobald.name
    dungeon_text.insert(1.0, "A rabid Kobald approaches!\n")
    root.update(), time.sleep(1)
    while True:
        mobdmg = random.randint(2, 4)   # damage resides here for mob
        playerdmg = random.choice(player.dmg)
        mobdmg = mobdmg
        emoney = kobald.emoney
        exp = kobald.eexp
        # combat
        mobhp = mobhp - playerdmg
        playerhp = playerhp - mobdmg
        # combat ^
        dungeon_text.insert(1.0, "You dealt " + str(playerdmg) + "!          Kobald HP: " + str(mobhp) + "\n")
        dungeon_text.insert(1.0, str(mobname) + " dealt " + str(mobdmg) + "!          Player HP: " + str(
            playerhp) + "\n")
        root.update(), time.sleep(.5)
        dungeon_text.delete(1.0, "end")
        if mobhp <= 0:
            global reqexp
            dungeon_text.delete(1.0, "end")
            money = money + emoney
            reqexp = reqexp - exp
            root.update(), time.sleep(0.2)
            dungeon_text.insert(1.0, mobname + " killed!\nLoot: $" + str(emoney))
            if reqexp <= 0:
                global level
                level = level + 1
                button_level_up.config(text="Level  \nUp+     ")
            break
        if playerhp <= 0:
            dungeon_text.delete(1.0, "end")
            root.update(), time.sleep(.2)
            dungeon_text.insert(1.0, "You died! Exiting...")
            root.update(), time.sleep(1.5)
            exit()






# enemies
button_Rat = Button(padx=25, pady=5, text="Rat", foreground="#ffffff", background="#825b48", command=rat_button)
button_Kobald = Button(padx=25, pady=5, text="Kobald", foreground="#ffffff", background="gray", command=kobald_button)

# random crap??
button_restore_hp = Button(padx=2, pady=2, text="Heal    ", command=restore_health)
dungeon_text = Text(height=50, width=50, background="black", borderwidth=0, foreground="white")
side_bar = Label(padx=5, pady=241, background="white")
button_Bank = Button(padx=2, pady=2, text="Bank     ", command=bank_button)
button_Clear = Button(padx=2, pady=2, text="clear", command=clear)
dung_info = Button(height=1, width=39, text="Dungeon Info", background="black", foreground="red", borderwidth=1, highlightcolor="red")
warning = Button(height=10, width=35, text="WARNING: You die; You lose your progress.", background="black", foreground="red", borderwidth=0)
bottom_bar = Label(padx=235, pady=2, background="white", text="Shop")
give_money1 = Button(padx=2, pady=10, text="give mula", command=give_money)
misc_text = Text(height=4, width=17, background="black",borderwidth=0, foreground="green")
# weapons
button_rusty_dagger = Button(height=4, width=14, text="Rusty Dagger\n$20", background="gray", command=rusty_dagger1)
button_dagger = Button(height=4, width=14, text="Dagger\n$40", background="white", command=dagger1)
button_sharp_dagger = Button(height=4, width=14, text="Sharp Dagger\n$60", background="cyan", command=sharp_dagger1)
button_bent_sword = Button(height=4, width=14, text="Bent Sword\n$80", background="gray", command=bent_sword1)
button_sword = Button(height=4, width=14, text="Sword\n$100", background="white", command=sword1)
button_sharp_sword = Button(height=4, width=14, text="Sharp Sword\n$120", background="cyan", command=sharp_sword1)
button_unbalanced_katana = Button(height=4, width=14, text="Unbalanced Katana\n$140", background="gray", command=unbalanced_katana1)
button_katana = Button(height=4, width=14, text="Katana\n$160", background="white", command=katana1)
button_perfected_katana = Button(height=4, width=14, text="Perfected Katana\n$180", background="cyan", command=perfected_katana1)
button_enchanted_dagger = Button(height=4, width=14, text="Enchanted Dagger\n$200", background="purple", command=enchanted_dagger1)
button_enchanted_sword = Button(height=4, width=14, text="Enchanted Sword\n$220", background="purple", command=enchanted_sword1)
button_enchanted_katana = Button(height=4, width=14, text="Enchanted Katana\n$240", background="purple", command=enchanted_katana1)
button_level_up = Button(height=2, width=5, text="Level  \nUp     ", background="white", command=button_level)

button_dev_sword = Button(height=4, width=4, text="Dev", background="teal", command=dev_sword1)


# enemies
button_Rat.place(x=25, y=25)
button_Kobald.place(x=25, y=65)
# Bars
side_bar.place(x=440)
bottom_bar.place(y=500)
# Buttons
button_dev_sword.place(x=460, y=420)
button_level_up.place(x=458, y=70)
give_money1.pack()
button_Bank.place(x=458, y=10)
button_restore_hp.place(x=458, y=40)
# 1st row
button_rusty_dagger.place(x=15,y=525)
button_bent_sword.place(x=137,y=525)
button_unbalanced_katana.place(x=258,y=525)
button_enchanted_dagger.place(x=380,y=525)
# 2nd row
button_dagger.place(x=15,y=600)
button_sword.place(x=137,y=600)
button_katana.place(x=258,y=600)
button_enchanted_sword.place(x=380,y=600)
# 3rd row
button_sharp_dagger.place(x=15,y=675)
button_sharp_sword.place(x=137,y=675)
button_perfected_katana.place(x=258,y=675)
button_enchanted_katana.place(x=380,y=675)
# Text
dungeon_text.place(x=10 ,y=151)
dung_info.place(x=10, y=120)
warning.place(x=50, y=405)
misc_text.place(x=300, y=10)


root.mainloop()


