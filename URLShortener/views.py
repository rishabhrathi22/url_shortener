from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.

from .models import *

def example_view(request, name):
    data = {
        "first_name": name
    }

    return render(request, 'index.html', data)


def shorten_url(request):
    context = {
        "submitted": False
    }

    if request.method == "POST":
        user_data = request.POST

        long_url = user_data['longurl']
        custom_name = user_data['custom_name']

        # push to the db
        try:
            obj = URL_table(long_url = long_url, custom_name = custom_name)
            obj.save()

            data = {
                "longurl": obj.long_url,
                "shorturl": obj.custom_name,
                "date": obj.created_date,
                "clicks": obj.visit_count
            }

            context["submitted"] = True
            context["data"] = data

            return HttpResponse("Saved to db")
        except Exception as e:
            print(e)
            return HttpResponse("The custom name is already taken")

    return render(request, 'home.html', context)


def redirect_url(request, custom_name):
    try:
        row = URL_table.objects.get(custom_name = custom_name)
        long_url = row.long_url
        row.visit_count += 1
        row.save()
        return redirect(long_url)
    except:
        return HttpResponse("This custom name has no mapping")