from django.urls import path
from restapi import views

urlpatterns = [
    path("expenses/", views.Expenselistcreate.as_view(), name="expense-list-create")
]
