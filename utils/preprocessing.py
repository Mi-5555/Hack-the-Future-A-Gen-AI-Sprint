def normalize_data(data):
    # Example preprocessing: normalize to range [0, 1]
    if not data:
        return []
    max_val = max(data)
    return [x / max_val for x in data] if max_val else data
