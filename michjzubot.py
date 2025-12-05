import numpy as np
import random

class Brain:
    def __init__(self, hidden_layers, inputs, outputs, bias=0.0):
        self.hidden_layers = hidden_layers
        self.inputs = inputs
        self.outputs = outputs
        self.bias = bias
        self.weights = [[
            random.random()
            for _ in range(self.inputs)
        ]] + [[
            random.random() 
            for _ in range(layer)
        ] for layer in self.hidden_layers ]

    def sigmoid(x):
        return 1 / (1 + np.exp(-x))

    def think(self, signals):
        z = 0
        return self.sigmoid(z)

    def visualize(self):
        RESET = "\033[0m"
        BLUE = "\033[34m"
        max_lines = max([
            len(layer)
            for layer in self.weights
        ])
        lines = [[] for _ in range(max_lines)]
        for layer in self.weights:
            for i, weight in enumerate(layer):
                lines[i].append(f"{BLUE}{str(round(weight, 1))}{RESET}")
            for i in range(max_lines - len(layer)):
                lines[i + len(layer)].append("   ")
        lines = [f"# - " + f" - # - ".join(line) + f"" for line in lines]
        print("\n".join(lines))

if __name__ == "__main__":
    import number_recognition.main as main