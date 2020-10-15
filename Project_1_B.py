from graphics import*
from random import *


class RPS:
    def _init(self, player, cpu):
        self.player = player
        self.cpu = cpu

    def has_won(self):
        #Draw when Player and CPU choose the same
        if self.player == self.cpu:
            #print('Tie')
            return 'Tie'

        # When player chooses Rock
        elif self.player == 'Rock':
            if self.cpu == 'Paper':
                #print('Lost')
                return 'Lost'
            else:
                #print('Won')
                return 'Won'

        # When Player chooses Paper
        elif self.player == 'Paper':
            if self.cpu == 'Scissor':
                #print('Lost')
                return 'Lost'
            else:
                #print('Won')
                return 'Won'

        # When Player chooses Scissor
        else:
            if self.cpu == 'Rock':
                #print('Lost')
                return 'Lost'
            else:
                #print('Won')
                return 'Won'


def main_menu():
    win = GraphWin("Rock, Paper and Scissors", 500, 500)
    i1 = Image(Point(250, 100), "mainrps.png").draw(win)
    r1 = Rectangle(Point(175,325), Point(325,375))
    r1.setFill('green')
    r1.draw(win)
    title = Text(Point(250, 230), "Rock Paper Scissors VS. CPU")
    title.setSize(20)
    title.setStyle('bold')
    title.draw(win)
    rules = Text(Point(250, 270), "Rules: Enter a number from 1 to 3. \nFirst to get 3 points wins.").draw(win)
    t1 = Text(Point(250, 350), "Start Game")
    t1.draw(win)
    win.getMouse()
    r1.undraw()
    t1.undraw()
    i1.undraw()
    title.undraw()
    rules.undraw()
    return win


def game(win):
    score_a = 0
    score_b = 0
    option_a = 0
    option_b = 0
    score_player = Text(Point(50, 10), f"My Score: {score_a}")
    score_cpu = Text(Point(50, 30 ), f"CPU Score: {score_b}")
    score_player.draw(win)
    score_cpu.draw(win)

    while score_a < 3 and score_b < 3:

        # CPU randomly chooses Rock, Paper, Scissor
        option_b = randint(1, 3)
        if option_b == 1:
            option_b = 'Rock'
            cpu_image = Image(Point(100, 300), "Rock.png")
        elif option_b == 2:
            option_b = 'Paper'
            cpu_image = Image(Point(100, 300), "Paper.png")
        else:
            option_b = 'Scissor'
            cpu_image = Image(Point(100, 300), "Scissor.png")

        out_1 = Text(Point(250, 175), "Choose Rock, Paper or Scissors.")
        image_2 = Image(Point(250, 275), "RPS.png").draw(win)
        out_1.setSize(16)
        out_1.draw(win)

        input1 = win.getKey()

        out_1.undraw()
        image_2.undraw()

        # Input Validation
        while input1 != '1' and input1 != '2' and input1 != '3':
            error_message = Text(Point(250, 250), 'Error, select a number from 1 to 3. Click to try again.')
            error_message.setOutline('red')
            error_message.setSize(14)
            error_message.draw(win)
            win.getMouse()
            error_message.undraw()
            out_1 = Text(Point(250, 175), "Choose Rock, Paper or Scissors.")
            image_2 = Image(Point(250, 275), "RPS.png").draw(win)
            out_1.setSize(16)
            out_1.draw(win)
            input1 = win.getKey()
            out_1.undraw()
            image_2.undraw()

        if input1 == '1':
            option_a = 'Rock'
            player_image = Image(Point(400, 300), "Rock.png").draw(win)
        elif input1 == '2':
            option_a = 'Paper'
            player_image = Image(Point(400, 300), "Paper.png").draw(win)
        else:
            option_a = 'Scissor'
            player_image = Image(Point(400, 300), "Scissor.png").draw(win)

        match = RPS()
        match.player = option_a
        match.cpu = option_b
        print(match.has_won())
        cpu_image.draw(win)
        vs_txt = Text(Point(250, 350), "VS")
        vs_txt.setSize(16)
        vs_txt.draw(win)
        cpu_choice_txt = Text(Point(100, 400), "CPU's Choice")
        player_choice_txt = Text(Point(400, 400), "Player's Choice")
        cpu_choice_txt.draw(win)
        player_choice_txt.draw(win)

        if match.has_won() == "Tie":
            t2 = Text(Point(250, 150), 'The Game was a Tie')
            t2.setOutline('orange')
            t2.setSize(16)
        elif match.has_won() == "Won":
            score_player.undraw()
            score_a += 1
            score_player = Text(Point(50, 10), f"My Score: {score_a}")
            score_player.draw(win)
            t2 = Text(Point(250, 150), 'You Won the Game')
            t2.setOutline('green')
            t2.setSize(16)

        else:
            score_cpu.undraw()
            score_b += 1
            score_cpu = Text(Point(50, 30), f"CPU Score: {score_b}")
            score_cpu.draw(win)
            t2 = Text(Point(250, 150), 'You Lost the Game')
            t2.setOutline('red')
            t2.setSize(16)
        t2.draw(win)
        t3 = Text(Point(250, 180), 'Click again for the next game.')
        t3.setSize(14)
        t3.draw(win)
        win.getMouse()
        t2.undraw()
        t3.undraw()
        cpu_image.undraw()
        player_image.undraw()
        cpu_choice_txt.undraw()
        player_choice_txt.undraw()
        vs_txt.undraw()

    if score_a > score_b:
        t3 = Text(Point(250, 200), "Congratulations, You Won The Match!")
        final_image = Image(Point(250, 300), "Win.png").draw(win)
        t3.setSize(18)
        t3.setOutline('green')
        t3.draw(win)
    else:
        t3 = Text(Point(250, 200), "Sorry, You Lost The Match.")
        final_image = Image(Point(250, 300), "Lost.png").draw(win)
        t3.setOutline('red')
        t3.setSize(18)
        t3.draw(win)

    win.getMouse()
    win.close()


def main():
    win = main_menu()
    game(win)


main()
