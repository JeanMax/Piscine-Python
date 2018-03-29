#!/usr/bin/env python3

import random
import beverages as bev


class CoffeeMachine:
    def __init__(self):
        self.drink = 0

    class EmptyCup(bev.HotBeverage):
        price = 0.90
        name = "empty cup"
        def description(self):
            return("An empty cup?! Gimme my money back!")

    class BrokenMachineException(Exception):
        def __init__(self):
            self.message = "This coffee machine has to be repaired."
        def __str__(self):
            return self.message

    def repair(self):
        self.drink = 0

    def serve(self, Beverage):
        if self.drink >= 10:
            raise self.BrokenMachineException()
        self.drink += 1
        return (Beverage() if random.random() < 0.5 else self.EmptyCup())


if __name__ == '__main__':
    m = CoffeeMachine()
    for i in range(2):
        for b in [bev.Coffee, bev.Tea, bev.Chocolate, bev.Cappuccino] * 3:
            try:
                print(m.serve(b))
            except m.BrokenMachineException as e:
                print(e)
                m.repair()
                if i:
                    break
