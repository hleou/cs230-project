import torch
import mido
import np as numpy
from sys import argv

NUM_NOTES = 128
notes_on = []
duration_dict = {}

def extractMelody(midi_file, new_file_name):
    
    mid = mido.MidiFile()
    track = mido.MidiTrack()
    mid.tracks.append(track)
    for msg in mido.MidiFile(midi_file).tracks[0]:
        if msg.type != 'note_on' or (msg.type == 'note_on' and msg.channel == 0):
            track.append(msg)
    print('DONE' + midi_file)
    mid.save(new_file_name)


def init_duration_dict(midi_file):
	on_notes = []
	for msg in mido.MidiFile(midi_file).tracks[0]: 
		if msg.type == 'note_on' and msg.velocity != 0:
			on_notes.append(msg)
		elif msg.type == 'note_off' and msg.velocity == 0: 
			for on_msg in on_notes:
				if on_msg.note == msg.note: 
					duration_dict[on_msg] = msg.time - on_msg.time
					on_notes.remove(on_msg)
	print("Done initializing dictionary")

# One hot vector encoding scheme
def to_encoding1(midi_msg):
	encoding = np.zeros((1, NUM_NOTES + 1))
	encoding[midi_msg.note] = 1
	encoding[NUM_NOTES] = midi_msg.velocity
	return encoding

# Experimental encoding scheme: byte 1 = note played, byte 2 = velocity, byte 3 & 4 = duration of the note played
def to_encoding2(midi_msg):
	encoding = np.zeros((1, 3))
	if msg.type == 'note_on' and msg.velocity == 0: 
		return encoding
	encoding[0] = midi_msg.note
	encoding[1] = midi_msg.velocity
	encoding[3] = duration_dict[msg]
	return encoding


if __name__ == '__main__':
    in_name = argv[1] + '.mid'
    out_name = "out_" + argv[2] + '.mid'
    extractMelody(in_name, out_name)
