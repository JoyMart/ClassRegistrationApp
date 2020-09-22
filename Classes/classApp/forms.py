from django.forms import ModelForm
from .models import djangoClasses


class ProductForm(ModelForm):
    class Meta:
        model = djangoClasses
        fields = '__all__'