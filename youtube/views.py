from django.shortcuts import render
from django.views.generic.base import View,HttpResponseRedirect,HttpResponse
from youtubeapp.models import Vedio, Comments


class HomeView(View):
    template_name = 'index.html'
    def get(self, request):
        most_recent_videos = Vedio.objects.all().order_by('-id')

        return render(request, self.template_name, {'most_recent_videos': most_recent_videos})
