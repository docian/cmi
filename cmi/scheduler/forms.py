from django import forms

class PacientForm(forms.Form):
    name = forms.CharField(label = "Nume", max_length=30, empty_value='Popescu')
    surname = forms.CharField(label="Prenume", max_length=30, empty_value='Ion')
    cnp  = forms.CharField(label = "CNP", max_length=15, empty_value='1660910400012')
    phone = forms.CharField(label="Telefon", max_length=14, empty_value='0723121213' )
    email = forms.EmailField(label="Email", empty_value='popescu_ion@yahoo.com')