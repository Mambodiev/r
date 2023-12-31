from django.views import generic
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Course, Video
from .mixins import CoursePermissionMixin
from django.db.models import Count

class CourseListView(generic.ListView):
    template_name = "content/course_list.html"
    queryset = Course.objects.all()


class CourseDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = "content/course_detail.html"
    queryset = Course.objects.all()


    qs = Video.objects.annotate(num_assets=Count('course'))


    def get_context_data(self, **kwargs):
        context = super(CourseDetailView, self).get_context_data(**kwargs)
        course = self.get_course()
        subscription = self.request.user.subscription
        pricing_tier = subscription.pricing
        subscription_is_active = subscription.status == "active" or subscription.status == "trialing" 
        context.update({
            "has_permission": pricing_tier in course.pricing_tiers.all() and subscription_is_active
        })
        return context
    
    def get_course(self):
        return get_object_or_404(Course, slug=self.kwargs["slug"])
    


class VideoDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = "content/video_detail.html"

    def get_context_data(self, **kwargs):
        context = super(VideoDetailView, self).get_context_data(**kwargs)
        course = self.get_course()
        subscription = self.request.user.subscription
        pricing_tier = subscription.pricing
        subscription_is_active = subscription.status == "active" or subscription.status == "trialing" 
        context.update({
            "has_permission": pricing_tier in course.pricing_tiers.all() and subscription_is_active
        })
        return context

    def get_course(self):
        return get_object_or_404(Course, slug=self.kwargs["slug"])

    def get_object(self):
        video = get_object_or_404(Video, slug=self.kwargs["video_slug"])
        return video

    def get_queryset(self):
        course = self.get_course()
        return course.videos.all()