def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


def dedupe(items, key):
    seen = set()
    for item in items:
        """if not hashable"""
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)
