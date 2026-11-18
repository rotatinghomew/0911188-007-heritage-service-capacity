def staffing(calendar, arrivals):
    result = {}
    for row in calendar:
        key = row['day'] + '/' + row['slot']
        if not row['gates']:
            result[key] = 'closed'
        else:
            result[key] = 'review' if arrivals.get(key, 0) >= row['capacity'] else 'normal'
    return result
