# Beltmatic Factoriser

This Python script is designed to calculate combinations of numbers to reach a specific goal. It uses the itertools library to generate all possible combinations of numbers from a given list, and then filters out the combinations that add up to the goal number. 

The script supports four operations for goal seeking: addition, multiplication, double multiplication, and triple multiplication.

## Usage

To use this script, you need to provide a goal number and a list of numbers as command line arguments. 

Here's an example:

```bash
python beltmatic_factoriser.py 747 1 2 3 4 5 6 7 8 9 11
```

In this example, `747` is the goal and `1 2 3 4 5 6 7 8 9 11` is the list of numbers. 

## Arguments

- `Goal`: The goal number to reach. Must be a positive integer.
- `Numbers`: The list of numbers to use. All numbers must be positive integers.
- `--max_set`: The maximum set of numbers to use. Default is 5.

## Output

The script will output the combinations of numbers that can be added or multiplied together to reach the goal number. The results are ranked by cost, with the lowest cost combination being displayed first. The cost is calculated based on the number of operations used, with addition costing 1 and multiplication costing 10. 

For example, if the goal is 747 and the numbers are 1 2 3 4 5 6 7 8 9 11 the script might output something like this:

```
python3 .\beltmatic_factoriser.py 747 1 2 3 4 5 6 7 8 9 11

Results ranked by cost:
Algo=> 747 = (2 * 9) + (9 * 9 * 9)
Cost: 51


Algo=> 747 = (2 * 6) + (3 * 5 * 7 * 7)
Cost: 61


Algo=> 747 = (2 * 9) + (1 * 9 * 9 * 9)
Cost: 61


Algo=> 747 = (1) + (11) + (3 * 5 * 7 * 7)
Cost: 61


Algo=> 747 = (1) + (4 * 5) + (6 * 11 * 11)
Cost: 61


Algo=> 747 = (1) + (1 * 11) + (3 * 5 * 7 * 7)
Cost: 71
```

This means that the numbers 1, 2, 3, 4, 5, 6, 7, 8, 9, and 10 can be added together to reach the goal of 531, and the cost of this combination is 10.