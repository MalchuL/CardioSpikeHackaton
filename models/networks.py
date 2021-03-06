import torch
import registry.registries as registry
from models.BiLSTMDetector import BiLSTMDetector
from models.UNet import UNet
from models.losses import WeightedBCEWithLogits, LocalBetterLoss
from models.optimizers.radam import RAdam
from models.simple_cnn import SimpleCNN, CRNN

registry.Criterion(WeightedBCEWithLogits)
registry.Criterion(LocalBetterLoss)

registry.Model(SimpleCNN)
registry.Model(BiLSTMDetector)
registry.Model(UNet)
registry.Model(CRNN)

registry.Optimizer(RAdam)

# Generator
def define_model(opt_net):
    which_model = opt_net['model']
    net = registry.MODELS.get_from_params(**opt_net)
    return net
