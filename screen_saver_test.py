#coding=utf-8
__author__ = 'zs'
from random import randint
from tkinter import *
import time

class RandBall():
    global X_MOVE
    global Y_MOVE
    X_MOVE = 20
    Y_MOVE = 20
    global IMAX
    global IMIN
    IMAX = 20
    IMIN = 10
    def __init__(self, canvas, scrn_width, scrn_height):
        self.canvas = canvas
        self.scrn_width = scrn_width
        self.scrn_height = scrn_height
        self.x_pos = randint(80, scrn_width - 80)
        self.y_pos = randint(80, scrn_height - 80)
        self.x_move = randint(5, X_MOVE)
        self.y_move = randint(5, Y_MOVE)
        self.radius = randint(IMIN, IMAX)
        rnd_color = lambda:randint(0, 255)
        self.color = '#%02x%02x%02x'%(rnd_color(), rnd_color(), rnd_color())

    def create_ball(self):
        x1 = self.x_pos - self.radius
        y1 = self.y_pos - self.radius
        x2 = self.x_pos + self.radius
        y2 = self.y_pos + self.radius

        self.item = self.canvas.create_oval(x1, y1, x2, y2, fill = self.color, outline = self.color)

    def move_ball(self):
        self.x_pos += self.x_move
        self.y_pos += self.y_move
        if self.x_pos > self.scrn_width - self.radius:
            self.x_move = -(X_MOVE)
        if self.y_pos > self.scrn_height - self.radius:
            self.y_move = -(Y_MOVE)
        if self.x_pos < self.radius:
            self.x_move = abs(X_MOVE)
        if self.y_pos < self.radius:
            self.y_move = abs(Y_MOVE)
        self.canvas.move(self.item, self.x_move, self.y_move)

class ScreenSaver():
    balls = []
    def __init__(self, ball_num):
        self.win = Tk()
        self.width = self.win.winfo_screenwidth()
        self.height = self.win.winfo_screenheight()
        self.win.overrideredirect(True)
        self.win.attributes('-alpha', 0.5)
        self.win.bind('<Any-Button>', self.exit_screensaver)
        self.win.bind('<Motion>', self.exit_screensaver)
        self.win.bind('<Any Key>', self.exit_screensaver)
        self.canvas = Canvas(self.win, width = self.width, height = self.height, bg = '#000000', highlightthickness=0)
        self.canvas.pack()

        for i in range(0, ball_num):
            ball = RandBall(self.canvas, self.width, self.height)
            ball.create_ball()
            self.balls.append(ball)
        self.run_screensaver()
        self.win.mainloop()

    def run_screensaver(self):
        for ball in self.balls:
            ball.move_ball()
        self.canvas.after(30, self.run_screensaver)

    def exit_screensaver(self, event):
        self.win.destroy()

def main():
    ScreenSaver(115)

if __name__ == '__main__':
    main()

