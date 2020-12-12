from django.shortcuts import render, redirect
from . models import Gift

# global variables

# gift_display is the data behind the display board
# it is a list of lists (for row, col) containing a list of
gift_display = []

# players is the list of players
players = []

# lamp_player is the lucky person to win the lamp
lamp_player = ''

# lamp_URL is the location of the lamp picture
lamp_URL = ''

# last_player is the player that opened the last gift
last_player = ''

# curr_player is the player selecting a gift
curr_player = ''

# next_player is the index of player to open the next gift
next_player = 0

# num_trades keeps track of how many trades occur in one turn
num_trades = 0


def start(request):
    from random import randrange, shuffle

    global gift_display, players, lamp_player, curr_player, next_player, lamp_player

    # size of the grid
    cols = 6
    rows = 6
    gift_display = [[{} for _ in range(cols)] for _ in range(rows)]
    # add the row numbers
    for i in range(rows):
        gift_display[i][0] = {"display": i}
    # add the column headers
    columns = [' ', 'G', 'R', 'A', 'S', 'M']
    for i, c in enumerate(columns):
        gift_display[0][i] = {"display": c}
    players = []

    # pull the gifts from the database
    gift_list = Gift.objects.exclude(giver='Lamp')

    # randomly place the gifts in the grid
    for gift_data in gift_list:
        r = randrange(rows - 1) + 1
        c = randrange(cols - 1) + 1
        while gift_display[r][c] != {}:
            r = randrange(rows - 1) + 1
            c = randrange(cols - 1) + 1

        # gift_loc is a string location as a pair of characters (i.e. "M4")
        gift_loc = "{}{}".format(columns[c], r)

        gift_display[r][c] = {"display": "wrapped gift",
                              "giver": gift_data.giver,
                              "title": gift_data.title,
                              "desc": gift_data.desc,
                              "color": gift_data.color,
                              "photo": gift_data.photo,
                              "location": gift_loc,
                              }
        # add each player to the players list
        players.append(gift_data.giver)

    shuffle(players)
    lamp_player = players[0]
    shuffle(players)
    next_player = 0
    curr_player = players[0]
    msgs = ["{} goes first!!  Which wrapped gift do you choose?".format(curr_player)]
    context = {
        'rows': gift_display,
        'msgs': msgs,
        'players': players,
    }
    # assert False
    return render(request, 'board.html', context)


def present(request, position):
    global gift_display, players, lamp_player, curr_player, next_player, last_player, num_trades, lamp_URL

    c = [' ', 'G', 'R', 'A', 'S', 'M'].index(position[0])
    r = int(position[1])
    g = gift_display[r][c]

    stealing = False
    if curr_player == lamp_player:
        result = "!!! WINNER !!!"
        g = {'title': "{}".format(curr_player),
             'desc': 'WON THE LAMP',
             'image': 'lamp',
             }
        lamp_player = ''
    else:
        new_owner = curr_player
        if 'owner' in g:
            old_owner = g["owner"]

            print("curr_player", curr_player)
            print("last_player", last_player)
            print("new_owner", new_owner)
            print("old_owner", old_owner)

            if old_owner == last_player:
                result = "*** ILLEGAL *** {} tried to take back {}'s".format(new_owner, old_owner)
                # curr_player = new_owner
                # new_owner = old_owner
            else:
                if num_trades < 6:
                    result = "Do you want to steal {}'s".format(old_owner)
                    stealing = True
                    # curr_player = old_owner
                    # last_player = new_owner
                    # num_trades += 1
                else:
                    result = "!!! JUST STOP !!!  Pick an wrapped gift.  You can't have the"
                    # curr_player = new_owner
                    # new_owner = old_owner
        else:
            result = "{} unwrapped the".format(curr_player)
            next_player += 1
            num_trades = 0
            gift_display[r][c]["open"] = True
            gift_display[r][c]["owner"] = curr_player
            gift_display[r][c]["display"] = "{}'s {}".format(curr_player, g["title"])
            if next_player < len(players):
                last_player = curr_player
                curr_player = players[next_player]
            else:
                curr_player = "EndOfRound"

    context = {
        'gift': g,
        'message': result,
        'stealing': stealing,
        'players': players,
    }
    return render(request, 'gift.html', context)


def board(request):
    global gift_display, curr_player, next_player, last_player

    msgs = ["{}'s turn What gift do you choose?".format(curr_player)]
    context = {
        'rows': gift_display,
        'msgs': msgs,
        'players': players,
    }
    # assert False
    print("curr_player", curr_player)
    print("last_player", last_player)
    return render(request, 'board.html', context)


def steal(request, position):
    global gift_display, curr_player, last_player, num_trades

    c = [' ', 'G', 'R', 'A', 'S', 'M'].index(position[0])
    r = int(position[1])
    g = gift_display[r][c]

    new_owner = curr_player
    curr_player = g["owner"]
    last_player = new_owner
    num_trades += 1
    print("curr_player", curr_player)
    print("last_player", last_player)
    print("new_owner", new_owner)

    gift_display[r][c]["owner"] = new_owner
    gift_display[r][c]["display"] = "{}'s {}".format(new_owner, g["title"])
    return redirect('board')
