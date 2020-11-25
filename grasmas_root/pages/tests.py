
from . views import create_grid
from . models import Gift


def setup():
    Gift.objects.create(giver="jon", title='pony', desc='Wonderful, sparkly, baby horse', recvr='', author='fred')


def test_create_grid():
    g = Gift.objects.all()
    rows = create_grid(g)
    assert '' == rows
