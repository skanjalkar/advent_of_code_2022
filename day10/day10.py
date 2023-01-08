#!/usr/bin/env python3
# 2022 Day 10: Cathode-Ray Tube

def process_input(filename):
    """Acquire input data"""
    with open(filename) as file:
        input = file.read().splitlines()

    # change addx instructions to a noop, followed by the addx
    program = []
    for line in input:
        token = line.split()
        if token[0] == 'addx':
            program.append('noop')
        program.append(line)

    return program


def run_program(program):
    signal_sum = 0
    X_reg = 1
    cycle = 0
    pixel = 0
    line = ''
    for instruction in program:
        cycle += 1

        if pixel in (X_reg-1, X_reg, X_reg+1):
            ch = '#'
        else:
            ch = '.'
        line += ch

        if cycle in (20,60,100,140,180,220):
            signal_strength = cycle * X_reg
            signal_sum += signal_strength
        token = instruction.split()
        if token[0] == 'addx':
            V = int(token[1])
            X_reg += V
        pixel += 1
        if pixel % 40 == 0:
            print(line)
            line = ''
            pixel = 0

    return signal_sum

#-----------------------------------------------------------------------------------------

filename = 'input.in'
#filename = 'sample.txt'

program = process_input(filename)

signal_sum = run_program(program)

print('')
print('Sum of signal strengths =',signal_sum)
print('')

# credit to msschmitt