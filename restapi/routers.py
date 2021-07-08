from myapis.viewsets import StudentViewset, BooksViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('student', StudentViewset)
router.register('books', BooksViewset)
