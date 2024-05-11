Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> %matplotlib notebook
from psychopy import visual, core, event, monitors
import random
import numpy as np

# Define a monitor
mon = monitors.Monitor('testMonitor')
mon.setDistance(75)  # Set the viewing distance in centimeters
mon.setSizePix([1280, 1024])  # Set the monitor size in pixels

# Create a window
win = visual.Window(size=(800, 600), color='black', units='pix', monitor=mon, fullscr=False)

# Define durations for each phase in seconds
fixation_duration = 2
target_presentation_duration = 2
preparation_duration = 1
stimulation_duration = 5
rest_duration = 5

# Define stimulation frequencies
stimulation_frequencies = {
    'center': 8.5714,
    'bottom': 10.9091,
    'right': 15,
    'top': 20,
    'left': 24
}

# Define stimuli
cross = visual.TextStim(win, text='+', color='white', height=40)
squares = {
    'center': visual.Rect(win, width=100, height=100, fillColor='black', lineColor='white', pos=(0, 0)),
    'bottom': visual.Rect(win, width=100, height=100, fillColor='black', lineColor='white', pos=(0, -200)),
    'right': visual.Rect(win, width=100, height=100, fillColor='black', lineColor='white', pos=(200, 0)),
    'top': visual.Rect(win, width=100, height=100, fillColor='black', lineColor='white', pos=(0, 200)),
    'left': visual.Rect(win, width=100, height=100, fillColor='black', lineColor='white', pos=(-200, 0))
}
information_box = visual.TextStim(win, text='', color='white', height=20, pos=(0, -250))

# Main experiment loop
for trial in range(5):  # Run 5 trials
    # Fixation phase
    cross.draw()
    win.flip(clearBuffer=True)
    core.wait(fixation_duration)

    # Target Presentation phase
    target_location = random.choice(list(squares.keys()))
    target_square = squares[target_location]
    target_square.fillColor = 'blue'
    information_box.text = f'Target: {target_location}'
    [square.draw() for square in squares.values()]
    information_box.draw()
    win.flip(clearBuffer=True)
    core.wait(target_presentation_duration)

    # Preparation phase
    information_box.text = ''
    [square.setFillColor('black') for square in squares.values()]
    win.flip(clearBuffer=True)
    core.wait(preparation_duration)

    # Stimulation phase
    start_time = core.getTime()
    while core.getTime() - start_time < stimulation_duration:
        for location, square in squares.items():
            frequency = stimulation_frequencies[location]
            phase = (core.getTime() - start_time) * frequency * 2 * np.pi
            square.fillColor = [0.5 * (1.0 + np.sin(phase))] * 3
            square.draw()
        information_box.text = 'Stimulation'
        information_box.draw()
        win.flip(clearBuffer=True)

    # Rest phase
    information_box.text = 'Rest'
    win.flip(clearBuffer=True)
    core.wait(rest_duration)

# Clean up
win.close()
core.quit()