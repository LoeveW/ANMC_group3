import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.autograd import Variable

from torch.utils.data import Dataset, DataLoader


import numpy as np

def fc_layer(D_in, D_out):
    layers = ()
    layers += (nn.Linear(D_in, D_out),)
    #layers += (nn.BatchNorm1d(num_features=D_out))
    layers += (nn.LeakyReLU(0.05),)
    return nn.Sequential(*layers)    

class Coder(nn.Module) :
    def __init__(self, D_in, D_h_list, D_out, output_activation=None) :
        super(Coder,self).__init__()
        
        self.layers = ()
        
        for i in range(len(D_h_list)):
            self.layers += (fc_layer(D_in, D_h_list[i]),)
            D_in = D_h_list[i]
        
        self.layers += (nn.Linear(D_in, D_out),)
        
        assert output_activation is None or output_activation in ["sigmoid","LeakyReLU"]
        if output_activation == "sigmoid":
            print("sigmoid")
            self.layers += (nn.Sigmoid(),)
        elif output_activation == "LeakyReLU":
            self.layers += (nn.LeakyReLU(.05),)
            
        self.layers = nn.Sequential( *self.layers)
        print(self.layers)

    def forward(self,z):
        return self.layers(z)


class betaVAE(nn.Module) :
    def __init__(self, D_x, D_h, D_z, use_cuda=True) :
        super(betaVAE,self).__init__()
        print("encoder")
        self.encoder = Coder(D_x, D_h, D_z*2, output_activation=None)
        print("decoder")
        self.decoder = Coder(D_z, D_h[::-1], D_x, output_activation="sigmoid")
        self.use_cuda = use_cuda

        if self.use_cuda :
            self = self.cuda()

    def reparameterize(self, mu, log_var) :
        eps = torch.randn((mu.size()[0], mu.size()[1]))
        veps = Variable(eps)
        #veps = Variable( eps, requires_grad=False)
        if self.use_cuda:
            veps = veps.cuda()
        z = mu + veps * torch.exp(log_var/2)
        return z

    def forward(self,x) :
        h = self.encoder(x)
        mu, log_var = torch.chunk(h, 2, dim=1)
        z = self.reparameterize(mu, log_var)
        out = self.decoder(z)

        return out, mu, log_var
    
class Autoencoder(nn.Module) :
    def __init__(self, D_x, D_h, D_z, use_cuda=True) :
        super(Autoencoder,self).__init__()
        print("encoder")
        self.encoder = Coder(D_x, D_h, D_z, output_activation=None)
        print("decoder")
        self.decoder = Coder(D_z, D_h[::-1], D_x, output_activation="sigmoid")
        self.use_cuda = use_cuda

        if self.use_cuda :
            self = self.cuda()

    def forward(self,x) :
        z = self.encoder(x)
        out = self.decoder(z)

        return out



