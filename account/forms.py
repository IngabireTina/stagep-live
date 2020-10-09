from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.forms import ModelForm


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
            'first_name',
            'last_name',
            'address',
            'phone_number',
            'profile_pic',
            'is_sectorIT'

        ]

        # def save(self, commit=True):
        #     user = super(CreateUserForm, self).save(commit=False)
        #     user.first_name = self.cleaned_data['first_name']
        #     user.last_name = self.cleaned_data['last_name']
        #     user.email = self.cleaned_data['email']
        #
        #     if commit:
        #         user.save()
        #
        #     return user


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        exclude = ['username']


class AddressForm(ModelForm):
    class Meta:
        model = Address
        fields = '__all__'


