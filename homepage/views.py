from django.template.response import TemplateResponse
def homepage (request):
  return TemplateResponse(request, 'homepage.html', {})
# Create your views here.
