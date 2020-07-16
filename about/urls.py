from django.urls import path
from about import views as about_views

app_name = 'about'

urlpatterns = [
    path('company', about_views.about_company, name='company'),
    path('privacy_policy', about_views.privacy_policy, name='privacy_policy'),
    path('terms_of_use', about_views.terms_of_use, name='terms_of_use'),
    path('contribute', about_views.contribute, name='contribute'),
    path('advertising', about_views.advertising, name='advertising'),
    path('contact', about_views.contact, name='contact'),

]
