from django.shortcuts import render
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from .models import *
from client_app.models import *
from .serializers import *
from django_email_verification import sendConfirm


# Category Registration API
class CreateCategoryApiView(APIView):

    def get(self, request, id=None):
        return Response(status=status.HTTP_200_OK)

    def post(self, request):
        try:
            # optional parameters
            category_description = request.data['description']
            try:
                # required parameters
                category_name = request.data['name'].title()
                if category_name == "":
                    return Response(status=status.HTTP_400_BAD_REQUEST,
                                    data={"message": "Ooops! 'name' of category can not be empty"})
                try:
                    saved_data = Category.objects.get(name=category_name)
                    return Response(status=status.HTTP_400_BAD_REQUEST,
                                    data={"message": f"Category name with '{category_name}' already exists!"})
                except:
                    try:
                        new_product_details = Category.objects.create(
                            name=category_name,
                            description=category_description
                        )
                        new_product_details.save()
                        serializer = CategorySerializer(new_product_details)
                        return Response(status=status.HTTP_200_OK,
                                        data={"category_created": serializer.data})
                    except:
                        return Response(status=status.HTTP_400_BAD_REQUEST,
                                        data={"message": "There was a error creating record!"})
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST,
                                data={"message": "Oops! 'name' of category is required"})
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data={"message": "Oops! Please provide description, send empty string if you do not want to set anything"})


# Category List API
class ListCategoryApiView(APIView):

    def get(self, request, id=None):
        if id:
            try:
                category = Category.objects.get(id=id)
                serializer = CategorySerializer(category)
                return Response(status=status.HTTP_200_OK,
                                data={"category": serializer.data})
            except:
                return Response(status=status.HTTP_200_OK,
                                data=f"No record with  '{id}'!")
        else:
            try:
                category = Category.objects.all()
                serializer = CategorySerializer(category, many=True)
                if not category:
                    return Response(status=status.HTTP_200_OK,
                                    data={"Category table is empty": serializer.data})
                return Response(status=status.HTTP_200_OK, data={"categories": serializer.data})
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST)


# Category Update API
class UpdateCategoryApiView(APIView):

    def get(self, request):
        return Response(status=status.HTTP_200_OK)

    def put(self, request, id=None):
        try:
            # optional parameters
            category_description = request.data['description']
            try:
                # required parameters
                category_id = request.data['id']
                category_name = request.data['name'].title()
                if category_name == "":
                    return Response(status=status.HTTP_400_BAD_REQUEST,
                                    data="Ooops! 'name' of category can not be empty")
                try:
                    saved_data = Category.objects.get(name=category_name)
                    return Response(status=status.HTTP_400_BAD_REQUEST,
                                    data=f"'{category_name}' already exists")
                except:
                    try:
                        updated_category = Category.objects.filter(id=category_id)
                        updated_category.update(
                            name=category_name,
                            description=category_description
                        )
                        serializer = CategorySerializer(updated_category, many=True)
                        return Response(status=status.HTTP_200_OK,
                                        data={'updated_category': serializer.data})
                    except:
                        return Response(status=status.HTTP_404_NOT_FOUND,
                                        data="No Record Found!")
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST,
                                data="Oops! 'id and name' of category is required")
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data="Oops! Please provide description, send the orignal "
                                 "description if you do not want to change anything")


# Category Delete API
class DeleteCategoryApiView(APIView):

    def get(self, request, id=None):
        return Response(status=status.HTTP_200_OK)

    def delete(self, request, id=None):
        if id:
            try:
                saved_data = Category.objects.get(id=id)
                category_name = saved_data.name
                saved_data.delete()
                return Response(status=status.HTTP_200_OK,
                                data=f"category name with '{category_name}' deleted")
            except:
                return Response(status=status.HTTP_404_NOT_FOUND, data="No Record Found!")
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data={"Error Msg": "ID missing from URL"})


# ------------------------------------------------------------------------------------------------------------------------


# Product Registration API
class CreateProductApiView(APIView):
    parser_classes = (MultiPartParser, FormParser, JSONParser)

    def get(self, request, id=None):
        return Response(status=status.HTTP_200_OK)

    def post(self, request):
        # try:
        # optional parameters
        print(request.data)
        company = request.data['company']
        vat = request.data['vat']
        description = request.data['description']
        short_description = request.data['short_description']
        image = request.data['image']
        # try:
            # required parameters
        sku = request.data['sku']
        name = request.data['name']
        unit = request.data['unit']
        # avg_price = request.data['avg_price']
        currency = request.data['currency']
        if sku == "" \
                or name == "" \
                or unit == "" \
                or currency == "":
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data={"message": "Ooops! following required fields can't "
                                 "be empty: (sku, name, unit, avg_price, "
                                 "currency)"})
        try:
            saved_data = Product.objects.get(name=name, unit=unit, company=company)
            return Response(status=status.HTTP_200_OK,
                            data={"message": "Product already registered!"})
        except:
            # try:
            category = Category.objects.get(id=request.data['category'])
            # try:
            new_product_details = Product.objects.create(
                category=category,
                sku=sku,
                name=name,
                company=company,
                description=description,
                short_description=short_description,
                image=image,
                unit=unit,
                vat=vat,
                # avg_price=avg_price,
                currency=currency
            )
            new_product_details.save()
            serializer = ProductSerializer(new_product_details)
            return Response(status=status.HTTP_200_OK,
                            data={"product_created": serializer.data})
            # except:
                    #     return Response(status=status.HTTP_400_BAD_REQUEST,
                    #                     data="There was a error creating record!")
                # except:
                #     return Response(status=status.HTTP_404_NOT_FOUND,
        #         #                     data="Product already in database!")
        # except:
        #     return Response(status=status.HTTP_400_BAD_REQUEST,
        #                     data="Oops! Make sure you're not missing one of the "
        #                          "following required fields: (sku, name, unit"
        #                          "avg_price, currency)")
        # except:
        #     return Response(status=status.HTTP_400_BAD_REQUEST,
        #                     data="Oops! Make sure you're not missing one "
        #                          "of the following optional fields: "
        #                          "(description, short_description, company, image) "
        #                          "Note: If you want to leave fields blank, then "
        #                          "send null or empty")


# Product List API
class ListProductApiView(APIView):

    def get(self, request, id=None):
        client_id = self.request.query_params.get('client_id')
        
        if client_id:
            try:
                client = Client.objects.get(id=client_id)
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST, data={'message': 'Client ID not provided or does not exist'})
            if id:
                try:
                    product = Product.objects.get(id=id)
                    serializer = ProductSerializer(product)
                    return Response(status=status.HTTP_200_OK,
                                    data={"product": serializer.data})
                except:
                    return Response(status=status.HTTP_404_NOT_FOUND,
                                    data={"No Product with ID!": id})
            else:
                # try:
                average_prices = AveragePrice.objects.filter(client=client_id)
                products = Product.objects.all()
                serializer = ProductSerializer(products, many=True)
                response = serializer.data

                for res in response:
                    try:
                        try:
                            product = Product.objects.get(id=res['id'])
                        except:
                            return Response(status=status.HTTP_400_BAD_REQUEST, data={'message': 'Client does not exist'})

                        avg_price_obj = AveragePrice.objects.get(client=client, product=product)
                        res['avg_price'] = avg_price_obj.avg_price
                        print('here ')
                    except Exception as e:
                        res['avg_price'] = 0.0

                if not products:
                    return Response(status=status.HTTP_200_OK,
                                    data={"message": 'Product table is empty'})


                return Response(response,
                                status=status.HTTP_200_OK)
        else:
            products = Product.objects.all()
            serializer = ProductSerializer(products, many=True)
            return Response(status=status.HTTP_200_OK, data={'products': serializer.data})
            # except:
            #     return Response(status=status.HTTP_400_BAD_REQUEST)


# Product List based on Category ID
class ListCategoryProductApiView(APIView):

    def get(self, request, id=None):
        if id:
            try:
                product = Product.objects.filter(category__id=id)
                serializer = ProductSerializer(product, many=True)
                return Response(status=status.HTTP_200_OK,
                                data={"category_products": serializer.data})
            except:
                return Response(status=status.HTTP_404_NOT_FOUND,
                                data="No Product in Database!")
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data={"Error Msg": "ID missing from URL"})


# Product Update API
class UpdateProductApiView(APIView):

    def get(self, request):
        return Response(status=status.HTTP_200_OK)

    def put(self, request, id=None):
        try:
            # optional parameters
            name = request.data['name']
            unit = request.data['unit']
            avg_price = request.data['avg_price']
            currency = request.data['currency']
            company = request.data['company']
            description = request.data['description']
            short_description = request.data['short_description']
            image = request.data['image']
            try:
                # required parameters
                id = request.data['id']
                if id is None:
                    return Response(status=status.HTTP_400_BAD_REQUEST,
                                    data="Ooops! following required fields can't "
                                         "be empty: (sku, name, unit, avg_price, "
                                         "currency)")
                try:
                    saved_product_data = Product.objects.filter(id=id)
                    try:
                        saved_product_data.update(
                            name=name,
                            unit=unit,
                            avg_price=avg_price,
                            currency=currency,
                            company=company,
                            description=description,
                            short_description=short_description,
                            image=image
                        )
                        serializer = ProductSerializer(saved_product_data, many=True)
                        return Response(status=status.HTTP_200_OK,
                                        data={'changes_updated': serializer.data})
                    except:
                        return Response(status=status.HTTP_404_NOT_FOUND,
                                        data='There was a error updating the data!')
                except:
                    return Response(status=status.HTTP_404_NOT_FOUND,
                                    data=f"No record found against {id}")
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST,
                                data="Oops! ID of the product is required to update")
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data="Oops! Make sure you're not missing one "
                                 "of the following optional fields: "
                                 "(name, unit, avr_price, currency, company, "
                                 "description, short_description, image) "
                                 "Note: If you want to leave fields blank, then "
                                 "send null or empty")


# Product Delete API
class DeleteProductApiView(APIView):

    def get(self, request, id=None):
        return Response(status=status.HTTP_200_OK)

    def delete(self, request, id=None):
        if id:
            try:
                saved_data = Product.objects.get(id=id)
                name = saved_data.name
                saved_data.delete()
                return Response(status=status.HTTP_200_OK,
                                data=f"product with name '{name}' deleted")
            except:
                return Response(status=status.HTTP_404_NOT_FOUND, data="No Record Found!")
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data={"Error Msg": "ID missing from URL"})


# ------------------------------------------------------------------------------------------------------------------------


# Review Registration API
class CreateReviewApiView(APIView):

    def get(self, request, id=None):
        return Response(status=status.HTTP_200_OK)

    def post(self, request):
        client_id = request.data['client']
        product_id = request.data['product']
        try:
            client = Client.objects.get(id=client_id)
            product = Product.objects.get(id=product_id)
            try:
                new_review_details = Review.objects.create(
                    client=client,
                    product=product,
                    rating=request.data['rating'],
                    comment=request.data['comment'],
                )
                new_review_details.save()
                serializer = ReviewSerializer(new_review_details)
                return Response(status=status.HTTP_200_OK,
                                data={"review_created": serializer.data})
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST,
                                data="There was a error creating record!")
        except:
            return Response(status=status.HTTP_404_NOT_FOUND,
                            data="Client or Product ID missing in body!")


# Review List API
class ListReviewApiView(APIView):

    def get(self, request, id=None):
        if id:
            try:
                review = Review.objects.get(id=id)
                serializer = ReviewSerializer(review)
                return Response(status=status.HTTP_200_OK,
                                data={id: serializer.data})
            except:
                return Response(status=status.HTTP_404_NOT_FOUND,
                                data={"No Review with ID!": id})
        else:
            try:
                review = Review.objects.all()
                serializer = ReviewSerializer(review, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except:
                return Response(status=status.HTTP_404_NOT_FOUND,
                                data="Database is empty!")


# Review List based on Product ID
class ListProductReviewApiView(APIView):

    def get(self, request, id=None):
        if id:
            product_id = id
            print(product_id)
            try:
                review = Review.objects.filter(product__id=product_id)
                serializer = ReviewSerializer(review, many=True)
                return Response(status=status.HTTP_200_OK,
                                data={"product_reviews": serializer.data})
            except:
                return Response(status=status.HTTP_404_NOT_FOUND,
                                data="No Product Review in Database!")
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data={"Error Msg": "ID missing from URL"})


# Review Update API
class UpdateReviewApiView(APIView):

    def get(self, request):
        return Response(status=status.HTTP_200_OK)

    def put(self, request, id=None):
        client_id = request.data['client']
        product_id = request.data['product']
        review_id = request.data['id']
        try:
            saved_client_data = Client.objects.get(id=client_id)
            saved_product_data = Product.objects.get(id=product_id)
            saved_review_data = Review.objects.filter(id=review_id)
            try:
                saved_review_data.update(
                    client=saved_client_data,
                    product=saved_product_data,
                    rating=request.data['rating'],
                    comment=request.data['comment']
                )
                serializer = ReviewSerializer(saved_review_data, many=True)
                return Response(status=status.HTTP_200_OK,
                                data={'changes_updated': serializer.data})
            except:
                return Response(status=status.HTTP_404_NOT_FOUND,
                                data='There was a error updating the data!')
        except:
            return Response(status=status.HTTP_404_NOT_FOUND,
                            data=f"No record found against '{registration_no}'")


# Review Delete API
class DeleteReviewApiView(APIView):

    def get(self, request, id=None):
        return Response(status=status.HTTP_200_OK)

    def delete(self, request, id=None):
        if id:
            try:
                saved_data = Review.objects.get(id=id)
                saved_data.delete()
                return Response(status=status.HTTP_200_OK,
                                data={'Record deleted against Review ID': id})
            except:
                return Response(status=status.HTTP_404_NOT_FOUND, data="No Record Found!")
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data={"Error Msg": "ID missing from URL"})
