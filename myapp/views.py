from django.shortcuts import render
from django.template import Context
from sklearn.externals import joblib
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
import pandas as pd
import numpy as np
# Create your views here.

file_address = '/home/anirudh/django1/cricket_predictor/mypro/myapp/serialized_model.sav'
file_address2 = '/home/anirudh/django1/cricket_predictor/mypro/myapp/Ground_Stats.csv'
regressor = joblib.load(file_address)
ground_stats=pd.read_csv(file_address2, header=None, index_col=0, squeeze=True).to_dict()

def HomePageView(request):
    if request.method == 'POST':
        balls_remaining = int(request.POST.get("balls_remaining"))
        wickets_remaining = int(request.POST.get("wickets_remaining"))
        avg_score = int(ground_stats[request.POST.get("venue")])
        pp_balls_rem = int(request.POST.get("pp_balls_rem"))
        cur_runs = int(request.POST.get('cur_runs'))

        wickets_remaining = wickets_remaining ** 3


        pp_balls_rem *= 3
        avg_score *= 3
        cur_runs *= 3

        x_self = np.array([balls_remaining,wickets_remaining,avg_score,pp_balls_rem,cur_runs]).reshape(1,-1)
        runs_pred = int(regressor.predict(x_self)/3)
        return render(request,template_name='resultpage.html',context={'runs_predicted':runs_pred})
        

    ground_names = list(ground_stats.keys())
    group_names=ground_names.sort()
    return render(request,template_name='homepage.html',context={'ground_stats':ground_names})
