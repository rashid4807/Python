def calculate_wrapping_paper(dimensions):
    total_paper = 0
    
    for dims in dimensions:
        l, w, h = dims
        # Calculate surface area
        surface_area = 2 * l * w + 2 * w * h + 2 * h * l
        # Calculate the area of the smallest side
        smallest_side = min(l * w, w * h, h * l)
        # Total paper required for this box
        total_for_box = surface_area + smallest_side
        
        total_paper += total_for_box

    return total_paper

# Manually input dimensions from the user
def get_dimensions_from_user():
    dimensions = []
    num_boxes = int(input("Enter the number of boxes: "))
    for i in range(num_boxes):
        print(f"Enter dimensions for box {i + 1} (length width height): ")
        dims = tuple(map(int, input().split()))
        if len(dims) == 3:
            dimensions.append(dims)
        else:
            print("Invalid input. Please enter exactly three integers.")
            break
    return dimensions

# Main script
dimensions = get_dimensions_from_user()
# Calculate the total wrapping paper required
total_paper_needed = calculate_wrapping_paper(dimensions)
print(f"Total wrapping paper needed: {total_paper_needed} square units")
2