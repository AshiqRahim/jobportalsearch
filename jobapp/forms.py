from django  import forms
from django.contrib.auth.models import User


class regisform(forms.Form):
    cmp_name=forms.CharField(max_length=25)
    address=forms.CharField(max_length=100)
    email=forms.EmailField()
    phone=forms.IntegerField()
    password=forms.CharField(max_length=20)
    cpassword=forms.CharField(max_length=20)



class loginform(forms.Form):
    email=forms.EmailField()
    password=forms.CharField(max_length=25)



class jobform(forms.Form):
    cmp_name=forms.CharField(max_length=50)
    cmp_email=forms.EmailField()
    title=forms.CharField(max_length=100)
    jobtype=forms.CharField(max_length=25)
    wrktype=forms.CharField(max_length=20)
    exp_required=forms.CharField(max_length=20)
    qualification=forms.CharField(max_length=20)


class user(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email','first_name','last_name','password']




class log(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=20)


# class user(forms.ModelForm):
#     class Meta:
#         model=User
#         fields='__all__'
#
#
# class ulogform(forms.Form):
#     email = forms.EmailField()
#     password = forms.CharField(max_length=20)