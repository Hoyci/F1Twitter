import requests
import xmltodict
import json
from datetime import datetime

class F1():
    def __init__(self):
        res = requests.get('http://ergast.com/api/f1/current')
        toDict = xmltodict.parse(res.content)
        self.toJson = json.loads(json.dumps(toDict))
        self.listRaces = self.toJson['MRData']['RaceTable']['Race']

        with open('emojis.json', 'r') as emoji:
            self.flags = json.load(emoji)

    def nextRace(self):
        listNextRaces = [key['Date'] for key in self.listRaces]
        for i in listNextRaces:
            data = datetime.strptime(i, "%Y-%m-%d").date()
            dataIndex = i
            if data < datetime.now().date():
                pass
            else:
                self.position = listNextRaces.index(dataIndex)
                return data
    
    def gpName(self):
        listGP = self.toJson['MRData']['RaceTable']['Race'][self.position]['RaceName']
        return listGP
    
    def nextCountry(self):
        listCountrys =  [key['Circuit']['Location']['Country'] for key in self.listRaces]
        self.country = listCountrys[self.position]
        return self.country

    def nextCircuit(self):
        listCircuits = [key['Circuit']['Location']['Locality'] for key in self.listRaces]
        self.circuit = listCircuits[self.position]
        return self.circuit


    def listaBandeiras(self):
        bandeira_atual = self.flags['paises'][self.nextCountry()]
        return bandeira_atual