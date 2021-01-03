from django.shortcuts import render

import requests

url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-key': "27da662219mshf15be3a4bdb0873p1e9366jsn121dc6cb5746",
    'x-rapidapi-host': "covid-193.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers).json()

def homePage(request):
    result = int(response['results'])
    mylist = []
    for x in range(0, result):
        mylist.append(response['response'][x]['country'])

    if request.method == "POST":
        selectCountry = request.POST['selectCountry']
        result = int(response['results'])
        for x in range(0, result):
            if selectCountry == response['response'][x]['country']:
                new = response['response'][x]['cases']['new']
                active = response['response'][x]['cases']['active']
                critical = response['response'][x]['cases']['critical']
                recovered = response['response'][x]['cases']['recovered']
                total = response['response'][x]['cases']['total']

                population = response['response'][x]['population']


                deaths = int(total) - int(active) - int(recovered)

                MortalityRate = (round((int(deaths) / int(active) * 100),2))
                MortalityRatePercentage = f'{MortalityRate} %'.format(MortalityRate)

                newDeath = response['response'][x]['deaths']['new']
                tests = response['response'][x]['tests']['total']

        context = {'selectCountry' : selectCountry, 'mylist' : mylist, 'new' : new, 'active' : active, 'critical' : critical, 'recovered' : recovered, 'total' : total, 'deaths' : deaths, 'population': population,'MortalityRatePercentage': MortalityRatePercentage, 'newDeath': newDeath,'tests': tests}
        return render(request, 'covid.html', context)


    context = {'mylist' : mylist}
    return render(request, 'covid.html', context)
