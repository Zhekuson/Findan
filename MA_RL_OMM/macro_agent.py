import torch
import numpy as np
import numpy.random as random
import torch.nn as nn
from collections import namedtuple, deque

Transition = namedtuple(
    'Transition', ('state', 'action', 'reward', 'next_state', 'done'))


class QNetwork(nn.Module):
    def __init__(self) -> None:
        super(QNetwork, self).__init__()
        self.input = nn.Linear(8, 8)
        self.hidden1 = nn.Linear(8, 8)
        self.hidden2 = nn.Linear(8, 8)
        self.out = nn.Linear(8, 3)
        self.DQN = nn.Sequential(
            self.input,
            nn.ReLU(),
            self.hidden1,
            nn.ReLU(),
            self.hidden2,
            nn.ReLU(),
            self.out
        )

    def forward(self, input):
        price = input['price']
        indicators = input['indicators']
        assets = input['assets']
        diff = np.sum(np.ones_like(assets) * price - assets)
        tensor = torch.from_numpy(np.hstack((price, indicators, diff)))
        return self.DQN(tensor)


class ReplayMemory:

    def __init__(self, capacity):
        self.memory = deque([], maxlen=capacity)

    def push(self, *args):
        """Save a transition"""
        self.memory.append(Transition(*args))

    def sample(self, batch_size):
        return random.choice(self.memory, size=batch_size)

    def __len__(self):
        return len(self.memory)


class MacroAgent:
    def __init__(self) -> None:
        self.assets = np.array([], dtype=float)
        self.q_network = QNetwork()
        pass
