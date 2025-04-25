def max_beauty_garden(flowers):
    """
    Find the subarray with maximum beauty where the first and last elements are identical.
    
    Args:
        flowers (list): List of integers representing beauty values of flowers
        
    Returns:
        dict: Dictionary containing max beauty value, best subarray, start and end indices,
              and visualization data
    """
    if not flowers:
        return {
            "max_beauty": 0,
            "best_subarray": [],
            "start_index": 0,
            "end_index": 0,
            "visual_data": []
        }
    
    # Initialize with the best single flower as default
    max_value = max(flowers)
    max_index = flowers.index(max_value)
    max_beauty = max_value
    start_idx, end_idx = max_index, max_index
    best_subarray = [flowers[max_index]]
    
    # Use a dictionary to track indices of each flower beauty value
    flower_indices = {}
    
    for i, beauty in enumerate(flowers):
        if beauty in flower_indices:
            # Check all previous occurrences of this beauty value
            for prev_index in flower_indices[beauty]:
                # Calculate beauty of subarray from prev_index to i
                current_subarray = flowers[prev_index:i+1]
                current_beauty = sum(current_subarray)
                
                # Update if this is better than our current best
                if current_beauty > max_beauty:
                    max_beauty = current_beauty
                    best_subarray = current_subarray.copy()
                    start_idx, end_idx = prev_index, i
            
            # Append current index to the list of indices for this beauty value
            flower_indices[beauty].append(i)
        else:
            # First occurrence of this beauty value
            flower_indices[beauty] = [i]
    
    # Check if we found any valid subarrays (with matching ends)
    found_valid = False
    for value, indices in flower_indices.items():
        if len(indices) > 1:
            found_valid = True
            break
    
    if not found_valid:
        return {
            "max_beauty": "No valid garden", 
            "best_subarray": [],
            "start_index": 0,
            "end_index": 0,
            "visual_data": flowers
        }
    
    # Prepare visualization data
    visual_data = []
    for i, beauty in enumerate(flowers):
        is_selected = start_idx <= i <= end_idx
        visual_data.append({
            "position": i,
            "beauty": beauty,
            "selected": is_selected
        })
    
    return {
        "max_beauty": max_beauty,
        "best_subarray": best_subarray,
        "start_index": start_idx,
        "end_index": end_idx,
        "visual_data": visual_data
    }