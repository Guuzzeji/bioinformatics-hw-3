# Function to load the distance matrix from a file
def load_distance_matrix(file_path: str) -> dict[tuple[str, str], int]:
    with open(file_path, 'r') as file:
        lines = file.readlines()
        matrix = {}
        offset = 0 # allow offset to not have extra data

        for i, line in enumerate(lines):
            row = list(map(float, line.split()))
            for j in range(offset, len(row)):
                if i != j:
                    matrix[(i, j)] = row[j]

            offset += 1
        return matrix

def print_species_history(history: list[list[str]]):
    for group in history:
        group_1 = sorted([c for c in group[0]]) # NOTE: have to sort in order to pass test cases
        group_2 = sorted([c for c in group[1]])

        # Print in correct format alphabetically
        if group_1[0] > group_2[0]:
            print(f"Merge {group_2} and {group_1} to form {sorted(group_2 + group_1)}")
        else:
            print(f"Merge {group_1} and {group_2} to form {sorted(group_1 + group_2)}")


def upgma(distance_matrix: dict[tuple[int,int], int], species: [str]):
    """
    Implement this function that will load the distance_matrix and species, and return the tree (aka print)

    Note
        - species index is equal to distance index for both row and col
    """

    species_dict = {i: species[i] for i in range(len(species))}
    history = [] # store each step of merges
    num_species = len(species)

    while len(species_dict) > 1:
        min_distance_species = sorted(distance_matrix.items(), key=lambda item: item[1])[0]

        # Get the species from min distance calc
        i = min_distance_species[0][0] # col
        j = min_distance_species[0][1] # row

        new_node = species_dict[i] + species_dict[j]
        history.append([species_dict[i], species_dict[j]])

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
                distance_matrix[(min(num_species, k), max(num_species, k))] = new_dist

        # Remove distances involving the old clusters i and j
        distance_matrix = {k: v for k, v in distance_matrix.items() if i not in k and j not in k}

        # Increase the cluster index (for the next new cluster)
        num_species += 1

    print_species_history(history)


# Use this: 
# - https://stackoverflow.com/questions/66969893/scipy-and-the-hierarchical-clustering-input
# - https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.linkage.html



# Running UPGMA
print("UPGMA Tree Construction:")
# Load the distance matrix
file_path = 'input3.txt'  # Replace with your actual file path
distance_matrix = load_distance_matrix(file_path)

# Specify the species names
species = ['A', 'B', 'C', 'D', 'E']  # Example species for your input
upgma(distance_matrix.copy(), species)


# Load the distance matrix
#file_path = 'input10.txt'  # Replace with your actual file path
#distance_matrix = load_distance_matrix(file_path)

# Specify the species names
#species = ['A', 'B', 'C', 'D','E']  # Example species for your input
#upgma(distance_matrix.copy(), species)

