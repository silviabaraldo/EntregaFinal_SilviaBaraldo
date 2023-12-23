from django import forms
class Pasajero(forms.Form):

               #campos
     nombre= forms.CharField()
     email= forms.EmailField()

     from django import forms
class Chofer(forms.Form):

               #campos
     nombre= forms.CharField()
     email= forms.CharField()