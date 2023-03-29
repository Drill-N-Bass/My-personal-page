class MyEssaysView(View):
    
    def get(self, request, slug):
        user_agent = get_user_agent(request)
        selected_essay = EssayCls.objects.get(slug=slug)
        user_feedback = UserFeedback() # handling form submission 3.18.20 

        context = {
                'essay_found': True,
                'essay_all': selected_essay,
                'post_tags': selected_essay.tags.all(), 
                'comments': selected_essay.comments.all().order_by("-id"), 
                'essay_videos': selected_essay.video.all()
            }

        if request.method == 'GET':
            
            if user_agent.is_pc:        
                return render(
                            request,
                            'dev/article-content_pc_tablet.html',
                            context
                            )