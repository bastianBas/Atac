from django import forms
from Inicio.models import Empleado
from django.forms import ValidationError

class FormEmpleado(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'

    nombre = forms.CharField(min_length=5, max_length=20)
    area = forms.CharField(min_length=5, max_length=20)
    cargo = forms.CharField(required=True)

    def clean_correo(self):
        inputCorreo = self.cleaned_data['correo']
        if inputCorreo.find('@') == -1:
            raise forms.ValidationError("El correo debe contener @")
        return inputCorreo

    