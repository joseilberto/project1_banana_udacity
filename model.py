import torch
import torch.nn as nn
import torch.nn.functional as F

class QNetwork(nn.Module):
    """Actor (Policy) Model."""

    def __init__(self, state_size, action_size, seed, nhidden = [64, 64]):
        """Initialize parameters and build model.
        Params
        ======
            state_size (int): Dimension of each state
            action_size (int): Dimension of each action
            seed (int): Random seed
        """
        super(QNetwork, self).__init__()
        self.seed = torch.manual_seed(seed)
        self.state_size = state_size
        self.action_size = action_size
        self.nhidden = nhidden
        
        self.hiddens = nn.ModuleList()
        cur_dim = self.state_size
        for n in nhidden:
            self.hiddens.append(nn.Linear(cur_dim, n))
            cur_dim = n
        self.hiddens.append(nn.Linear(cur_dim, self.action_size))

        self.activation = nn.ReLU()
        

    def forward(self, state):
        """Build a network that maps state -> action values."""
        x = state.clone()
        for i in range(len(self.nhidden)):
            x = self.activation(self.hiddens[i](x))
        return self.hiddens[-1](x)
