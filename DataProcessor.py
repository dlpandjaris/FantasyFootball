# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 11:46:04 2020

@author: Dylan Pandjaris
"""

import csv

class Player():
    def __init__(self, rank, name, team, position, price, bye, taken, mine):
        self.rank = rank
        self.name = name
        self.team = team
        self.position = position
        self.price = price
        self.bye = bye
        self.taken = taken
        self.mine = mine
        
    def __str__(self):
        return("{} {} {} {} {} {}".format(self.rank, self.name, self.team, self.position, self.price, self.bye))
        
def get_rank(rank_name):
    rank = ""
    for char in rank_name:
        if char == ".":
            break
        else:
            rank += char
    return(int(rank))

def get_name(rank_name):
    name = ""
    spaces = 0
    for char in rank_name:
        if spaces > 0:
            name += char
        if char == " ":
            spaces += 1
    return(name)

def get_team(team_position):
    team = ""
    spaces = 0
    for char in team_position:
        if spaces == 1 and char != " ":
            team += char
        if char == " ":
            spaces += 1
    return(team)

def get_position(team_position):
    position = ""
    spaces = 0
    for char in team_position:
        if spaces == 3:
            if char not in "1234567890":
                position += char
        if char == " ":
            spaces += 1
    return(position)

def get_price(price_bye):
    price = ""
    spaces = 0
    for char in price_bye:
        if spaces == 1 and char in "1234567890":
            price += char
        if char == " ":
            spaces += 1
    return(int(price))

def get_bye(price_bye):
    bye = ""
    spaces = 0
    for char in price_bye:
        if spaces == 3 and char in "1234567890":
            bye += char
        if char == " ":
            spaces += 1
    if bye == "":
        bye = 0
    return(int(bye))

data = []
with open("RawData.txt") as csvfile:
    readcsv = csv.reader(csvfile)#, delimiter = ",")
    for row in readcsv:
        rank = get_rank(row[0])
        name = get_name(row[0])
        team = get_team(row[1])
        position = get_position(row[1])
        price = get_price(row[2])
        bye = get_bye(row[2])
        player = Player(rank, name, team, position, price, bye, False, False)
        data.append(player)

ranks = []
names = ""
teams = ""
positions = ""
prices = []
byes = []
for player in data:
    ranks.append(player.rank)
    names += '"%s", ' %player.name
    teams += '"%s", ' %player.team
    positions += '"%s", ' %player.position
    prices.append(player.price)
    byes.append(player.bye)
    
    
taken = []
mine = []
def cross_off_players(taken, mine):
    for player in data:
        if player.name in taken:
            player.taken = True
        if player.name in mine:
            player.mine = True
cross_off_players(taken, mine)

def get_players():
    players = []
    for player in data:
        if player.taken == False:
            players.append(player)
    return(players)

players = get_players()

def get_by_position(players, position, num = -1):
    lst = []
    for player in players:
        if player.position == position:
            lst.append(player)
    return(lst[:num])

# print(get_by_position(players, "QB", 1)[0].name)

def get_positions():
    positions = []
    for player in data:
        if player.position not in positions:
            positions.append(player.position)
    return(positions)

positions = get_positions()
starters = [2, 3, 1, 1, 1, 1]
needed_positions = [4, 4, 2, 2, 2, 2]
# print(positions)

def update_starters():
    for i in range(len(positions)):
        candidates = get_by_position(data, positions[i])
        for player in candidates:
            if player.mine == True:
                starters[i] -= 1
                needed_positions -= 1
update_starters()

def get_starters():
    roster = []
    for i in range(len(positions)):
        picks = get_by_position(players, positions[i], starters[i])
        for pick in picks:
            roster.append(pick)
    return(roster)

def get_players_left():
    players = []
    for player in data:
        if player.mine == False:
            if player.taken == False:
                players.append(player)
    return(players)

# print(starters)

players_left = get_players_left()
def get_next_pick(position):
    most_needed = 0
    pick = get_by_position(players_left, position, 1)
    return(pick[0])

def get_roster():
    players = []
    for player in data:
        if player.mine == True:
            players.append(player)
current_roster = get_roster()


print(positions)
print(starters)
print(current_roster)
print(get_next_pick("RB").name)
        
        

