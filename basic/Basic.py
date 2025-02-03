def calculate_wrapping_paper(dimensions):
    total_paper = 0
    for l, w, h in dimensions:
        # Surface area of the box
        surface_area = 2 * l * w + 2 * w * h + 2 * h * l
        # Area of the smallest side
        smallest_side = min(l * w, w * h, h * l)
        # Total paper for this box
        total_paper += surface_area + smallest_side
    return total_paper

# Input dimensions from the user
dimensions = []
print("Enter the number of boxes:")
num_boxes = int(input())
for i in range(num_boxes):
    print(f"Enter dimensions for box {i + 1} (length width height):")
    l, w, h = map(int, input().split())
    dimensions.append((l, w, h))

# Calculate total wrapping paper required
total_paper_needed = calculate_wrapping_paper(dimensions)
print(f"Total wrapping paper needed: {total_paper_needed} square units")