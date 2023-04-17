"""
My views responsible for rendering all 
templates related to pawel_pedryc_developer folder
"""

"""
My views responsible for rendering all 
templates related to pawel_pedryc_developer folder
"""

from django.shortcuts import render, redirect, get_object_or_404 # `redirect` shortcut for `my_essays`` -> `confirm_registration` 3:33:00  # `redirect` shortcut for `my_essays`` -> `confirm_registration` 3:33:00 
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

from .models import EssayCls, SendMeMessage, VideoObject, MyEmail, Comment # `EssayCls, SendMeMessage`: query our db 2:07:00, VideoItem # `EssayCls, SendMeMessage`: query our db 2:07:00

from .forms import UserFeedback # for instantiate our form for rendered templates 3:14:00

from .forms import CommentForm # for comments in each article

from django.template.loader import get_template # used in part: # Show videos for essay on the index page # https://www.fullstackpython.com/django-template-loader-get-template-examples.html

# Needed for display log with the error exeption function:
# https://realpython.com/the-most-diabolical-python-antipattern/
import logging

# Libraries needed for the Skype API:
from bs4 import BeautifulSoup
import requests 
from skpy import Skype

from os import getenv # s15e214 00:30

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

    try: # https://stackoverflow.com/a/3090342/15372196
        my_email = MyEmail.objects.latest('date')
    except MyEmail.DoesNotExist:
        my_email = str("email not available, sorry")

    """
    # Show videos for essay on the index page
    Below I want to get all related videos for particular essay
    that will be display in main/index page.
    Because I would end up with two `context` objects that 
    would be needed to define in my template's `for loop`
    instead of that I will zip both objects: `essay` and `video_essay`.
    Inspired by: https://stackoverflow.com/a/12684697/15372196
    """
    video_essay = [vid.video.all() for vid in essay]
    # load_essay_video = loader.get_template('django_my_page_pawel_pedryc\pawel_pedryc_developer\templates\pawel_pedryc_developer\pawel_pedryc-pc.html')

    """
    If someone wonders how I set video preview in my index/home page, 
    I've redirected my video objects from VideoObject class(models.py) 
    directly in my template: "essay_items".

    Another way to do it is to use `select_related()` or `prefetch_related()`
    A good discussion about usage here: https://stackoverflow.com/questions/31237042/whats-the-difference-between-select-related-and-prefetch-related-in-django-orm
    """

    context = {
                'text_content': essay,
                'show_text_content': True,
                'hangman_icon': True,
                'my_email': my_email
                # 'video_essay': video_essay
                # 'zipped_videos_essay': zip(essay, list(video_essay))
                # 'essay_videos': video_obj.video_item_url
                }
    if user_agent.is_pc:
        # my_template='mobile_template.html'
        return render(
                    request,
                    'pawel_pedryc_developer/pawel_pedryc-pc.html',
                    context
                    )

    elif user_agent.is_mobile:
        # my_template='tablet_template.html'
        return render(
                    request,
                    'pawel_pedryc_developer/pawel_pedryc_mobile.html',
                    {
                    'text_content': essay,
                    'show_text_content': True,
                    'hangman_icon': False,
                    'my_email': my_email
                    # 'video_obj': video_obj
                    })
    elif user_agent.is_tablet:
        return render(
                    request,
                    'pawel_pedryc_developer/pawel_pedryc_tablet.html',
                    context)


def all_essays(request):

    """
    I can add `.order_by` after all(). Method `all()` gives you all objects from class.
    """
    essay = EssayCls.objects.all().order_by('-date')
    video_obj = VideoObject.objects.all()
    user_agent = get_user_agent(request)

    try: # https://stackoverflow.com/a/3090342/15372196
        my_email = MyEmail.objects.latest('date')
    except MyEmail.DoesNotExist:
        my_email = str("email not available, sorry")

    context = {
            'all_text_content': essay,
            'show_text_content': True,
            'video_content': video_obj,
            'hangman_icon': True,
            'my_email': my_email
            }
    # return HttpResponse('Test')

    if user_agent.is_pc:
        # my_template='mobile_template.html'
        return render(
                    request,
                    'pawel_pedryc_developer/pawel_pedryc-pc.html',
                    context
                    )

    elif user_agent.is_mobile:
        # my_template='tablet_template.html'
        return render(
                    request,
                    'pawel_pedryc_developer/pawel_pedryc_mobile.html',
                    {
                    'text_content': essay,
                    'show_text_content': True,
                    'video_content': video_obj,
                    'hangman_icon': False,
                    'my_email': my_email
                    })
    elif user_agent.is_tablet:
        return render(
                    request,
                    'pawel_pedryc_developer/pawel_pedryc_tablet.html',
                    context)

class MyEssaysView(View):
    
    



    def is_stored_essay(self, request, post_id):
        """
        Removing saved essays in session s14e200:
        """
        stored_essays = request.session.get("stored_essays")
        print("post_id: ", post_id) # Test
        if stored_essays is not None:
            is_saved_for_later = post_id in stored_essays
        else:
            is_saved_for_later = False
        return is_saved_for_later

    def get(self, request, slug):
        # print("GET: slug:", slug) # test
        user_agent = get_user_agent(request)
        selected_essay = EssayCls.objects.get(slug=slug)
        user_feedback = UserFeedback() # handling form submission 3.18.20 

        # # Check the session content test:
        # stored_essays = request.session.get("stored_essays")
        # print("stored_essays: ", stored_essays)  
        

        try: # https://stackoverflow.com/a/3090342/15372196
            my_email = MyEmail.objects.latest('date')
        except MyEmail.DoesNotExist:
            my_email = str("email not available, sorry")
        
        context = {
                'essay_found': True,
                'essay_all': selected_essay,
                'post_tags': selected_essay.tags.all(),  #s9:128 6:00
                'form': user_feedback,
                'comment_form': CommentForm(),
                'hangman_icon': True,
                'comments': selected_essay.comments.all().order_by("-id"), # s14:194 1:00
                'my_email': my_email,
                'saved_for_later': self.is_stored_essay(request, selected_essay.id),
                'essay_videos': selected_essay.video.all()
                # "user_feedback": UserFeedback()
            }

        if request.method == 'GET': # handling form submission 3.18.20
            
            if user_agent.is_pc:        
                return render(
                            request,
                            'pawel_pedryc_developer/article-content_pc_tablet.html',
                            context
                            )

            elif user_agent.is_mobile:        
                return render(
                            request,
                            'pawel_pedryc_developer/article-content_mobile.html', {
                            'essay_found': True,
                            'essay_all': selected_essay,
                            'post_tags': selected_essay.tags.all(),  #s9:128 6:00
                            'form': user_feedback,
                            'comment_form': CommentForm(),
                            'hangman_icon': False,
                            'comments': selected_essay.comments.all().order_by("-id"), # s14:194 1:00
                            'my_email': my_email,
                            'saved_for_later': self.is_stored_essay(request, selected_essay.id),
                            'essay_videos': selected_essay.video.all()
                            # "user_feedback": UserFeedback()
                        })
            
            elif user_agent.is_tablet:        
                return render(
                            request,
                            'pawel_pedryc_developer/article-content_pc_tablet.html',
                            context
                            )



    def post(self, request, slug):
        
        """
        The incoming request from Django will have
        a POST property which contains any submitted data
        that might be attached to incoming POST request. # 3:22:00
        """
        # print("POST: slug:", slug) # test
        
        comment_model = Comment.objects.all()
        comment_form = CommentForm(request.POST)
        user_feedback = UserFeedback(request.POST) 
        user_agent = get_user_agent(request)

        post = EssayCls.objects.get(slug=slug)

        context = {
          "post": post,
          "post_tags": post.tags.all(),
          "comment_form": comment_form,
          'comments': post.comments.all().order_by("-id"), # s14:194 1:00
          'saved_for_later': self.is_stored_essay(request, post.id)
        }
        
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
            
            return redirect('confirm-registration', slug=slug) # 3.52.00

        if comment_form.is_valid():
            comment = comment_form.save(commit=False) # s14:192 10:00
            comment.post = post # `post` is a tittle of post/essay
            comment.save()
            # comment output: Comment object (id)
            # str(type(comment) output: <class 'pawel_pedryc_developer.models.Comment'>
        
           # Skype Api:
            sk = Skype(getenv("SKYPE_LOGIN"), getenv("SKYPE_PASS")) # connect to Skypesk.user

            # Important doc about authentication: https://skpy.t.allofti.me/background/authentication.html
            # about this authentication (bottom of a page): https://github.com/Terrance/SkPy.docs/blob/master/guides/login.rst
            sk.conn.liveLogin(getenv("SKYPE_LOGIN"), getenv("SKYPE_PASS"))

            sk.conn

            
            ch = sk.contacts["live:.cid.50398699ab2d0b0b"].chat
            
            # This part works but shows only column names for comment form:
            # msg = ch.sendMsg(
            #     " ".join(str(comment_form).split()), # https://stackoverflow.com/a/1546251/15372196
            #     rich=True) # skype needs html line breaks: "rich=True"
            
            user_name = comment_model[comment.id - 1].user_name
            user_email = comment_model[comment.id - 1].user_email
            user_text = comment_model[comment.id - 1].text

            comment_list = [user_name, user_email, user_text]
            skype_comment = '\n'.join(comment_list) # https://bobbyhadz.com/blog/python-list-join-with-newline

            msg = ch.sendMsg(
                skype_comment,
                rich=True # skype needs html line breaks: "rich=True"
                ) 

            msg

            

            return HttpResponseRedirect(reverse("essay-path", args=[slug]))  # I use `reverse` to not violate the DRY (Don't Repeat Yourself) principle s14:192 6:10

        # if user_agent.is_pc:
        #     return render(request, "pawel_pedryc_developer/article-content_pc_tablet.html", context)

        # elif user_agent.is_mobile:
        #     return render(request, "pawel_pedryc_developer/article-content_mobile.html", context)






def confirm_registration(request, slug):
    # contact = EssayCls.objects.get(slug=slug)
    user_agent = get_user_agent(request)
    # return render(request, 'pawel_pedryc_developer/registration-success_pc_tablet.html')

    try: # https://stackoverflow.com/a/3090342/15372196
        my_email = MyEmail.objects.latest('date')
    except MyEmail.DoesNotExist:
        my_email = str("email not available, sorry")

    if user_agent.is_pc:
        return render(
            request,
            'pawel_pedryc_developer/registration-success_pc_tablet.html',
        {
            'my_email': my_email,
            'different_base_css': True
        })

    elif user_agent.is_mobile:
        return render(
            request,
            'pawel_pedryc_developer/registration-success_mobile.html',
        {
            'my_email': my_email,
            'different_base_css': True
        })

    elif user_agent.is_tablet:
        return render(
            request,
            'pawel_pedryc_developer/registration-success_pc_tablet.html',
        {
            'my_email': my_email,
            'different_base_css': True
        })

class ReadLaterView(View):

    """
    About `get` - I want to dive into the session, get the stored essays and send
    those essays to the template, however not just the ids,
    which is the data sotred in this session,
    but the hole stored objects. I need to, first of all, get my stored essays.
    It might be none, or a list I'm looking for. Then I want to check is it none. 
    if list extist but it has no items then this will find it: `len(stored_essays) == 0`
    With no essays in list, I want to rederict user to information about that `context["has_essays"] = False`.
    If there are essays in the list, then I want to  reach a database and fetch data for there. 
    Having a EssayCls model I want to get objects, but not all. 
    I want to filter objects for the ids stored in sored essays.
    It can be done with a special modifier `id__in=stored_essays` #s14e198 6:00
    """
    
    def get(self, request):
        stored_essays = request.session.get("stored_essays")
        user_agent = get_user_agent(request)
        # print('stored_essaysline 305:', stored_essays) # test

        try: # https://stackoverflow.com/a/3090342/15372196
            my_email = MyEmail.objects.latest('date')
        except MyEmail.DoesNotExist:
            my_email = str("email not available, sorry")

        context = {}

        if stored_essays is None or len(stored_essays) == 0:
            context["essays"] = []
            context["has_essays"] = False
            context["my_email"] = my_email
            context["hangman_icon"] = True
            context["different_base_css"] = True
            
            
            if user_agent.is_pc:
                return render(request, "pawel_pedryc_developer/stored-essays_pc_tablet.html", context)

            elif user_agent.is_mobile:
                context["hangman_icon"] = False

                return render(request, "pawel_pedryc_developer/stored-essays_mobile.html", context)
        else:
            essays_read_later = EssayCls.objects.filter(id__in=stored_essays)
            context["essays"] = essays_read_later
            context["has_essays"] = True
            context["my_email"] = my_email
            context["hangman_icon"] = True
            context["different_base_css"] = True
          
        if user_agent.is_pc:
            return render(request, "pawel_pedryc_developer/stored-essays_pc_tablet.html", context)
            
        elif user_agent.is_mobile:
            context["hangman_icon"] = False

            return render(request, "pawel_pedryc_developer/stored-essays_mobile.html", context)


    def post(self, request):
        stored_essays = request.session.get("stored_essays")
        # print('stored_essays line 333:', stored_essays) # Test
        if stored_essays is None:
            stored_essays = []

        post_id = int(request.POST["post_id"])
        # print('stored_essays line 338:', stored_essays)  # Test

        if post_id not in stored_essays:
            stored_essays.append(post_id)
            # print('stored_essays line 341:', stored_essays)  # Test
        else:
            stored_essays.remove(post_id) # s14e200 5:00
            # print('stored_essays line 344:', stored_essays)  # Test
            request.session["stored_essays"] = stored_essays #s14e198 11:30
            return redirect(request.META['HTTP_REFERER']) # redirect to the same page: https://stackoverflow.com/a/26798686/15372196

        request.session["stored_essays"] = stored_essays #s14e198 11:30
        # print('stored_essays line 348:', stored_essays)  # Test
        
        return HttpResponseRedirect("/")


        


###     For videos - in progress   ###
# https://www.youtube.com/watch?v=dGF1x14QNGA

def video_main(request):
    video_obj = VideoObject.object.all()
    return render(request, 'pawel_pedryc_developer/pawel_pedryc-pc.html', 
    {
        'video_obj': video_obj
    })

def video_article(request, pk):
    video_obj = VideoObject.object.get(pk=pk)
    return render(request, 'pawel_pedryc_developer/article-content_pc_tablet.html', 
    {
        'video_obj': video_obj
    })


# terminal shell for SQL: s14:192 12:10

###   An old version of essay article - now as `MyEssaysView`   ###


# def my_essays(request, slug):
#     # print("print('slug'):", slug)
#     user_agent = get_user_agent(request)
    
#     try: # first exception model at 2:13:20 # first exception model at 2:13:20
#         selected_essay = EssayCls.objects.get(slug=slug) # 2.11.50 Method `get()` gives you one object from class
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
                
#                 return redirect('confirm-registration', slug=slug) # 3.52.00
        
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

