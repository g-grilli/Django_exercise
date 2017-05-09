from django.template.response import TemplateResponse
def homepage (request):
  return TemplateResponse(request, 'homepage.html', {})
# Create your views here.
def photos (request):
  return TemplateResponse(request, 'photos.html', {})
def food (request):
  return TemplateResponse(request, 'food.html', {})