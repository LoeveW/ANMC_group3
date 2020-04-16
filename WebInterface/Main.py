from flask import Flask, escape, request, render_template
from werkzeug.datastructures import ImmutableMultiDict
from scipy.io.wavfile import write, read

import sys, os


from pydub import AudioSegment


sys.path.append('..')
sys.path.append('../RenderMan/Builds/LinuxMakefile/build')
vst_path = "../Dexed.so"
import FormatConverter as fc
import librenderman as rm
import RenderPatches as rp
engine = rp.create_engine(vst_path)
generator = rm.PatchGenerator(engine)


sys.path.append('../autoencoder')
from model import *

import torch
import numpy as np

# Model :
D_x = 145
D_h = [800,500]
D_z = 10
use_cuda = False
model = betaVAE(D_x, D_h, D_z, use_cuda).float()
weights_path = "../autoencoder/weights/"
weights_fname = "w_beta1_v1_4600"
model.load_state_dict(torch.load(weights_path + weights_fname))


app = Flask(__name__)
PORT = 8080


# Handler = http.server.SimpleHTTPRequestHandler


@app.route("/", methods=['GET', 'POST'])
def index():
	if request.method == "POST":

		global model
		global weights_fname

		# Get the sliders values as integers
		request_data = request.form.to_dict(flat=False).keys()[0]
		request_data = request_data.replace('[','').replace(']','').replace('"','')
		latent = [float(s) for s in request_data.split(',')[:-1]]

		new_weights_fname = request_data.split(',')[-1]

		# Reload model if it has changed
		if new_weights_fname != weights_fname:
			weights_fname = new_weights_fname
			model.load_state_dict(torch.load(weights_path + new_weights_fname))
			print("reload model")
		

		
		# Model forward pass with the values as latent space
		latent = torch.from_numpy(np.array(latent)).float()
		params = model.decoder(latent).detach()
		params = np.array(params.detach(), dtype=float)
		params = fc.syx_to_rm(params)
		audio = np.array(rp.render_patch(params, engine, override=True), dtype='float32')

		fname = "static/audio/audio"
		write(fname+".wav",44100,audio)

		wav = AudioSegment.from_wav(fname+".wav")
		wav.export(fname+".mp3", format="mp3")


	return render_template("index.html")

if __name__ == '__main__':
	app.run(debug=True, port=8080, host='0.0.0.0')
