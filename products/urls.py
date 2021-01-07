from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

app_name = 'products'

urlpatterns = [
    # Category API Routes
    path('create_category/', CreateCategoryApiView.as_view()),
    path('category_list/', ListCategoryApiView.as_view()),
    path('category_list/<id>/', ListCategoryApiView.as_view()),
    path('update_category/', UpdateCategoryApiView.as_view()),
    path('delete_category/<id>/', DeleteCategoryApiView.as_view()),

    # ------------------------------------------------------------------------------------------------------------------

    # Product API Routes
    path('create_product/', CreateProductApiView.as_view()),
    path('product_list/', ListProductApiView.as_view()),
    path('product_list/<id>/', ListProductApiView.as_view()),
    path('product_list/category/<id>/', ListCategoryProductApiView.as_view()),
    path('update_product/', UpdateProductApiView.as_view()),
    path('delete_product/<id>/', DeleteProductApiView.as_view()),

    # ------------------------------------------------------------------------------------------------------------------

    # Review API Routes
    path('create_review/', CreateReviewApiView.as_view()),
    path('review_list/', ListReviewApiView.as_view()),
    path('review_list/<id>/', ListReviewApiView.as_view()),
    path('review_list/product/<id>/', ListProductReviewApiView.as_view()),
    path('update_review/', UpdateReviewApiView.as_view()),
    path('delete_review/<id>/', DeleteReviewApiView.as_view()),
]
