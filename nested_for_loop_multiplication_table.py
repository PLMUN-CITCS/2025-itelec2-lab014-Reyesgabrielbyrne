# Outer loop for rows (1 to 5)
for i in range(1, 6):
    # Inner loop for columns (1 to 5)
    for j in range(1, 6):
        product = i * j  # Calculate the product
        print(f"{product:4}", end="")  # Print formatted output with consistent spacing
    
    print()  # Print a newline after each row