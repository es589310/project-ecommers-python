from django.shortcuts import render
from .models import ContactInfo
from .forms import AppealingForm


def contact(request):
    # return render(request, 'contact/index.html')
    contact_info = ContactInfo.objects.first()
    form = AppealingForm()
    if request.method == 'POST':
        form = AppealingForm(request.POST)
        if form.is_valid(): #formun düzgün məlumatlarla doldurulub doldurulmadığını yoxluyur = is_valid()
            form.save()
            
    context = {
        'contact_info' : contact_info,
        'form' : form,
    }
    return render(request, 'contact/index.html', context)
