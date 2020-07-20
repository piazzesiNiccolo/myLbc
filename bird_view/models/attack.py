import torch
import numpy as np
from art.classifiers import PyTorchClassifier
from art.attacks.evasion import PixelAttack, SpatialTransformation, HopSkipJump, NewtonFool, VirtualAdversarialMethod, ElasticNet, DeepFool, BasicIterativeMethod, BoundaryAttack,FastGradientMethod
import bird_view.utils.bz_utils as bzu
import torch.nn as nn
import torch.optim as optim
from bird_view.models import image
from torchsummary import summary
#mpath = '/home/piazzesi/Desktop/carla_lbc/ckpts/image/'
def load_model(model_path):

    config = bzu.load_json('/'.join([model_path, 'config.json']))
    model_args = config['model_args']
    model_name = model_args['model']
    model_class = image.ImagePolicyModelSS
    model = model_class(**config['model_args'])
    model.load_state_dict(torch.load('/'.join([model_path, 'model-10.th'])))
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(),lr=0.0001)
    classifier = PyTorchClassifier(model=model, loss=criterion,optimizer=optimizer, input_shape=(3, 160, 184),
    nb_classes=10,device_type='gpu')
    return classifier

def load_attack(classifier,attack):
    attacks = {
    'hopskipjump':load_hopskip,
    'spatialtransformation':load_spatial,
    'newton':load_newton,
    'bim':load_bim
    }
    return attacks[attack](classifier)

def load_hopskip(classifier):
    return HopSkipJump(classifier=classifier,
                        targeted=False,
                        max_iter=0,
                        max_eval=1000,
                        init_eval=10)

def load_newton(classifier):
    return NewtonFool(classifier,max_iter=10)

def load_bim(classifier):
    return BasicIterativeMethod(classifier=classifier, max_iter=20, eps=0.2 )

def load_spatial(classifier):
    return SpatialTransformation(classifier=classifier,
                                    max_translation=80,
                                    num_translations=1,
                                    max_rotation=230,
                                    num_rotations=1)

if __name__ == '__main__':
    load_model('/home/piazzesi/Desktop/carla_lbc/ckpts/image')
