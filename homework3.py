# Function to load the distance matrix from a file
def load_distance_matrix(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        matrix = {}
        for i, line in enumerate(lines):
            row = list(map(float, line.split()))
            for j, dist in enumerate(row):
                if i != j:
                    matrix[(i, j)] = dist
        return matrix


def upgma(distance_matrix, species):
    """
    Implement this function that will load the distance_matrix and species, and return the tree
    """
    pass


# Use this: 
# - https://stackoverflow.com/questions/66969893/scipy-and-the-hierarchical-clustering-input
# - https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.linkage.html



# Running UPGMA
#print("UPGMA Tree Construction:")
# Load the distance matrix
#file_path = 'input4.txt'  # Replace with your actual file path
#distance_matrix = load_distance_matrix(file_path)

# Specify the species names
#species = ['A', 'B', 'C', 'D']  # Example species for your input
#upgma(distance_matrix.copy(), species)


# Load the distance matrix
#file_path = 'input10.txt'  # Replace with your actual file path
#distance_matrix = load_distance_matrix(file_path)

# Specify the species names
#species = ['A', 'B', 'C', 'D','E']  # Example species for your input
#upgma(distance_matrix.copy(), species)

