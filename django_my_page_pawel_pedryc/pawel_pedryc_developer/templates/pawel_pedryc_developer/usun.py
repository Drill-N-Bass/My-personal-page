class MyEssaysView(View):
    
    def is_stored_essay(self, request, post_id):
        stored_essays = request.session.get("stored_essays")
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
                'my_email': my_email
                # 'saved_for_later': self.is_stored_essay(request, selected_essay.id)
                # "user_feedback": UserFeedback()
            }

        if request.method == 'GET': # handling form submission 3.18.20
            
            if user_agent.is_pc:        
                return render(
                            request,
                            'dev/article-content_pc_tablet.html',
                            context
                            )

            elif user_agent.is_mobile:        
                return render(
                            request,
                            'dev/article-content_mobile.html', {
                            'essay_found': True,
                            'essay_all': selected_essay,
                            'post_tags': selected_essay.tags.all(),  #s9:128 6:00
                            'form': user_feedback,
                            'comment_form': CommentForm(),
                            'my_email': my_email
                            # "user_feedback": UserFeedback()
                        })
            
            elif user_agent.is_tablet:        
                return render(
                            request,
                            'dev/article-content_pc_tablet.html',
                            context
                            )

def post(self, request, slug):
        
        comment_form = CommentForm(request.POST)
        user_feedback = UserFeedback(request.POST) 
        user_agent = get_user_agent(request)

        post = EssayCls.objects.get(slug=slug)
        
        context = {
          "post": post,
          "post_tags": post.tags.all(),
          "comment_form": comment_form,
          'comments': post.comments.all().order_by("-id")
        }
        
        if user_feedback.is_valid(): 
            user_email = user_feedback.cleaned_data['email']
            send_me_message, was_created = SendMeMessage.objects.get_or_create(email=user_email)
            post.guest.add(send_me_message) 
            
            return redirect('confirm-registration', slug=slug)

        if comment_form.is_valid():
          comment = comment_form.save(commit=False)
          comment.post = post
          comment.save()

          return HttpResponseRedirect(reverse("some-path", args=[slug]))  