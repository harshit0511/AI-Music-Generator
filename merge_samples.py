import numpy as np
from tqdm import tqdm
import glob2
import msgpack
import midi_manipulation

#files = glob.glob('{}/*.mid*'.format(path))
try:
    files = glob2.glob('generated*.mid*')
except Exception as e:
    raise e

songs = np.zeros((0,156))
for f in tqdm(files):
    try:
        song = np.array(midi_manipulation.midiToNoteStateMatrix(f))

        if np.array(song).shape[0] >= 0:
            songs = np.concatenate((songs,song))
    except Exception as e:
        raise e
print ("Merging the samples...")
print (np.shape(songs))
midi_manipulation.noteStateMatrixToMidi(songs, "final")
