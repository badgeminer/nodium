import pygame,nodeium,sys



pygame.init()
scr = pygame.display.set_mode((500,500))
nd = nodeium.node((255,0,0),(10,10,100,50),"start")
n = nodeium.node((0,255,0),(120,10,50,50))
ne = nodeium.node((0,255,0),(180,10,50,50),"end")
n.incon[0].connd = nd.outcon[0]
n.incon[1].connd = nd.outcon[1]
nd.incon = []
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