from django import views
from django.shortcuts import render
from video import forms
from video.services import logic, selectors


class Videos(views.View):

    def get(self, request, *args, **kwargs):
        form = forms.UploadForm()
        videos = selectors.video_all()
        return render(request, 'index.html', {'form': form, 'videos': videos})

    def post(self, request, *args, **kwargs):
        form = forms.UploadForm(request.POST, request.FILES)
        if form.is_valid():

            if form.is_file:
                logic.create_video(form.cleaned_data['video'])
            else:
                logic.download_video(form.cleaned_data['video_url'])

            return render(request, 'index.html', {'form': forms.UploadForm(), 'videos': selectors.video_all()})

        return render(request, 'index.html', {'form': form})
