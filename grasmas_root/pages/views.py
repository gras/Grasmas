from django.shortcuts import render
from . models import Gift

# global variables
gift_display = []
gifts = []
msgs = []
players = []
curr_player = 0


def index(request):
    # gift_list = Gift.objects.all()
    # gift = gift_list[0]
    context = {
        # 'giver': gift.giver,
        # 'title': gift.title,
        # 'title': pg.title,
        # 'content': pg.bodytext,
        # 'last_updated': pg.update_date,
        'gift_list': Gift.objects.all(),
    }
    # assert False
    return render(request, 'pages/page.html', context)


def populate(request):
    # get rid of the old data
    Gift.objects.all().delete()

    Gift(giver='Jon', title='Pony', desc='A lovely little pony with a sparkly tail!', author='Fred').save()
    Gift(giver='Maria', title='Pony1', desc='A lovely little pony with a sparkly tail!', author='Fred').save()
    Gift(giver='Jim', title='Pony2', desc='A lovely little pony with a sparkly tail!', author='Fred').save()
    Gift(giver='Lizzie', title='Pony3', desc='A lovely little pony with a sparkly tail!', author='Fred').save()
    Gift(giver='Emma', title='Pony4', desc='A lovely little pony with a sparkly tail!', author='Fred').save()
    Gift(giver='Albert', title='Pony5', desc='A lovely little pony with a sparkly tail!', author='Fred').save()
    Gift(giver='Dan', title='Pony6', desc='A lovely little pony with a sparkly tail!', author='Fred').save()
    Gift(giver='Margee', title='Pony7', desc='A lovely little pony with a sparkly tail!', author='Fred').save()
    Gift(giver='Nick', title='Pony8', desc='A lovely little pony with a sparkly tail!', author='Fred').save()
    Gift(giver='Christine', title='Pony9', desc='A lovely little pony with a sparkly tail!', author='Fred').save()
    Gift(giver='Mark R', title='Pony10', desc='A lovely little pony with a sparkly tail!', author='Fred').save()
    Gift(giver='Mark G', title='Pony11', desc='A lovely little pony with a sparkly tail!', author='Fred').save()
    Gift(giver='Dee', title='Pony12', desc='A lovely little pony with a sparkly tail!', author='Fred').save()
    Gift(giver='Chuck', title='Pony13', desc='A lovely little pony with a sparkly tail!', author='Fred').save()
    Gift(giver='Sophie', title='Pony14', desc='A lovely little pony with a sparkly tail!', author='Fred').save()

    context = {
        'gift_list': Gift.objects.all(),
    }
    # assert False
    return render(request, 'pages/page.html', context)


def start(request):
    from random import randrange, shuffle

    # size of the grid
    cols = 6
    rows = 6

    # gifts is a dictionary where the key is the location on the board (i.e.'G1')
    # the value is another dictionary containing: giver, title, desc, owner
    global gifts
    gifts = {}

    # gift_display is the data behind the display board
    # it is a list of lists (for row, col) containing a list of
    global gift_display
    gift_display = [[{} for _ in range(cols)] for _ in range(rows)]
    # add the row numbers
    for i in range(rows):
        gift_display[i][0] = {"desc": i}
    # add the column headers
    columns = [' ', 'G', 'R', 'A', 'S', 'M']
    for i, c in enumerate(columns):
        gift_display[0][i] = {"desc": c}

    # msgs is a list of messages for the users, displayed above the grid
    global msgs

    # players is the list of players
    global players
    players = []

    # pull the gifts from the database
    gift_list = Gift.objects.all()
#    gl_size = len(gift_list)
#    msgs = ["{} gifts are loaded".format(gl_size)]

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
        gift_url = "show_gift/" + gift_loc

        # put the url into the grid
        gift_display[r][c] = {"desc": "wrapped gift", "url": gift_url}
        # add each gift to the gifts dictionary
        gifts[gift_loc] = {"giver": gift_data.giver, "title": gift_data.title, "desc": gift_data.desc}
        # add each player to the players list
        players.append(gift_data.giver)

    shuffle(players)
    msgs = ["{} goes first!!".format(players[curr_player]), "Which wrapped gift do you choose?"]
    context = {
        'rows': gift_display,
        'msgs': msgs,
    }
    # assert False
    return render(request, 'pages/page.html', context)


def show_gift(request):
    # for gift in gift_list:
    #     gg = gift.giver
    #     gt = gift.title
    #     gd = gift.desc
    #     gr = gift.recvr
    #     ga = gift.author
    #     assert False
    context = {
        'rows': gift_display,
        'msgs': msgs,
    }
    return render(request, 'pages/gift.html', context)
