# small utilities, no deps

def flatten(xs):
    return [y for x in xs for y in x]

def most_common(xs):
    return max(set(xs), key=xs.count) if xs else None

def group_by(items, key):
    out = {}
    for it in items:
        out.setdefault(key(it), []).append(it)
    return out

# cleanup later
