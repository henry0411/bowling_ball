from game import Game

def round(player,sorce):
    for i in range(len(sorce)):
        player.roll(scorce(i))

def test_player_1():
    scorces=[8,0,0,1,0,1,6,0,0,7,5,1,0,9,0,0,0,4,1,4,0]#47
    player=Game(scorces)
    ans=player.sum
    assert ans == 47

def test_player_2():
    scorces=[0,8,9,1,10,0,8,1,6,0,9,0,8,1,4,5,10,0,9,0,0]#117
    player=Game(scorces)
    ans=player.sum
    assert ans == 117

def test_player_3():
    scorces=[10,0,3,4,6,3,8,2,10,0,3,7,4,4,10,0,3,7,10,3,7]#155
    player=Game(scorces)
    ans=player.sum
    assert ans == 155

def test_player_4():
    scorces=[10,0,10,0,10,0,10,0,10,0,10,0,10,0,10,0,10,0,10,10,10]#300
    player=Game(scorces)
    ans=player.sum
    assert ans == 300

def test_player_4():
    scorces=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]#0
    player=Game(scorces)
    ans=player.sum
    assert ans == 0



   
