from django.shortcuts import render
import requests
 #used to send http requests to and from api
API_KEY = 'ad6b50ee9fcd4c98b7ec05eef90c80a9'

# Create your views here.

def home(request):
    country = request.GET.get('country')  # get the country from user from home.html
    category = request.GET.get('category')

    if country:
        url = f'https://newsapi.org/v2/top-headlines?country={country}&apikey={API_KEY}'
        response = requests.get(url)  # get the response from the api
        data = response.json() #convert to the json format
        articles = data['articles']
    
    else:
        url = f'https://newsapi.org/v2/top-headlines?category={category}&apikey={API_KEY}'
        response = requests.get(url)  # get the response from the api
        data = response.json() #convert to the json format
        articles = data['articles']




    context = {
        'articles' : articles
    }

    return render(request,'newsAPI/home.html',context)



