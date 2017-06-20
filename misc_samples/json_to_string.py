json_raw = '''{
  "Find": {
    "Status": "Success",
    "Result": [
      {
        "ParkingSpot": {
          "sid": "Altiux__SPTP00000001__PS00000009",
          "boundary": {
            "geoPoint": [
              {
                "longitude": 77.69260212779045,
                "latitude": 12.933392076321773
              },
              {
                "longitude": 77.69260212779045,
                "latitude": 12.933925
              },
              {
                "longitude": 77.69211664795876,
                "latitude": 12.933925
              },
              {
                "longitude": 77.69211664795876,
                "latitude": 12.933392076321773
              }
            ]
          },
          "state": {
            "total": 6,
            "occupied": 2
          },
          "opParams": {
            "zoneType": "ValidParking"
          },
          "providerDetails": {
            "providerId": "w2cr4d45ybzfne6tpsndwjnh4z3ytqwm",
            "provider": "altiux"
          },
          "operatedBy": "altiux",
          "hierId": "parking_hierarchy_sid",
          "label": "CIMSimulated2",
          "demarcated": true
        }
      }
    ]
  }
}'''

json_raw = '''{
  "_links": [
    {
      "self": "http://api.football-data.org/alpha/soccerseasons/354/teams"
    },
    {
      "soccerseason": "http://api.football-data.org/alpha/soccerseasons/354"
    }
  ],
  "count": 20,
  "teams": [
    {
      "_links": {
        "fixtures": {
          "href": "http://api.football-data.org/alpha/teams/62/fixtures"
        },
        "players": {
          "href": "http://api.football-data.org/alpha/teams/62/players"
        },
        "self": {
          "href": "http://api.football-data.org/alpha/teams/62"
        }
      },
      "code": "EFC",
      "crestUrl": "http://upload.wikimedia.org/wikipedia/de/f/f9/Everton_FC.svg",
      "name": "Everton FC",
      "shortName": "Everton",
      "squadMarketValue": "179,250,000 "
    }
  ]
}'''

#~ json_raw = '''{

#~ }'''

import json
from pprint import pprint

json_dict = json.loads(json_raw)

# pprint(json_dict)

#~ pprint(json_dict['teams'])

#~ print '-'*10

#~ for team in json_dict['teams']:
    #~ x = team
    #~ print type(x)
    #~ print team['_links']['fixtures']['href']

#~ for idx1 in json_dict['Find']['Result'][0]['ParkingSpot'].iteritems():
    #~ print ">>>"
    #~ print type(idx1[1])
    #~ print idx1[1]
    #~ if isinstance(idx1[1],list): print idx1[1][0]
        #~ for index,item in enumerate(idx1[1]):

#~ def reccursive(idx1, prefix=""):
    #~ if isinstance(idx1[1],dict):
        #~ for idx2 in idx1[1].iteritems():
            #~ if isinstance(idx2[1],list) or isinstance(idx2[1],dict): 
                #~ reccursive(idx2,idx1[0]+"."+idx2[0]+".")
            #~ else:
                #~ print("[DICT] {}={}".format(prefix+idx1[0]+"."+idx2[0],idx2[1]))
    #~ elif isinstance(idx1[1],list):
        #~ for index,item in enumerate(idx1[1]):
            #~ for idx3 in item.iteritems():
                #~ if isinstance(idx3[1],list) or isinstance(idx3[1],dict): 
                    #~ reccursive(idx3,idx1[0]+"."+str(index)+"."+idx3[0]+".")
                #~ else:
                    #~ print("[LIST] {}={}".format(prefix+str(index)+"."+idx3[0],idx3[1]))
    #~ else:
        #~ print("[str] {}={}".format(prefix+idx1[0],idx1[1]))

def reccursive(idx1, prefix=""):
    if isinstance(idx1[1],dict):
        for idx2 in idx1[1].iteritems():
            reccursive(idx2,prefix+idx1[0]+".")
    elif isinstance(idx1[1],list):
        for index,item in enumerate(idx1[1]):
            for idx3 in item.iteritems():
                reccursive(idx3,prefix+idx1[0]+"."+str(index)+".")
    else:
        print("[str] {}={}".format(prefix+idx1[0],idx1[1]))

#~ for idx1 in json_dict['Find']['Result'][0]['ParkingSpot'].iteritems():
for idx1 in json_dict.iteritems():
    reccursive(idx1)
