from rest_framework import viewsets
from .models import Todo
from .serializers import TodoSerializer

class TodoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows todos to be viewed or edited.
    ModelViewSet provides CRUD operations by default:
    - list (GET all)
    - retrieve (GET single)
    - create (POST)
    - update (PUT)
    - partial_update (PATCH)
    - destroy (DELETE)
    """
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
