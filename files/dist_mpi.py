from mpi4py import MPI
import numpy as np
from scipy.spatial.distance import pdist
import pandas as pd
# Initialize MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Rank 0 initializes data
if rank == 0:
    #x = np.arange(20)
    #y = np.arange(10, 30)
    #z = np.arange(15, 35)
    fd = pd.read_csv("A_data.csv")  # Data file
    fd = fd.sample(n = 100)
    xx, yy, zz = fd['x'].to_numpy(), fd['y'].to_numpy(), fd['z'].to_numpy()
    points = np.column_stack((xx, yy, zz))  # Shape: (20,3)
    num_points = len(points)
    
    # Generate unique pairs (i, j) where i < j
    pair_indices = [(i, j) for i in range(num_points) for j in range(i + 1, num_points)]
    
    # Split pair indices among processes
    split_pairs = np.array_split(pair_indices, size)
else:
    points = None
    split_pairs = None

# Broadcast points to all ranks
points = comm.bcast(points, root=0)

# Scatter pair indices to processes
local_pairs = comm.scatter(split_pairs, root=0)

# Compute local pairwise distances
local_distances = np.array([np.linalg.norm(points[i] - points[j]) for i, j in local_pairs])

# Gather all computed distances at Rank 0
all_distances = comm.gather(local_distances, root=0)

# Rank 0 saves results
if rank == 0:
    all_distances = np.concatenate(all_distances)  # Merge results
    with open("distances.dat", "w") as f:
        for dist in all_distances:
            f.write(f"{dist:.6f}\n")  # Save with 6 decimal places
    print("Pairwise distances saved to distances.dat")

