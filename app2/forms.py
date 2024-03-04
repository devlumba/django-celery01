from django import forms
from app2.tasks import send_review_email_task


class ReviewForm(forms.Form):
    name = forms.CharField(
        label='Name', min_length=4, max_length=16, widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    email = forms.EmailField(label='Email', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    review_content = forms.CharField(label='Review', widget=forms.Textarea(attrs={'rows': '5'}))

    def send_email(self):
        send_review_email_task.delay(
            self.cleaned_data['name'], self.cleaned_data['email'], self.cleaned_data['review_content']
        )

