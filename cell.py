import ctypes
import random
import sys
from tkinter import Button, Label
from settings import MINES_COUNT, CELL_COUNT


class Cell:
    all=[]
    cell_count=CELL_COUNT
    cell_count_label_object=None
    def __init__(self, x, y, is_mine=False):
        self.is_mine = is_mine
        self.is_open = False
        self.has_flag = False
        self.cell_btn_object = None
        self.x = x
        self.y = y

        Cell.all.append(self)

    def create_btn_object(self, location):
        btn = Button(location, width=10, height=5)
        btn.bind('<Button-1>', self.left_click_action)
        btn.bind('<Button-3>', self.right_click_action)
        self.cell_btn_object = btn

    @staticmethod
    def create_cell_count_label(location):
        lbl = Label(location, text=f'Cells remaining: {Cell.cell_count}', width=16, height=4, bg='black', fg='white', font=('', 14))
        Cell.cell_count_label_object = lbl

    def left_click_action(self, event):
        if self.is_mine:
            self.show_mine()
        else:
            if self.surrounded_cells_total_mines == 0:
                for surrounded_cell in self.surrounded_cells:
                    surrounded_cell.show_cell()
            self.show_cell()
            # Show winning message if cell remaining is equal to the mines count
            if Cell.cell_count == MINES_COUNT:
                ctypes.windll.user32.MessageBoxW(0, 'You avoided all mines.', 'You won!', 0)
                sys.exit()


        # Cancel click events if cell is open
        self.cell_btn_object.unbind('<Button-1>')
        self.cell_btn_object.unbind('<Button-3>')

    def get_cell_by_axis(self, x, y):
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell

    @property
    def surrounded_cells(self):
        cells = [
            self.get_cell_by_axis(self.x - 1, self.y - 1),
            self.get_cell_by_axis(self.x - 1, self.y),
            self.get_cell_by_axis(self.x - 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y),
            self.get_cell_by_axis(self.x + 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y + 1),
        ]
        cells = [cell for cell in cells if cell is not None]
        return cells

    @property
    def surrounded_cells_total_mines(self):
        counter = 0
        for cell in self.surrounded_cells:
            if cell.is_mine:
                counter += 1
        return counter

    def show_cell(self):
        if not self.is_open:
            Cell.cell_count -= 1
            self.cell_btn_object.configure(text=self.surrounded_cells_total_mines)
            # Replace label with new count
            if Cell.cell_count_label_object:
                Cell.cell_count_label_object.configure(text=f'Cells remaining: {Cell.cell_count}')
            # Unflag button if the button has a flag
            self.cell_btn_object.configure(bg='SystemButtonFace')
            # Mark cell as opened
            self.is_open = True

    def show_mine(self):
        self.cell_btn_object.configure(bg='red')
        ctypes.windll.user32.MessageBoxW(0, 'You clicked on a mine.', 'Game over!', 0)
        sys.exit()
   
    def right_click_action(self, event):
        if not self.has_flag:
            self.cell_btn_object.configure(bg='orange')
            self.has_flag = True
        else:
            self.cell_btn_object.configure(bg='SystemButtonFace')
            self.has_flag = False


    @staticmethod
    def randomize_mines():
        picked_cells = random.sample(Cell.all, MINES_COUNT)
        for picked_cell in picked_cells:
            picked_cell.is_mine = True

    def __repr__(self):
        return f'Cell({self.x}, {self.y})'