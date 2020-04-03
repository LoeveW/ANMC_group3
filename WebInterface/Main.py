from flask import Flask, escape, request, render_template
from werkzeug.datastructures import ImmutableMultiDict

import sys

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
beta = 1
model = betaVAE(D_x, D_h, D_z, use_cuda).float()
model.load_state_dict(torch.load("../autoencoder/weights"))


app = Flask(__name__)
PORT = 8080

# Handler = http.server.SimpleHTTPRequestHandler


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == "POST":

    	# Get the sliders values as integers
        latent = request.form.to_dict(flat=False).keys()[0]
        latent = latent.replace('[','').replace(']','').replace('"','')
        latent = [int(s) for s in latent.split(',')]
        
        # Model forward pass with the values as latent space
        latent = torch.from_numpy(np.array(latent)).float()
        params = model.decoder(latent).detach()
        params = np.array(params.detach(), dtype=float)
        params = fc.syx_to_rm(params)
        audio = rp.render_patch(params, engine, override=True)
        print(len(audio))

    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True, port=8080, host='0.0.0.0')
