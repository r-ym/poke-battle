import abc
import random
import time

HPS={'Bulbasaur':45,'Ivysaur':60,'Venusaur':80,'Charmander':39,'Charmeleon':58,'Charizard':78,'Squirtle':44,'Wartortle':59,'Blastoise':79,'Caterpie':45,'Metapod':50,'Butterfree':60,'Weedle':40,'Kakuna':45,'Beedrill':65,'Pidgey':40,'Pidgeotto':63,'Pidgeot':83,'Rattata':30,'Raticate':55,'Spearow':40,'Fearow':65,'Ekans':35,'Arbok':60,'Pikachu':35,'Raichu':60,'Sandshrew':50,'Sandslash':75,'Nidoran(F)':55,'Nidorina':70,'Nidoqueen':90,'Nidoran(M)':46,'Nidorino':61,'Nidoking':81,'Clefairy':70,'Clefable':95,'Vulpix':38,'Ninetales':73,'Jigglypuff':115,'Wigglytuff':140,'Zubat':40,'Golbat':75,'Oddish':45,'Gloom':60,'Vileplume':75,'Paras':35,'Parasect':60,'Venonat':60,'Venomoth':70,'Diglett':10,'Dugtrio':35,'Meowth':40,'Persian':65,'Psyduck':50,'Golduck':80,'Mankey':40,'Primeape':65,'Growlithe':55,'Arcanine':90,'Poliwag':40,'Poliwhirl':65,'Poliwrath':90,'Abra':25,'Kadabra':40,'Alakazam':55,'Machop':70,'Machoke':80,'Machamp':90,'Bellsprout':50,'Weepinbell':65,'Victreebel':80,'Tentacool':40,'Tentacruel':80,'Geodude':40,'Graveler':55,'Golem':80,'Ponyta':50,'Rapidash':65,'Slowpoke':90,'Slowbro':95,'Magnemite':25,'Magneton':50,'Farfetchd':52,'Doduo':35,'Dodrio':60,'Seel':65,'Dewgong':90,'Grimer':80,'Muk':105,'Shellder':30,'Cloyster':50,'Gastly':30,'Haunter':45,'Gengar':60,'Onix':35,'Drowzee':60,'Hypno':85,'Krabby':30,'Kingler':55,'Voltorb':40,'Electrode':60,'Exeggcute':60,'Exeggutor':95,'Cubone':50,'Marowak':60,'Hitmonlee':50,'Hitmonchan':50,'Lickitung':90,'Koffing':40,'Weezing':65,'Rhyhorn':80,'Rhydon':105,'Chansey':250,'Tangela':65,'Kangaskhan':105,'Horsea':30,'Seadra':55,'Goldeen':45,'Seaking':80,'Staryu':30,'Starmie':60,'Mr. Mime':40,'Scyther':70,'Jynx':65,'Electabuzz':65,'Magmar':65,'Pinsir':65,'Tauros':75,'Magikarp':20,'Gyarados':95,'Lapras':130,'Ditto':48,'Eevee':55,'Vaporeon':130,'Jolteon':65,'Flareon':65,'Porygon':65,'Omanyte':35,'Omastar':70,'Kabuto':30,'Kabutops':60,'Aerodactyl':80,'Snorlax':160,'Dratini':41,'Dragonair':61,'Dragonite':91}
TYPES={'Bulbasaur':'grass','Ivysaur':'grass','Venusaur':'grass','Charmander':'fire','Charmeleon':'fire','Charizard':'fire','Squirtle':'water','Wartortle':'water','Blastoise':'water','Caterpie':'bug','Metapod':'bug','Butterfree':'bug','Weedle':'bug','Kakuna':'bug','Beedrill':'bug','Pidgey':'normal','Pidgeotto':'normal','Pidgeot':'normal','Rattata':'normal','Raticate':'normal','Spearow':'normal','Fearow':'normal','Ekans':'poison','Arbok':'poison','Pikachu':'electric','Raichu':'electric','Sandshrew':'ground','Sandslash':'ground','Nidoran(F)':'poison','Nidorina':'poison','Nidoqueen':'poison','Nidoran(M)':'poison','Nidorino':'poison','Nidoking':'poison','Clefairy':'fairy','Clefable':'fairy','Vulpix':'fire','Ninetales':'fire','Jigglypuff':'normal','Wigglytuff':'normal','Zubat':'poison','Golbat':'poison','Oddish':'grass','Gloom':'grass','Vileplume':'grass','Paras':'bug','Parasect':'bug','Venonat':'bug','Venomoth':'bug','Diglett':'ground','Dugtrio':'ground','Meowth':'normal','Persian':'normal','Psyduck':'water','Golduck':'water','Mankey':'fighting','Primeape':'fighting','Growlithe':'fire','Arcanine':'fire','Poliwag':'water','Poliwhirl':'water','Poliwrath':'water','Abra':'psychic','Kadabra':'psychic','Alakazam':'psychic','Machop':'fighting','Machoke':'fighting','Machamp':'fighting','Bellsprout':'grass','Weepinbell':'grass','Victreebel':'grass','Tentacool':'water','Tentacruel':'water','Geodude':'rock','Graveler':'rock','Golem':'rock','Ponyta':'fire','Rapidash':'fire','Slowpoke':'water','Slowbro':'water','Magnemite':'electric','Magneton':'electric','Farfetchd':'normal','Doduo':'normal','Dodrio':'normal','Seel':'water','Dewgong':'water','Grimer':'poison','Muk':'poison','Shellder':'water','Cloyster':'water','Gastly':'ghost','Haunter':'ghost','Gengar':'ghost','Onix':'rock','Drowzee':'psychic','Hypno':'psychic','Krabby':'water','Kingler':'water','Voltorb':'electric','Electrode':'electric','Exeggcute':'grass','Exeggutor':'grass','Cubone':'ground','Marowak':'ground','Hitmonlee':'fighting','Hitmonchan':'fighting','Lickitung':'normal','Koffing':'poison','Weezing':'poison','Rhyhorn':'ground','Rhydon':'ground','Chansey':'normal','Tangela':'grass','Kangaskhan':'normal','Horsea':'water','Seadra':'water','Goldeen':'water','Seaking':'water','Staryu':'water','Starmie':'water','Mr. Mime':'psychic','Scyther':'bug','Jynx':'ice','Electabuzz':'electric','Magmar':'fire','Pinsir':'bug','Tauros':'normal','Magikarp':'water','Gyarados':'water','Lapras':'water','Ditto':'normal','Eevee':'normal','Vaporeon':'water','Jolteon':'electric','Flareon':'fire','Porygon':'normal','Omanyte':'rock','Omastar':'rock','Kabuto':'rock','Kabutops':'rock','Aerodactyl':'rock','Snorlax':'normal','Dratini':'dragon','Dragonair':'dragon','Dragonite':'dragon'}
BASES={'Bulbasaur':228,'Ivysaur':285,'Venusaur':365,'Charmander':205,'Charmeleon':267,'Charizard':356,'Squirtle':227,'Wartortle':288,'Blastoise':373,'Caterpie':105,'Metapod':125,'Butterfree':265,'Weedle':105,'Kakuna':125,'Beedrill':255,'Pidgey':155,'Pidgeotto':215,'Pidgeot':295,'Rattata':151,'Raticate':261,'Spearow':152,'Fearow':277,'Ekans':198,'Arbok':298,'Pikachu':195,'Raichu':315,'Sandshrew':210,'Sandslash':310,'Nidoran(F)':179,'Nidorina':239,'Nidoqueen':339,'Nidoran(M)':177,'Nidorino':239,'Nidoking':339,'Clefairy':218,'Clefable':328,'Vulpix':196,'Ninetales':332,'Jigglypuff':135,'Wigglytuff':250,'Zubat':150,'Golbat':290,'Oddish':245,'Gloom':295,'Vileplume':365,'Paras':225,'Parasect':315,'Venonat':200,'Venomoth':290,'Diglett':160,'Dugtrio':250,'Meowth':160,'Persian':260,'Psyduck':215,'Golduck':335,'Mankey':195,'Primeape':295,'Growlithe':235,'Arcanine':370,'Poliwag':170,'Poliwhirl':230,'Poliwrath':350,'Abra':195,'Kadabra':255,'Alakazam':325,'Machop':200,'Machoke':280,'Machamp':360,'Bellsprout':210,'Weepinbell':270,'Victreebel':340,'Tentacool':225,'Tentacruel':335,'Geodude':240,'Graveler':300,'Golem':370,'Ponyta':270,'Rapidash':330,'Slowpoke':210,'Slowbro':365,'Magnemite':255,'Magneton':345,'Farfetchd':240,'Doduo':200,'Dodrio':300,'Seel':215,'Dewgong':315,'Grimer':220,'Muk':345,'Shellder':235,'Cloyster':405,'Gastly':200,'Haunter':265,'Gengar':330,'Onix':280,'Drowzee':226,'Hypno':331,'Krabby':245,'Kingler':345,'Voltorb':190,'Electrode':280,'Exeggcute':225,'Exeggutor':370,'Cubone':235,'Marowak':320,'Hitmonlee':318,'Hitmonchan':329,'Lickitung':265,'Koffing':265,'Weezing':365,'Rhyhorn':240,'Rhydon':340,'Chansey':150,'Tangela':310,'Kangaskhan':295,'Horsea':205,'Seadra':300,'Goldeen':212,'Seaking':302,'Staryu':225,'Starmie':345,'Mr. Mime':330,'Scyther':325,'Jynx':295,'Electabuzz':320,'Magmar':337,'Pinsir':350,'Tauros':305,'Magikarp':100,'Gyarados':364,'Lapras':345,'Ditto':192,'Eevee':215,'Vaporeon':330,'Jolteon':330,'Flareon':395,'Porygon':290,'Omanyte':285,'Omastar':370,'Kabuto':270,'Kabutops':355,'Aerodactyl':305,'Snorlax':350,'Dratini':209,'Dragonair':289,'Dragonite':429}
SPEEDS={'Bulbasaur':45,'Ivysaur':60,'Venusaur':80,'Charmander':65,'Charmeleon':80,'Charizard':100,'Squirtle':43,'Wartortle':58,'Blastoise':78,'Caterpie':45,'Metapod':30,'Butterfree':70,'Weedle':50,'Kakuna':35,'Beedrill':75,'Pidgey':56,'Pidgeotto':71,'Pidgeot':101,'Rattata':72,'Raticate':97,'Spearow':70,'Fearow':100,'Ekans':55,'Arbok':80,'Pikachu':90,'Raichu':110,'Sandshrew':40,'Sandslash':65,'Nidoran(F)':41,'Nidorina':56,'Nidoqueen':76,'Nidoran(M)':50,'Nidorino':65,'Nidoking':85,'Clefairy':35,'Clefable':60,'Vulpix':65,'Ninetales':100,'Jigglypuff':20,'Wigglytuff':45,'Zubat':55,'Golbat':90,'Oddish':30,'Gloom':40,'Vileplume':50,'Paras':25,'Parasect':30,'Venonat':45,'Venomoth':90,'Diglett':95,'Dugtrio':120,'Meowth':90,'Persian':115,'Psyduck':55,'Golduck':85,'Mankey':70,'Primeape':95,'Growlithe':60,'Arcanine':95,'Poliwag':90,'Poliwhirl':90,'Poliwrath':70,'Abra':90,'Kadabra':105,'Alakazam':120,'Machop':35,'Machoke':45,'Machamp':55,'Bellsprout':40,'Weepinbell':55,'Victreebel':70,'Tentacool':70,'Tentacruel':100,'Geodude':20,'Graveler':35,'Golem':45,'Ponyta':90,'Rapidash':105,'Slowpoke':15,'Slowbro':30,'Magnemite':45,'Magneton':70,'Farfetchd':60,'Doduo':75,'Dodrio':100,'Seel':45,'Dewgong':70,'Grimer':25,'Muk':50,'Shellder':40,'Cloyster':70,'Gastly':80,'Haunter':95,'Gengar':110,'Onix':70,'Drowzee':42,'Hypno':67,'Krabby':50,'Kingler':75,'Voltorb':100,'Electrode':140,'Exeggcute':40,'Exeggutor':55,'Cubone':35,'Marowak':45,'Hitmonlee':87,'Hitmonchan':76,'Lickitung':30,'Koffing':35,'Weezing':60,'Rhyhorn':25,'Rhydon':40,'Chansey':50,'Tangela':60,'Kangaskhan':90,'Horsea':60,'Seadra':85,'Goldeen':63,'Seaking':68,'Staryu':85,'Starmie':115,'Mr. Mime':90,'Scyther':105,'Jynx':95,'Electabuzz':105,'Magmar':93,'Pinsir':85,'Tauros':110,'Magikarp':80,'Gyarados':81,'Lapras':60,'Ditto':48,'Eevee':55,'Vaporeon':65,'Jolteon':130,'Flareon':65,'Porygon':40,'Omanyte':35,'Omastar':55,'Kabuto':55,'Kabutops':80,'Aerodactyl':130,'Snorlax':30,'Dratini':50,'Dragonair':70,'Dragonite':80}
#very very long dictionary that determines attack efficiency during battle with regards to type-advantage
TYPE_MATRIX = {'grass':{'fire': 0.5, 'grass': 0.5, 'water': 2.0,'poison':0.5,'ground':2.0,'flying':0.5,'bug':0.5,'rock':2.0,'dragon':0.5},'fire':{'fire':0.5,'grass':2.0,'water':0.5,'ice':2.0,'bug':2.0,'rock':0.5,'dragon':0.5},'water':{'fire': 2.0, 'grass': 0.5, 'water': 0.5,'ground':2.0,'rock':2.0,'dragon':0.5},'bug':{'ghost':0.5,'grass':2.0,'fire':0.5,'poison': 2.0,'fighting':0.5,'flying':0.5,'psychic':2.0},'normal':{'rock':0.5,'ghost':0},'poison':{'grass':2.0,'bug':2.0,'poison':0.5,'ground':0.5,'rock':0.5,'ghost':0.5},'electric':{'grass': 0.5,'water':2.0 ,'flying':2.0 ,'electric': 0.5,'ground':0 ,'dragon': 0.5},'ground':{'grass': 0.5,'fire':2.0 ,'flying':0,'bug': 0.5 ,'poison': 2.0,'electric':2.0 ,'rock': 2.0},'flying':{'grass': 2.0,'electric': 0.5,'fighting': 2.0,'bug':2.0 ,'rock':0.5},'fighting':{'flying':0.5,'bug': 0.5,'normal': 2.0,'poison': 0.5,'psychic': 0.5,'rock': 2.0,'ghost': 0,'ice': 2.0},'psychic':{'poison': 2.0,'fighting': 2.0 ,'psychic': 0.5},'rock':{'flying': 2.0,'fire': 2.0,'bug': 2.0,'ground': 0.5,'fighting': 0.5,'ice': 2.0},'ghost':{'normal': 0,'psychic': 0,'ghost': 2.0},'ice':{'grass': 2.0,'water': 0.5,'flying': 2.0,'ground': 2.0,'ice': 0.5,'dragon': 2.0},'dragon':{'dragon':2.0}}
opponent_roster=[]
trainer_roster=[]
#abstract base class to hold Pokemon info, abstract so as to provide the scaffolding for other derived classes
class pokemon(object):
    def __init__(self,name,hp,types,base,speed,starting_health):
        self.name=name
        self.hp=hp
        self.type=types
        self.base=base #base stat that accounts for every attack/defense parameter and is used to scale the attack relative to the other pokemon's base stat
        self.speed=speed
        self.starting_health=starting_health
    def attack(self,opponent):
        random.seed()
        if opponent.type in TYPE_MATRIX[self.type]:
            scale=TYPE_MATRIX[self.type][opponent.type]
            DAMAGE = (random.randint(8,12)/10)*scale*int(self.base/opponent.base)*24
            damage=int(DAMAGE)
            opponent.hp = opponent.hp - damage
            if opponent.hp<0:
                opponent.hp=0
            print('{} attacked and did {} damage'.format(self.name,damage))
            if scale==2.0:
                print('Its super effective!')
            elif scale==0.5:
                print('Its not very effective...')
            else:
                print('The move had no effect.')
        else:
            DAMAGE = (random.randint(8,12)/10)*int(self.base/opponent.base)*24
            damage=int(DAMAGE)
            opponent.hp = opponent.hp - damage
            if opponent.hp<0:
                opponent.hp=0
            print('{} attacked and did {} damage'.format(self.name,damage))
   

def print_health():
    p1=in_battle(trainer_roster)
    p2=in_battle(opponent_roster)
    p1_hp=(trainer_roster[p1][0].hp)
    p2_hp=(opponent_roster[p2][0].hp)
    p1_sh=(trainer_roster[p1][0].starting_health)
    p2_sh=(opponent_roster[p2][0].starting_health)
    print('                 {}s HP:{}/{}'.format(opponent_roster[p2][0].name,p2_hp,p2_sh))
    print('                |'+('*'*int(60*p2_hp/p2_sh))+(' '*(60-int(60*(p2_hp/p2_sh))))+'|')
    print('\n')
    print(' {}s HP:{}/{}'.format(trainer_roster[p1][0].name,p1_hp,p1_sh))
    print('|'+('*'*int(60*p1_hp/p1_sh))+(' '*(60-int(60*(p1_hp/p1_sh))))+'|')


def in_battle(roster):
    for i in range(0,len(roster)):
        if roster[i][1]==True:
            return i

def poke_avail(roster):
    for i in range(0, len(roster)):
        if roster[i][0].hp > 0:
            return True
    return False


def switch(roster):
    index=in_battle(roster)
    if roster[index][0].hp==0:
        for i in range(0, len(roster)):
            if roster[i][0].hp > 0:
                roster[index][1]=False
                roster[i][1]=True
                return

    avail=[]
    print('Available Pokemon:')
    if roster[0][0].hp>0:
        print(' {}'.format(roster[0][0].name))
        avail.append(roster[0][0].name)
    else:
        avail.append(0)
    if roster[1][0].hp>0:
        print(' {}'.format(roster[1][0].name))
        avail.append(roster[1][0].name)
    else:
        avail.append(0)
    if roster[2][0].hp>0:
        print(' {}'.format(roster[2][0].name))
        avail.append(roster[2][0].name)
    else:
        avail.append(0)
    if roster[3][0].hp>0:
        print(' {}'.format(roster[3][0].name))
        avail.append(roster[3][0].name)
    else:
        avail.append(0)
    if roster[4][0].hp>0:
        print(' {}'.format(roster[4][0].name))
        avail.append(roster[4][0].name)
    else:
        avail.append(0)
    if roster[5][0].hp>0:
        print(' {}'.format(roster[5][0].name))
        avail.append(roster[5][0].name)
    else:
        avail.append(0)
    if avail == [0,0,0,0,0,0]:
        print(' ...No other Pokemon available')
        return
    while True:
        choice = input('Choose a pokemon ')
        if choice in avail:
            indexx=avail.index(choice)
            roster[index][1]=False
            roster[indexx][1]=True
            break
        else:
            print('Invalid')


#initializing the intimidating list of legendary pokemon your opponent possesses
o_1=pokemon('Rayquaza',105,'flying',480,95,105)
opponent_roster.append([o_1,False])
o_2=pokemon('Kyogre',100,'water',480,90,100)
opponent_roster.append([o_2,False])
o_3=pokemon('Groudon',100,'ground',480,90,100)
opponent_roster.append([o_3,False])
o_4=pokemon('Mewtwo',106,'psychic',444,130,106)
opponent_roster.append([o_4,False])
o_5=pokemon('Darkrai',70,'dark',405,125,70)
opponent_roster.append([o_5,False])
o_6=pokemon('Arceus',120,'normal',480,120,120)
opponent_roster.append([o_6,False])

def main():
    print('WELCOME TO THE POKEMON LEAGUE FINAL BETWEEN...')
    time.sleep(0.5)
    trainer=input('Your name?: ')
    time.sleep(0.5)
    print('{} and the current League Champion Gary!!!'.format(trainer))
    time.sleep(2)
    print('We will now evaluate the Pokemon each player posseses. Garys roster is as such:')
    time.sleep(2)
    print('Rayquaza - Kyogre - Groudon - Mewtwo - Darkrai - Arceus. In that order.')
    time.sleep(2)
    print('...And yours?')
    time.sleep(2)
    print('Hint: when choosing Pokemon remember to exploit type advantage considering the inherent base superiority the legendary Pokemons possess.')

    while True:
        one = input('What is your FIRST Pokemon --please refer to the Pokedex for available Pokemon and associated stats--: ')
        if one in HPS:
            p_1=pokemon(one,HPS[one],TYPES[one],BASES[one],SPEEDS[one],HPS[one])
            trainer_roster.append([p_1,False])
            break
        else:
            print('Invalid Pokemon. Try again')
    while True:
        two = input('What is your SECOND Pokemon --please refer to the Pokedex for available Pokemon and associated stats--: ')
        if two in HPS:
            p_2=pokemon(two,HPS[two],TYPES[two],BASES[two],SPEEDS[two],HPS[two])
            trainer_roster.append([p_2,False])
            break
        else:
            print('Invalid Pokemon. Try again')
    while True:
        three = input('What is your THIRD Pokemon --please refer to the Pokedex for available Pokemon and associated stats--: ')
        if three in HPS:
            p_3=pokemon(three,HPS[three],TYPES[three],BASES[three],SPEEDS[three],HPS[three])
            trainer_roster.append([p_3,False])
            break
        else:
            print('Invalid Pokemon. Try again')
    while True:
        four = input('What is your FOURTH Pokemon --please refer to the Pokedex for available Pokemon and associated stats--: ')
        if four in HPS:
            p_4=pokemon(four,HPS[four],TYPES[four],BASES[four],SPEEDS[four],HPS[four])
            trainer_roster.append([p_4,False])
            break
        else:
            print('Invalid Pokemon. Try again')
    while True:
        five = input('What is your FIFTH Pokemon --please refer to the Pokedex for available Pokemon and associated stats--: ')
        if five in HPS:
            p_5=pokemon(five,HPS[five],TYPES[five],BASES[five],SPEEDS[five],HPS[five])
            trainer_roster.append([p_5,False])
            break
        else:
            print('Invalid Pokemon. Try again')
    while True:
        six = input('What is your SIXTH Pokemon --please refer to the Pokedex for available Pokemon and associated stats--: ')
        if six in HPS:
            p_6=pokemon(six,HPS[six],TYPES[six],BASES[six],SPEEDS[six],HPS[six])
            trainer_roster.append([p_6,False])
            break
        else:
            print('Invalid Pokemon. Try again')
    
    print('Are you ready?')
    print('3')
    time.sleep(1)
    print('2')
    time.sleep(1)
    print('1')
    print('BEGIN!')
    trainer_roster[0][1]=True
    opponent_roster[0][1]=True
    turn = bool(random.getrandbits(1))
    while True:
        print_health()
        p1=in_battle(trainer_roster)
        p2=in_battle(opponent_roster)
        if (trainer_roster[p1][0].hp>0) and (opponent_roster[p2][0].hp > 0):
            if turn:
                turn = not turn
                if trainer_roster[p1][0].hp==0:
                    switch(trainer_roster)
                print('{}s turn.'.format(trainer_roster[p1][0].name))
                action = input('Attack or Switch? ')
                while True:
                    if action == 'Attack':
                        trainer_roster[p1][0].attack(opponent_roster[p1][0])
                        time.sleep(2)
                        print_health()
                        break
                    elif action == 'Switch':
                        switch(trainer_roster)
                        time.sleep(2)
                        print_health()
                        break
                    else:
                        print('Invalid input')
            else:
                turn = not turn
                if opponent_roster[p2][0].hp==0:
                    switch(opponent_roster)
                print('{}s turn.'.format(opponent_roster[p2][0].name))
                opponent_roster[p2][0].attack(trainer_roster[p1][0])
                
                time.sleep(2)
                print_health()
                
            if (not turn) and trainer_roster[p1][0].speed < opponent_roster[p2][0].speed:
                if trainer_roster[p1][0].hp==0:
                    switch(trainer_roster)
                print('{}s turn.'.format(trainer_roster[p1][0].name))
                action = lower(input('Attack or Switch? '))
                turn = not turn
                while True:
                    if action == 'attack':
                        trainer_roster[p1][0].attack(opponent_roster[p1][0])
                        time.sleep(2)
                        print_health()
                        break
                    elif action == 'switch':
                        switch(trainer_roster)
                        time.sleep(2)
                        print_health()
                        break
                    else:
                        print('Invalid input')
            else:
                if opponent_roster[p2][0].hp==0:
                    switch(opponent_roster)
                print('{}s turn.'.format(opponent_roster[p2][0].name))
                opponent_roster[p2][0].attack(trainer_roster[p1][0])
                turn = not turn
                time.sleep(2)
                print_health()
        elif (trainer_roster[p1][0].hp == 0) and (poke_avail(trainer_roster)):
            switch(trainer_roster)
        elif (opponent_roster[p2][0].hp == 0) and (poke_avail(opponent_roster)):
            switch(opponent_roster)
        else:
            if poke_avail(trainer_roster):
                print('UNBELIEVABLE!!! Gary has been defeated. The visitor has won the LEAGUE!')
                break
            else:
                print('The visitor loses as was expected. Gary retains his status as League Champion!')
                break

if __name__ == "__main__":
    main()