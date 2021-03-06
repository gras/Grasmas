from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from .forms import GiftForm
from pages.models import Gift
from django.forms.models import model_to_dict


def status(request):
    context = get_gift_list(request)
    gift_list = Gift.objects.all()
    # check for duplicates
    giver_seen = set()
    giver_dups = set()
    giver_uniq = []
    author_uniq = set()
    for g in gift_list:
        author_uniq.add(g.author)
        if g.giver not in giver_seen:
            giver_uniq.append(g.giver)
            giver_seen.add(g.giver)
        else:
            giver_dups.add(g.giver)
    errors = None
    if len(giver_dups) > 0:
        errors = giver_dups
    # build the display
    rows = []
    for a in author_uniq:
        givers = Gift.objects.filter(author=a)
        g = []
        for gvr in givers:
            g.append(gvr.giver)
        rows.append("{} entered gifts for: {}".format(a, g))
    context['rows'] = rows
    context['errors'] = errors
    return render(request, 'status.html', context)


def get_gift_list(request):
    gift_list = Gift.objects.all()
    if len(gift_list.filter(title='Lamp')):
        lamp_msg = "(including the LAMP)"
    else:
        lamp_msg = "(but no LAMP yet...)"
    gl_all = len(gift_list)
    gift_list = Gift.objects.filter(author=request.user)
    gl_user = len(gift_list)
    if gl_all == 0:
        gl_all = 'no'
    if gl_user == 0:
        gl_user = 'no'
    lamp_in_DB = 1
    if request.user.username == 'Mark_R':
        lamp_in_DB = len(gift_list.filter(title='Lamp'))
    context = {
        'lamp_msg': lamp_msg,
        'gl_user': gl_user,
        'gl_all': gl_all,
        'gift_list': gift_list,
        'lamp_owner': lamp_in_DB
    }
    return context


def show(request):
    context = get_gift_list(request)
    return render(request, 'show.html', context)


def add(request):
    if request.method == 'POST':
        form = GiftForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.author = request.user.username
            obj.color = request.user.last_name
            myfile = request.FILES.get('myfile', False)
            if myfile:
                fs = FileSystemStorage()
                filename = fs.save(myfile.name, myfile)
                obj.photo = fs.url(filename)
            obj.save()
            context = get_gift_list(request)
            return render(request, 'show.html', context)
        else:
            return HttpResponse(form.errors)
    else:
        form = GiftForm()
    return render(request, 'add.html', {'form': form})


def add_lamp(request):
    if request.method == 'POST':
        form = GiftForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.author = request.user.username
            obj.color = request.user.last_name
            myfile = request.FILES.get('myfile', False)
            if myfile:
                fs = FileSystemStorage()
                filename = fs.save(myfile.name, myfile)
                obj.photo = fs.url(filename)
            obj.save()
            context = get_gift_list(request)
            return render(request, 'show.html', context)
        else:
            return HttpResponse(form.errors)
    else:
        form = GiftForm(initial={
            'giver': 'Lamp',
            'title': 'Lamp',
            'desc': 'Lamp',
        })
    return render(request, 'add.html', {'form': form})


def edit(request, pk):
    gift = Gift.objects.get(pk=pk)
    if request.method == 'POST':
        form = GiftForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.author = request.user.username
            obj.color = request.user.last_name
            obj.pk = pk
            myfile = request.FILES.get('myfile', False)
            if myfile:
                fs = FileSystemStorage()
                filename = fs.save(myfile.name, myfile)
                obj.photo = fs.url(filename)
            else:
                obj.photo = gift.photo
            obj.save()
            context = get_gift_list(request)
            return render(request, 'show.html', context)
        else:
            return HttpResponse(form.errors)
    else:
        form = GiftForm(initial=model_to_dict(gift))
        context = {
            'form': form,
            'gift': gift,
        }
    return render(request, 'edit.html', context)


def RU_SURE(request, pk):
    context = {'allowed': False}
    if request.method == 'POST':
        gift = Gift.objects.get(pk=pk)
        if request.user.username == gift.author:
            context = {
                'allowed': True,
                'gift': gift,
            }
    return render(request, 'RU_SURE.html', context)


def delete(request, pk):
    if request.method == 'GET':
        gift = Gift.objects.get(pk=pk)
        gift.delete()
    return redirect('show')


def preview(request, pk):
    g = Gift.objects.get(pk=pk)
    result = "Preview of the display for {}'s".format(g.giver)
    context = {
        'gift': g,
        'message': result,
    }
    return render(request, 'preview.html', context)


def maintenance(request):
    return render(request, 'IN_WORK.html')
