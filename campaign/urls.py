from django.urls import path

from .views import *

app_name = 'campaign'

urlpatterns = [
    path('create', CampaignCreateView.as_view(), name='campaign-create'),
    path('details/<uuid:pk>', CampaignDetailView.as_view(), name='campaign-detail'),
    path('<uuid:pk>/donation', DonationView.as_view(), name='campaign-donation'),
    path('campaigns/', CampaignListView.as_view(), name='campaign-list'),
    path('donation/success/', DonationSuccessView.as_view(), name='donation-success'),
    path('campaigns-by-category/<int:pk>/', CampaignsByCategoryListView.as_view(), name='campaigns-by-category'),
    path('stripe/webhook/', stripe_webhook, name='stripe-webhook'),
]
