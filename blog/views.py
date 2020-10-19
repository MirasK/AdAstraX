from django.shortcuts import render, get_object_or_404, redirect
from blog.models import User, Event, Student
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
from zoomus import ZoomClient
import http.client

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
        user = self.request.user.id
        all_events = [model_to_dict(event) for event in Event.objects.filter(student_id = user)]
        data['events'] = json.dumps(all_events, cls=DjangoJSONEncoder)
        return data


class StudentsView(LoginRequiredMixin, ListView):

    model = User
    fields = ['content']
    template_name = 'blog/sidebar/students.html'

    def get_context_data(self, **kwargs):

        client = ZoomClient('fKjTSVtsTzGsr0EeE1gq5w', 'xju52QwSShGiPv7iSHROt9Zy2b81j8HJSPdd')

        user_list_response = client.user.list()
        user_list = json.loads(user_list_response.content)

        for user in user_list['users']:
            user_id = user['id']
            print(json.loads(client.meeting.create(user_id=user_id, topic = 'AdAstra', settings = {'host_video': True, 'participant_video': True, 'audio': 'both'}).content))

        data = super().get_context_data(**kwargs)
        data['students'] =  [model_to_dict(user) for user in User.objects.filter(user_type = 3)]

        return data


class LessonView(LoginRequiredMixin, ListView):
    
    model = Event
    fields = ['content']
    template_name = 'blog/sidebar/lesson.html'

    def get_context_data(self, **kwargs):

        data = super().get_context_data(**kwargs)

        client = ZoomClient('fKjTSVtsTzGsr0EeE1gq5w', 'xju52QwSShGiPv7iSHROt9Zy2b81j8HJSPdd')

        user_list_response = client.user.list()
        user_list = json.loads(user_list_response.content)

        for user in user_list['users']:
            user_id = user['id']
            data['lesson'] = json.loads(client.meeting.create(user_id=user_id, topic = 'AdAstra', settings = {'host_video': True, 'participant_video': True, 'audio': 'both'}).content)

        return data