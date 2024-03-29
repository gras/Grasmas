from django.shortcuts import render, redirect
from . models import Gift


def start(request):
    from random import randrange, shuffle

    '''
    These are the session data elements
    
    gift_display is the data behind the display board
    it is a list of lists (for row, col) containing a list of
    gift_display = []
    
    players is the list of players
    players = []
    
    lamp_player is the lucky person that is GOING TO win the lamp
    lamp_player = ''
    
    lamp_winner is the lucky person that HAS won the lamp
    lamp_winner = ''
    
    lamp_URL is the location of the lamp picture
    lamp_URL = ''
    
    last_player is the player that opened the last gift
    last_player = ''
    
    curr_player is the player selecting a gift
    curr_player = ''
    
    next_player is the index of player to open the next gift
    next_player = 0
    
    num_trades keeps track of how many trades occur in one turn
    num_trades = 0
    '''
    # size of the grid
    column_header = [' ', 'H', 'O', 'L', 'I', 'D', 'A', 'Y']
    cols = len(column_header)
    rows = 6
    print('rows:', rows, 'cols', cols)
    gift_display = [[{} for _ in range(cols)] for _ in range(rows)]
    # add the row numbers
    for i in range(rows):
        gift_display[i][0] = {"display": i}
    # add the column headers
    for i, c in enumerate(column_header):
        gift_display[0][i] = {"display": c}
    players = []
    # pull the gifts from the database
    gift_list = Gift.objects.exclude(giver='Lamp')
    lamp = Gift.objects.filter(giver='Lamp')
    lamp_URL = lamp[0].photo
    # randomly place the gifts in the grid
    for gift_data in gift_list:
        r = randrange(rows - 1) + 1
        c = randrange(cols - 1) + 1
        while gift_display[r][c] != {}:
            r = randrange(rows - 1) + 1
            c = randrange(cols - 1) + 1

        # gift_loc is a string location as a pair of characters (i.e. "M4")
        gift_loc = "{}{}".format(column_header[c], r)

        gift_display[r][c] = {"display": "wrapped gift",
                              "giver": gift_data.giver,
                              "title": gift_data.title,
                              "desc": gift_data.desc,
                              "color": gift_data.color,
                              "photo": str(gift_data.photo),
                              "location": gift_loc,
                              }
        # add each player to the players list
        players.append(gift_data.giver)
    shuffle(players)
    lamp_player = players[0]
    if lamp_player == 'Mark_R':
        lamp_player = players[1]
    lamp_winner = ''
    shuffle(players)
    next_player = 0
    curr_player = players[0]
    last_player = ''
    num_trades = 0
    msgs = ["{} goes first!!  Which wrapped gift do you choose?".format(curr_player)]
    context = {
        'rows': gift_display,
        'msgs': msgs,
        'players': players,
        'curr_player': curr_player,
        'lamp_winner': lamp_winner,
        'lamp_URL': lamp_URL,
        'column_header': column_header
    }
    request.session['gift_display'] = gift_display
    request.session['players'] = players
    request.session['lamp_player'] = lamp_player
    request.session['lamp_winner'] = lamp_winner
    request.session['curr_player'] = curr_player
    request.session['next_player'] = next_player
    request.session['last_player'] = last_player
    request.session['num_trades'] = num_trades
    request.session['lamp_URL'] = str(lamp_URL)
    request.session['column_header'] = column_header

    return render(request, 'board.html', context)


def present(request, position):
    gift_display = request.session.get('gift_display')
    players = request.session.get('players')
    lamp_player = request.session.get('lamp_player')
    lamp_winner = request.session.get('lamp_winner')
    curr_player = request.session.get('curr_player')
    next_player = request.session.get('next_player')
    last_player = request.session.get('last_player')
    num_trades = request.session.get('num_trades')
    lamp_URL = request.session.get('lamp_URL')
    column_header = request.session.get('column_header')

    c = column_header.index(position[0])
    r = int(position[1])
    g = gift_display[r][c]

    end_of_round_names = ['EndOfRound1', 'EndOfFinalRound']
    stealing = False
    if curr_player == lamp_player:
        result = "!!! WINNER !!!"
        g = {'title': "{}".format(curr_player),
             'desc': 'WON THE LAMP',
             'photo': lamp_URL,
             }
        lamp_player = ''
        lamp_winner = curr_player
    else:
        # stealing an open gift
        new_owner = curr_player
        if 'owner' in g:
            old_owner = g["owner"]
            if num_trades > 0 and old_owner == last_player:
                result = "*** ILLEGAL *** {} tried to take back {}'s".format(new_owner, old_owner)
            else:
                if num_trades < 4:
                    if curr_player in end_of_round_names:
                        result = "{}'s".format(old_owner)
                    else:
                        result = "{} do you want to steal {}'s".format(new_owner, old_owner)
                        stealing = True
                else:
                    result = "{} !!! JUST STOP !!!  You can't have {}'s".format(new_owner, old_owner)
        else:
            # opening a wrapped gift
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
                curr_player = "EndOfRound1"

    context = {
        'gift': g,
        'message': result,
        'stealing': stealing,
        'players': players,
        'lamp_winner': lamp_winner,
        'lamp_URL': lamp_URL,
    }
    request.session['gift_display'] = gift_display
    request.session['players'] = players
    request.session['lamp_player'] = lamp_player
    request.session['lamp_winner'] = lamp_winner
    request.session['curr_player'] = curr_player
    request.session['next_player'] = next_player
    request.session['last_player'] = last_player
    request.session['num_trades'] = num_trades
    request.session['lamp_URL'] = lamp_URL
    request.session['column_header'] = column_header
    return render(request, 'gift.html', context)


def board(request):
    gift_display = request.session.get('gift_display')
    players = request.session.get('players')
    lamp_player = request.session.get('lamp_player')
    lamp_winner = request.session.get('lamp_winner')
    curr_player = request.session.get('curr_player')
    next_player = request.session.get('next_player')
    last_player = request.session.get('last_player')
    num_trades = request.session.get('num_trades')
    lamp_URL = request.session.get('lamp_URL')

    if curr_player == "EndOfRound1":
        msgs = ["---  Time to review the gifts!  ---"]
    elif curr_player == "EndOfFinalRound":
        msgs = ["***  !!! MERRY GRASMAS !!!  ***"]
    else:
        msgs = ["{}'s turn What gift do you choose?".format(curr_player)]

    context = {
        'rows': gift_display,
        'msgs': msgs,
        'players': players,
        'curr_player': curr_player,
        'lamp_winner': lamp_winner,
        'lamp_URL': lamp_URL,
    }
    request.session['gift_display'] = gift_display
    request.session['players'] = players
    request.session['lamp_player'] = lamp_player
    request.session['lamp_winner'] = lamp_winner
    request.session['curr_player'] = curr_player
    request.session['next_player'] = next_player
    request.session['last_player'] = last_player
    request.session['num_trades'] = num_trades
    request.session['lamp_URL'] = lamp_URL
    return render(request, 'board.html', context)


def steal(request, position):
    gift_display = request.session.get('gift_display')
    players = request.session.get('players')
    lamp_player = request.session.get('lamp_player')
    lamp_winner = request.session.get('lamp_winner')
    curr_player = request.session.get('curr_player')
    next_player = request.session.get('next_player')
    last_player = request.session.get('last_player')
    num_trades = request.session.get('num_trades')
    lamp_URL = request.session.get('lamp_URL')
    column_header = request.session.get('column_header')

    c_new = column_header.index(position[0])
    r_new = int(position[1])
    g_new = gift_display[r_new][c_new]

    if last_player == 'FinalRound':
        r_old = -1
        c_old = -1
        for r in range(6):
            for c in range(6):
                if 'owner' in gift_display[r][c]:
                    if gift_display[r][c]['owner'] == curr_player:
                        r_old = r
                        c_old = c
        old_owner = gift_display[r_new][c_new]['owner']
        old_title = gift_display[r_old][c_old]["title"]
        new_owner = curr_player
        gift_display[r_old][c_old]["owner"] = old_owner
        gift_display[r_old][c_old]["display"] = "{}'s {}".format(old_owner, old_title)
        num_trades = 0
        next_player -= 1
        if next_player >= 0:
            curr_player = players[next_player]
        else:
            curr_player = "EndOfFinalRound"
    else:
        # first round
        new_owner = curr_player
        curr_player = g_new["owner"]
        last_player = new_owner
        num_trades += 1

    gift_display[r_new][c_new]["owner"] = new_owner
    gift_display[r_new][c_new]["display"] = "{}'s {}".format(new_owner, g_new["title"])

    request.session['gift_display'] = gift_display
    request.session['players'] = players
    request.session['lamp_player'] = lamp_player
    request.session['lamp_winner'] = lamp_winner
    request.session['curr_player'] = curr_player
    request.session['next_player'] = next_player
    request.session['last_player'] = last_player
    request.session['num_trades'] = num_trades
    request.session['lamp_URL'] = lamp_URL
    return redirect('board')


def final(request):
    gift_display = request.session.get('gift_display')
    players = request.session.get('players')
    lamp_player = request.session.get('lamp_player')
    lamp_winner = request.session.get('lamp_winner')
    curr_player = request.session.get('curr_player')
    next_player = request.session.get('next_player')
    last_player = request.session.get('last_player')
    num_trades = request.session.get('num_trades')
    lamp_URL = request.session.get('lamp_URL')

    last_player = 'FinalRound'
    next_player = len(players) - 1
    curr_player = players[next_player]
    msgs = ["{} goes first!!  Which gift do you choose?".format(curr_player)]
    context = {
        'rows': gift_display,
        'msgs': msgs,
        'players': players,
        'curr_player': curr_player,
        'lamp_winner': lamp_winner,
        'lamp_URL': lamp_URL,
    }
    request.session['gift_display'] = gift_display
    request.session['players'] = players
    request.session['lamp_player'] = lamp_player
    request.session['lamp_winner'] = lamp_winner
    request.session['curr_player'] = curr_player
    request.session['next_player'] = next_player
    request.session['last_player'] = last_player
    request.session['num_trades'] = num_trades
    request.session['lamp_URL'] = lamp_URL
    return render(request, 'board.html', context)
