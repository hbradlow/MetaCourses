from courses.models import Category
def categories(request):
    return {
        "categories":Category.objects.all().order_by("name")
    }

