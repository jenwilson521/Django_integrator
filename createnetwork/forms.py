from django import forms
from .models import NetworkAnalysis
from django.utils import timezone

LOCATIONS = (  
    ('BRO', 'Bronx'),
    ('BRK', 'Brooklyn'),
    ('QNS', 'Queens'),
    ('MAN', 'Manhattan'),
)

class MakeNetworkCommand(forms.ModelForm):
    error_css_class = 'error'
    location = forms.ChoiceField(choices=LOCATIONS, required=True )
    created_date = forms.DateTimeField(initial=timezone.now)
    published_date = forms.DateTimeField(initial=timezone.now) 

    class Meta:
        model = NetworkAnalysis 
        fields = "__all__"
        widgets = {
            'author': forms.TextInput(attrs={'placeholder': 'What\'s your name?'}),
            'email': forms.TextInput(attrs={'placeholder': 'john@example.com'}),
            'analysis_title': forms.TextInput(attrs={'placeholder': 'ex: Metformin_target_network'}),
            'analysis_description': forms.TextInput(attrs={'placeholder': 
                'Investigating disease associations in the Metformin drug network'}),
            'gene_target': forms.TextInput(attrs={'placeholder': 'ex: PRKAB1'}),
            'threshold': forms.TextInput(attrs={'placeholder': 'What score threshold do you want for this network?'}),
             'eQTL':forms.CheckboxInput(attrs={'check_test':'True'}),
             }

