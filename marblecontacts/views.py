from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contactmarble
from django.core.mail import send_mail
from django.contrib.auth.models import User


def marbleinquiry(request):
    if request.method == 'POST':
        marble_id = request.POST['marble_id']
        marble_title = request.POST['marble_title']
        user_id = request.POST['user_id']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        customer_need = request.POST['customer_need']
        city = request.POST['city']
        state = request.POST['state']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']


        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contactmarble.objects.all().filter(marble_id=marble_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'You have already made an inquiry about this car. Please wait until we get back to you.')
                return redirect('/marbles/'+marble_id)

        contactmarble = Contactmarble(marble_id=marble_id, marble_title=marble_title, user_id=user_id,
        first_name=first_name, last_name=last_name, customer_need=customer_need, city=city,
        state=state, email=email, phone=phone, message=message)



        contactmarble.save()
        messages.success(request, 'Your request has been submitted, we will get back to you shortly.')
        return redirect('/marbles/'+marble_id)
