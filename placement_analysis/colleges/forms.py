from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit
from accounts.models import PlacementRequests, CompanyModel


class PlacementRequestForm(forms.ModelForm):
    company = forms.ModelChoiceField(
        queryset=CompanyModel.objects.all(), label='Select Company')

    class Meta:
        model = PlacementRequests
        fields = ['company', 'description']

    # def __init__(self, *args, **kwargs):
    #     super(PlacementRequestForm, self).__init__(*args, **kwargs)
    #     self.helper = FormHelper()
    #     self.helper.layout = Layout(
    #         'company',
    #         'description',
    #         Submit('submit', 'Send Placement Request')
    #     )
