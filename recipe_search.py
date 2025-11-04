import json

def parse_ingredients(raw_input):
    # accepts comma-separated or newline-separated ingredients
    # returns a clean list of ingredients

    # splitter; on commas or newlines
    ingredients = raw_input.replace('\n', ',').split(',')

    # normalize list: lowercase and strip whitespace
    cleaned = [ing.strip().lower() for ing in ingredients if ing.strip()]

    return cleaned

def load_recipes():
    # Load recipes from a JSON file
    with open('recipes.json', 'r') as file:
        data = json.load(file)
    return data['recipes']

def main():
    # Current testing: Does input and list parsing work?
    print("Enter your available ingredients (comma-separated):")
    print("Ex: eggs, bread, cheese, butter\n")

    # get user input
    user_input = input("Your ingredients: ").strip()

    # guard against empty input
    if not user_input:
        print("\n No ingredients entered. Exiting.\n")
        return
    
    # parse ingredients and print
    user_ing = parse_ingredients(user_input)
    print(f"\nCollected ingredients: {', '.join(user_ing)}")

    recipes = load_recipes()
    print(recipes)

if __name__ == "__main__":
    main()