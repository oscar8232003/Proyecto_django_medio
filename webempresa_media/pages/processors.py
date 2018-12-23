from .models import Page


def politicas(request):
    objetos = Page.objects.all()
    return {'objetos':objetos}