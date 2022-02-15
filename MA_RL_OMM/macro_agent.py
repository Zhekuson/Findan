import torch
import numpy as np
import random
import torch.nn as nn
from collections import namedtuple, deque

Transition = namedtuple(
    'Transition', ('state', 'action', 'reward', 'next_state', 'done'))


class QNetwork(nn.Module):
    """_summary_

    Args:
        nn (_type_): _description_
    """    
    def __init__(self) -> None:
        super(QNetwork, self).__init__()
        self.input = nn.Linear(7, 7)
        self.hidden1 = nn.Linear(7, 7)
        self.hidden2 = nn.Linear(7, 7)
        self.out = nn.Linear(7, 3)
        self.DQN = nn.Sequential(
            self.input,
            nn.BatchNorm1d(7),
            nn.ReLU(),
            self.hidden1,
            nn.ReLU(),
            self.hidden2,
            nn.ReLU(),
            self.out,
            nn.Softmax()
        )

    def forward(self, input):
        """_summary_

        Args:
            input (_type_): _description_

        Returns:
            _type_: _description_
        """        
        price = input[0]
        indicators = input[1]
        assets = input[2]
        diff = np.sum(np.ones_like(assets) * price - assets) if len(assets) > 0 else 0
        x = np.hstack((price, indicators, diff))
        x = np.nan_to_num(x)
        return self.DQN.forward(torch.tensor(x, dtype=torch.float32))


class ReplayMemory:
    """_summary_

    """    
    def __init__(self, capacity):
        self.memory = deque([], maxlen=capacity)

    def push(self, *args):
        """Save a transition"""
        self.memory.append(Transition(*args))

    def sample(self, batch_size):
        """_summary_

        Args:
            batch_size (_type_): _description_

        Returns:
            _type_: _description_
        """        
        return random.sample(self.memory, batch_size if len(self.memory) >= batch_size else len(self.memory))

    def __len__(self):
        return len(self.memory)


class MacroAgent:
    """_summary_
    """    
    def __init__(self) -> None:
        self.assets = np.array([], dtype=np.float32)
        self.q_network = QNetwork()
        pass

    def sell_assets(self, price):
        """_summary_
        """        
        earning = np.sum(np.ones_like(self.assets) * price - self.assets)
        self.assets = np.array([], dtype=np.float32)
        return earning
    
    def buy_asset(self, price):
        """_summary_

        Args:
            price (_type_): _description_
        """        
        self.assets = np.append(self.assets, price)
        pass
