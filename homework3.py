"""
File Name: homework3.py
Created: Gabe

Main file where upgma is done through custom upgma algorthim and 
the one used byscipy.
"""

import numpy
from scipy.cluster.hierarchy import dendrogram, linkage
from matplotlib import pyplot as plt

def load_distance_matrix(file_path: str) -> dict[tuple[str, str], int]:
    """
    Function to load the distance matrix from a file

    Args:
        file_path (str): Path to the file to load distance matrix

    Returns:
        dict[tuple[str, str], int] A dict of our distances for each 
        species we are dealing with. [(col, row) -> distance]
    """

    with open(file_path, encoding="utf-8") as file:
        lines = file.readlines()
        matrix = {}
        offset = 0  # allow offset to not have extra data

        for i, line in enumerate(lines):
            row = list(map(float, line.split()))
            for j in range(offset, len(row)):
                if i != j:
                    matrix[(i, j)] = row[j]
            offset += 1
        return matrix

def print_species_history(history: list[list[str]]):
    """
    Print out the species history in "Merge A and B to form AB"

    Args:
        - history: list[list[str]]: A list of species and how each 
            one was connected to each other
    """

    for group in history:
        # NOTE: have to sort in order to pass test cases
        group_1 = sorted([c for c in group[0]])
        group_2 = sorted([c for c in group[1]])

        combine_groups = sorted(group_2 + group_1)

        # Print in correct format alphabetically
        if group_1[0] > group_2[0]:
            print(f"Merge {group_2} and {group_1} to form {combine_groups}")
        else:
            print(f"Merge {group_1} and {group_2} to form {combine_groups}")


def upgma(distance_matrix: dict[tuple[int, int], int], species: list[str]):
    """
    Implement this function that will load the distance_matrix and species, 
    and return the tree (aka print)

    Note:
        - species index is equal to distance index for both row and col

    Args:
        distance_matrix (dict[tuple[int, int], int]): A dict of our distances 
            for each species we are dealing with. [(col, row) -> distance]

        species (list[str]): A list of species, should line up base on index
            i.e [A,B,C] => [A = 0, B = 1, C = 2] 
    """

    species_dict = {i: species[i] for i in range(len(species))}
    history = []  # store each step of merges
    num_species = len(species)

    # Loop over ever specie created
    while len(species_dict) > 1:
        min_distance_species = sorted(
            distance_matrix.items(), key=lambda item: item[1])[0]

        # Get the species from min distance calc
        i = min_distance_species[0][0]  # col
        j = min_distance_species[0][1]  # row

        # Create new species group
        new_node = species_dict[i] + species_dict[j]
        history.append([species_dict[i], species_dict[j]])

        # Remove from list and add back as combine specie group
        del species_dict[i]
        del species_dict[j]
        species_dict[num_species] = new_node

        # Calculate new distances to the merged cluster
        for k in species_dict:
            if species_dict[k] != new_node:
                # Calculate average distance between clusters (i, j) and k
                dist_ik = distance_matrix.get((min(i, k), max(i, k)), 0)
                dist_jk = distance_matrix.get((min(j, k), max(j, k)), 0)
                new_dist = (dist_ik + dist_jk) / 2
                distance_matrix[(min(num_species, k),
                                 max(num_species, k))] = new_dist

        # Remove distances involving the old clusters i and j
        distance_matrix = {
            k: v for k, v in distance_matrix.items() if i not in k and j not in k}

        # Increase the cluster index (for the next new cluster)
        num_species += 1

    # Output
    print_species_history(history)
    # print("List of species -> ", history)


################################################################
# Lib implementation
# Use this for lib upgma:
# - https://stackoverflow.com/questions/66969893/scipy-and-the-hierarchical-clustering-input
# - https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.linkage.html
################################################################

def convert_matrix_2d(distance_matrix: dict[tuple[int, int], int],
                      len_matrix: int) -> list[list[int]]:
    """
    Convert dict matrix of distances into simple 2d array
    
    Args:
        distance_matrix (dict[tuple[int, int], int]): A dict of our distances 
            for each species we are dealing with. [(col, row) -> distance]

        len_matrix (int): The number of rows * columns in the matrix

    Returns:
        list[list[int]]: A 2D array (distance matrix)
    """
    distance_2d = numpy.zeros((len_matrix, len_matrix))

    for _, j in enumerate(distance_matrix):
        dis = distance_matrix[j]
        col = j[0]
        row = j[1]
        distance_2d[col][row] = dis

    return distance_2d

def upgma_from_scipy(distance_matrix: dict[tuple[int, int], int], species: list[str]):
    """
    Use scipy upgma algorthim to show connection of species

    Args:
        distance_matrix (dict[tuple[int, int], int]): A dict of our distances 
            for each species we are dealing with. [(col, row) -> distance]

        species (list[str]): A list of species, should line up base on index
            i.e [A,B,C] => [A = 0, B = 1, C = 2] 
    """
    dis_2d_matrix = convert_matrix_2d(distance_matrix, len(species))
    species_tree = linkage(dis_2d_matrix)

    # print("From upgma_from_scipy - >\n", species_tree)

    # Plot and show
    plt.figure(figsize=(25, 10))
    dendrogram(species_tree, labels=species)
    plt.xlabel("Species")

    plt.show()


# ! Running UPGMA
# print("UPGMA Tree Construction:")
# Load the distance matrix
# file_path = 'input3.txt'  # Replace with your actual file path
# distance_matrix = load_distance_matrix(file_path)

# # Specify the species names
# species = ['A', 'B', 'C', 'D', 'E']  # Example species for your input
# upgma(distance_matrix.copy(), species)
# upgma_from_scipy(distance_matrix.copy(), species)


# Load the distance matrix 1
# file_path = 'input1.txt'  # Replace with your actual file path
# distance_matrix = load_distance_matrix(file_path)

# # Specify the species names
# species = ['A', 'B', 'C']  # Example species for your input
# # upgma(distance_matrix.copy(), species)
# upgma_from_scipy(distance_matrix.copy(), species)

# Load the distance matrix 2
# file_path = 'input2.txt'  # Replace with your actual file path
# distance_matrix = load_distance_matrix(file_path)

# # Specify the species names
# species = ['A', 'B', 'C', 'D'] # Example species for your input
# # upgma(distance_matrix.copy(), species)
# upgma_from_scipy(distance_matrix.copy(), species)
