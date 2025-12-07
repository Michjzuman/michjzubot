import numpy as np
import random

class Brain:
    def __init__(self,hidden_layers, inputs, outputs, bias=0.0):
        self.hidden_layers = hidden_layers
        self.inputs = inputs
        self.outputs = outputs
        self.bias = bias
        self.weights = [[
            [
                random.random()
                for _ in range(self.hidden_layers[0])
            ]
            for _ in range(self.inputs)
        ]] + [[
            [
                random.random()
                for _ in range(
                    (self.hidden_layers + [self.outputs])[i + 1]
                )
            ]
            for _ in range(layer)
        ] for i, layer in enumerate(self.hidden_layers)]

    def sigmoid(x):
        return 1 / (1 + np.exp(-x))

    def think(self, signals):
        z = 0
        return self.sigmoid(z)

if __name__ == "__main__":
    import main as main