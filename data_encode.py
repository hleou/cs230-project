import numpy as np
import mido
from sys import argv


def extractEncoding(midi_file, encoding_file):
	array = np.zeros((1,128))
	vector = array[0]
	for msg in mido.MidiFile(midi_file).tracks[0]:
		if (msg.type == 'note_on' and msg.velocity != 0):
			array = np.vstack([array, vector])
			vector[msg.note] = 1
		elif (msg.type == 'note_off' or (msg.type == 'note_on' and msg.velocity == 0)):
			array = np.vstack([array, vector])
			vector[msg.note] = 0
   	np.save(encoding_file + '.npy', array)
   	print 'Done with encoding for ' + midi_file

def extractAllEncodings(path_name, num_encodings):
	for i in range (1, num_encodings + 1):
		midi_file = path_name + '/' + str(i) + '_out.mid'
		encoding_file = path_name + '/' + str(i) + '_encoding'
		extractEncoding(midi_file, encoding_file)

def smashAllEncodings(path_name, num_encodings, cat_encoding_file):
	smashedEncodings = np.load(path_name + '/' + str(1) + '_encoding.npy')
	for i in range (2, num_encodings + 1):
		encoding = np.load(path_name + '/' + str(i) + '_encoding.npy')
		smashedEncodings = np.vstack([smashedEncodings, encoding])
	np.save(cat_encoding_file + '.npy', smashedEncodings)

if __name__ == '__main__':
	mode = argv[1]
	if (mode == '--single'):
		midi_file = argv[2]
		encoding_file = argv[3]
		extractEncoding(midi_file, encoding_file)
	elif (mode == '--all'):
		path_name = argv[2]
		num_encodings = argv[3]
		extractAllEncodings(path_name, int(num_encodings))
	elif (mode == '--smash'):
		path_name = argv[2]
		num_encodings = argv[3]
		cat_encoding_file = argv[4]
		smashAllEncodings(path_name, int(num_encodings), cat_encoding_file)
	else :
		print 'Wrong Usage'