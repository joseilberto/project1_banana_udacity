parameters_dict = {
    "buffer_size": int(1e5),
    "batch_size": 64,
    "gamma": 0.99,
    "tau": 1e-3,
    "lr": 5e-4,
    "update_every": 4,
    "nhidden": [64, 64]
}

BUFFER_SIZE = int(1e5)  # replay buffer size
BATCH_SIZE = 64         # minibatch size
GAMMA = 0.99            # discount factor
TAU = 1e-3              # for soft update of target parameters
LR = 5e-4               # learning rate 
UPDATE_EVERY = 4        # how often to update the network