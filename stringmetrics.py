from numpy import array, arange, minimum, add

def levenshtein(source, target):
    if len(source) < len(target):
        return levenshtein(target, source)
    if len(target) == 0:
        return len(source)

    source = array(tuple(source))
    target = array(tuple(target))

    previous_row = arange(target.size + 1)
    for s in source:
        current_row = previous_row + 1
        current_row[1:] = minimum(
                current_row[1:],
                add(previous_row[:-1], target != s))
        current_row[1:] = minimum(
                current_row[1:],
                current_row[0:-1] + 1)
        previous_row = current_row
    return previous_row[-1]

def hamming(source, target):
    """Return the Hamming distance between equal-length sequences"""
    if len(source) != len(target):
        raise ValueError("Undefined for sequences of unequal length")
    return sum(el1 != el2 for el1, el2 in zip(source, target))