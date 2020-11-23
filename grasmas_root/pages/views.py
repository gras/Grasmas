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


def gridtest(request):
    context = {
        'gift_list': Gift.objects.all(),
    }
    # assert False
    return render(request, 'pages/page.html', context)
