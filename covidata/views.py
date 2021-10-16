from django.shortcuts import render
from rest_framework.response import Response
import json
import requests

url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-host': "covid-193.p.rapidapi.com",
    'x-rapidapi-key': "2fd93bfb0bmsh3d7eb27c6fd00b5p1d2767jsncbe3d3e8484c"
    }
response = requests.request("GET", url, headers=headers).json()
def covidata(request):
    a=235
    l=[]
    for i in range(0,a):
        l.append(response['response'][i]['country'])
    if request.method=='POST':
        selectedcountry=request.POST['selectedcountry']
        for x in range(0,235):

            if selectedcountry==response['response'][x]['country']:
                new=response['response'][x]['cases']['new']
                active=response['response'][x]['cases']['active']
                critical=response['response'][x]['cases']['critical']
                recovered=response['response'][x]['cases']['recovered']
                total=response['response'][x]['cases']['total']
                deaths=int(total)-int(recovered)-int(active)




        context={'selectedcountry':selectedcountry,'list':l,'new':new,'active':active,'critical':critical,'recovered':recovered,'total':total,'deaths':deaths}
        return render(request,'data.html',context)
    context={'list':l}
    return render(request,'data.html',context)
# Create your views here.
