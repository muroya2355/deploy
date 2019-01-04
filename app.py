#import sys
#import wave
#import numpy as np
#import os
#import glob
#import torch
#import torch.nn as nn
#import torch.nn.functional as F
#import torch.optim as optim
#import time
from flask import Flask
from flask import request

labels=["中央東口", "東口（地下）", "みどりの窓口（東口）", "東口（1F）", "ルミネエスト（地下）", "階段下", "定期券売場前", "大江戸線エスカレータ上", "ケンタッキー周辺", "B13出口前改札", "B10出口周辺", "A17出口方面", "プロムナード地下通路", "案内所前", "D2出口周辺", "D3出口付近", "都庁前寄り改札", "飯田橋寄り改札", "JR西口", "小田急西口（地下）", "小田急西口（1F）", "京王西口", "京王新線大江戸線新宿改札", "KEIOMALL", "小田急南口", "JR南口", "JR東南口"]

#class Net(nn.Module):
#	def __init__(self):
#		super(Net, self).__init__()
#		self.layer1=nn.Linear(48000, 200)
#		self.layer2=nn.Linear(200, 100)
#		self.layer3=nn.Linear(100, 27)
#	
#	def forward(self, x):
#		x=F.relu(self.layer1(x))
#		x=F.relu(self.layer2(x))
#		x=self.layer3(x)
#		return x
#
#def infer(file):
#	test=[]
#	#w=wave.open(sys.argv[1], mode='rb')
#	w=wave.open(file, mode='rb')
#	sounds=np.frombuffer(w.readframes(w.getnframes()), dtype='int16')
#	for i in range(0, len(sounds)//48000):
#		sound=abs(np.fft.fft(sounds[i*48000:(i+1)*48000]))
#		sound=(sound-sound.mean())/sound.std()
#		test.append(sound)
#	w.close()
#	
#	test=np.array(test, dtype='float32')
#	
#	net=Net()
#	net.load_state_dict(torch.load('./model'))
#	net.eval()
#	
#	infer_data=net(torch.from_numpy(test))
#	infer_label=','.join(
#	[labels[x] for x in torch.argmax(infer_data, dim=1).numpy().tolist()]
#	)
#	return infer_label



app = Flask(__name__)

@app.route('/')
def index():
	html='<form action="./a" method="post" enctype="multipart/form-data">'
	html+='<input type="file" accept="audio/*" capture="microphone" name="file"><br>'
	html+='<input type="submit" value="upload">'
	html+='</form>'
	return html


#@app.route('/a', methods=['POST'])
#def sound():
#	name='./sounds/'+str(time.time())+'.wav'
#	request.files['file'].save(name)
#	return infer(name)

## おまじない
if __name__ == "__main__":
    app.run(debug=True)

