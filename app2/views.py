from django.shortcuts import render
from app2.forms import ReviewForm
from django.views.generic.edit import FormView
from django.http import HttpResponse


class ReviewEmailView(FormView):
    template_name = 'app2/review.html'
    form_class = ReviewForm

    def form_valid(self, form):
        form.send_email()
        msg = "Thanks for the review"
        return HttpResponse(msg)

# I can use "template_name" without "app_name/" in path...
# if in app_name directory folder "templates" has no additional app_name dir
