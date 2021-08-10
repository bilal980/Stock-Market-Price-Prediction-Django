from django.shortcuts import render, redirect, HttpResponse
from django.conf import settings
from django.contrib import messages
import requests
import csv
from model.data import data
from model.lstm import lstm
import pandas as pd
from tensorflow.keras import models
import pandas as pd
from datetime import date
from datetime import timedelta
from django.conf import settings
import json
from django.contrib.auth.decorators import login_required

# this function return only page of prediction


@login_required(login_url='/')
def prediction_home(request):
    try:
        return render(request, 'trading/tradinghome.html', {'sbar': 'trading'})
    except:
        return HttpResponse("Page Not Found ....")


# this function returned the trained prediction with graph and table
@login_required(login_url='/')
def trained_pred(request):
    try:
        if request.method == 'POST':
            ticker = request.POST.get('ticker')
            pathfile = settings.STATICFILES_DIRS[0] + \
                '/csv/'+'aaple_pred.csv'
            df = pd.read_csv(pathfile)
            json_records = df.reset_index().to_json(orient='records')
            data = []
            data = json.loads(json_records)
            context = {'d': data, 'sbar': 'trading'}
            return render(request, 'trading/trainded_result.html', context)
    except:
        return HttpResponse("Page Not Found ....")


# get prediction of specific that is selected from user
@login_required(login_url='/')
def new_prediction(request):
    try:
        if request.method == 'POST':
            symbol = request.POST.get('symbol')
            from_date = request.POST.get('from')
            to_date = request.POST.get('to')
            predvariable = request.POST.get('variable')
            context = {'symbol': symbol, 'from_date': from_date,
                       'to_date': to_date, 'predvariable': predvariable, 'sbar': 'trading'}
            return render(request, 'trading/model_design.html', context)
    except:
        return HttpResponse("Page Not Found ....")


# show the result after prediction of specific that is selected from user
@login_required(login_url='/')
def new_predicted_result(request):
    try:
        if request.method == 'POST':
            symbol = request.POST.get('symbol')
            from_date, to_date = request.POST.get(
                'from'), request.POST.get('to')
            predvariable = request.POST.get('variable')
            window_size = request.POST.get('window')
            daypredicted = request.POST.get('ahead')
            neurons = request.POST.get('neurons')
            window = int(window_size)
            neurons = int(neurons)
            ahead = int(daypredicted)
            stock = data(symbol, from_date, to_date, predvariable)
            stock.get_dates()
            stock.get_data()
            model = lstm(stock.ts, size=window)
            model.ts_preprocessing(scaler=None)
            model.fit_lstm(units=neurons)
            img = model.predict_lstm(ts=stock.ts, ahead=ahead)
            dtf = model.dtf[pd.notnull(model.dtf["pred"])][["pred"]].reset_index(drop=True)
            dtf['pred'].to_csv(settings.STATICFILES_DIRS[0] +
                               ''+'\\csv\\'+'temp.csv')
            return redirect('/trading/show_pred/')

    except:
        return HttpResponse("Error....Please Try again")


@login_required(login_url='/')
def show_pred(request):
    pathfile = settings.STATICFILES_DIRS[0]+'/csv/'+'temp.csv'
    df = pd.read_csv(pathfile)
    json_records = df.reset_index().to_json(orient='records')
    pred_data = []
    pred_data = json.loads(json_records)
    context = {'sbar': 'trading', 'd': pred_data
               }
    return render(request, "trading/new_predicted.html", context)
