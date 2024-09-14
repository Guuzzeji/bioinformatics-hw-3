import os
from homework3 import *

def test_upgma_function(input_file, expected_output_file, species):
    # Load the distance matrix from the input file
    distance_matrix = load_distance_matrix(input_file)
    
    # Capture the actual UPGMA output
    actual_output = []
    def capture_print(s):
        actual_output.append(s)

    # Override the print function to capture output instead of printing it
    import builtins
    original_print = builtins.print
    builtins.print = capture_print
    
    try:
        # Run UPGMA algorithm
        upgma(distance_matrix, species)
    finally:
        # Restore the original print function
        builtins.print = original_print

    # Load expected output from file
    with open(expected_output_file, 'r') as file:
        expected_output = [line.strip() for line in file.readlines()]

    # Compare actual and expected output
    if actual_output == expected_output:
        print(f"Test passed for {input_file}")
    else:
        print(f"Test failed for {input_file}")
        print("Expected output:")
        print(expected_output)
        print("Actual output:")
        print(actual_output)

# Example test cases
test_upgma_function('input1.txt', 'expected_output1.txt', ['A', 'B', 'C'])
test_upgma_function('input2.txt', 'expected_output2.txt', ['A', 'B', 'C', 'D'])
test_upgma_function('input3.txt', 'expected_output3.txt', ['A', 'B', 'C', 'D', 'E'])

