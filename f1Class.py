import requests
import xmltodict
import json
import flag
import emoji
from datetime import datetime


class F1():
    def __init__(self):
        res = requests.get('http://ergast.com/api/f1/current')
        toDict = xmltodict.parse(res.content)
        self.toJson = json.loads(json.dumps(toDict))
        self.listRaces = self.toJson['MRData']['RaceTable']['Race']
        

        with open('F1Twitter\emojis.json', 'r') as emojis:
            self.flags = json.load(emojis)


    def nextRace(self):
        listNextRaces = [key['Date'] for key in self.listRaces]
        for i in listNextRaces:
            data = datetime.strptime(i, "%Y-%m-%d").date()
            if data < datetime.now().date():
                pass
            else:
                return data
    
    
    def value(self):
        listNextRaces = [key['Date'] for key in self.listRaces]
        for i in listNextRaces:
            data = datetime.strptime(i, "%Y-%m-%d").date()
            dataIndex = i
            if data < datetime.now().date():
                pass
            else:
                self.position = listNextRaces.index(dataIndex)
                return self.position
    
    
    def gpName(self):
        listGP = self.toJson['MRData']['RaceTable']['Race'][self.value()]['RaceName']
        return listGP
    

    def nextCircuit(self):
        listCircuits = [key['Circuit']['Location']['Locality'] for key in self.listRaces]
        self.circuit = listCircuits[self.value()]
        return self.circuit
    
    
    def nextCountry(self):
        listCountrys =  [key['Circuit']['Location']['Country'] for key in self.listRaces]
        self.country = listCountrys[self.value()]
        return self.country


    def listFlag(self):
        bandeira_atual = self.flags['paises'][self.nextCountry()]
        return bandeira_atual
    
    
    def regressiveCount(self):
        if datetime.now().date() != self.nextRace():
            self.restDays = self.nextRace() - datetime.now().date()
            return self.restDays.days
        
    def lastGP(self):
        listGP = self.toJson['MRData']['RaceTable']['Race'][self.value() - 1]['RaceName']
        return listGP
         
        
    def message(self):
        if self.regressiveCount() != 0:
            message = f"{flag.flag(self.listFlag())} {self.gpName()} {flag.flag(self.listFlag())}\nFaltam {self.regressiveCount()} dias para a corrida em {self.nextCircuit()}"
            return message
        else:
            message = f"Finalmente chegou o grande dia do {self.gpName()} {flag.flag(self.listFlag())}"
    
    
    def constructorResults(self):
        resConstructor = requests.get(f'https://ergast.com/api/f1/2021/{self.value()}/constructorStandings')
        toDictConstructor = xmltodict.parse(resConstructor.content)
        self.jsonConstructor = json.loads(json.dumps(toDictConstructor))
        jsonConstructor = self.jsonConstructor['MRData']['StandingsTable']['StandingsList']['ConstructorStanding']

        text = ""
        for index in range(len(jsonConstructor)):
            text += f"{jsonConstructor[index]['@position']} - {jsonConstructor[index]['Constructor']['Name']} - {jsonConstructor[index]['@points']}\n"
            
        return text
            
            
    def raceResult(self):
        resRace = requests.get(f'https://ergast.com/api/f1/2021/{self.value()}/results')
        toDictResult = xmltodict.parse(resRace.content)
        self.json = json.loads(json.dumps(toDictResult))
        jsonResult = self.json['MRData']['RaceTable']['Race']['ResultsList']['Result']
       
        text = ""
        for index in range(len(jsonResult)):
            text += f"{jsonResult[index]['@position']}° - {jsonResult[index]['Driver']['GivenName']} {jsonResult[index]['Driver']['FamilyName']} - Largando em {jsonResult[index]['Grid']}°\n"
        
        return text
        

    def qualifyResult(self):
        resRace = requests.get(f'https://ergast.com/api/f1/2021/{self.value()}/qualifying')
        toDictResult = xmltodict.parse(resRace.content)
        self.json = json.loads(json.dumps(toDictResult))
        jsonResult = self.json['MRData']['RaceTable']['Race']['QualifyingList']['QualifyingResult']
               
        text = ""
        for index in range(len(jsonResult)):
            if 'Q3' in jsonResult[index]:
                text += f"{jsonResult[index]['@position']}° - {jsonResult[index]['Driver']['GivenName']} {jsonResult[index]['Driver']['FamilyName']} - Q1: {jsonResult[index]['Q1']} - Q2: {jsonResult[index]['Q2']} - Q3: {jsonResult[index]['Q3']}\n"
            elif 'Q2' in jsonResult[index]:
                text += f"{jsonResult[index]['@position']}° - {jsonResult[index]['Driver']['GivenName']} {jsonResult[index]['Driver']['FamilyName']} - Q1: {jsonResult[index]['Q1']} - Q2: {jsonResult[index]['Q2']}\n"
            elif 'Q1' in jsonResult[index]:
                text += f"{jsonResult[index]['@position']}° - {jsonResult[index]['Driver']['GivenName']} {jsonResult[index]['Driver']['FamilyName']} - Q1: {jsonResult[index]['Q1']}\n"
            else:
                text += f"{jsonResult[index]['@position']}° - {jsonResult[index]['Driver']['GivenName']} {jsonResult[index]['Driver']['FamilyName']} - Não fez o qualify\n"
        
        return f"{text}"
        