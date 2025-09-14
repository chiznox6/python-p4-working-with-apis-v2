import requests
import json


class Search:

    def get_search_results(self):
        search_term = "the lord of the rings"

        search_term_formatted = search_term.replace(" ", "+")
        fields = ["title", "author_name"]
        # formats the list into a comma separated string
        # output: "title,author_name"
        fields_formatted = ",".join(fields)
        limit = 1

        URL = f"https://openlibrary.org/search.json?title={search_term_formatted}&fields={fields_formatted}&limit={limit}"

        response = requests.get(URL)
        return response.content

    def get_search_results_json(self):
        search_term = "the lord of the rings"

        search_term_formatted = search_term.replace(" ", "+")
        fields = ["title", "author_name"]
        fields_formatted = ",".join(fields)
        limit = 1

        URL = f"https://openlibrary.org/search.json?title={search_term_formatted}&fields={fields_formatted}&limit={limit}"
        print(URL)
        response = requests.get(URL)
        return response.json()

    def get_user_search_results(self, search_term):
        search_term_formatted = search_term.replace(" ", "+")
        fields = ["title", "author_name"]
        fields_formatted = ",".join(fields)
        limit = 1

        URL = f"https://openlibrary.org/search.json?title={search_term_formatted}&fields={fields_formatted}&limit={limit}"

        response = requests.get(URL).json()

        if response["docs"]:
            title = response["docs"][0].get("title", "Unknown Title")
            authors = response["docs"][0].get("author_name", ["Unknown Author"])
            response_formatted = f"Title: {title}\nAuthor: {authors[0]}"
        else:
            response_formatted = "No results found."
        return response_formatted


# results = Search().get_search_results()
# print(results)

# results_json = Search().get_search_results_json()
# print(json.dumps(results_json, indent=1))

if __name__ == "__main__":
    search_term = input("Enter a book title: ")
    result = Search().get_user_search_results(search_term)
    print("Search Result:\n")
    print(result)
