from rest_framework.pagination import PageNumberPagination as PageNumberPagination_


class PageNumberPagination(PageNumberPagination_):
    page_size = 5
