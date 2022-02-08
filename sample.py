import requests
import json
import pandas as pd
from requests.structures import CaseInsensitiveDict

query = """query {
    characters {
    results {
      name
      status
      species
      type
      gender
    }
  }
}"""

url = 'https://rickandmortyapi.com/graphql/'
headers = CaseInsensitiveDict()
r = requests.post(url, json={'query': query})
print(r.status_code)
print(r.text)

json_data = json.loads(r.text)
df_data = json_data['data']['characters']['results']
df = pd.DataFrame(df_data)