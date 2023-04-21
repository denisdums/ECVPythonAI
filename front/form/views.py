from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import requests


@csrf_exempt
def index(request):
    if request.method == "POST":
        r = requests.post('http://127.0.0.1:8000', params=request.POST)
        prediction = r.json()['prediction']
        predictionPercent = int(prediction * 100)

        context = {
            'prediction': prediction,
            'predictionPercent': predictionPercent,
            'energy': request.POST['energy'],
            'valence': request.POST['valence'],
            'acousticness': request.POST['acousticness'],
            'liveness': request.POST['liveness'],
        }
    else:
        context = {
            'prediction': None,
            'energy': 0,
            'valence': 0,
            'acousticness': 0,
            'liveness': 0,
        }

    return render(request, "index.html", context)
