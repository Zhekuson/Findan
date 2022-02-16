import torch
import numpy as np
import random
import torch.nn as nn
from collections import namedtuple, deque
ACTIONS={"BUY":torch.tensor([1,0,0], dtype=torch.float32),
 "HOLD":torch.tensor([0,1,0], dtype=torch.float32),
  "SELL":torch.tensor([0,0,1], dtype=torch.float32)}
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
            nn.ReLU(),
            self.hidden1,
            nn.ReLU(),
            self.hidden2,
            nn.ReLU(),
            self.out,
            nn.Softmax()
        )


    def forward(self, x):
        """_summary_

        Args:
            input (_type_): _description_

        Returns:
            _type_: _description_
        """      
        x = torch.nan_to_num(x)
        # 0 HOLD 1 BUY 2 SELL
        id = torch.argmax(self.DQN.forward(x))
        if id == 0:
            return ACTIONS['HOLD'], 0
        elif id == 1:
            return ACTIONS['BUY'], 0
        else:
            if x[6] == 0:
                return ACTIONS['SELL'],-1
            else:
                return ACTIONS['SELL'],1 if x[6] > 0 else ACTIONS['SELL'],-1


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

    def estimate_assets(self, price):
        """_summary_

        Args:
            price (_type_): _description_

        Returns:
            _type_: _description_
        """        
        if len(self.assets) > 0:
            return np.sum(np.ones_like(self.assets, dtype=np.float32) * price - self.assets)
        else:
            return 0

    def sell_assets(self, price):
        """_summary_
        """        
        earning = self.estimate_assets(price)
        self.assets = np.array([], dtype=np.float32)
        return earning
    
    def buy_asset(self, price):
        """_summary_

        Args:
            price (_type_): _description_
        """        
        self.assets = np.append(self.assets, price)
        pass
    
