from __future__ import unicode_literals
from django.views.generic import TemplateView,CreateView,ListView,DetailView,FormView
from django.shortcuts import render,redirect
from myapp.forms import GalleryForm,CustomerForm,EmailForm
from myapp.models import Gallery,Customer,Email
from django.conf import settings

# Create your views here.
class HomeView(TemplateView):
	template_name='index.html'
class GalleryView(TemplateView):
	template_name='gallery.html'
class ServicesView(TemplateView):
	template_name='service.html'
class ElementView(TemplateView):
	template_name='element.html'
class AboutView(TemplateView):
	template_name='about.html'
class ContactView(TemplateView):
	template_name='contact.html'
class SuccessView(TemplateView):
	template_name='success.html'

class GallCreateView(CreateView):
    template_name='gall1.html'
    form_class=GalleryForm
    success_url='success'
class GallistView(ListView):
    template_name="gallery.html"
    model=Gallery
    context_object_name="GallistView" 



class EmailView(CreateView):
    template_name='email.html'
    form_class=EmailForm
    success_url='success'



class RegisterCustomer(FormView):
     template_name = 'register.html'
     form_class = CustomerForm
     def get(self,request,*args,**kwargs):
         self.object = None
         form_class = self.get_form_class()
         cust_form = CustomerForm()
         return self.render_to_response(self.get_context_data(form=cust_form))

     def post(self,request,*args,**kwargs):
         self.object = None
         form_class = self.get_form_class()
         cust_form = CustomerForm(self.request.POST, self.request.FILES)
         if (cust_form.is_valid()):
             return self.form_valid(cust_form)
         else:
             return self.form_invalid(cust_form)

     def get_success_url(self, **kwargs):
         return ('success')

     def form_valid(self,cust_form):
         cust_obj = cust_form.save(commit=False)
         cust_obj.save()
         return redirect('/success/')

     def form_invalid(self,cust_form):
         return self.render_to_response(self.get_context_data(form=cust_form))
