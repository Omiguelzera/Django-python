from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

from django.template.loader import get_template
from django.template.exceptions import TemplateDoesNotExist
from django.urls import reverse

from .forms import ContactForm, NameForm




def  create(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return HttpResponseRedirect(reverse("contacts:thanks", args=(instance.name,)))
            
    else:
        form = ContactForm()
    return render (request, 'contacts/create.html', {'form': form})

def get_name(request):
    if request.method == "POST":
        form = NameForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            return HttpResponseRedirect(reverse("contacts:thanks", args=(name,)))
    else:
        form = NameForm()

    try:
        get_template('contacts/name.html')  
    except TemplateDoesNotExist:
        print("Template não encontrado no caminho esperado")
        raise

    return render(request, 'contacts/name.html', {'form': form})


def thanks(request, name):
    return render(request, 'contacts/thanks.html', {'name': name})
