from django.shortcuts import render
from .forms import ContactForm


def about_company(request):
    return render(request, 'about/about_company.html')


def privacy_policy(request):
    return render(request, 'about/privacy_policy.html')


def terms_of_use(request):
    return render(request, 'about/terms_of_use.html')


def contribute(request):
    return render(request, 'about/contribute.html')


def advertising(request):
    return render(request, 'about/advertising.html')


def contact(request):
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            post = contact_form.save(commit=False)
            post.save()
            print("Success!")
            return render(request, 'about/about_company.html')
        else:
            return render(request, "about/contact.html", {'form': contact_form})
    else:
        form = ContactForm(None)
        return render(request, 'about/contact.html', {'form': form})
