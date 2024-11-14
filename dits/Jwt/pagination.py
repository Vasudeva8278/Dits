from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class CustomPagination(PageNumberPagination):
    page_size = 10  # Default number of results per page
    page_size_query_param = 'page_size'  # Allow clients to override page size
    max_page_size = 100  # Maximum page size
    page_query_param = 'page'  # Query param for the page number

    def get_paginated_response(self, data):
        """
        Override the method to customize the paginated response.
        """
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'total_results': self.page.paginator.count,
            'total_pages': self.page.paginator.num_pages,
            'current_page': self.page.number,
            'results': data
        })
