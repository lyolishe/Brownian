import numpy as np
# import tkinter
from constants import *

#root = tkinter.Tk()
#root.title('Brownian')
#root.geometry('480x480')
#root.update()

int_type = np.dtype('int')
vector_type = np.dtype([('x', int_type), ('y', int_type)])
particle_type = np.dtype([
    ('cords', vector_type),
    ('velocity', vector_type)
])

particles = np.zeros(10, dtype=particle_type)

def init():
    global particles
    for particle in particles:
        rand = np.random.randint(0,initial_particle_max_speed, 4 )
        particle['cords']['x'] = rand[0]
        particle['cords']['y'] = rand[1]
        particle['velocity']['x'] = rand[2]
        particle['velocity']['y'] = rand[3]

init()

def tick():
    for particle in particles:
        particle['cords']['x'] = particle['cords']['x'] + particle['velocity']['x']
        particle['cords']['y'] = particle['cords']['y'] + particle['velocity']['y']
        # if collide with wall
        # if collide with particle
    # rerun by framerate

tick()