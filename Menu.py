import pygame

class Menu(object):
    pygame.init()
    #fonts
    gameOverFont = pygame.font.Font('images/ARDARLING.ttf' ,70)
    clickToStart = pygame.font.Font('images/ARDARLING.ttf',40)
    highScore = pygame.font.Font('images/ARDARLING.ttf',50)

    def __init__(self):
        
#MENU IMAGES
    #0 centi
    #200 play
    #325 high
    #425 ins
    #525 quit
    #700 footer
        self.menu_header=[]
        self.menu_header.append(pygame.image.load("images/menuMario_centi1.png"))
        self.menu_header.append(pygame.image.load("images/menuMario_centi2.png"))
        self.menu_high=[]
        self.menu_high.append(pygame.image.load("menu_high1.png"))
        self.menu_high.append(pygame.image.load("menu_high2.png"))
        self.menu_ins=[]
        self.menu_ins.append(pygame.image.load("menu_ins1.png"))
        self.menu_ins.append(pygame.image.load("menu_ins2.png"))
        self.menu_play=[]
        self.menu_play.append(pygame.image.load("menu_play1.png"))
        self.menu_play.append(pygame.image.load("menu_play2.png"))
        self.menu_quit=[]
        self.menu_quit.append(pygame.image.load("menu_quit1.png"))
        self.menu_quit.append(pygame.image.load("menu_quit2.png"))
        self.menu_footer=pygame.image.load("menu_footer.png")
#INSTRUCTIONS IMAGES
        self.inst_space=[]
        for i in range(1,5):
            self.inst_space.append(pygame.image.load("instructions%d.png" % i))
        self.inst_up=[]
        for i in range(1,5):
            self.inst_up.append(pygame.image.load("instructions_up%d.png" % i))
        self.inst_shroom=[]
        for i in range(1,7):
            self.inst_shroom.append(pygame.image.load("instructions_shroom%d.png" % i))
        self.inst_bomb=[]
        for i in range(1,5):
            self.inst_bomb.append(pygame.image.load("instructions_bomb%d.png" % i))
        self.inst_spider=[]
        for i in range(1,5):
            self.inst_spider.append(pygame.image.load("instructions_sp%d.png" % i))
        self.inst_centi=[]
        for i in range(1,5):
            self.inst_centi.append(pygame.image.load("instructions_centi%d.png" % i))
        self.inst_footer=pygame.image.load("instructions_footerAAA.png")


    high_footer=pygame.image.load("high_footer.png")
