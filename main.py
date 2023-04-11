import pygame,nodeium,sys

pygame.init()
scr = pygame.display.set_mode((500,500))
nd = nodeium.node((255,0,0),(10,10,50,50))
n = nodeium.node((0,255,0),(70,10,50,50))
n.incon[0].connd = nd.outcon[0]
nds = [n,nd]
while True:
    scr.fill((0,0,0))
    for i in nds:
        i.draw(scr)
    pygame.display.flip()
    if pygame.mouse.get_pressed()[0]:
        mp = pygame.mouse.get_pos()
        for i in nds:
            i.click(mp)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()