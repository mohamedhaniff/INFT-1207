# Author: Your Name
# Student ID: 100XX
# Description: Analyze movie budgets and save results to a file.

def calculate_average_budget(movies):
    """Calculate the average budget of all movies."""
    budgets = [budget for _, budget in movies]
    return sum(budgets) / len(budgets)

def find_high_budget_movies(movies, average_budget):
    """Find movies with budgets higher than the average."""
    return [(name, budget) for name, budget in movies if budget > average_budget]

def read_movies_from_file(file_name):
    """Read movies from a file."""
    movies = []
    with open(file_name, "r") as file:
        lines = file.readlines()[1:]  # Skip header
        for line in lines:
            name, budget = line.strip().split(", ")
            movies.append((name, int(budget)))
    return movies

def write_results_to_file(file_name, average_budget, high_budget_movies):
    """Write analysis results to a file."""
    with open(file_name, "w") as file:
        file.write(f"Average Budget: ${average_budget:,.2f}\n")
        file.write("Movies with Budgets Higher than Average:\n")
        for name, budget in high_budget_movies:
            file.write(f"{name}: ${budget:,}\n")


if __name__ == "__main__":
    # Read movies from file
    new_movie = input ("Pl enter a movie ")



    movies = read_movies_from_file("MovieList.txt")

    # Display all movies
    print("Full Movie List:")
    for name, budget in movies:
        print(f"  {name}: ${budget:,}")

    # Calculate average budget
    average_budget = calculate_average_budget(movies)

    # Find high-budget movies
    high_budget_movies = find_high_budget_movies(movies, average_budget)

    # Print results
    print(f"Average Budget: ${average_budget:,.2f}")
    print("Movies with Budgets Higher than Average:")
    for name, budget in high_budget_movies:
        print(f"  {name}: ${budget:,}")

    # Write results to output file
    write_results_to_file("Output.txt", average_budget, high_budget_movies)
    print("Results saved to 'Output.txt'.")