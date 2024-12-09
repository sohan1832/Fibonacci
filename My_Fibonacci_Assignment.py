def generate_fibonacci_by_terms(n):
    """Generate My Fibonacci series with  n terms."""
    if n <= 0:
        return []
    series = [0, 1]
    while len(series) < n:
        series.append(series[-1] + series[-2])
    return series[:n]

def generate_fibonacci_by_max_value(max_value):
    #Generate Fibonacci series with values up to max_value.
    if max_value < 0:
        return []
    series = [0, 1]
    while series[-1] + series[-2] <= max_value:
        series.append(series[-1] + series[-2])
    return series if series[-1] <= max_value else series[:-1]

def get_positive_integer(prompt):
    
    while True:
        try:
            value = int(input(prompt))
            if value >= 0:
                return value
            else:
                print("Please enter a non-negative integer.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def main():
    while True:
        print("\nChoose an option:")
        print("1. Generate Fibonacci series by number of terms")
        print("2. Generate Fibonacci series by maximum value")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            num_terms = get_positive_integer("Enter the number of terms: ")
            series = generate_fibonacci_by_terms(num_terms)
            print(f"Fibonacci series ({num_terms} terms): {', '.join(map(str, series))}")
        
        elif choice == "2":
            max_value = get_positive_integer("Enter the maximum value: ")
            series = generate_fibonacci_by_max_value(max_value)
            print(f"Fibonacci series (up to {max_value}): {', '.join(map(str, series))}")
        
        elif choice == "3":
            print("Goodluck!")
            break
        
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
