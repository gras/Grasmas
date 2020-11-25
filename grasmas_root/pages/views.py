from django.shortcuts import render
from . models import Gift


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


def showgrid(request):
    rows = create_grid(Gift.objects.all())
    context = {
        'rows': rows,
    }
    #     'gift_list': Gift.objects.all(),
    # }
    # assert False
    return render(request, 'pages/page.html', context)


def create_grid(gift_list):
    from random import randrange
    cols = 6
    rows = 5
    # gift_display = [["" for i in range(cols)] for j in range(rows)]
    gift_array = [["" for i in range(cols)] for j in range(rows)]
    # add the row numbers
    for i in range(rows):
        gift_array[i][0] = i + 1
    gift_list = Gift.objects.all()
    gl_size = len(gift_list)
    for g in gift_list:
        r = randrange(5)
        c = randrange(5) + 1
        while gift_array[r][c] != "":
            r = randrange(5)
            c = randrange(5) + 1
        gift_array[r][c] = "wrapped gift"

    # row1 = ['1', 'toyG1', 'toyR1', 'toyA1', 'toyS1', 'toyM1']
    # row2 = ['2', 'toyG2', 'toyR2', 'toyA2', 'toyS2', 'toyM2']
    # row3 = ['3', 'toyG3', 'toyR3', 'toyA3', 'toyS3', 'toyM3']
    # row4 = ['4', 'toyG4', 'toyR4', 'toyA4', 'toyS4', 'toyM4']
    # row5 = ['5', 'toyG5', 'toyR5', 'toyA5', 'toyS5', 'toyM5']
    # rows = [row1, row2, row3, row4, row5]
    # gift_list = Gift.objects.all()
    # for gift in gift_list:
    #     gg = gift.giver
    #     gt = gift.title
    #     gd = gift.desc
    #     gr = gift.recvr
    #     ga = gift.author
    #     assert False
    return gift_array


