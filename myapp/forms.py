from django import forms
from myapp.models import Gallery,Customer,Email

class CustomerForm(forms.ModelForm):
     class Meta:
        model = Customer
        exclude = ('create_date',)


class GalleryForm(forms.ModelForm):
	class Meta:
		model=Gallery
		exclude=('create_date',)

class EmailForm(forms.ModelForm):
    class Meta:
        model=Email
        exclude=('create_date',)

			
        
