import serial
import pygame
import sys

noteInp = serial.Serial('COM4', 9600)

pygame.mixer.init()
pygame.mixer.set_num_channels(10)

octave = 4

while True:
    keys = {'c': 'C'+str(octave),
            'd': 'D'+str(octave),
            'e': 'E'+str(octave),
            'f': 'F'+str(octave),
            'g': 'G'+str(octave),
            'a': 'A'+str(octave),
            'b': 'B'+str(octave),
            'D': 'Db'+str(octave),
            'E': 'Eb'+str(octave),
            'G': 'Gb'+str(octave),
            'A': 'Ab'+str(octave),
            'B': 'Bb'+str(octave),
			'C': 'C'+str(octave+1)}

    inp = noteInp.readline()
    inp1 = str(inp)
    mainInp = inp1[2]
    print(inp1)
    
    if mainInp == 'q':
        if(octave > 3):
            octave -= 1
            noteInp.reset_input_buffer()
        continue
    elif mainInp == 'w':
        if(octave < 5):
            octave += 1
            noteInp.reset_input_buffer()
        continue

    if len(inp1)-5 > 1:
        for i in range(len(inp1)-5):
            print(keys[inp1[i+2]])
            pygame.mixer.Channel(i).play(pygame.mixer.Sound('sounds/' + keys[inp1[i+2]] + '.wav'))
    else:
        print(keys[mainInp])
        note = pygame.mixer.Sound('sounds/' + keys[mainInp] + '.wav')
        note.play()
    
