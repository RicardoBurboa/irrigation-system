from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Censado


@login_required
def graficas(request):

    censo = Censado.objects.all()
    num_riego_no = Censado.objects.filter(status_riego=1).count()
    num_riego_si = Censado.objects.filter(status_riego=2).count()
    num_anomalia_no = Censado.objects.filter(anomalia=1).count()
    num_anomalia_si = Censado.objects.filter(anomalia=2).count()

    return render(request, 'censado/graficas.html', {'censo': censo,
        'riego_si': num_riego_si,
        'riego_no': num_riego_no,
        'anomalia_si': num_anomalia_si,
        'anomalia_no': num_anomalia_no})


@login_required
def int_artificial(request):

    censo = Censado.objects.all()
    
    return render(request, 'censado/int_artificial.html', {'censo': censo})


    #POR SI LO QUIERO HACER UNO POR UNO

    #dests = Destination.objects.all()

    #return render(request, "index.html", {'dests': dests})

    # dest1 = Destination()
    # dest1.name = 'Mumbai'
    # dest1.desc = 'The City That Never Sleeps'
    # dest1.img = 'destination_1.jpg'
    # dest1.price = 700
    # dest1.offer = False

    # dest2 = Destination()
    # dest2.name = 'Mexico City'
    # dest2.desc = 'Capital City of Mexico'
    # dest2.img = 'destination_2.jpg'
    # dest2.price = 1500
    # dest2.offer = True

    # dest3 = Destination()
    # dest3.name = 'Guadalajara'
    # dest3.desc = 'The City of Tequila'
    # dest3.img = 'destination_3.jpg'
    # dest3.price = 1200
    # dest3.offer = True

    # dests = [dest1, dest2, dest3]

    # return render(request, 'index.html', {'dests': dests})