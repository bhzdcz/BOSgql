#!/bin/bash
echo "Enter your device IP: "
read device_ip
echo ""

curl --cookie-jar shcookie.txt "http://$device_ip/graphql" \
  -X POST \
  -H 'content-type: application/json' \
  --data '{"query":"mutation ($username: String!, $password: String!) {\n  auth {\n    login(username: $username, password: $password) {\n      ... on Error {\n        message\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n","variables":{"username":"root","password":"root"}}'


curl -b shcookie.txt "http://$device_ip/graphql" \
  -X POST \
  -H 'content-type: application/json' \
  --data '{"query": "{   bos {  hwid  hostname  uptime {    durationS  }  info {    mode    version {      full    }  }} bosminer {  info {    summary {      tunerStatus      realHashrate {        mhsAv      }      poolStatus      temperature {        degreesC      }      power {        limitW        approxConsumptionW      }    }    poolGroups {      pools {        url        user       status      }    }    fans {      speed    }    tempCtrl {      targetC      hotC      dangerousC    }  }} }"}'