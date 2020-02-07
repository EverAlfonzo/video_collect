from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset
from dal import autocomplete
from django import forms

from videocollect.models import VideoEntrenamiento


class VideoEntrenamientoForm(forms.ModelForm):
    video = forms.URLField()

    class Meta:
        model = VideoEntrenamiento
        fields = '__all__'
        widgets = {
            'signo': autocomplete.ModelSelect2(url='signo-autocomplete')
        }

    def __init__(self, *args, **kwargs):
        super(VideoEntrenamientoForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-video-upload-form'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'
        self.helper.add_input(Submit('submit', 'Submit'))
        self.helper.layout = Layout(
            Fieldset(
                'Subir tu aporte al proyecto',
                'signo',
                'video',
                'video_entrenamiento',
            )
        )
