from mpi4py import MPI
import numpy as np
import pandas as pd

# Initialize MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Define bin parameters
nbin = 10  # Example number of bins
dr = 10   # Bin width
r_min = 5.0  # Minimum radius

# Rank 0 loads data
if rank == 0:
    df_d = pd.read_csv("A_data.csv")  # Data file
    #df_d = df_d.sample(n = 100000)
    df_r = pd.read_csv("A_rand.csv")  # Random data file
    #df_r = df_r.sample(n = 100000)
    
    # Split bins among processes
    bin_indices = np.array_split(range(nbin), size)
else:
    df_d = df_r = None
    bin_indices = None


# Broadcast dataframes to all processes
df_d = comm.bcast(df_d, root=0)
df_r = comm.bcast(df_r, root=0)

# Preallocate arrays for storing local results
local_results_d = []
local_results_r = []
local_results_dr = []

# Scatter bin indices to processes
local_bins = comm.scatter(bin_indices, root=0)

# Compute distances for assigned bins
local_results = []
for k in local_bins:

    fd = df_d[(df_d.r >= k * dr + r_min) & (df_d.r < (k + 1) * dr + r_min)]
    fd_r = df_r[(df_r.r >= k * dr + r_min) & (df_r.r < (k + 1) * dr + r_min)]
    fd = fd.sample(frac = 0.1)
    fd_r = fd_r.sample(frac = 0.1)
    xx, yy, zz = fd['x'].to_numpy(), fd['y'].to_numpy(), fd['z'].to_numpy()
    xx_r, yy_r, zz_r = fd_r['x'].to_numpy(), fd_r['y'].to_numpy(), fd_r['z'].to_numpy()
    
    points_d = np.column_stack((xx, yy, zz))
    points_r = np.column_stack((xx_r, yy_r, zz_r))
    num_points_d = len(points_d)
    num_points_r = len(points_r)
    
    # Generate unique pairs within data and random datasets
    pair_indices_d = [(i, j) for i in range(num_points_d) for j in range(i + 1, num_points_d)]
    pair_indices_r = [(i, j) for i in range(num_points_r) for j in range(i + 1, num_points_r)]
    pair_indices_dr = [(i, j) for i in range(num_points_d) for j in range(num_points_r)]
    
    # Split pair indices among processes
    split_pairs_d = np.array_split(pair_indices_d, size)
    split_pairs_r = np.array_split(pair_indices_r, size)
    split_pairs_dr = np.array_split(pair_indices_dr, size)
    
    # Broadcast points to all ranks
    #points_d = comm.bcast(points_d, root=0)
    #points_r = comm.bcast(points_r, root=0)

    # Scatter pair indices to processes
    local_pairs_d = comm.scatter(split_pairs_d, root=0)
    local_pairs_r = comm.scatter(split_pairs_r, root=0)
    local_pairs_dr = comm.scatter(split_pairs_dr, root=0)

    # Compute local pairwise distances
    local_distances_d = np.array([np.linalg.norm(points_d[i] - points_d[j]) for i, j in local_pairs_d])
    local_distances_r = np.array([np.linalg.norm(points_r[i] - points_r[j]) for i, j in local_pairs_r])
    local_distances_dr = np.array([np.linalg.norm(points_d[i] - points_r[j]) for i, j in local_pairs_dr])
    
    
    # Store local results for this bin
    local_results_d.append((k, local_distances_d))
    local_results_r.append((k, local_distances_r))
    local_results_dr.append((k, local_distances_dr))

# Gather all computed distances at Rank 0
all_results_d = comm.gather(local_results_d, root=0)
all_results_r = comm.gather(local_results_r, root=0)
all_results_dr = comm.gather(local_results_dr, root=0)

# Rank 0 processes the gathered data
if rank == 0:
    # Initialize array for storing 2PCF values
    two_pcf_array_w1 = np.zeros((nbin, 10))
    two_pcf_array_w1 = np.zeros((nbin, 10))

    # Flatten gathered results
    all_results_d = [item for sublist in all_results_d for item in sublist]
    all_results_r = [item for sublist in all_results_r for item in sublist]
    all_results_dr = [item for sublist in all_results_dr for item in sublist]

    # Convert to dictionary for easy access
    bin_distances_d = {k: np.concatenate([d for i, d in all_results_d if i == k]) for k in range(nbin)}
    bin_distances_r = {k: np.concatenate([d for i, d in all_results_r if i == k]) for k in range(nbin)}
    bin_distances_dr = {k: np.concatenate([d for i, d in all_results_dr if i == k]) for k in range(nbin)}

    # Compute 2PCF for each bin
    def compute_2pcf(bin_id, w_min, w_max):
        distances_d = bin_distances_d.get(bin_id, np.array([]))
        distances_r = bin_distances_r.get(bin_id, np.array([]))
        distances_dr = bin_distances_dr.get(bin_id, np.array([]))

        dd, _ = np.histogram(distances_d, range=(w_min, w_max), bins=10)
        rr, _ = np.histogram(distances_r, range=(w_min, w_max), bins=10)
        dr, _ = np.histogram(distances_dr, range=(w_min, w_max), bins=10)

        RR = rr / len(distances_r) 
        DR = dr / len(distances_dr) 
        DD = dd / len(distances_d) 

        return ((DD - (2 * DR)) / RR)

    for k in range(nbin):
        two_pcf_array_w1[k] = compute_2pcf(k, 0.5, 1.5)  # Storing results
        two_pcf_array_w2[k] = compute_2pcf(k, 1.6, 2.6)  # Storing results
        
    df_w1 = pd.DataFrame(two_pcf_array_w1)
    df_w1.to_csv("two_pcf_w1.csv", index=False, header=[f"Bin {i}" for i in range(10)])

    df_w2 = pd.DataFrame(two_pcf_array_w2)
    df_w2.to_csv("two_pcf_w2.csv", index=False, header=[f"Bin {i}" for i in range(10)])




