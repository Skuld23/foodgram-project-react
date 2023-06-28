from .permissions import IsAdminOrReadOnly
from django.shortcuts import get_object_or_404
from recipes.models import Recipe
from rest_framework.permissions import AllowAny

from .serializers import SubscribeRecipeSerializer


class GetObjectMixin:
    serializer_class = SubscribeRecipeSerializer
    permission_classes = (AllowAny,)

    def get_object(self):
        recipe_id = self.kwargs['recipe_id']
        recipe = get_object_or_404(Recipe, id=recipe_id)
        self.check_object_permissions(self.request, recipe)
        return recipe


class PermissionAndPaginationMixin:
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = None
