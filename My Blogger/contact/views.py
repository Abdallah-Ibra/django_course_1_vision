from django.shortcuts import redirect, render
from django.urls import reverse
from .models import Contact


# Create your views here.
def contact(request):
    
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        
        contact_details = Contact(fname=fname,lname=lname,email=email,subject=subject,message=message)
        contact_details.save()
        
        return redirect(reverse('home:home'))
    
    context = {}
    return render(request,'contact/contact.html',context)