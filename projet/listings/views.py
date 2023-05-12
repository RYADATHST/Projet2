from django.shortcuts import render
from rest_framework.views import APIView
from listings.serializer import DomainSerializer
from listings.form import DomainForm
from listings.models import Domain
from rest_framework.response import Response
import dnstwist





class DomainAPIView(APIView):
    def get(self, request):
        form = DomainForm()
        return render(request, 'listings/api.html', {'form': form})

    def post(self, request):
        form = DomainForm(request.POST)
        if form.is_valid():
            domaine_name= form.cleaned_data.get('nom')
            data = dnstwist.run(domain=domaine_name, registered=True, format='null')

            return Response(data)
        else:
            return Response(form.errors)
































