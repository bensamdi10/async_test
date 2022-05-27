#-*- coding: utf-8 -*-

import asyncio

from django.utils.decorators import classonlymethod
from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import TemplateView, View
from movie.models import Movie
from asgiref.sync import sync_to_async
import sys

if sys.platform == 'win32':
    loop = asyncio.ProactorEventLoop()
    asyncio.set_event_loop(loop)

class IndexPage(View):
    http_method_names = ['get', ]
    template_name = 'index.html'
    name = "home"

    @classonlymethod
    def as_view(cls, **initkwargs):
        view = super().as_view(**initkwargs)
        view._is_coroutine = asyncio.coroutines._is_coroutine
        return view

    @sync_to_async
    def getData(self):
        print("get data")
        result = Movie.objects.all()
        for movie in result:
            print(movie.title)
            print("----------------------------------")

    async def get(self, request):
        print("test view async")
        #result = await self.getData()
        return render(request, self.template_name, {})


class HomePage(View):
    http_method_names = ['get', ]
    template_name = 'index.html'
    name = "home"




    def get(self, request):
        print("test view sync")
        '''
        result = Movie.objects.all()
        for movie in result:
            print(movie.title)
            print("----------------------------------")
        '''
        return render(request, self.template_name, {})