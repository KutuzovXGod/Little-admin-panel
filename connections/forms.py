from django import forms

from connections.models import Agreements, Connections


class EditAgreementForm(forms.ModelForm):
    class Meta:
        model = Agreements
        fields = '__all__'
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


class EditConnectionsForm(forms.ModelForm):
    class Meta:
        model = Connections
        fields = '__all__'
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
