from django import forms
from .models import correspondencia

class correspondenciaForm(forms.ModelForm):
    class Meta:
        model = correspondencia
        fields = ['destinatario','estado']

    def _init_(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        set.fields['destinatario'].widget.attrs.update({
            'class': 'form-control',
        })

        set.fields['estado'].widget.attrs.update({
            'class': 'form-control',
        })