class Bin(object):
    def __init__(self):
        self.items = []
        self.sum = 0

    def append(self, item):
        self.items.append(item)
        self.sum += item

    def __str__(self):
        return "Bin(sum = {0}, items = {1})".format(self.sum, str(self.items))
    
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

def best_fit(items, bin_size):
    bins =[]
    for item in items:
        min_bin = None
        capacity = float("inf")

        for bin in bins:
            if (bin.sum + item <= bin_size and
                bin_size - (bin.sum + item) < capacity):
                min_bin = bin
                capacity = bin_size - (bin.sum + item)
        
        if min_bin is not None:
            min_bin.append(item)
        else:
            bin = Bin()
            bin.append(item)
            bins.append(bin)    
    return bins