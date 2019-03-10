from Bin import first_fit, first_fit_d, best_fit, Bin
from csv import reader

with open("bin.txt", "r") as f:
    my_list = [[int (character) for character in line] for line in reader(f, delimiter = " ")]

num_cases = my_list.pop(0)[0]
for case in range(num_cases):
    bin_size = my_list.pop(0)[0]
    num_items = my_list.pop(0)[0]
    weights = my_list.pop(0)

    n_bins = len(first_fit(weights, bin_size))
    n_bins_d = len(first_fit_d(weights, bin_size))
    b_bins = len(best_fit(weights, bin_size))

    print("Test Case ", case + 1, 
        "First Fit ", n_bins,
        ", First Fit Decreasing ", n_bins_d,
        ", Best Fit: ", b_bins)
