from tkinter import *
from cell import Cell
import settings
import utils 
from importlib import reload # reload 
reload(settings)
reload(utils)

root = Tk()
# Overide window settings
root.configure(bg='black')
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title('Minesweeper')
root.resizable(False, False)

top_frame = Frame(root, bg='black', width=settings.WIDTH, height=utils.height_perc(25))
top_frame.place(x=0, y=0)

game_title = Label(top_frame, bg='black', fg='white', text='Minesweeper', font=('', 18))
game_title.place(x=utils.width_perc(50), y=0)

left_frame = Frame(root, bg='black', width=utils.width_perc(25), height=utils.height_perc(75))
left_frame.place(x=0, y=utils.height_perc(25))

center_frame = Frame(root, bg='black', width=utils.width_perc(75), height=utils.height_perc(75))
center_frame.place(x=utils.width_perc(25), y=utils.height_perc(25))

for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c1 = Cell(x, y)
        c1.create_btn_object(center_frame)
        c1.cell_btn_object.grid(row=x, column=y)

Cell.randomize_mines()
Cell.create_cell_count_label(left_frame)
Cell.cell_count_label_object.place(x=0,y=0)
        
# Run/open window
root.mainloop()