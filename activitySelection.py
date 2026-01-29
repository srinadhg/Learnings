# Events is a list of tuples (start_time, end_time)
def max_visitable_events(events):
    # Step 1: Sort events by their end times
    events.sort(key=lambda x: x[1])
    n = len(events)
    
    # Step 2: Precompute P[], where P[i] is the index of last non-overlapping event with i
    P = [-1] * n
    for i in range(1, n):
        # Binary search to find the latest event that ends before events[i][0] (start time of i)
        low, high = 0, i - 1
        while low <= high:
            mid = (low + high) // 2
            if events[mid][1] <= events[i][0]:
                P[i] = mid
                low = mid + 1
            else:
                high = mid - 1
    
    # Step 3: DP array for maximum number of events
    dp = [0] * n
    dp[0] = 1  # First event can always be attended
    
    for i in range(1, n):
        # Case 1: Include current event
        include = 1 + (dp[P[i]] if P[i] != -1 else 0)
        # Case 2: Exclude current event
        exclude = dp[i - 1]
        # Take the maximum of both cases
        dp[i] = max(include, exclude)
    
    return dp[-1]  # The maximum number of events