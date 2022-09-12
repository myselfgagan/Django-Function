from turtle import title
from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = {
            "title",
            "description",
            "price"
        }

    # def clean_title(self, *args, **kwargs):  #validating specific fields
    #     title = self.cleaned_data.get("title")
    #     # if "CFE" in title:
    #     #     return title
    #     # else:
    #     #     raise forms.ValidationError("This is not a valid title")

    #     # this can be used for mutiple validation
    #     if not "CFE" in title:
    #         raise forms.ValidationError("This is not a valid title")
    #     return title

class RawProductForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField()
    price = forms.DecimalField()