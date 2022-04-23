from tkinter import *
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

top_frame = Frame(root, bg='red', width=settings.WIDTH, height=utils.height_perc(25))
top_frame.place(x=0, y=0)

left_frame = Frame(root, bg='green', width=utils.width_perc(25), height=utils.height_perc(75))
left_frame.place(x=0, y=utils.height_perc(25))

# Run/open window
root.mainloop()