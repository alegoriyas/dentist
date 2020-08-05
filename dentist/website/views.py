from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'website/home.html', {})

def contact(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

        return render(request, 'website/contact.html', {'message_name': message_name})

    else:
        return render(request, 'website/contact.html', {})