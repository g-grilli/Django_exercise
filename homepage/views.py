from django.template.response import TemplateResponse
def homepage (request):
  return TemplateResponse(request, 'homepage.html', {})
# Create your views here.
<<<<<<< HEAD
def photos (request):
  return TemplateResponse(request, 'photos.html', {})
def food (request):
  return TemplateResponse(request, 'food.html', {})
=======
>>>>>>> 3b873ce11fc10cbea50fcd04f6345b266f0e749b
