import django_filters
from django.contrib.auth import get_user_model
User = get_user_model()

class UserFilter(django_filters.FilterSet):
    keyword = django_filters.CharFilter(method='keyword_filter')

    class Meta:
        model = User
        fields = []

    def keyword_filter(self, queryset, name, value):
        # If the keyword matches an email exactly, return that user
        if queryset.filter(email__iexact=value).exists():
            return queryset.filter(email__iexact=value)
        # Otherwise, filter users whose names contain the keyword (case-insensitive)
        return queryset.filter(name__icontains=value)