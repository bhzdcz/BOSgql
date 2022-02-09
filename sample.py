import requests
import json
import pandas as pd
from requests.structures import CaseInsensitiveDict

url = 'http://192.168.88.251/graphql'

query = """mutation {
  auth {
    login(username: "root", password: "root") {
      ... on Error {
        message
      }
    }
  }
}"""

session = requests.Session()
s = session.post(url, json={'query': query})

with open('pycookie.txt', 'w') as f:
    json.dump(requests.utils.dict_from_cookiejar(session.cookies), f)

query = """query {
  bos {
    hwid
    hostname
    uptime {
      durationS
    }
    info {
      mode
      version {
        full
      }
    }
  }
  bosminer {
    info {
      summary {
        tunerStatus
        realHashrate {
          mhsAv
        }
        poolStatus
        temperature {
          degreesC
        }
        power {
          limitW
          approxConsumptionW
        }
      }
      poolGroups {
        pools {
          url
          user
          status
        }
      }
      fans {
        speed
      }
      tempCtrl {
        targetC
        hotC
        dangerousC
      }
    }
  }
}"""

headers = CaseInsensitiveDict()
r = requests.post(url, json={'query': query}, cookies=s.cookies)
print(r.text)

json_data = json.loads(r.text)
df_data = json_data['data']
df = pd.DataFrame(df_data)