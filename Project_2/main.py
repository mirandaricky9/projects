# Testing an Escape From Tarkov API

# Goals with mini-project 
# Create a website that'll display items searched using graphql 
import requests

def run_query(query):
    response = requests.post('https://api.tarkov.dev/graphql', json={'query': query})
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Query failed to run by returning code of {}. {}".format(response.status_code, query))


new_query = """
{
    items(name: "m855a1") {
        id
        name
        shortName
        basePrice
        avg24hPrice
    }
}
"""

result = run_query(new_query)
print(result)
