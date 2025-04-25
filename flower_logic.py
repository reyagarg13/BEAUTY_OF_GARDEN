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
            "visual_data": [],
            "garden_stats": {"total": 0, "positive": 0, "negative": 0, "neutral": 0}
        }
    
    # Garden stats for extra insights
    garden_stats = {
        "total": len(flowers),
        "positive": sum(1 for x in flowers if x > 0),
        "negative": sum(1 for x in flowers if x < 0),
        "neutral": sum(1 for x in flowers if x == 0),
        "avg_beauty": sum(flowers) / len(flowers),
        "highest_beauty": max(flowers),
        "lowest_beauty": min(flowers)
    }
    
    # Initialize with the best single flower as default
    max_value = max(flowers)
    max_index = flowers.index(max_value)
    max_beauty = max_value
    start_idx, end_idx = max_index, max_index
    best_subarray = [flowers[max_index]]
    
    # Use a dictionary to track indices of each flower beauty value
    flower_indices = {}
    
    # Store the beauty calculation for each valid subarray
    all_valid_subarrays = []
    
    for i, beauty in enumerate(flowers):
        if beauty in flower_indices:
            # Check all previous occurrences of this beauty value
            for prev_index in flower_indices[beauty]:
                # Calculate beauty of subarray from prev_index to i
                current_subarray = flowers[prev_index:i+1]
                current_beauty = sum(current_subarray)
                
                # Store this valid subarray
                all_valid_subarrays.append({
                    "start": prev_index,
                    "end": i,
                    "beauty": current_beauty,
                    "subarray": current_subarray
                })
                
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
            "visual_data": flowers,
            "garden_stats": garden_stats,
            "all_valid_subarrays": []
        }
    
    # Prepare visualization data
    visual_data = []
    for i, beauty in enumerate(flowers):
        is_selected = start_idx <= i <= end_idx
        emoji = get_flower_emoji_for_value(beauty)
        visual_data.append({
            "position": i,
            "beauty": beauty,
            "selected": is_selected,
            "emoji": emoji
        })
    
    # Calculate cumulative beauty
    cumulative_beauty = [0]
    current_sum = 0
    for beauty in flowers:
        current_sum += beauty
        cumulative_beauty.append(current_sum)
    
    # Sort valid subarrays by beauty
    all_valid_subarrays.sort(key=lambda x: x["beauty"], reverse=True)
    
    # Generate flower arrangement patterns for the best subarray
    flower_pattern = generate_flower_pattern(best_subarray)
    
    return {
        "max_beauty": max_beauty,
        "best_subarray": best_subarray,
        "start_index": start_idx,
        "end_index": end_idx,
        "visual_data": visual_data,
        "garden_stats": garden_stats,
        "cumulative_beauty": cumulative_beauty,
        "all_valid_subarrays": all_valid_subarrays[:5],  # Top 5 for performance
        "flower_pattern": flower_pattern
    }


def get_flower_emoji_for_value(value):
    """
    Return a flower emoji based on the beauty value.
    
    Args:
        value (int): Beauty value of the flower
        
    Returns:
        str: Emoji representation of the flower
    """
    if value > 5:
        return "🌹"  # Rose for high beauty
    elif value > 0:
        return "🌷"  # Tulip for positive beauty
    elif value == 0:
        return "🌱"  # Seedling for neutral
    elif value > -5:
        return "🥀"  # Wilted flower for slightly negative
    else:
        return "🌵"  # Cactus for very negative


def generate_flower_pattern(subarray):
    """
    Generate a visual flower pattern string based on the subarray.
    
    Args:
        subarray (list): List of integers representing flower beauty values
        
    Returns:
        str: A visual pattern of flowers
    """
    if not subarray:
        return ""
    
    emojis = []
    for value in subarray:
        emoji = get_flower_emoji_for_value(value)
        emojis.append(emoji)
    
    return " ".join(emojis)


def get_garden_description(garden_stats):
    """
    Generate a description of the garden based on its statistics.
    
    Args:
        garden_stats (dict): Dictionary containing garden statistics
        
    Returns:
        str: Description of the garden
    """
    if garden_stats["total"] == 0:
        return "Empty garden"
    
    # Determine the garden type based on statistics
    if garden_stats["positive"] > garden_stats["total"] * 0.7:
        garden_type = "vibrant and full of life"
    elif garden_stats["negative"] > garden_stats["total"] * 0.7:
        garden_type = "challenging and needs attention"
    elif garden_stats["neutral"] > garden_stats["total"] * 0.5:
        garden_type = "neutral and balanced"
    else:
        garden_type = "mixed with various flowers"
    
    # Generate description
    description = f"Your garden is {garden_type} with {garden_stats['total']} flowers. "
    description += f"It has {garden_stats['positive']} beautiful flowers, {garden_stats['negative']} challenging plants, "
    description += f"and {garden_stats['neutral']} neutral elements."
    
    return description