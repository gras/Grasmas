from django.shortcuts import render
from django.http import HttpResponse
from . models import Gift

# global variables

# gift_display is the data behind the display board
# it is a list of lists (for row, col) containing a list of
gift_display = []

# players is the list of players
players = []

# lamp_player is the lucky person to win the lamp
lamp_player = ''

# last_player is the player that opened the last gift
last_player = ''

# curr_player is the player selecting a gift
curr_player = ''

# next_player is the index of player to open the next gift
next_player = 0

# num_trades keeps track of how many trades occur in one turn
num_trades = 0


# run this once to put fake data into the database for testing
def populate(request):
    # get rid of the old data
    Gift.objects.all().delete()

    Gift(giver='Jon', title='Shiny Pony', desc='A lovely little pony with a sparkly tail!',
         author='Jon', color="blue", image="15").save()
    Gift(giver='Maria', title='Teddy Bear', desc='A soft guy to cuddle',
         author='Jon', color="brown", image="6").save()
    Gift(giver='Jim', title='Electric Drill', desc='You need more holes',
         author='Fred', color="gold", image="5").save()
    Gift(giver='Lizzie', title='Chain Saw', desc="Don't cut the wrong limb!!",
         author='Barney', color="green", image="10").save()
    Gift(giver='Emma', title='Rocking Chair', desc='A place to put your babies to sleep!',
         author='Barney', color="grey", image="2").save()
    Gift(giver='Albert', title='Red Bicycle', desc='It is faster than a rocket!',
         author='Wilma', color="lavender", image="3").save()
    Gift(giver='Dan', title='Sled', desc='Made by Radio Flyer',
         author='Wilma', color="black", image="12").save()
    Gift(giver='Margee', title='Wagon', desc='Haul all your stuff',
         author='Betty', color="lime", image="7").save()
    Gift(giver='Nick', title='Pow-pow-power Wheels', desc='Whatever the hell those are...',
         author='Betty', color="orange", image="8").save()
    Gift(giver='Christine', title='American Girl Doll', desc='Looks just like you',
         author='Bam-Bam', color="pink", image="9").save()
    Gift(giver='Mark R', title='Barbie', desc="You'll need to get your own Ken",
         author='Dino', color="purple", image="1").save()
    Gift(giver='Mark G', title='GI Joe', desc='Dress him like Rambo',
         author='Dino', color="red", image="11").save()
    Gift(giver='Dee', title='Drum Set', desc='Your kids will love it!!  (Ear plugs included)',
         author='Pebbles', color="turquoise", image="4").save()
    Gift(giver='Chuck', title='Skate Board', desc='You too can be a Sk8r Boi',
         author='Pebbles', color="white", image="13").save()
    Gift(giver='Sophie', title='Mario Cart Game', desc='Heavily used but still fun',
         author='Pebbles', color="yellow", image="14").save()

    # pull the gifts from the database
    gift_list = Gift.objects.all()
    gl_size = len(gift_list)
    msgs = ["{} gifts are loaded".format(gl_size)]

    context = {
        'msgs': msgs,
    }
    # assert False
    return render(request, 'page.html', context)


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
    gift_list = Gift.objects.all()

    # randomly place the gifts in the grid
    for gift_data in gift_list:
        r = randrange(rows - 1) + 1
        c = randrange(cols - 1) + 1
        while gift_display[r][c] != {}:
            r = randrange(rows - 1) + 1
            c = randrange(cols - 1) + 1

        # gift_loc is a string location as a pair of characters (i.e. "M4")
        gift_loc = "{}{}".format(columns[c], r)

        # gift_url is the url that takes us to the unveiling of the gift
        gift_url = "present/" + gift_loc

        # put the url into the grid
        gift_display[r][c] = {"display": "wrapped gift",
                              "url": gift_url,
                              "giver": gift_data.giver,
                              "title": gift_data.title,
                              "desc": gift_data.desc,
                              "color": gift_data.color,
                              "image": gift_data.image,
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
    return render(request, 'page.html', context)


def present(request, position):
    global gift_display, players, lamp_player, curr_player, next_player, last_player, num_trades

    c = [' ', 'G', 'R', 'A', 'S', 'M'].index(position[0])
    r = int(position[1])
    g = gift_display[r][c]

    msgs = []

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
            if old_owner == last_player:
                result = "*** ILLEGAL *** {} tried to take back {}'s".format(new_owner, old_owner)
                curr_player = new_owner
                new_owner = old_owner
            else:
                if num_trades < 6:
                    result = "{} stole {}'s".format(new_owner, old_owner)
                    curr_player = old_owner
                    last_player = new_owner
                    num_trades += 1
                else:
                    result = "!!! JUST STOP !!!  Pick an wrapped gift.  You can't have the"
                    curr_player = new_owner
                    new_owner = old_owner
        else:
            result = "{} unwrapped the".format(curr_player)
            next_player += 1
            num_trades = 0
            gift_display[r][c]["open"] = True
            if next_player < len(players):
                curr_player = players[next_player]
            else:
                curr_player = "EndOfRound"

        gift_display[r][c]["owner"] = new_owner
        gift_display[r][c]["display"] = "{}'s {}".format(new_owner, g["title"])

    context = {
        'gift': g,
        'message': result,
        'msgs': msgs,
        'players': players,
    }
    return render(request, 'gift.html', context)


def board(request):
    global gift_display, curr_player

    msgs = ["{}'s turn What gift do you choose?".format(curr_player)]
    context = {
        'rows': gift_display,
        'msgs': msgs,
        'players': players,
    }
    # assert False
    return render(request, 'page.html', context)
