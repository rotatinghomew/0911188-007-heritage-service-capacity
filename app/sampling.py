from collections import Counter


def response_counts(frames, replies, day=None):
    invited = {row['id']: row['invited'] for row in frames if day is None or row['day'] == day}
    counts = Counter(row['frame'] for row in replies if row['frame'] in invited)
    return {key: {'invited': value, 'replies': counts[key]} for key, value in invited.items()}
