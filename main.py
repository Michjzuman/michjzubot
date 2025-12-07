import os
import random
import json

from michjzubot import Brain

with open("./numbers.json", "r") as file:
    numbers = json.load(file)

def random_number():
    nums = []
    for num in numbers:
        nums.append(num)
    return random.choice(nums)

def draw_number(number):
    for i in range(int(len(number) / 3)):
        line = [number[i * 3], number[i * 3 + 1], number[i * 3 + 2]]
        l = []
        for pixel in line:
            l.append([" ", "#"][int(pixel)])
        print(" ".join(l))

def to_vector(number_str):
    return [int(ch) for ch in number_str]

os.system("clear")
print("\n" * 2)

num_str = random_number()
draw_number(num_str)
print()
print(numbers[num_str])
vec = to_vector(num_str)
print()

brain = Brain(
    hidden_layers=[15],
    inputs=15,
    outputs=10,
)

print(brain.weights)