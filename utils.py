import settings
from importlib import reload # reload 
reload(settings)

def height_perc(percentage):
    return (settings.HEIGHT / 100) * percentage

def width_perc(percentage):
    return (settings.WIDTH / 100) * percentage

print(width_perc(25))