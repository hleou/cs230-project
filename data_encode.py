import 

def to_one_hot(midi_msg) {
	
}
def extractMelody(midi_file, new_file_name):
	mid = mido.MidiFile();
	track = mido.MidiTrack();
	mid.tracks.append(track);
	for msg in mido.MidiFile(midi_file).tracks[0]: 
		if msg.type == 'note_on' and msg.channel == 0:
			track.append(msg)
		elif msg.type == 'note_off' and msg.channel == 0: # Transform note_off message to a note_on message by changing the velocity to 0 (turns msg.note off)
			track.append(mido.Message('note_on', note = msg.note, velocity = 0, time = msg.time))
		else:
			track.append(msg)
	mid.save(new_file_name)
	print("Done stripping " + midi_file + " ... saved as " + new_file_name)