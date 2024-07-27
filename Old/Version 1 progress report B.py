import pandas as pd
from rapidfuzz import fuzz, process

# Function to load data into a DataFrame
def load_data(file_path):
    try:
        df = pd.read_csv(file_path)
        if df.empty:
            print(f"Error: File '{file_path}' is empty.")
            return None
        if not all(column in df.columns for column in ["Title", "Author", "Year", "Summary"]):
            print(f"Error: File '{file_path}' does not contain the required columns.")
            return None
        return df
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except pd.errors.EmptyDataError:
        print(f"Error: File '{file_path}' is empty.")
        return None
    except pd.errors.ParserError:
        print(f"Error: Parsing error occurred while reading '{file_path}'.")
        return None

# Function to find the best match for a search term in the loaded DataFrame
def fuzzy_find(df, search_term, threshold=50):
    matches = process.extract(search_term, df["Title"], scorer=fuzz.token_set_ratio, score_cutoff=threshold)
    
    if not matches:
        return None
    
    best_match = matches[0]
    index = best_match[2]
    title = df.loc[index, "Title"]
    author = df.loc[index, "Author"]
    year = df.loc[index, "Year"]
    
    return title, author, year

def main():
    # Prompt user for file path until a valid file is loaded
    while True:
        file_path = input("Enter the path to the books data file (CSV format): ").strip()
        df = load_data(file_path)
        if df is not None:
            break  # Exit loop if data is successfully loaded
    
    while True:
        # 1) Ask the user for the title search term
        search_term = input("Enter a book title to search (or press Enter to quit): ").strip()
        
        if not search_term:
            break  # Exit the loop if the user presses Enter without entering a search term
        
        # 2) Ask for a quality threshold (our match %), default to 50
        threshold_str = input(f"Enter quality threshold (default is 50): ").strip()
        threshold = int(threshold_str) if threshold_str else 50
        
        # 3) Search the Title column in the DataFrame df for the search term with fuzzy search
        result = fuzzy_find(df, search_term, threshold)
        
        if result:
            title, author, year = result
            print(f"The summary for '{title}' by {author} (published in {year}) is:")
            # Additional logic can be added here to fetch and print more details or summaries
        else:
            print("No good enough match found.")
    
    # Exit message
    print("Exiting the program. Goodbye!")

if __name__ == "__main__":
    main()