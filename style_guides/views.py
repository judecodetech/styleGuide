from django.http import HttpResponse
from django.shortcuts import render

from .models import StyleGuide

def style_guide_list(request):
  style_guides = StyleGuide.objects.all()
  return render(request, 'style_guides/style_guide.html', {'style_guides': style_guides})
