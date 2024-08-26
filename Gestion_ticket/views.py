from rest_framework import viewsets
from .serializers import *
from .models import Ticket

from django.shortcuts import render, redirect
from django.conf import settings
# from paygate.client import PaygateClient 

# Create your views here.
class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

# def process_payment(request):
#     if request.method == 'POST':
#         # Récupérer les informations de paiement depuis le formulaire
#         amount = request.POST['amount']
#         card_number = request.POST['card_number']
#         # ...

#         # Initialiser le client PayGate
#         client = PaygateClient(
#             merchant_id=settings.PAYGATE_MERCHANT_ID,
#             secret_key=settings.PAYGATE_SECRET_KEY
#         )

#         # Effectuer la transaction de paiement
#         response = client.make_payment(
#             amount=amount,
#             card_number=card_number,
#             # Autres paramètres requis
#         )

#         if response.is_successful():
#             # Traiter le paiement réussi
#             return redirect('success_page')
#         else:
#             # Gérer l'échec du paiement
#             return render(request, 'payment_failed.html', {'error': response.error_message})

#     # Afficher le formulaire de paiement
#     return render(request, 'payment_form.html')