# -*- coding: utf-8 -*-

from radish import before, after


# Production code to be imported instead of directly using it here
class Calculator:
    def add(self, number1, number2):
        return number1 + number2


@before.each_scenario
def init_calculator(scenario):
    scenario.context.calculator = Calculator()

@after.each_scenario
def destory_calculator(scenario):
    del scenario.context.calculator