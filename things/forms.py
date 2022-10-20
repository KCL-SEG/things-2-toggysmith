"""Forms of the project."""

# Create your forms here.
from django import forms
from .models import Thing

class ThingForm(forms.ModelForm):
    class Meta:
        model = Thing
        fields = ["name", "description", "quantity"]
        widgets = {"description": forms.Textarea(), "quantity": forms.NumberInput()}

    name = forms.CharField(
        label="Name",
        widget=forms.TextInput(),
        validators=[MaxLengthValidator(
            limit_value=35,
            message="Name cannot be longer than 35 characters."
        )]
    )

    description = forms.Textarea(
        label="Description",
        widget=forms.TextInput(),
        validators=[MaxLengthValidator(
            limit_value=120,
            message="Name cannot be longer than 120 characters."
        )]
    )

    quantity = forms.NumberInput(
        label="Name",
        widget=forms.TextInput(),
        validators=[MinValueValidator(0),MaxValueValidator(50)]
    )