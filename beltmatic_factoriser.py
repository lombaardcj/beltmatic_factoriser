# Author: Chris Lombaard
# Date: 2024-05-12

COST_ADD = 1
COST_MULT = 10

import itertools

def calculate(goal, numbers, max_set=5,operation='addition', print_combinations=False, max_solutions=3):
    # generate all possible combinations of numbers
    cost_add = 0
    cost_mult = 0
    soutions_found = 0
    solutions = []
    for i in range(1, max_set+1):
        if print_combinations:
            print(f"Calculating for {i} numbers")
        for combination in itertools.combinations_with_replacement(numbers, i):
            if print_combinations:
                print(f"Combination: {combination}")
            total = 1

            # GOAL = (N1 + N2 +..N5) 
            if operation == 'addition':
                total = sum(combination)
                if total == goal:
                    # FOUND THE GOAL EXIT
                    cost_add = len(combination)     # 1 for every addition
                    return COST_ADD*cost_add+ COST_MULT*cost_mult, operation, combination
                
            elif operation == 'multiplication':
                total = 1
                for number in combination:
                    total *= number
                if total == goal:
                    # FOUND THE GOAL EXIT
                    cost_mult = len(combination)     # 1 for every addition
                    soutions_found += 1                                      
                    solutions.append((COST_ADD*cost_add + COST_MULT*cost_mult, operation, combination, None, None))
                    if soutions_found >= max_solutions:
                        return solutions
            
            # GOAL = (N1*N2..N5) + (N1*N2..N5)
            elif operation == 'mult_add_mult':
                total = 1
                
                # build combination of two numbers out of set and add to current multiplication
                for number in combination:
                    total *= number
                
                # optimise from low to high
                for j in range(1, max_set+1):
                    for combination_mult in itertools.combinations_with_replacement(numbers, j):
                        total_sum_combination = 1
                        for number1 in combination_mult:
                            total_sum_combination *= number1
                        if print_combinations:
                            print(f"Combination: {combination} + {combination_mult} = {total} + {total_sum_combination}")
                        if total + total_sum_combination == goal:
                            if print_combinations:
                                print(f"Combination: {combination} + {combination_mult} = {total} + {total_sum_combination}")

                            # FOUND THE GOAL EXIT
                            cost_add = 1     # 1 for every addition
                            cost_mult = len(combination) + len(combination_mult)     # 1 for every addition

                            soutions_found += 1                                      
                            solutions.append((COST_ADD*cost_add + COST_MULT*cost_mult, operation, combination, combination_mult, None))
                            if soutions_found >= max_solutions:
                                return solutions
                        
            # GOAL = (N1*N2..N5) + (N1*N2..N5) + (N1*N2..N5)
            elif operation == 'mult_add_mult_add_mult':
                total = 1
                
                # build combination of two numbers out of set and add to current multiplication
                for number in combination:
                    total *= number
                
                # optimise from low to high
                for j in range(1, max_set+1):
                    for combination_mult in itertools.combinations_with_replacement(numbers, j):
                        total_sum_combination = 1
                        for number1 in combination_mult:
                            total_sum_combination *= number1

                        grand_total = total + total_sum_combination
                        
                        for k in range(1, max_set+1):
                            for combination_mult2 in itertools.combinations_with_replacement(numbers, k):
                                total_sum_combination2 = 1
                                for number1 in combination_mult2:
                                    total_sum_combination2 *= number1
                                if grand_total + total_sum_combination2 == goal:
                                    if print_combinations:
                                        print(f"Combination: {combination} + {combination_mult} + {combination_mult2} = {total} + {total_sum_combination} + {total_sum_combination2}")

                                    # FOUND THE GOAL EXIT
                                    cost_add = 1     # 1 for every addition
                                    cost_mult = len(combination) + len(combination_mult) + len(combination_mult2)     # 1 for every addition

                                    soutions_found += 1                                      
                                    solutions.append((COST_ADD*cost_add + COST_MULT*cost_mult, operation, combination, combination_mult, combination_mult2))
                                    if soutions_found >= max_solutions:
                                        return solutions
    return None

import argparse
import sys

# Create the parser
parser = argparse.ArgumentParser(description='Calculate combinations to reach a goal.')

# Add the arguments
parser.add_argument('Goal', metavar='goal', type=int, help='the goal to reach')
parser.add_argument('Numbers', metavar='numbers', type=int, nargs='+', help='the numbers to use')
parser.add_argument('--max_set', type=int, default=5, help='the maximum set of numbers to use')

# Parse the arguments
args = parser.parse_args()

# Check if goal is positive
if args.Goal <= 0:
    print("Error: Goal must be a positive integer.")
    sys.exit()

# Check if numbers are positive
for number in args.Numbers:
    if number <= 0:
        print("Error: All numbers must be positive integers.")
        sys.exit()

# Check if max_set is positive
if args.max_set <= 0:
    print("Error: max_set must be a positive integer.")
    sys.exit()

# Run the calculations
goal = args.Goal
numbers = args.Numbers
max_set_arg = args.max_set
results = []


result = calculate(goal, numbers, max_set=max_set_arg,operation='addition')
# result can contain multiple solutions, unpack them and then append to results
if result is not None:
    for r in result:
        results.append(r)

result = calculate(goal, numbers, max_set=max_set_arg,operation='multiplication')
if result is not None:
    for r in result:
        results.append(r)

result = calculate(goal, numbers, max_set=max_set_arg,operation='mult_add_mult')
if result is not None:
    for r in result:
        results.append(r)

result = calculate(goal, numbers, max_set=max_set_arg,operation='mult_add_mult_add_mult')
if result is not None:
    for r in result:
        results.append(r)

# Remove None results and sort by the first element
results = [r for r in results if r is not None]
results.sort(key=lambda x: x[0])

print("\nResults ranked by cost:")
for result in results:
    # print(result)
    if (result[1] == 'addition'):
        # print the list seperated by + sign        
        print(f"Algo=> {goal} = ({' + '.join(map(str, result[2]))})")
        print(f"Cost: {result[0]}")
    elif (result[1] == 'multiplication'):
        # print the list seperated by + sign with each combination seperated by *
        print(f"Algo=> {goal} = ({' * '.join(map(str, result[2]))})")
        print(f"Cost: {result[0]}")
    elif (result[1] == 'mult_add_mult'):
        # print the list seperated by + sign with each combination seperated by *
        print(f"Algo=> {goal} = ({' * '.join(map(str, result[2]))}) + ({' * '.join(map(str, result[3]))})")
        print(f"Cost: {result[0]}")
    elif (result[1] == 'mult_add_mult_add_mult'):
        # print the list seperated by + sign with each combination seperated by *
        print(f"Algo=> {goal} = ({' * '.join(map(str, result[2]))}) + ({' * '.join(map(str, result[3]))}) + ({' * '.join(map(str, result[4]))})")
        print(f"Cost: {result[0]}")
    print("\n")
