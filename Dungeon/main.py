#
# TODO add balance to the game
#
#
#
#
#
#
#  biggest project i've done 3/21/22
#  Nathaniel Masson // Naedrae // Razuul
#
from tkinter import *
import random
from player import *
from enemies import *
import time
from PIL import ImageTk, Image




# window creation
root = Tk()
root.geometry("500x760")
root.title("Dungeon")
root.configure(bg="black")
e = Entry()
e.grid


frame = Frame(width=500, height=500)

# background creation (obviously)

level_bg = ImageTk.PhotoImage(Image.open("C:/Users/natha/PycharmProjects/Dungeon/images/level_image.jpg"))
shop_bg = ImageTk.PhotoImage(Image.open("C:/Users/natha/PycharmProjects/Dungeon/images/shop_image.jpg"))
sidebar_bg = ImageTk.PhotoImage(Image.open("C:/Users/natha/PycharmProjects/Dungeon/images/sidebar_image.jpg"))
dungeon_bg = ImageTk.PhotoImage(Image.open("C:/Users/natha/PycharmProjects/Dungeon/images/dungeon_image.jpg"))

money = player.money
player_hpp = player.hp
playerhp = player.hp
level = player.level
reqexp = player.reqexp
y = 50
# Weapons
def give_money():
    global money
    money = money + 500000
    bank_info.config(text="Bank: " + str(money))
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
        hp_info.config(text="HP: " + str(playerhp))
        money = money - reqs
        bank_info.config(text="Bank: " + str(money))
        root.update(), time.sleep(2)
        misc_text.delete(1.0, "end")
    if reqs > money:
        misc_text.insert(1.0, "\n\nNot enough money!")
        root.update(), time.sleep(2)
        misc_text.delete(1.0, "end")
# level functions
def button_level():
    global reqexp
    global level
    global y
    global hpUp
    global armorUp
    global attackUp
    global playerhp
    if reqexp <= 0:
        player.level = player.level + 1
        reqexp = player.reqexp + y
        button_level_up.config(text="Level Up")
        hp_info.config(text="HP: " + str(playerhp))
        hpUp = True
        armorUp = True
        attackUp = True
        level_info.config(text="Level: " + str(player.level))
        button_hp_up.config(text="HP( ) +")
        button_armor_up.config(text="Armor( ) +")
        button_attack_up.config(text="Attack( ) +")

        print("this worked!\n player.hp = " + str(player.hp))
        print("Y =  " + str(y))
def button_hp():
    global hpUp
    global attackUp
    global armorUp
    if hpUp:
        sum = player.hp * 0.25
        player.hp = player.hp + sum
        playerhp = player.hp
        button_hp_up.config(text="HP( )")
        button_armor_up.config(text="Armor( )")
        button_attack_up.config(text="Attack( )")
        hp_info.config(text="HP: " + str(playerhp))
        hpUp = False
        attackUp = False
        armorUp = False
# TODO make a function for HP, armor, and attack after clicking "level up" when you get enough xp
# stats



#mobs
def rat_button():
    global money
    global playerhp
    mobhp = rat.hp
    mobname = rat.name
    dungeon_text.insert(1.0, "A rat approaches!\n")
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
            dungeon_text.insert(1.0, mobname + " killed!\nLoot: $" + str(emoney) + "\nXP: " + str(rat.eexp))
            hp_info.config(text="HP: " + str(playerhp))
            bank_info.config(text="Bank: " + str(money))
            if reqexp <= 0:
                global level
                level = level + 1
                button_level_up.config(text="Level Up +")
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
    dungeon_text.insert(1.0, "A crazed Kobald approaches!\n")
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
            dungeon_text.insert(1.0, mobname + " killed!\nLoot: $" + str(emoney) + "\nXP: " + str(kobald.eexp))
            hp_info.config(text="HP: " + str(playerhp))
            bank_info.config(text="Bank: " + str(money))
            if reqexp <= 0:
                global level
                level = level + 1
                button_level_up.config(text="Level Up +")
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
dungeon_background = Label(image=dungeon_bg, height=400, width=445)
sidebar_background = Label(image=sidebar_bg, height=400, width=15)
shop_background = Label(image=shop_bg, height=700, width=500)
level_background = Label(image=level_bg, height=150, width=450)
button_restore_hp = Button(padx=2, pady=2, text="Heal    ", command=restore_health)
dungeon_text = Text(height=10, width=40, background="black", borderwidth=1, foreground="white")
side_bar = Label(padx=5, pady=241, background="white")
dung_info = Button(height=1, width=39, text="Dungeon Info", background="black", foreground="red", borderwidth=1, highlightcolor="red")
warning = Label(height=1, width=35, text="WARNING: You die; You lose your progress.", background="black", foreground="red", borderwidth=0)
bottom_bar = Label(padx=235, pady=2, background="white", text="Shop")
give_money1 = Button(padx=2, pady=10, text="give mula", command=give_money)
misc_text = Text(height=4, width=17, background="black",borderwidth=0, foreground="green")
level_side_bar = Label(padx=190, pady=2, background="white", text="Level Panel")
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
button_dev_sword = Button(height=4, width=4, text="Dev", background="teal", command=dev_sword1)
# level stuff
button_level_up = Button(height=2, width=7, text="Level Up", background="white", command=button_level)
button_hp_up = Button(height=3, width=7, text="HP( )", background="red", foreground="white", command=button_hp)
button_attack_up = Button(height=3, width=7, text="Attack( )", background="green", foreground="white")
button_armor_up = Button(height=3, width=7, text="Armor( )", background="blue", foreground="white")
# stats
level_info = Label(height=1, width=10, text="Level: 1", background="black", foreground="white")
hp_info = Label(height=1, width=10, text="HP: 20", background="black", foreground="white")
attack_info = Label(height=1, width=10, text="Attack: 1-2", background="black", foreground="white")
armor_info = Label(height=1, width=10, text="Armor: 0", background="black", foreground="white")
bank_info = Label(height=1, width=10, text="Bank: 0", background="black", foreground="white")





# backgrounds
#dungeon_background.place(x=0, y=0)
shop_background.place(y=423)
level_background.place(y=350)
# enemies
button_Rat.place(x=25, y=25)
button_Kobald.place(x=25, y=65)
# Bars
side_bar.place(x=440)
bottom_bar.place(y=500)
level_side_bar.place(y=330)
# Buttons
button_dev_sword.place(x=460, y=420)
button_level_up.place(x=193, y=355)
button_hp_up.place(x=90, y=400)
button_attack_up.place(x=193, y=400)
button_armor_up.place(x=295, y=400)
give_money1.pack()
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
warning.place(x=50, y=310)
misc_text.place(x=300, y=10)
# stats
level_info.place(x=350, y=145)
hp_info.place(x=350, y=160)
attack_info.place(x=350, y=175)
armor_info.place(x=350, y=190)
bank_info.place(x=350, y=205)

root.mainloop()


