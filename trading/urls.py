from django.urls import path
from . import views


urlpatterns = [
    path('', views.prediction_home, name='prediction_home'),
    path('model_design/', views.new_prediction, name='model_design'),
    path('new_prediction_result/', views.new_predicted_result,
         name='new_predicton_result'),
    path('trained_model/', views.trained_pred, name='trained_model'),
    path('show_pred/', views.show_pred, name='show_pred'),
]
