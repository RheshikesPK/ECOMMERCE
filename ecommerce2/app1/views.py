from django.shortcuts import render,get_object_or_404,redirect,HttpResponse
from django.contrib.auth import login,authenticate
from django.views import View
from django.http import JsonResponse
from .models import Product,ProductImages,Cart,CartItem,Review,WishList,WishListItem,Order,OrderItem
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm
from .models import UserProfile,ShippingAddress, OrderPayment
from django.views.generic.edit import FormView, DeleteView
from django.contrib.auth.forms import AuthenticationForm
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum
from . forms import ReviewForm,ContactForm
from datetime import datetime
from django.db import transaction
from django.conf import settings
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView
from django.views.generic.detail import DetailView
import stripe
import json



class IndexView(View):
    def get(self, request):
        new_products = Product.objects.order_by('-created_at')[:5]
        top_selling_product = Product.objects.annotate(total_quantity_ordered=Sum('orderitem__quantity')).order_by('-total_quantity_ordered').first()
        other_top_products = Product.objects.annotate(total_quantity_ordered=Sum('orderitem__quantity')).order_by('-total_quantity_ordered')[1:6]
        return render(request, 'app/index.html', {'new_products':new_products,'top_selling_product': top_selling_product,'other_top_products': other_top_products})

    

class StoreView(View):
    def get(self, request):
        page=1
        if request.GET:
            page=request.GET.get('page',1)
        min_price = request.GET.get('min_price')
        max_price = request.GET.get('max_price')       
        products = Product.objects.all()
        if min_price and max_price:
            products = products.filter(price__range=(min_price, max_price))
        product_paginator =Paginator(products,3)
        products=product_paginator.get_page(page)
        top_selling_product = Product.objects.annotate(total_quantity_ordered=Sum('orderitem__quantity')).order_by('-total_quantity_ordered').first()
        other_top_products = Product.objects.annotate(total_quantity_ordered=Sum('orderitem__quantity')).order_by('-total_quantity_ordered')[1:6]
        return render(request, 'app/store.html', {'products': products,'top_selling_product': top_selling_product,'other_top_products': other_top_products})

class ProductView(View):
    def get(self, request, id):
        page=1
        if request.GET:
            page=request.GET.get('page',1)
        products = Product.objects.filter(id=id)
        product_images = ProductImages.objects.filter(product=id)
        product = Product.objects.get(id=id)
        form=ReviewForm()
        reviews=Review.objects.filter(product_id=id)
        reviews_paginator =Paginator(reviews,2)
        reviews=reviews_paginator.get_page(page)
        for review in reviews:
            review.stars = range(review.rating)
            review.empty_stars = range(5 - review.rating)       
        related_products = Product.objects.filter(category=product.category).exclude(id=id)[:4] if product.category else []
        return render(request, 'app/product.html', {'reviews':reviews,'form':form,'products': products,'product_images': product_images,'related_products':related_products})

class LaptopView(View):
    def get(self, request, id):
        page=1
        if request.GET:
            page=request.GET.get('page',1)
        min_price = request.GET.get('min_price')
        max_price = request.GET.get('max_price')
        products = Product.objects.filter(category=id)
        if min_price and max_price:
            products = products.filter(price__range=(min_price, max_price))
        product_paginator =Paginator(products,2)
        products=product_paginator.get_page(page)
        top_selling_product = Product.objects.annotate(total_quantity_ordered=Sum('orderitem__quantity')).order_by('-total_quantity_ordered').first()
        other_top_products = Product.objects.annotate(total_quantity_ordered=Sum('orderitem__quantity')).order_by('-total_quantity_ordered')[1:6]
        return render(request, 'app/store.html', {'products': products,'top_selling_product': top_selling_product,'other_top_products': other_top_products})

class MobileView(View):
    def get(self, request, id):
        page=1
        if request.GET:
            page=request.GET.get('page',1)
        min_price = request.GET.get('min_price')
        max_price = request.GET.get('max_price')
        products = Product.objects.filter(category=id)
        if min_price and max_price:
            products = products.filter(price__range=(min_price, max_price))
        product_paginator =Paginator(products,2)
        products=product_paginator.get_page(page)
        top_selling_product = Product.objects.annotate(total_quantity_ordered=Sum('orderitem__quantity')).order_by('-total_quantity_ordered').first()
        other_top_products = Product.objects.annotate(total_quantity_ordered=Sum('orderitem__quantity')).order_by('-total_quantity_ordered')[1:6]
        return render(request, 'app/store.html', {'products': products,'top_selling_product': top_selling_product,'other_top_products': other_top_products})

class CameraView(View):
    def get(self, request, id):
        page=1
        if request.GET:
            page=request.GET.get('page',1)
        min_price = request.GET.get('min_price')
        max_price = request.GET.get('max_price')
        products = Product.objects.filter(category=id)
        if min_price and max_price:
             products = products.filter(price__range=(min_price, max_price))
        product_paginator =Paginator(products,2)
        products=product_paginator.get_page(page)
        top_selling_product = Product.objects.annotate(total_quantity_ordered=Sum('orderitem__quantity')).order_by('-total_quantity_ordered').first()
        other_top_products = Product.objects.annotate(total_quantity_ordered=Sum('orderitem__quantity')).order_by('-total_quantity_ordered')[1:6]
        return render(request, 'app/store.html', {'products': products,'top_selling_product': top_selling_product,'other_top_products': other_top_products})

class AccessoriesView(View):
    def get(self, request, id):
        page=1
        if request.GET:
            page=request.GET.get('page',1)
        min_price = request.GET.get('min_price')
        max_price = request.GET.get('max_price')
        products = Product.objects.filter(category=id)
        if min_price and max_price:
            products = products.filter(price__range=(min_price, max_price))
        product_paginator =Paginator(products,2)
        products=product_paginator.get_page(page)
        top_selling_product = Product.objects.annotate(total_quantity_ordered=Sum('orderitem__quantity')).order_by('-total_quantity_ordered').first()
        other_top_products = Product.objects.annotate(total_quantity_ordered=Sum('orderitem__quantity')).order_by('-total_quantity_ordered')[1:6]
        return render(request, 'app/store.html', {'products': products,'top_selling_product': top_selling_product,'other_top_products': other_top_products})

class RegisterView(View):
    def get(self, request):
        form = CustomUserCreationForm()
        return render(request,'app/signup.html', {'form': form})
    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data['phone_number']
            age = form.cleaned_data['age']
            gender = form.cleaned_data['gender']
            user = form.save()
            UserProfile.objects.create(user=user,phone_number=phone_number, age=age, gender=gender)
            login(request, user)
            return redirect('signin') 
        return render(request,'app/signup.html', {'form': form})


class LoginView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request,'app/signin.html', {'form': form})

    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            request.session['username']=username
            request.session['id']=user.id
            

            if user is not None:
                login(request, user)
                return redirect('index')

        return render(request,'app/signin.html', {'form': form})


# class CheckoutView(View):


#     def post(self, request):
#         user = request.user
#         cart = Cart.objects.filter(user=user).first()
#         order_items = []

#         if cart:
#             order = Order.objects.create(user=user)
#             total_price = 0

#             with transaction.atomic():
#                 for cart_item in cart.cartitem_set.all():
#                     order_item = OrderItem.objects.create(order=order, product=cart_item.products, quantity=cart_item.quantity)
#                     order_items.append(order_item)
#                     total_price += cart_item.products.price * cart_item.quantity

#                 order.total_price = total_price
#                 order.save()

#             user_profile = UserProfile.objects.get(user=user)
#             shipping_address = ShippingAddress.objects.filter(user=user_profile).first()

#             form = ContactForm()

#             # Pass shipping address if available, else pass None
#             return render(request, 'app/checkout.html', {'form': form, 'order_items': order_items, 'total_price': total_price, 'shipping_address': shipping_address})
        
        
class SignOutView(View):
    def get(self, request):
        if request.user.is_authenticated:
            request.session.flush()
            return redirect('signin')  
        else:
            return redirect('signin')


class AddToCartView(LoginRequiredMixin, View):
    login_url = reverse_lazy('signin')

    def get(self, request, product_id):
        product = get_object_or_404(Product, pk=product_id)
        user_cart, created = Cart.objects.get_or_create(user=request.user)
        cart_item, created = CartItem.objects.get_or_create(cart=user_cart, products=product)

        if not created:
            cart_item.quantity += 1
            cart_item.save()

        return redirect(request.META.get('HTTP_REFERER', 'default-view'))
        

class UpdateCartView(LoginRequiredMixin, View):
    login_url = reverse_lazy('signin')

    def post(self, request, cart_item_id):
        action = request.POST.get('action')
        cart_item = get_object_or_404(CartItem, pk=cart_item_id)

        if action == 'add':
            cart_item.quantity += 1
            cart_item.save()
        elif action == 'subtract':
            if cart_item.quantity > 1:
                cart_item.quantity -= 1
                cart_item.save()
            else:
                cart_item.delete()
        return redirect('cart_view')


class CartView(LoginRequiredMixin, View):
    login_url = reverse_lazy('signin')
    def get(self, request):
            try:
                user_cart = Cart.objects.get(user=request.user)
                cart_items = CartItem.objects.filter(cart=user_cart)
                total_price = sum(cart_item.quantity * cart_item.products.price for cart_item in cart_items)
                
                for cart_item in cart_items:

                    cart_item.product_image_url = cart_item.products.image.url
                    cart_item.total_price = cart_item.quantity * cart_item.products.price
                
                return render(request, 'app/blank.html', {'cart_items': cart_items, 'total_price': total_price})
            except Cart.DoesNotExist:
                msg='Your cart is empty'
                return render(request, 'app/blank.html',{'msg':msg})
            
            
class CartRemove(View):
    def post(self, request, cart_item_id):
        cart_item = CartItem.objects.get(pk=cart_item_id)
        cart_item.delete()
        return redirect('cart_view')       

class GetCartItemsView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            user_cart = Cart.objects.filter(user=request.user).first()
            if user_cart:
                total_quantity = user_cart.cartitem_set.aggregate(total_quantity=Sum('quantity'))['total_quantity']
                total_quantity = total_quantity if total_quantity else 0
                return JsonResponse({'total_quantity': total_quantity})
            else:
                return JsonResponse({'total_quantity': 0})
        else:
            return JsonResponse({'error': 'User is not authenticated'}, status=401)
        
class WishlistView(LoginRequiredMixin, View):
    login_url = reverse_lazy('signin') 

    def get(self, request):
        user_wishlist = WishList.objects.filter(user=request.user).first()
        if user_wishlist:
            wishlist_items = WishListItem.objects.filter(wishlist=user_wishlist)
        else:
            wishlist_items = []
        return render(request, 'app/wishlist.html', {'wishlist_items': wishlist_items})

class GetWishlistItemsView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            user_wishlist = WishListItem.objects.filter(wishlist__user=request.user)
            total_quantity = user_wishlist.count()
            return JsonResponse({'total_quantity': total_quantity})
        else:
            return JsonResponse({'error': 'User is not authenticated'}, status=401)
    

class SaveReviewView(View):
    def post(self, request):
        product_id = request.POST.get('product_id')
        product = get_object_or_404(Product, id=product_id)
        
        form = ReviewForm(request.POST)
        if form.is_valid():
            user = request.user  # Assuming the user is authenticated
            rating=request.POST.get('rating')
            review_text = form.cleaned_data['review']
            date = datetime.now()
            
            review = Review.objects.create(user=user, product=product, rating=rating, review=review_text, date=date)  # Redirect to a success URL after saving
            review.save()
        
        return redirect(request.META.get('HTTP_REFERER', 'default-view'))
    
    


class SearchProductsView(View):
    def get(self, request):
        if 'query' in request.GET:
            query = request.GET.get('query')
            
            products = Product.objects.filter(name__icontains=query)
            
            data = [{'id': product.id,'name': product.name,'image': product.image.url, 'price': str(product.price)} for product in products]
            return JsonResponse(data, safe=False)
        else:
            return JsonResponse({'error': 'Invalid request'})
        
class AddToWishlistView(View):
    def post(self, request, product_id):
        product = get_object_or_404(Product, pk=product_id)
        user = request.user
        wishlist, created = WishList.objects.get_or_create(user=user)
        wishlist_item = WishListItem.objects.get_or_create(wishlist=wishlist, product=product)
        return redirect('wishlist')  # Redirect to wishlist page

class SaveAddressView(View):    
    def post(self, request):
        user=request.user
        form = ContactForm(request.POST)
        if form.is_valid():
            
            user_profile = UserProfile.objects.get(user=request.user)

            
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            address = form.cleaned_data['address']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            zip_code = form.cleaned_data['zip_code']
            

            
            shipping_address = ShippingAddress.objects.create(
                user=user_profile,  # Pass the UserProfile instance
                name=name,
                email=email, 
                address=address,
                city=city,
                state=state,
                zip_code=zip_code,
               
            )
            return redirect(request.META.get('HTTP_REFERER', 'default-view'))



# class CheckoutView(View):
#     def post(self, request):
#         user = request.user
#         cart = Cart.objects.filter(user=user).first()
#         order_items = []

#         if cart:
#             order = Order.objects.create(user=user)
#             total_price = 0

#             with transaction.atomic():
#                 for cart_item in cart.cartitem_set.all():
#                     item_total_price = cart_item.products.price * cart_item.quantity
#                     order_item = OrderItem.objects.create(
#                         order=order,
#                         product=cart_item.products,
#                         quantity=cart_item.quantity,
#                         total_price=item_total_price
#                     )
#                     order_items.append(order_item)
#                     total_price += item_total_price

#             user_profile = UserProfile.objects.get(user=user)
#             shipping_address = ShippingAddress.objects.filter(user=user_profile).first()
#             form = ContactForm()

#             return render(request, 'app/checkout.html', {
#                 'form': form,
#                 'order_items': order_items,
#                 'total_price': total_price,
#                 'shipping_address': shipping_address
#             })
#         return redirect('home') 



class CheckoutView(View):
    def post(self, request):
        user = request.user
        cart = Cart.objects.filter(user=user).first()
        order_items = []

        if cart:
            order = Order.objects.create(user=user)
            total_price = 0

            with transaction.atomic():
                for cart_item in cart.cartitem_set.all():
                    order_item = OrderItem.objects.create(order=order, product=cart_item.products, quantity=cart_item.quantity)
                    order_items.append(order_item)
                    total_price += cart_item.products.price * cart_item.quantity

                order.total_price = total_price
                order.save()

            user_profile = UserProfile.objects.get(user=user)
            shipping_address = ShippingAddress.objects.filter(user=user_profile).first()

            form = ContactForm()
            
            total_price_in_paise = total_price * 100

            
            return render(request, 'app/checkout.html', {'form': form, 'order_items': order_items, 'total_price': total_price, 'shipping_address': shipping_address,'total_price_in_paise' :total_price_in_paise})




stripe.api_key = 'sk_test_51PpmUz043xJZrQQTaG2ykPbTVQql9pkvYLCwbjFGMMk5aR3n62iPHzbsNfGlj2OOqlXFsrXgpQNIrgUz5t287aRI00FdR5UGmD'


@csrf_exempt
def process_payment(request):
    if request.method == 'POST':
        try:
            # Load the request data
            data = json.loads(request.body)
            payment_method_id = data.get('payment_method_id')
            amount = data.get('amount')
            order_id = data.get('order_id')

            
            if not amount or not isinstance(amount, int) or amount <= 0:
                print(f'Invalid amount: {amount}')
                return JsonResponse({'error': 'Invalid or missing amount'}, status=400)

            
            print('Received data:', data)

            
            intent = stripe.PaymentIntent.create(
                amount=amount,
                currency='inr',
                payment_method=payment_method_id,
                automatic_payment_methods={'enabled': True},
                confirm=True,
                return_url='https://yourdomain.com/payment_success/' 
            )



            
            if intent.status == 'succeeded':

               
                if order_id:
                    
                    
                    order_items = OrderItem.objects.filter(order_id=order_id)
                    products = [
                    {
                        'product_id': item.product.id,
                        'product_name': item.product.name,
                        'quantity': item.quantity,
                        'price': float(item.product.price),
                    }
                    for item in order_items
                ]


                    for item in order_items:
                        product = Product.objects.get(id=item.product.id)
                        stock_str = int(product.stock)
                        if stock_str >= item.quantity:
                            stock_str -= item.quantity
                            product.stock=stock_str
                            product.save()
                        else:
                            print(f'Insufficient stock for product ID {item.product.id}')



                # Save order payment with product details
                OrderPayment.objects.create(
                    user=request.user,
                    amount=amount,
                    order_id=order_id,
                    paid=True,
                    products=products,  # Store product details in the OrderPayment model
                )
                


                    

                if order_id:
                    try:
                        order = Order.objects.get(id=order_id)
                        OrderItem.objects.filter(order=order).delete()  
                        print(f'Order items and order with ID {order_id} deleted from the cart.')
                    except Order.DoesNotExist:
                        print(f'Order with ID {order_id} does not exist.')

            # Return the client secret to confirm the payment on the client side
            return JsonResponse({
                'client_secret': intent.client_secret
            })

        except stripe.error.CardError as e:
            print(f'Stripe CardError: {e}')
            return JsonResponse({'error': str(e)}, status=400)
        except stripe.error.RateLimitError as e:
            print(f'Stripe RateLimitError: {e}')
            return JsonResponse({'error': str(e)}, status=400)
        except stripe.error.InvalidRequestError as e:
            print(f'Stripe InvalidRequestError: {e}')
            return JsonResponse({'error': str(e)}, status=400)
        except stripe.error.AuthenticationError as e:
            print(f'Stripe AuthenticationError: {e}')
            return JsonResponse({'error': str(e)}, status=400)
        except stripe.error.APIConnectionError as e:
            print(f'Stripe APIConnectionError: {e}')
            return JsonResponse({'error': str(e)}, status=500)
        except stripe.error.StripeError as e:
            print(f'Stripe StripeError: {e}')
            return JsonResponse({'error': str(e)}, status=500)
        except Exception as e:
            print(f'General Exception: {e}')
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request method'}, status=400)

class PaymentSuccessView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'app/payment_success.html')


class OrderDetailView(LoginRequiredMixin, ListView):
    model = OrderPayment
    template_name = 'app/order_details.html'
    context_object_name = 'orders'

    # This function is used to filter the orders for the logged-in user
    def get_queryset(self):
        return OrderPayment.objects.filter(user=self.request.user)
    
class OrderView(DetailView):
    model = OrderPayment
    template_name = 'app/myorder.html'
    context_object_name = 'order'

    def get_object(self, queryset=None):
        obj = get_object_or_404(OrderPayment, pk=self.kwargs.get('pk'))
        return obj