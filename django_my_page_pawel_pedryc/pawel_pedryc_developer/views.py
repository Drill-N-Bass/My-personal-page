from django.shortcuts import render, redirect
# from django.http import HttpResponse

from .models import EssayCls, SendMeMessage

from .forms import UserFeedback

# Needed for display log with the error exeption function:
# https://realpython.com/the-most-diabolical-python-antipattern/
import logging

# Create your views here.


def home_view_pawel(request):
    essay = EssayCls.objects.all()

    # return HttpResponse('Test')
    return render(
        request,
        'pawel_pedryc_developer/pawel_pedryc.html',
        {
        'text_content': essay,
        'show_text_content': True
        })


def my_essays(request, home_view_pawel_slug):
    # print("print('home_view_pawel_slug'):", home_view_pawel_slug)

    try:
        selected_essay = EssayCls.objects.get(slug=home_view_pawel_slug)
        if request.method == 'GET': # handling form submission 3.18.20
            user_feedback = UserFeedback() # handling form submission 3.18.20
            
        else:
            user_feedback = UserFeedback(request.POST)
            if user_feedback.is_valid():
                user_email = user_feedback.cleaned_data['email']
                send_me_message, was_created = SendMeMessage.objects.get_or_create(email=user_email) # 3.44.00
                # send_me_message = user_feedback.save() # 3.41.00
                selected_essay.guest.add(send_me_message) # 3.26.00
                return redirect('confirm-registration', home_view_pawel_slug=home_view_pawel_slug) # 3.52.00
                
        return render(
            request,
            'pawel_pedryc_developer/learning-programming-is-a-long-run-not-a-sprint.html', 
            {
                'essay_found': True,
                'essay_all': selected_essay,
                'form': user_feedback
            })

    except Exception as exc:
        print('Exception error message:', exc) # Test
        return render(
            request,
            'pawel_pedryc_developer/learning-programming-is-a-long-run-not-a-sprint.html', 
            {
                'essay_found': False
            })
            # 'essay_title': selected_essay.title,
            # 'essay_description': selected_essay.description,
            # 'essay_prog_language': selected_essay.language


def confirm_registration(request, home_view_pawel_slug):
    contact = EssayCls.objects.get(slug=home_view_pawel_slug)
    # return render(request, 'pawel_pedryc_developer/registration-success.html')
    return render(
        request,
        'pawel_pedryc_developer/registration-success.html',
    {
        'organizer_email': contact.organizer_email
    })