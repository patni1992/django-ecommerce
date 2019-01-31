from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column,  ButtonHolder, HTML
from .models import Order
from cities_light.models import City

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address',
                  'postal_code', 'city', 'country']
                  

class CustomFieldForm(OrderForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['city'].queryset = City.objects.none()
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('first_name', css_class='form-group col-md-6 mb-0 pr-3'),
                Column('last_name', css_class='form-group col-md-6 mb-0 pl-3'),
                css_class='form-row'
            ),
            'email',
            'address', 
             Row(
                Column('country', css_class='form-group col-md-4 mb-0 pr-3'),
                Column('city', css_class='form-group col-md-4 mb-0 pl-3'),
                Column('postal_code', css_class='form-group col-md-4 mb-0 pl-3'),
                css_class='form-row'
            ),
            ButtonHolder(  
            HTML("<hr class='mb-4'>"),
            HTML("<button class='btn btn-primary btn-lg btn-block' type='submit'> <i class='fa fa-credit-card'></i> Place order</button>") ),
        )

