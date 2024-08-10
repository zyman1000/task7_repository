import pygame as pg

pg.init()
screen = pg.display.set_mode((480, 480))
pg.display.set_caption("Chess")
icon = pg.image.load("white_knite.png")
pg.display.set_icon(icon)
white_bishop = pg.image.load("white_bishop.png")
white_king = pg.image.load("white_king.png")
white_knite = pg.image.load("white_knite.png")
white_pawn = pg.image.load("white_pawn.png")
white_queen = pg.image.load("white_queen.png")
white_rook = pg.image.load("white_rook.png")
black_bishop = pg.image.load("black_bishop.png")
black_king = pg.image.load("black_king.png")
black_knite = pg.image.load("black_knite.png")
black_pawn = pg.image.load("black_pawn.png")
black_queen = pg.image.load("black_queen.png")
black_rook = pg.image.load("black_rook.png")

W_bishop1 = [white_bishop, 120, 420]
W_bishop2 = [white_bishop, 300, 420]
W_knite1 = [white_knite, 60, 420]
W_knite2 = [white_knite, 360, 420]
W_rook1 = [white_rook, 0, 420]
W_rook2 = [white_rook, 420, 420]
W_pawn1 = [white_pawn, 0, 360]
W_pawn2 = [white_pawn, 60, 360]
W_pawn3 = [white_pawn, 120, 360]
W_pawn4 = [white_pawn, 180, 360]
W_pawn5 = [white_pawn, 240, 360]
W_pawn6 = [white_pawn, 300, 360]
W_pawn7 = [white_pawn, 360, 360]
W_pawn8 = [white_pawn, 420, 360]
B_bishop1 = [black_bishop, 120, 0]
B_bishop2 = [black_bishop, 300, 0]
B_knite1 = [black_knite, 60, 0]
B_knite2 = [black_knite, 360, 0]
B_rook1 = [black_rook, 0, 0]
B_rook2 = [black_rook, 420, 0]
B_pawn1 = [black_pawn, 0, 60]
B_pawn2 = [black_pawn, 60, 60]
B_pawn3 = [black_pawn, 120, 60]
B_pawn4 = [black_pawn, 180, 60]
B_pawn5 = [black_pawn, 240, 60]
B_pawn6 = [black_pawn, 300, 60]
B_pawn7 = [black_pawn, 360, 60]
B_pawn8 = [black_pawn, 420, 60]
white = {
    'bishop' : [W_bishop1, W_bishop2],
    'king' : [white_king, 240, 420],
    'queen' : [white_queen, 180, 420],
    'knite' : [W_knite1, W_knite2],
    'rook' : [W_rook1, W_rook2],
    'pawn' : [W_pawn1, W_pawn2, W_pawn3, W_pawn4, W_pawn5, W_pawn6, W_pawn7, W_pawn8]
}
black = {
    'bishop' : [B_bishop1, B_bishop2],
    'king' : [black_king, 240, 0],
    'queen' : [black_queen, 180, 0],
    'knite' : [B_knite1, B_knite2],
    'rook' : [B_rook1, B_rook2],
    'pawn' : [B_pawn1, B_pawn2, B_pawn3, B_pawn4, B_pawn5, B_pawn6, B_pawn7, B_pawn8]
}
peices = [white, black]
def main():
    game_on = True
    while game_on:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                game_on = False
            elif event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_click(event.pos[0], event.pos[1])
        #if pg.mouse.get_pressed()[0] == True:
            #print("click!")
        #screen.blit(white_bishop, (60,0))
        draw_peices()

def draw_board():
    c = 1
    for i in range(8):
        for j in range(8):
            pg.draw.rect(screen, (255*c, 255*c, 255*c), [j*60, i*60, 60, 60], 0)
            c = -c + 1
        c = -c + 1
    pg.display.update()

def draw_peices():
    for i in range(2):
        for j in range(2):
            screen.blit(peices[i]["bishop"][j][0], (peices[i]["bishop"][j][1], peices[i]["bishop"][j][2]))
            screen.blit(peices[i]["knite"][j][0], (peices[i]["knite"][j][1], peices[i]["knite"][j][2]))
            screen.blit(peices[i]["rook"][j][0], (peices[i]["rook"][j][1], peices[i]["rook"][j][2]))
        screen.blit(peices[i]["king"][0], (peices[i]["king"][1], peices[i]["king"][2]))
        screen.blit(peices[i]["queen"][0], (peices[i]["queen"][1], peices[i]["queen"][2]))
        for k in range(8):
            screen.blit(peices[i]["pawn"][k][0], (peices[i]["pawn"][k][1], peices[i]["pawn"][k][2]))
            pg.display.update()

def place_holder(x, y):
    Xadd =  60
    Yadd = 60
    for i in range(2):
        for j in range(2):
            if x >= peices[i]["bishop"][j][1] and x <= peices[i]["bishop"][j][1] + Xadd:
                if y <= peices[i]["bishop"][j][2] and y >= peices[i]["bishop"][j][2] - Yadd:
                    if i == 0:
                        return ["white", "bishop", j]
                    else:
                        return ["black", "bishop", j]
                    
            if x >= peices[i]["knite"][j][1] and x <= peices[i]["knite"][j][1] + Xadd:
                if y <= peices[i]["knite"][j][2] and y >= peices[i]["knite"][j][2] - Yadd:
                    if i == 0:
                        return ["white", "knite", j]
                    else:
                        return ["black", "knite", j]
                    
            if x >= peices[i]["rook"][j][1] and x <= peices[i]["rook"][j][1] + Xadd:
                if y <= peices[i]["rook"][j][2] and y >= peices[i]["rook"][j][2] - Yadd:
                    if i == 0:
                        return ["white", "rook", j]
                    else:
                        return ["black", "rook", j]
                    
        if x >= peices[i]["king"][1] and x <= peices[i]["king"][1] + Xadd:
                if y <= peices[i]["king"][2] and y >= peices[i]["king"][2] - Yadd:
                    if i == 0:
                        return ["white", "king"]
                    else:
                        return ["black", "king"]
        
        if x >= peices[i]["queen"][1] and x <= peices[i]["queen"][1] + Xadd:
                if y <= peices[i]["queen"][2] and y >= peices[i]["queen"][2] - Yadd:
                    if i == 0:
                        return ["white", "queen"]
                    else:
                        return ["black", "queen"]
        for k in range(8):
            if x >= peices[i]["pawn"][k][1] and x <= peices[i]["bishop"][k][1] + Xadd:
                if y <= peices[i]["pawn"][k][2] and y >= peices[i]["bishop"][k][2] - Yadd:
                    if i == 0:
                        return ["white", "pawn", k]
                    else:
                        return ["black", "pawn", k]
    Xadd = -60
    Yadd = -60

def possible_pawn_moves(team, number):
    if team == "white":
        Nteam = 0
        y1 = 60
        y2 = 120
    else:
        Nteam = 1
        y1 = -60
        y2 = -120
    pg.draw.rect(screen, (255, 0, 0), [peices[Nteam]["pawn"][number][1], peices[0]["pawn"][number][2] + y1, 60, 60], 1)
    pg.draw.rect(screen, (255, 0, 0), [peices[Nteam]["pawn"][number][1], peices[0]["pawn"][number][2] + y2, 60, 60], 1)
    pg.display.update()

def mouse_click(x, y):
    result = place_holder(x, y)
    if len(result) == 3:
        possible_pawn_moves(result[0], result[2])
draw_board()
main()