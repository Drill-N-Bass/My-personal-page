"""
My views responsible for rendering all 
templates related to pawel_pedryc_developer folder
"""

"""
My views responsible for rendering all 
templates related to pawel_pedryc_developer folder
"""

from django.shortcuts import render, redirect # `redirect` shortcut for `my_essays`` -> `confirm_registration` 3:33:00  # `redirect` shortcut for `my_essays`` -> `confirm_registration` 3:33:00 
# from django.http import HttpResponse
"""
Detect mobile, tablet or Desktop on Django:
https://stackoverflow.com/a/59274447/15372196
https://github.com/selwin/django-user_agents
"""
from django_user_agents.utils import get_user_agent
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import EssayCls, SendMeMessage, VideoObject # `EssayCls, SendMeMessage`: query our db 2:07:00, VideoItem # `EssayCls, SendMeMessage`: query our db 2:07:00

from .forms import UserFeedback # for instantiate our form for rendered templates 3:14:00

from .forms import CommentForm # for comments in each article

# Needed for display log with the error exeption function:
# https://realpython.com/the-most-diabolical-python-antipattern/
import logging

# Create your views here.

def home_view_pawel(request):

    """
    I can add `.order_by` after all(). Method `all()` gives you all objects from class.

    I will slice my query to just the 3 newest posts ie. `[:3]`.
    It won't downgrade performance because it's part of a query,
    in other words: it's not done later after the query all Db. S9:125 4:30
    Using `[-3:]` is not allowed in SQL queries, but I can manipulate slices with
    `order_by` (ascending/descending order).
    """
    essay = EssayCls.objects.all().order_by('-date')[:3]
    video_obj = VideoObject.objects.all()
    user_agent = get_user_agent(request)
    # return HttpResponse('Test')
    if user_agent.is_pc:
        # my_template='mobile_template.html'
        return render(
        request,
        'pawel_pedryc_developer/pawel_pedryc-pc.html',
        {
        'text_content': essay,
        'show_text_content': True,
        'video_content': video_obj

        })
    elif user_agent.is_mobile:
        # my_template='tablet_template.html'
        return render(
        request,
        'pawel_pedryc_developer/pawel_pedryc_mobile.html',
        {
        'text_content': essay,
        'show_text_content': True,
        'video_content': video_obj

        })
    elif user_agent.is_tablet:
        return render(
            request,
            'pawel_pedryc_developer/pawel_pedryc_tablet.html',
            {
            'text_content': essay,
            'show_text_content': True,
            'video_content': video_obj

            })

class MyEssaysView(View):
    def get(self, request, home_view_pawel_slug):
        print("home_view_pawel_slug:", home_view_pawel_slug)
        user_agent = get_user_agent(request)
        selected_essay = EssayCls.objects.get(slug=home_view_pawel_slug)
        user_feedback = UserFeedback() # handling form submission 3.18.20
        
        if user_agent.is_pc:        
            return render(
                request,
                'pawel_pedryc_developer/article-content_pc_tablet.html', 
                {
                    'essay_found': True,
                    'essay_all': selected_essay,
                    'form': user_feedback,
                    'post_tags': selected_essay.tags.all(), #s9:128 6:00
                    'comment_form': CommentForm()
                })

        if user_agent.is_mobile:        
            return render(
                request,
                'pawel_pedryc_developer/article-content_mobile.html', 
                {
                    'essay_found': True,
                    'essay_all': selected_essay,
                    'form': user_feedback,
                    'post_tags': selected_essay.tags.all(), #s9:128 6:00
                    'comment_form': CommentForm()
                })
        
        if user_agent.is_tablet:        
            return render(
                request,
                'pawel_pedryc_developer/article-content_pc_tablet.html', 
                {
                    'essay_found': True,
                    'essay_all': selected_essay,
                    'form': user_feedback,
                    'post_tags': selected_essay.tags.all(), #s9:128 6:00
                    'comment_form': CommentForm()
                })


        elif request.method == 'GET': # handling form submission 3.18.20

            context = {
                'essay_found': True,
                'essay_all': selected_essay,
                'post_tags': selected_essay.tags.all(),
                'form': user_feedback,
                "comment_form": CommentForm(),
                # "user_feedback": UserFeedback() # jeśli mail nie działa to spróbuj to odhaszować
            }
            return render(request, "pawel_pedryc_developer/article-content_mobile.html", context)

    def post(self, request, home_view_pawel_slug):
        
        comment_form = CommentForm(request.POST)
        post = EssayCls.objects.get(slug=home_view_pawel_slug)
        
        """
        The incoming request from Django will have
        a POST property which contains any submitted data
        that might be attached to incoming POST request. # 3:22:00
        """
        user_feedback = UserFeedback(request.POST) 
        if user_feedback.is_valid(): 
            user_email = user_feedback.cleaned_data['email']
            send_me_message, was_created = SendMeMessage.objects.get_or_create(email=user_email) # 3.44.00
            ## v1:
            # send_me_message = user_feedback.save() # v1 problem: user can sign just once 3.41.00
            # v2:
            # user_email = user_feedback.cleaned_data['email'] # `email` key from SendMeMessage model 3.42.21
            """
            Having `user_email` object I can create a `send_me_message` by myself
            I will do so, because if I use `send_me_message` model from models.py instead of this form
            then I won't have control over how it's created. Doing the line of code below,
            I have control over how it's created and I can check
            whether I have added an email before I try to create a new one in db. 
            If I don't have an email in db I can create a new instance in db with the line:
            `send_me_message_new, _ = send_me_message.objects.get_or_create(email=user_email)`.
            I can write, also 
            send_me_message_new, was_created = send_me_message.objects.get_or_create(email=user_email)
            the flag `was_created` tells us whether a new entry was created or not.
            `_` ignore value: `was_created`.
            """
            # send_me_message_new, _ = send_me_message.objects.get_or_create(email=user_email)
            # selected_essay.guest.add(send_me_message_new)
            ## end v2

            post.guest.add(send_me_message) # 3.26.00
            
            return redirect('confirm-registration', home_view_pawel_slug=home_view_pawel_slug) # 3.52.00

        elif comment_form.is_valid():
          comment = comment_form.save(commit=False)
          comment.post = post
          comment.save()

          return HttpResponseRedirect(reverse("essay-path", args=[slug]))  # jak nie działa to albo wpisz slug albo home_view_pawel_slug 

        context = {
          "post": post,
          "post_tags": post.tags.all(),
          "comment_form": comment_form
        }
        return render(request, "pawel_pedryc_developer/article-content_mobile.html", context)






def confirm_registration(request, home_view_pawel_slug):
    contact = EssayCls.objects.get(slug=home_view_pawel_slug)
    user_agent = get_user_agent(request)
    # return render(request, 'pawel_pedryc_developer/registration-success_pc_tablet.html')

    if user_agent.is_pc:
        return render(
            request,
            'pawel_pedryc_developer/registration-success_pc_tablet.html',
        {
            'organizer_email': contact.organizer_email
        })

    elif user_agent.is_mobile:
        return render(
            request,
            'pawel_pedryc_developer/registration-success_mobile.html',
        {
            'organizer_email': contact.organizer_email
        })

    elif user_agent.is_tablet:
        return render(
            request,
            'pawel_pedryc_developer/registration-success_pc_tablet.html',
        {
            'organizer_email': contact.organizer_email
        })


###     For videos - in progress   ###

# def video_main(request):
#     video_obj = VideoObject.object.all()
#     return render(request, 'pawel_pedryc_developer/pawel_pedryc-pc.html', 
#     {
#         'video_obj': video_obj
#     })

# def video_article(request, pk):
#     video_obj = VideoObject.object.get(pk=pk)
#     return render(request, 'pawel_pedryc_developer/article-content_pc_tablet.html', 
#     {
#         'video_obj': video_obj
#     })


###   An old version of essay article - now as `MyEssaysView`   ###


# def my_essays(request, home_view_pawel_slug):
#     # print("print('home_view_pawel_slug'):", home_view_pawel_slug)
#     user_agent = get_user_agent(request)
    
#     try: # first exception model at 2:13:20 # first exception model at 2:13:20
#         selected_essay = EssayCls.objects.get(slug=home_view_pawel_slug) # 2.11.50 Method `get()` gives you one object from class
#         if request.method == 'GET': # handling form submission 3.18.20
#             user_feedback = UserFeedback() # handling form submission 3.18.20
            
#         else:
#             """
#             The incoming request from Django will have
#             a POST property which contains any submitted data
#             that might be attached to incoming POST request. # 3:22:00
#             """
#             user_feedback = UserFeedback(request.POST) 
#             if user_feedback.is_valid():
#                 user_email = user_feedback.cleaned_data['email']
#                 send_me_message, was_created = SendMeMessage.objects.get_or_create(email=user_email) # 3.44.00
#                 ## v1:
#                 # send_me_message = user_feedback.save() # v1 problem: user can sign just once 3.41.00
#                 # v2:
#                 # user_email = user_feedback.cleaned_data['email'] # `email` key from SendMeMessage model 3.42.21
#                 """
#                 Having `user_email` object I can create a `send_me_message` by myself
#                 I will do so, because if I use `send_me_message` model from models.py instead of this form
#                 then I won't have control over how it's created. Doing the line of code below,
#                 I have control over how it's created and I can check
#                 whether I have added an email before I try to create a new one in db. 
#                 If I don't have an email in db I can create a new instance in db with the line:
#                 `send_me_message_new, _ = send_me_message.objects.get_or_create(email=user_email)`.
#                 I can write, also 
#                 send_me_message_new, was_created = send_me_message.objects.get_or_create(email=user_email)
#                 the flag `was_created` tells us whether a new entry was created or not.
#                 `_` ignore value: `was_created`.
#                 """
#                 # send_me_message_new, _ = send_me_message.objects.get_or_create(email=user_email)
#                 # selected_essay.guest.add(send_me_message_new)
#                 ## end v2

#                 selected_essay.guest.add(send_me_message) # 3.26.00
                
#                 return redirect('confirm-registration', home_view_pawel_slug=home_view_pawel_slug) # 3.52.00
        
#         if user_agent.is_pc:        
#             return render(
#                 request,
#                 'pawel_pedryc_developer/article-content_pc_tablet.html', 
#                 {
#                     'essay_found': True,
#                     'essay_all': selected_essay,
#                     'form': user_feedback,
#                     'post_tags': selected_essay.tags.all(), #s9:128 6:00
#                     'comment_form': CommentForm()
#                 })

#         if user_agent.is_mobile:        
#             return render(
#                 request,
#                 'pawel_pedryc_developer/article-content_mobile.html', 
#                 {
#                     'essay_found': True,
#                     'essay_all': selected_essay,
#                     'form': user_feedback,
#                     'post_tags': selected_essay.tags.all(), #s9:128 6:00
#                     'comment_form': CommentForm()
#                 })
        
#         if user_agent.is_tablet:        
#             return render(
#                 request,
#                 'pawel_pedryc_developer/article-content_pc_tablet.html', 
#                 {
#                     'essay_found': True,
#                     'essay_all': selected_essay,
#                     'form': user_feedback,
#                     'post_tags': selected_essay.tags.all(), #s9:128 6:00
#                     'comment_form': CommentForm()
#                 })

#     except Exception as exc:
#         print('Exception error message:', exc) # Test

#         if user_agent.is_pc:
#             return render(
#                 request,
#                 'pawel_pedryc_developer/article-content_pc_tablet.html', 
#                 {
#                     'essay_found': False
#                 })
#                 # 'essay_title': selected_essay.title,
#                 # 'essay_description': selected_essay.description,
#                 # 'essay_prog_language': selected_essay.language

#         elif user_agent.is_mobile:
#             return render(
#                 request,
#                 'pawel_pedryc_developer/article-content_mobile.html', 
#                 {
#                     'essay_found': False
#                 })

#         elif user_agent.is_tablet:
#             return render(
#                 request,
#                 'pawel_pedryc_developer/article-content_pc_tablet.html', 
#                 {
#                     'essay_found': False
#                 })

