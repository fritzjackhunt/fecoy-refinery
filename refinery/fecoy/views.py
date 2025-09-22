from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def home(request):
    return render(request, 'refinery/index.html')

def contact(request):
    if request.method == "POST":
        contact_fname = request.POST['fname']
        contact_lname = request.POST['lname']
        contact_email = request.POST['email']
        contact_message = request.POST['message']

        send_mail(
            contact_fname, 
            contact_message,
            contact_email,
            ['essiet.aniekan@yahoo.com'],
            fail_silently = False,
        )


        return render(request, 'refinery/contact.html', {'contact_fname' : contact_fname})


    else:
        return render(request, 'refinery/contact.html')
    

def aboutus(request):
    return render(request, 'refinery/aboutus.html')

def services(request):
    return render(request, 'refinery/services.html')

def terminals(request):
    return render(request, 'refinery/terminals.html')