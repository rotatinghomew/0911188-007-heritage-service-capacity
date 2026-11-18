from collections import Counter


def arrivals(log, schedule):
    active = {(row['day'], row['slot']): set(row['gates']) for row in schedule}
    counts = Counter()
    for row in log:
        key = (row['day'], row['slot'])
        if row['direction'] == 'in' and row['gate'] in active.get(key, ()):
            counts['/'.join(key)] += 1
    return dict(counts)
