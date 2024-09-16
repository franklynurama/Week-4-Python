import json
import difflib

# Load the dictionary data from a JSON file
def load_dictionary(filename):
    with open(filename, 'r') as file:
        return json.load(file)

# Function to get the definition of a word
def get_definition(word, dictionary):
    word_lower = word.lower()  # Convert the input word to lowercase
    if word_lower in dictionary:
        return dictionary[word_lower][0] # Return the first definition
    else:
        # Suggest similar words if the word is not found
        suggestions = difflib.get_close_matches(word_lower, dictionary.keys(), n=5)
        return f"'{word}' not found. Did you mean: {', '.join(suggestions)}?" if suggestions else f"'{word}' not found."

# Main function to run the program
def main():
    # Load the dictionary data
    dictionary = load_dictionary('data.json') # Assuming the JSON file is named 'data.json'

    while True:
        user_input = input("Enter a word to get its definition (or type 'exit' to quit): ")
        word = user_input.strip()
        
        if word.lower() == 'exit': # Check for exit command
            print("Thank you for using the dictionary. Goodbye!")
            break
        
        definition = get_definition(user_input, dictionary)
        print(definition)

# Run the program
if __name__ == '__main__':
    main()
