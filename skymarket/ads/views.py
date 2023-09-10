from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import pagination, viewsets
from rest_framework.generics import get_object_or_404

from .filters import AdsFilter
from .models import Ad, Comment
from .serializers import AdSerializer, CommentSerializer


class AdPagination(pagination.PageNumberPagination):
    page_size = 4


# TODO view функции. Предлагаем Вам следующую структуру - но Вы всегда можете использовать свою
class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    filter_backends = (DjangoFilterBackend,)   #Бэкенд для обработки фильтра
    filterset_class = AdsFilter    #Набор полей для фильтрации
    pagination_class = AdPagination  # Используем PageNumberPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        user = self.request.user
        ad_id = self.kwargs.get('ad_pk')
        ad = get_object_or_404(Ad, id=ad_id)
        serializer.save(author=user, ad=ad)

    def get_queryset(self):
        ad_id = self.kwargs.get('ad_pk')
        ad = get_object_or_404(Ad, id=ad_id)
        return Comment.objects.filter(ad=ad)