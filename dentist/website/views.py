from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def home(request):
    return render(request, 'website/home.html', {})

def contact(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

        # send an email
        send_mail(
            message_name, # subject
            message, # message
            message_email, # from email
            ['egorinkas@gmail.com'], # To Email
            )

        return render(request, 'website/contact.html', {'message_name': message_name})

    else:
        return render(request, 'website/contact.html', {})

def about(request):
    return render(request, 'website/about.html', {})

def pricing(request):
    return render(request, 'website/pricing.html', {})

def service(request):
    return render(request, 'website/service.html', {})

def appointment(request):
    if request.method == "POST":
        your_name = request.POST['your-name']
        your_phone = request.POST['your-phone']
        your_email = request.POST['your-email']
        your_address = request.POST['your-address']
        your_schedule = request.POST['your-schedule']
        your_date = request.POST['your-date']
        your_message = request.POST['your-message']

        appointment = 'Name: ' + your_name + '\n Phone: ' + your_phone + '\n Email:' + your_email + '\n Address: ' + your_address + '\n When: ' + your_schedule + '\n Day: ' + your_date + '\n Message: ' + your_message
        
        
        # send an email
        send_mail(     
            'Appointment Request', # subject
            appointment, # message
            your_email, # from email
            ['egorinkas@gmail.com'], # To Email
            )

        return render(request, 'website/appointment.html', {     
            'your_name': your_name,
            'your_phone': your_phone,
            'your_email': your_email,
            'your_address': your_address,
            'your_schedule': your_schedule,
            'your_date': your_date,
            'your_message': your_message,
            })
    else:
        return render(request, 'website/home.html', {})