from turtle import Turtle
ALIGN = 'center'
FONT = ('Arial', 22, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.lscore = 0
        self.rscore = 0
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(0, 200)
        self.update_score_board()


    def update_score_board(self):
        self.write(f'{self.lscore}: SCORE: {self.rscore}', move=False, align=ALIGN, font=FONT)

    def refresh(self):
        self.clear()
        self.update_score_board()

    def check(self):
        self.refresh()
        if self.rscore == 2:
            print('Right won')
            return True

        elif self.lscore == 2:
            print('Left won')
            return True
        return False
