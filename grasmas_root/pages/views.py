from django.shortcuts import render
from . models import Gift

# global variables
gift_display = []
gift_array = []
msgs = []
players = []


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
    gifts = Gift.objects.all()
    gifts.delete()

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
    global gift_array, gift_display, msgs, players
    cols = 5
    rows = 5
    # store the data for the gift
    gift_array = [["" for _ in range(cols + 1)] for _ in range(rows)]
    # display the status of the gift
    gift_display = [["" for _ in range(cols + 1)] for _ in range(rows)]
    # add the row numbers
    for i in range(rows):
        gift_display[i][0] = i + 1
    # pull the gifts from the database
    gift_list = Gift.objects.all()
#    gl_size = len(gift_list)
#    msgs = ["{} gifts are loaded".format(gl_size)]
    players = []
    column = [' ', 'G', 'R', 'A', 'S', 'M']
    for gift_data in gift_list:
        r = randrange(rows)
        c = randrange(cols) + 1
        while gift_display[r][c] != "":
            r = randrange(rows)
            c = randrange(cols) + 1
        gift_display[r][c] = ["wrapped gift", r + 1, column[c]]
        gift_array[r][c] = gift_data
        players.append(gift_data.giver)
    shuffle(players)
    msgs = ["{} goes first!!".format(players[0]), "Which wrapped gift do you choose?"]
    context = {
        'rows': gift_display,
        'msgs': msgs,
    }
    return render(request, 'pages/page.html', context)


def run_game(request):
    # for gift in gift_list:
    #     gg = gift.giver
    #     gt = gift.title
    #     gd = gift.desc
    #     gr = gift.recvr
    #     ga = gift.author
    #     assert False

    pass


def show_gift(request):
    assert False
    # for gift in gift_list:
    #     gg = gift.giver
    #     gt = gift.title
    #     gd = gift.desc
    #     gr = gift.recvr
    #     ga = gift.author
    #     assert False

    pass
