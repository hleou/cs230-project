import torch
import mido
import numpy as np
from sys import argv

NUM_NOTES = 128
notes_on = []
duration_dict = {}

def extractMelody(midi_file, new_file_name, melody_track):
    
    mid = mido.MidiFile()
    newtrack = mido.MidiTrack()
    for msg in mido.MidiFile(midi_file).tracks[melody_track]:
        newtrack.append(msg)
    mid.tracks.append(newtrack)
    print('DONE ' + midi_file)
    mid.save(new_file_name)

def extractAllMelodies(num_outs, path_name, melody_track):
	for i in range (1, int(num_outs) + 1):
		in_file = path_name + '/' + str(i) + '.mid'
		out_file = path_name + '/' + str(i) + '_out.mid'
		extractMelody(in_file, out_file, int(melody_track))

if __name__ == '__main__':
    # in_name = argv[1]
    # out_name = argv[2]
    # num_outs = argv[3]
    # extractMelody(in_name, out_name)
    melody_track = argv[3]
    path_name = argv[2]
    num_outs = argv[1]
    extractAllMelodies(num_outs, path_name, melody_track)
