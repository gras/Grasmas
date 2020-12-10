from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import GiftForm
from django.core.files.storage import FileSystemStorage
from pages.models import Gift
from django.forms.models import model_to_dict


def get_gift_list(request):
    gift_list = Gift.objects.all()
    gl_all = len(gift_list)
    gift_list = Gift.objects.filter(author=request.user)
    gl_user = len(gift_list)
    if gl_all == 0:
        gl_all = 'no'
    if gl_user == 0:
        gl_user = 'no'
    context = {
        'gl_user': gl_user,
        'gl_all': gl_all,
        'gift_list': gift_list,
    }
    return context


def show(request):
    context = get_gift_list(request)
    return render(request, 'show.html', context)


def add(request):
    if request.method == 'POST' and request.FILES['myfile']:
        print("ADD POST")
        form = GiftForm(request.POST, request.FILES)
        if form.is_valid():
            myfile = request.FILES['myfile']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            obj = form.save(commit=False)
            obj.author = request.user.username
            obj.color = request.user.last_name
            obj.photo = fs.url(filename)
            obj.save()
            return redirect('show')
        else:
            return HttpResponse(form.errors)
    else:
        print("ADD ELSE ", request.method)
        form = GiftForm()
    return render(request, 'add.html', {'form': form})


def edit(request, pk):
    gift = Gift.objects.get(pk=pk)
    print(request.FILES)
    if request.method == 'POST':
        print("EDIT POST")
        form = GiftForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.author = request.user.username
            obj.color = request.user.last_name
            obj.pk = pk
            myfile = request.FILES.get('myfile', False)
            print('***** ', myfile)
            print('***** ', gift.photo)
            if myfile:
                fs = FileSystemStorage()
                filename = fs.save(myfile.name, myfile)
                obj.photo = fs.url(filename)
                print('IF   ##### ', obj.photo)
            else:
                obj.photo = gift.photo
                print('ELSE ##### ', obj.photo)
            obj.save()
            context = get_gift_list(request)
            return render(request, 'show.html', context)
        else:
            print("ADD FORM INVALID ")
            # todo return readable form errors
            return HttpResponse(form.errors)
    else:
        print("EDIT ELSE ", request.method)
        # todo add the image to the context and html!
        # todo add submit button
        # todo make the upload button work
        form = GiftForm(initial=model_to_dict(gift))
        print(gift)
        context = {
            'form': form,
            'gift': gift,
        }
    return render(request, 'edit.html', context)


def RU_SURE(request, pk):
    if request.method == 'POST':
        gift = Gift.objects.get(pk=pk)
        context = {
            'gift': gift,
        }
    return render(request, 'RU_SURE.html', context)


def delete(request, pk):
    if request.method == 'GET':
        gift = Gift.objects.get(pk=pk)
        gift.delete()
    return redirect('show')
