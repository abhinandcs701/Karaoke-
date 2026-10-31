import librosa 
import librosa.display
import numpy as np 
import matplotlib.pyplot as plt 
import sys


def inspect_audio(path):

    y,sr=librosa.load(path,sr=None)
    print("Sample rate",sr,"hz")

    print("Duration",len(y)/sr)
    print('Number of samples ',len(y))
    print("shape",y.shape)

    plt.figure(figsize=(14,4))
    librosa.display.waveshow(y[60*sr:70*sr],sr=sr)
    plt.title('WAVEFORM')
    plt.xlabel('time')
    plt.ylabel('amplitude')
    plt.show()
    print(np.abs(y).max(),np.abs(y).min(),np.abs(y).mean())
    #SPECTROGRAM
    d=librosa.stft(y)

    db=librosa.amplitude_to_db(np.abs(d),ref=np.max)
    plt.figure(figsize=(14,5))
    librosa.display.specshow(db,sr=sr,y_axis='log',x_axis='time')
    plt.colorbar(format='%2.0f db')
    plt.xlim(120,140)
    plt.title('spectrogram')
    plt.show()
if __name__== "__main__":        
    inspect_audio(sys.argv[1])
