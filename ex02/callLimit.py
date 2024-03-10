def callLimit(limit: int):
    """call limit"""
    count = 0

    def callLimiter(function):
        """call limiter"""
        def limit_function(*args, **kwds):
            """limit function"""
            nonlocal count
            if count < limit:
                count += 1
                return function(*args, **kwds)
            else:
                print(f"Error: {repr(function)} call too many times")
        return limit_function
    return callLimiter
