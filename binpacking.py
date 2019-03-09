class Bin(object):
    def __init__(self):
        self.items = []
        self.sum = 0

    def append(self, item):
        self.items.append(item)
        self.sum += item

    def __str__(self):
        return "Bin(sum = {0}}, items = {1})".format(self.sum, str(self.items))
    
    def __repr__(self):
        return "Bin(sum = {0}, items = {1})".format(self.sum, str(self.items))


def first_fit(items, bin_size):
    bins = []
    for item in items:
        for bin in bins:
            if bin.sum + item <= bin_size:
                bin.append(item)
                break
        else:
            bin = Bin()
            bin.append(item)
            bins.append(bin)

    return bins

def first_fit_d(items, bin_size):
    values = sorted(items, reverse=True)
    return (first_fit(values, bin_size))

# weights = [3, 8, 2, 7]
# weights = [5, 10, 2, 5, 4, 4]
weights = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
bin_size = 10

n_bins = first_fit(weights, bin_size)
n_bins_d = first_fit_d(weights, bin_size)

print(n_bins)
print(len(n_bins_d))