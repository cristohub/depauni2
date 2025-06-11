from django import forms
from .models import Message

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={
              'class': 'form-control rounded-3 shadow-sm',
                 'placeholder': 'Ingresa tu nombre',
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control rounded-3 shadow-sm',
                'placeholder': 'Ingresa tu apellido',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control rounded-3 shadow-sm ',
                 'placeholder': 'Ej. ejemplo@email.com',
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control  rounded-3 shadow-sm  ',
                'placeholder': 'Ej. +34 600 123 456',
            }),
            'comment': forms.Textarea(attrs={
                'class': 'form-control  rounded-3 shadow-sm ',
                'placeholder': 'Ingresa tu mensaje o comentario',
                'rows': 4,  # para que no sea tan alto
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Mantén requerido True para backend, pero evita validación HTML nativa
        for field_name, field in self.fields.items():
            field.required = True
            field.widget.attrs.pop('required', None)
