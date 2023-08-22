from django import forms
from .models import MyData


class CreateDataForm(forms.ModelForm):
    class Meta:
        model = MyData
        # fields = ['name','email','phone','image']
        fields = '__all__'


class UpdateDataForm(forms.ModelForm):
    # image = forms.ImageField(required=False, widget=forms.FileInput(attrs={'style':"display: none;"}))
    class Meta:
        model = MyData
        fields = ['name','email','phone','image']
        widgets = {
            'image' : forms.FileInput(attrs={"required":False,'style':"display: none;"}),
        }
    
    def save(self, commit=True):
        update_form = self.instance
        update_form.name = self.cleaned_data['name']
        update_form.email = self.cleaned_data['email']
        update_form.phone = self.cleaned_data['phone']

        if self.cleaned_data['image']:
            update_form.image = self.cleaned_data['image']
        
        if commit:
            update_form.save()
        return update_form
    