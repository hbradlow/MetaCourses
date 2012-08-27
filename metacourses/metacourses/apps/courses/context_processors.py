from courses.models import Category, School, Material
def filters(request):
    return {
        "categories":Category.objects.all().order_by("name"),
        "schools":School.objects.all().order_by("name"),
        "materials":Material.objects.all().order_by("name"),
    }
