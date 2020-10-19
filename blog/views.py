from django.shortcuts import render, get_object_or_404, redirect
from blog.models import User, Event
import sys
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Count
from django.contrib.auth.decorators import login_required
from django.conf import settings
import json
from django.forms.models import model_to_dict
from django.core.serializers.json import DjangoJSONEncoder
import requests

def is_users(post_user, logged_user):
    return post_user == logged_user


PAGINATION_COUNT = 3


class PostListView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'blog/sidebar.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = PAGINATION_COUNT

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        return data


class CalendarView(LoginRequiredMixin, ListView):

    model = User
    fields = ['content']
    template_name = 'blog/sidebar/calendar.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        all_events = [model_to_dict(event) for event in Event.objects.all()]
        data['events'] = json.dumps(all_events, cls=DjangoJSONEncoder)
        response = requests.get("https://api.zoom.us/v2/users/")
        print(response.status_code)
        return data