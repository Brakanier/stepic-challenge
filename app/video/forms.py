from django import forms
from django.core import exceptions, validators
from video import validators as video_validators


class UploadForm(forms.Form):
    video = forms.FileField(
        required=False,
        validators=(
            validators.FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv']),
            video_validators.size_validator
        )
    )
    video_url = forms.CharField(max_length=256, required=False)

    def clean(self):
        cleaned_data = super(UploadForm, self).clean()
        video = cleaned_data.get('video')
        video_url = cleaned_data.get('video_url')

        if not video and not video_url:
            raise exceptions.ValidationError('Select video file or put video url')

    @property
    def is_file(self) -> bool:
        return bool(self.cleaned_data.get('video'))
