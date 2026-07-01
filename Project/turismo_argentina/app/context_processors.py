from .models import Province

def global_context(request):
    return {
        'provinces': Province.objects.all(),
    }
