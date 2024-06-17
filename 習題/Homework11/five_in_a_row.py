import pygame

pygame.init()
screen = pygame.display.set_mode((750,850))
pygame.display.set_caption("五子棋遊戲")

border_left = 25
border_right = 725
border_top = 25
border_bottom = 725
width = 50
height = 50


font = pygame.font.Font("font.ttf",25)

class Button:
    def __init__(self,x,y,width,height,text,color,click_color,text_color) -> None:
        self.text = text
        self.color = color
        self.click_color = click_color
        self.text_color = text_color
        self.rect = pygame.Rect(x,y,width,height)
        self.clicked = False

    def draw(self,screen):
        if self.clicked:
            pygame.draw.rect(screen,self.click_color,self.rect)
        else:
            pygame.draw.rect(screen,self.color,self.rect)

        text_surface = font.render(self.text,True,self.text_color)
        text_rect = text_surface.get_rect(center = self.rect.center)
        screen.blit(text_surface,text_rect)
    def handle_event(self,event,game):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                if(self.clicked):
                    print('已開始')
                else:
                    if game.winner == 0:
                        self.clicked = True
                        game.started = True
                        print("點擊已開始")
                    else:       
                        self.clicked = True
                        game.started = True                
                        game.plplayer = 1
                        game.winner = 0
                        game.map = [0]*15
                        for i in range(15):
                            game.map[i] = [0]*15
                        print("重新開始了!")

class Game:
    def __init__(self) -> None:
        self.started = False
        self.plplayer = 1
        self.winner = 0
        self.map = [0]*15
        for i in range(15):
            self.map[i] = [0]*15
    def start(self):
        screen.fill("#EE9A49")

        #直線
        for x in range(15):
            pygame.draw.line(screen,"#000000",[border_left+width*x,border_top],[border_left+width*x,border_bottom],2)
        #橫線
        for y in range(15):
            pygame.draw.line(screen,"#000000",[border_left,border_top+height*y],[border_right,border_top+height*y],2)

        pygame.draw.circle(screen,"#000000",[25+50*7,25+50*7],8)

        #落棋
        x,y = pygame.mouse.get_pos()
        if x >= border_left and x<=border_right and y>=border_top and y<=border_bottom:
            x = round((x - border_left)/width)*width + border_left
            y = round((y - border_top)/height)*height + border_top

            pygame.draw.rect(screen,"#FFFFFF",[x-25,y-25,50,50],1)


        button.draw(screen)
        button_ai.draw(screen)

        for row in range(15):
            for col in range(15):
                if self.map[row][col] == 1:
                    pygame.draw.circle(screen,"#000000",[col*width+border_left,row*height+border_top],20)
                elif self.map[row][col] == 2:
                    pygame.draw.circle(screen,"#FFFFFF",[col*width+border_left,row*height+border_top],20)
        if(self.winner!=0):
            if self.winner == 1:
                text = '黑子贏了!'
                color = (0,0,0)
            else:
                text = '白子贏了!'
                color = (255,255,255)
            font = pygame.font.Font("font.ttf",40)
            text_surface = font.render(text,True,color)
            text_position = (180,100)
            screen.blit(text_surface,text_position)
            pygame.display.update()
            pygame.time.wait(3000)
            button.clicked = False
    def check(self,row,col):
        #判斷左右方向是否五子連線
        score = 1
        for i in range(4):
            try:
                if self.map[row][col+i] == self.map[row][col+i+1]:
                    score = score + 1
                else:
                    break
            except:
                break
        for i in range(4):
            try:
                if self.map[row][col-i] == self.map[row][col-i-1]:
                    score = score + 1
                else:
                    break
            except:
                break
        if score >= 5:
            return True
            
        #判斷上下方向是否五子連線
        score = 1
        for i in range(4):
            try:
                if self.map[row+i][col] == self.map[row+i+1][col]:
                    score = score + 1
                else:
                    break
            except:
                break
        for i in range(4):
            try:
                if self.map[row-i][col] == self.map[row-i-1][col]:
                    score = score + 1
                else:
                    break
            except:
                break
        if score >= 5:
            return True
            
        #判斷左下到右上傾斜方向是否五子連線
        score = 1
        for i in range(4):
            try:
                if self.map[row+i][col+i] == self.map[row+i+1][col+i+1]:
                    score = score + 1
                else:
                    break
            except:
                break
        for i in range(4):
            try:
                if self.map[row-i][col-i] == self.map[row-i-1][col-i-1]:
                    score = score + 1
                else:
                    break
            except:
                break
        if score >= 5:
            return True
            
        #判斷左上到右下傾斜方向是否五子連線
        score = 1
        for i in range(4):
            try:
                if self.map[row-i][col+i] == self.map[row-i-1][col+i+1]:
                    score = score + 1
                else:
                    break
            except:
                break
        for i in range(4):
            try:
                if self.map[row+i][col-i] == self.map[row+i+1][col-i-1]: 
                    score = score + 1
                else:
                    break
            except:
                break
        if score >= 5:
            return True
    def mouseClick(self,x,y):
        if x >= border_left and x<=border_right and y>=border_top and y<=border_bottom:
            if self.started:
                col = round((x - 25)/50)        
                row = round((y - 25)/50)  
                if self.map[row][col] == 0:
                    print(row+1,col+1)
                    self.map[row][col] = self.plplayer
                    if(self.check(row,col)):
                        self.winner = self.plplayer
                    else:
                        if self.plplayer == 1:
                            self.plplayer = 2
                        else:
                            self.plplayer = 1
                else:
                    print("已有棋子!")
            else:
                print("遊戲尚未開始，請先點擊按鈕")        

button = Button(50,750,100,50,"雙人模式",(223,183,103),(221,160,221),(255,255,255))
button_ai = Button(200,750,100,50,"AI模式",(223,183,103),(221,160,221),(255,255,255))
game = Game()
while True:
    for event in pygame.event.get():
        button.handle_event(event,game)
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x,y = pygame.mouse.get_pos()
            game.mouseClick(x,y)

    game.start()
    pygame.display.update()

