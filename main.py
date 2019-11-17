import pgzrun
WIDTH = 560
HEIGHT = 480

alien = Actor('alien_1')
alien.pos = 40, 400

def draw():
    screen.fill((0, 0, 0))
    screen.clear()
    alien.draw()

def update():
    check_keys()
    clock.schedule(gravitation, 0.5)
def check_keys():

    if keyboard.left:
        alien.x-=20
        alien.image='alien_2'
    if keyboard.right:
        alien.x+=20
        alien.image='alien_1'
    if alien.x<=40:
        alien.x=40
    if alien.x>=WIDTH-40:
        alien.x=WIDTH-40
    if keyboard.space:
        alien.y-=20

    if alien.y<=46:
        alien.y=46

def gravitation():
    if alien.y<=400:
        alien.y+=10
pgzrun.go()