from django.shortcuts import render, redirect #redirect mesaj gonderlienden sonra form yenilenir
from django.urls import reverse_lazy
from django.contrib import messages #form POST edildikden sonra birdefe gorunen mesaj
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
            messages.success(request, 'Müraciətiniz uğurlar qeydə alındı!')#form POST edildikden sonra birdefe gorunen mesaj
            return redirect(reverse_lazy('contact')) #contact name-dir
            #redirect mesaj gonderlienden sonra form yenilenir

    context = {
        'contact_info' : contact_info,
        'form' : form,
    }
    return render(request, 'contact/index.html', context)
