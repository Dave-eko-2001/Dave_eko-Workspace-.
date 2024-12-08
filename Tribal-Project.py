# Tribal Dictionary Program
tribal_dictionary = {
    "Yoruba": {
        "house": "ilé",
        "water": "omi",
        "fire": "ina",
        "food": "ounje",
        "love": "ifẹ",
        "friend": "ọrẹ",
        "tree": "igi",
        "child": "ọmọ",
        "earth": "ayé",
        "heaven": "orun",
        "river": "odò",
        "stone": "okuta",
        "market": "ọjà",
        "sun": "oorun",
        "moon": "osupa",
        "rain": "ọjo",
        "day": "ọjọ",
        "night": "alẹ",
        "road": "ọna",
        "money": "owo",
        "wind": "afẹfẹ",
        "time": "akoko",
        "king": "oba",
        "queen": "ayaba",
        "song": "orin"
    },
    "Igbo": {
        "house": "'ụlọ",
        "water": "mmiri",
        "fire": "ọkụ",
        "food": "nri",
        "love": "ihunanya",
        "friend": "enyi",
        "tree": "osisi",
        "child": "nwa",
        "earth": "ụwa",
        "heaven": "eluigwe",
        "river": "osimiri",
        "stone": "nkume",
        "market": "ahịa",
        "sun": "anyanwụ",
        "moon": "ọnwa",
        "rain": "mmiri ozuzo",
        "day": "ụbọchị",
        "night": "abalị",
        "road": "ụzọ",
        "money": "ego",
        "wind": "ifufe",
        "time": "oge",
        "king": "eze",
        "queen": "lolo",
        "song": "abụ"
    },
    "Hausa": {
        "house": "gida",
        "water": "ruwa",
        "fire": "wuta",
        "food": "abinci",
        "love": "soyayya",
        "friend": "aboki",
        "tree": "itace",
        "child": "yaro",
        "earth": "ƙasa",
        "heaven": "sama",
        "river": "kogi",
        "stone": "dutse",
        "market": "kasuwa",
        "sun": "rana",
        "moon": "wata",
        "rain": "ruwan sama",
        "day": "rana",
        "night": "dare",
        "road": "hanya",
        "money": "kuɗi",
        "wind": "iska",
        "time": "lokaci",
        "king": "sarki",
        "queen": "sarauniya",
        "song": "wakar"
    },
    "Idoma": {
        "house": "oje",
        "water": "umi",
        "fire": "uma",
        "food": "edje",
        "love": "unu",
        "friend": "ama",
        "tree": "ugbe",
        "child": "onyi",
        "earth": "ojene",
        "heaven": "ogboma",
        "river": "umoga",
        "stone": "ogbe",
        "market": "ojema",
        "sun": "ameh",
        "moon": "amaona",
        "rain": "omama",
        "day": "okọ",
        "night": "onyagbe",
        "road": "ogbaji",
        "money": "ogwumage",
        "wind": "uchoko",
        "time": "okpagodo",
        "king": "ochi",
        "queen": "onyame",
        "song": "odoma"
    },
    "Tiv": {
        "house": "kaa",
        "water": "saka",
        "fire": "isu",
        "food": "mkan",
        "love": "umenger",
        "friend": "orjor",
        "tree": "kur",
        "child": "or",
        "earth": "kule",
        "heaven": "orvungu",
        "river": "inya",
        "stone": "dyera",
        "market": "iyol",
        "sun": "wang",
        "moon": "kumen",
        "rain": "ngyer",
        "day": "iyol",
        "night": "iwan",
        "road": "angen",
        "money": "doho",
        "wind": "inen",
        "time": "icha",
        "king": "tor",
        "queen": "wan tor",
        "song": "mbati"
    }
}


# Function to invert the dictionary for reverse lookup
def invert_dictionary(dictionary):
    return {v: k for k, v in dictionary.items()}


# Function to search for a word in the selected language
def search_word(language, word):
    if language in tribal_dictionary:
        language_dict = tribal_dictionary[language]
        inverted_dict = invert_dictionary(language_dict)

        if word in language_dict:
            translation = language_dict[word]
            print(f"Word Found: '{word}' in {language} means '{translation}'")
        elif word in inverted_dict:
            translation = inverted_dict[word]
            print(f"Word Found: '{word}' in {language} is translated to English as '{translation}'")
        else:
            print(f"Word '{word}' not found in {language}.")
    else:
        print(f"Language '{language}' not identified .")


def main():
    while True:
        language_options = {
            "1": "Yoruba",
            "2": "Igbo",
            "3": "Hausa",
            "4": "Idoma",
            "5": "Tiv",
            "6": "Exit",
            "7": "Restart"
        }

        print("\nSelect an option:")
        for key, value in language_options.items():
            print(f"{key}: {value}")

        selected_option = input("Enter the number corresponding to your choice: ").strip()

        if selected_option == "6":
            print("Exiting the program.")
            break
        elif selected_option == "7":
            print("Restarting the program.")
            continue
        else:
            selected_language = language_options.get(selected_option)
            if selected_language:
                search_term = input("Enter the word you want to search: ").lower()
                search_word(selected_language, search_term)
            else:
                print("Invalid option selected.")


if __name__ == "__main__":
    main()
