from rest_framework import routers
from blahg.api import CategoryViewSet, PostViewSet

router = routers.DefaultRouter()
router.register(r"category", CategoryViewSet)
router.register(r"post", PostViewSet)
