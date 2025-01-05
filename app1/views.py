from django.shortcuts import render , HttpResponse , redirect
from .models import *
from django.core.exceptions import ObjectDoesNotExist 

# Create your views here.

def home(request):
    return HttpResponse("this is my home page")

def first(request):
    blogdata = Blog.objects.all()
    # print(blogdata)
    return render(request,'first.html',{'blogdata':blogdata})


def store(request):
    if request.method == 'POST':
        user = Blog()
        user.email = request.POST['uemail']
        user.name = request.POST['uname']
        user.save()
    return render(request,'store.html')


def catstore(request):
    if request.method == 'POST' and request.FILES['img']:
        catdata = Category()
        catdata.name = request.POST['name']
        catdata.image = request.FILES['img']
        catdata.save()
    return render(request,'catimg.html')

from django.contrib.auth.hashers import make_password,check_password

from .encrypt_pass import encry


# def register(request):
#     if 'user' in request.session:
#         if request.method == 'POST':
#             registeruser  = registeration()
#             registeruser.name = request.POST['uname']
#             registeruser.email = request.POST['email']
#             registeruser.mob = request.POST['mob']
#             encrypted_password = encrypt(request.POST['password'])  ##encrept password
#             registeruser.add = request.POST['add']
            
#             encrypted_password=encry(password)
#             print("0000000000000000000000")
#             registeruser.password=encrypted_password
#             print("1111111111111111111111")
#             alreadyuser = registeration.objects.filter(email =  request.POST['email'])
#             # if alreadyuser:
#             #     return render(request,'register.html',{'alreadyuser':"this email already exists..!"})
#             # else:
#                 # registeruser.save()
#                 # return render(request,'register.html')
#             if alreadyuser:
                
#                 return render(request,'register.html',{'alreadyuser':"this email already exists..!"})
#             else:
#                 registeruser.save()
#                 return render(request,'register.html')
#         else:
#             return render(request,'register.html')
#     elif 'vendor' in request.session:   ##########################################################################
#         if request.method == 'POST':
#             registeruser  = vendor()
#             registeruser.name = request.POST['uname']
#             registeruser.email = request.POST['email']
#             registeruser.mob = request.POST['mob']
#             registeruser.password = request.POST['password']
#             registeruser.add = request.POST['add']
#             alreadyuser = vendor.objects.filter(email =  request.POST['email'])
#             if len(alreadyuser) <= 0:
#                 registeruser.save()
#                 return render(request,'register.html')
#             else:
#                 return render(request,'register.html',{'alreadyuser':"this email already exists..!"})
#         else:
#             return render(request,'register.html')
        
#     else:

#             return render(request,'register.html')


from django.contrib.auth.hashers import make_password,check_password

from .encrypt_pass import encry,descry

def register(request):
    if 'user' in request.session:
        if request.method == 'POST':
            registeruser  = registeration()
            registeruser.name = request.POST['uname']
            registeruser.email = request.POST['email']
            registeruser.mob = request.POST['mob']
            encrypted_password =  encry(request.POST['password'])
            print(encrypted_password,"======= encrypted password =====")
            registeruser.add = request.POST['add']
            alreadyuser = registeration.objects.filter(email =  request.POST['email'])
            decrypted_password = descry(encrypted_password)
            print(decrypted_password,"====== decrypted password =====")
            registeruser.password = encrypted_password
            if len(alreadyuser) <= 0:
                registeruser.save()
                return render(request,'register.html')
            else:
                return render(request,'register.html',{'alreadyuser':"this email already exists..!"})
        else:
            return render(request,'register.html')
    elif 'vendor' in request.session:
        if request.method == 'POST':
            registeruser  = vendor()
            registeruser.name = request.POST['uname']
            registeruser.email = request.POST['email']
            registeruser.mob = request.POST['mob']
            registeruser.password = request.POST['password']
            registeruser.add = request.POST['add']
            alreadyuser = vendor.objects.filter(email =  request.POST['email'])
            if len(alreadyuser) <= 0:
                registeruser.save()
                return render(request,'register.html')
            else:
                return render(request,'register.html',{'alreadyuser':"this email already exists..!"})
        else:
            return render(request,'register.html')
##########################################################################   inbuil method ###############################       

# def register(request):
#     if 'user' in request.session:
#         if request.method == 'POST':
#             registeruser  = registeration()
#             registeruser.name = request.POST['uname']
#             registeruser.email = request.POST['email']
#             registeruser.mob = request.POST['mob']
#             password = request.POST['password']  ##encrept password
#             registeruser.add = request.POST['add']
            
#             encr=make_password(password)
#             print("0000000000000000000000")
#             registeruser.password=encr
#             print("1111111111111111111111")
#             alreadyuser = registeration.objects.filter(email =  request.POST['email'])
#             # if alreadyuser:
#             #     return render(request,'register.html',{'alreadyuser':"this email already exists..!"})
#             # else:
#                 # registeruser.save()
#                 # return render(request,'register.html')
#             if alreadyuser:
                
#                 return render(request,'register.html',{'alreadyuser':"this email already exists..!"})
#             else:
#                 registeruser.save()
#                 return render(request,'register.html')
#         else:
#             return render(request,'register.html')
#     elif 'vendor' in request.session:   ##########################################################################
#         if request.method == 'POST':
#             registeruser  = vendor()
#             registeruser.name = request.POST['uname']
#             registeruser.email = request.POST['email']
#             registeruser.mob = request.POST['mob']
#             registeruser.password = request.POST['password']
#             registeruser.add = request.POST['add']
#             alreadyuser = vendor.objects.filter(email =  request.POST['email'])
#             if len(alreadyuser) <= 0:
#                 registeruser.save()
#                 return render(request,'register.html')
#             else:
#                 return render(request,'register.html',{'alreadyuser':"this email already exists..!"})
#         else:
#             return render(request,'register.html')
        
        
# def login(request):
#     if 'user' in request.session:
#         if request.method == 'POST':
#             try:
#                 userdata = registeration.objects.get(email = request.POST['email'])

#                 use_enter= request.POST['password']
#                 password_check=check_password(use_enter,userdata.password)
#                 print(1111111111111111111111)
#                 print(password_check)
#                 print(2222222222222222222222)
#                 if password_check:

#                     request.session['email'] = userdata.email
#                     request.session['userid'] = userdata.pk
                
                   
#                     return redirect('index')
#                 else:

#                     return render(request,'login.html',{'invalid':"Invalid credentials"})
#             except ObjectDoesNotExist:
                
#                 return render(request,'login.html',{'register':"you haven't registered yet"})
#         else:
#                 return render(request,'login.html')
#     elif 'vendor' in request.session:
#         if request.method == 'POST':
#             try:
#                 print(000000000000000000000000)
#                 userdata = vendor.objects.get(email = request.POST['email'])
#                 print(11111111111111111111)
#                 if userdata.password == request.POST['password']:
#                     print(22222222222222222222222)
#                     request.session['vemail'] = userdata.email  ############################################
#                     print(33333333333333333333333333333333)
#                     request.session['vendorid'] = userdata.pk
#                     print(444444444444444444444)
#                     return redirect('addproduct')
#                 else:
#                     print(5555555555555555555555555)
#                     return render(request,'login.html',{'invalid':"Invalid credentials"})
#             except ObjectDoesNotExist:
#                 print(66666666666666666666)
#                 return render(request,'login.html',{'register':"you haven't registered yet"})
#         else:
#                 return render(request,'login.html')
#     else:
#         return render(request,'login.html')

from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect

def login(request):
    if 'user' in request.session:
        if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')

            if not email or not password:
                return render(request, 'login.html', {'invalid': "Email and password are required"})

            try:
                userdata = registeration.objects.get(email=email)
                decrypted_password = descry(userdata.password)

                if decrypted_password and decrypted_password == password:
                    request.session['email'] = userdata.email
                    request.session['userid'] = userdata.pk
                    return redirect('index')
                else:
                    return render(request, 'login.html', {'invalid': "Invalid credentials"})
            except ObjectDoesNotExist:
                return render(request, 'login.html', {'register': "You haven't registered yet"})
            except Exception as e:
                print(f"Error during login: {e}")
                return render(request, 'error.html', {'error': 'An error occurred during login'})
        else:
            return render(request, 'login.html')

    elif 'vendor' in request.session:
        if request.method == 'POST':
            try:
                userdata = vendor.objects.get(email = request.POST['email'])
                if userdata.password == request.POST['password']:
                    request.session['vemail'] = userdata.email  
                    request.session['vendorid'] = userdata.pk
                    return redirect('addproduct')
                else:
                    return render(request,'login.html',{'invalid':"Invalid credentials"})
            except ObjectDoesNotExist:
                return render(request,'login.html',{'register':"you haven't registered yet"})
        else:
                return render(request,'login.html')
    else:
        return render(request,'login.html')
        

def index(request):
    if 'email' in request.session:
        catdata = Category.objects.all()
        loggedinuser = registeration.objects.get(email = request.session['email']) ### for dispaly name in index page ## get a email in perticular user
        
        return render(request,'index.html',{'category':catdata,'loggedin':loggedinuser.name})##get user name
    else:
        catdata = Category.objects.all()
        return render(request,'index.html',{'category':catdata})

def logout(request):
    if 'user' in request.session:
        del request.session['email']
        del request.session['user']
        print("user logggeddd outtttt")
        return redirect('index')
    elif 'vendor' in request.session:
        del request.session['vemail']
        print("vendorrrr loggggeeddd ouuuttttttttt")
        return redirect('login')



def profile(request):
    if 'email' in request.session:
        loggedinuser = registeration.objects.get(email = request.session['email'])
        if request.method == 'POST':
            loggedinuser.name = request.POST['name']
            loggedinuser.email = request.POST['email']
            loggedinuser.add = request.POST['add']
            loggedinuser.mob = request.POST['mob']
            loggedinuser.save()
        return render(request,'profile.html',{'loggedin':loggedinuser.name,'alldata':loggedinuser})
    else:
        return render(request,'profile.html')


def  update(request):
    blogdata = Blog.objects.get(name = 'bd')
    if request.method == 'POST':
        
        blogdata.name = request.POST['name']
        blogdata.email = request.POST['email']
        blogdata.save()
        return render(request,'update.html',{'blog':blogdata})
    else:
        
        
        return render(request,'update.html',{'blog':blogdata})




def changepass(request):
    if 'email' in request.session:
        userdata = registeration.objects.get(email = request.session['email'])
        if request.method == 'POST':
            if userdata.password == request.POST['opass']:
                if request.POST['npass'] == request.POST['cpass']:
                    userdata.password = request.POST['npass']
                    userdata.save()
                    return redirect('index')
                else:
                    return render(request,'changepass.html',{'confirm':"password and confirm password did not matched!!"})
            else:
                return render(request,'changepass.html',{'wrong':"Old password is incorrect!!"})
        else:
            return render(request,'changepass.html')
    else:
        return redirect('login')
    

def catpro(request,id):
    if 'email' in request.session:############################################### for categry page
        prodata = product.objects.filter(category = id)
        return render(request,'catpro.html',{'prodata':prodata ,'loggedin':True})
    else:
        prodata = product.objects.filter(category = id)
        return render(request,'catpro.html',{'prodata':prodata})



def prodetails(request,id):
    if 'email' in request.session:
        userdata = registeration.objects.get(email = request.session['email'])
        prodata = product.objects.get(id = id)
        if request.method == 'POST':
            cartdata = cart()
            cartdata.proid = id
            cartdata.userid = request.session['userid']
            cartdata.qty = request.POST['qty']
            cartdata.totalprice = prodata.price * int(cartdata.qty)
            alreadycart = cart.objects.filter(proid = id,userid = request.session['userid'],orderid = '0')
            try:
                if alreadycart:
                    updatecart = cart.objects.get(proid = id,userid = request.session['userid'])
                    updatecart.qty = int(updatecart.qty) + int(request.POST['qty'])
                    updatecart.save()
                    prodata.stock = int(prodata.stock) -  int(request.POST['qty'])
                    prodata.save()
                    return render(request,'product.html',{'prodata':prodata,'loggedin':userdata.name,'alreadycart':"this product is already in cart"})
                else:
                    cartdata.save()
                    prodata.stock = int(prodata.stock) -  int(cartdata.qty)
                    prodata.save()
                    return render(request,'product.html',{'prodata':prodata,'loggedin':userdata.name})
            except Exception as e:
                print(e)
                return render(request,'product.html',{'prodata':prodata,'loggedin':userdata.name,'integrity':"kale avjooooo!!!!"})
        else:
            return render(request,'product.html',{'prodata':prodata,'loggedin':userdata.name})
    else:
        prodata = product.objects.get(id = id)
        return render(request,'product.html',{'prodata':prodata})
    

def cartdata(request):
    if 'email' in request.session:
        prolist = []
        cartdata_u = cart.objects.filter(userid = request.session['userid'],orderid = '0')
        if cartdata_u:
            totalprice = 0
            for i in cartdata_u:
                prodata = product.objects.get(id = i.proid)
                prodict = {'cart_id':i.id,'proimage':prodata.image,'proprice':prodata.price,'qty':i.qty
                           ,'totalprice':i.totalprice}
                prolist.append(prodict)
                totalprice += int(i.totalprice)
            if 'outofstock'  in request.session:
                del request.session['outofstock']
                return render(request,'cart.html',{'loggedin':True,'prolist':prolist,'totalprice':totalprice
                                                   ,'outofstock':"Kalee avjee!!",'remove':'remove'})
            else:
                return render(request,'cart.html',{'loggedin':True,'prolist':prolist,'totalprice':totalprice
                                                   ,'remove':'remove'})
        else:
            return render(request,'cart.html',{'loggedin':True})
    else:
        return redirect('login')


def plusitem(request,cartid):
    cartitem = cart.objects.get(id = cartid)
    prodata = product.objects.get(id = cartitem.proid)
    if prodata.stock > 0:
        print("if blockkkkkkkkkkkkkkkkkkkkk")
        cartitem.qty = int(cartitem.qty) + 1
        prodata.stock = int(prodata.stock) - 1
        cartitem.save()
        prodata.save()
        return redirect('cartdata')
    else:
        print("elsee blockkkkkkkkkkkkkkkkkkkkkkkkkkk")
        request.session['outofstock'] = 1
        return redirect('cartdata')
    

def minusitem(request,cartid):
    cartdata = cart.objects.get(id = cartid)
    if cartdata.qty <= 1:
        prodata = product.objects.get(id = cartdata.proid)
        cartdata.delete()
        prodata.stock = int(prodata.stock) + 1
        prodata.save()
        return redirect('cartdata')
    else:
        cartdata.qty = int(cartdata.qty) - 1
        prodata = product.objects.get(id = cartdata.proid)
        prodata.stock = int(prodata.stock) + 1
        cartdata.save()
        prodata.save()
        return redirect('cartdata')
    
def removeone(request,cartid):
    cartpro = cart.objects.get(id = cartid)
    prod = product.objects.get(id = cartpro.proid)
    prod.stock = int(prod.stock) + int(cartpro.qty)
    prod.save()
    cartpro.delete()
    return redirect('cartdata')

def removeall(request):
    cartpro = cart.objects.filter(userid = request.session['userid'])
    for i in cartpro:
        prodata = product.objects.get(id = i.proid)
        prodata.stock = int(prodata.stock) + int(i.qty)
        prodata.save()
    cartpro.delete()
    return redirect('cartdata')


def checkout(request):
    if 'email' in request.session:
        userdata = registeration.objects.get(email = request.session['email'])
        total = 0
        cartdata = cart.objects.filter(userid = userdata.id,orderid = '0')
        proids = []
        for i in cartdata:
            total += int(i.totalprice)
            proids.append(i.proid)
        if request.method == 'POST':
            orderdata = order()
            orderdata.userid = userdata
            orderdata.proid = proids
            orderdata.add = request.POST['add']
            orderdata.city = request.POST['city']
            orderdata.state = request.POST['state']
            orderdata.pincode = request.POST['pin']
            orderdata.mobile = request.POST['mob']
            orderdata.paymenttype = request.POST['paymentvia']
            orderdata.transactionid = "1234"
            orderdata.total = total
            if orderdata.paymenttype == "cod":
                orderdata.save()
                orderid = order.objects.latest('id')
                for i in cartdata:
                    i.orderid = orderid.pk
                    i.save()
                return render(request,'checkout.html',{'loggedin':userdata.name,'userdata':userdata})
            else:
                request.session['amount'] = total
                request.session['proid'] = proids
                request.session['mob'] = request.POST['mob'] 
                request.session['pin'] = request.POST['pin']
                request.session['state'] = request.POST['state']
                request.session['city'] = request.POST['city']
                request.session['add'] = request.POST['add']
                return redirect('razorpayment')
        else:
            return render(request,'checkout.html',{'loggedin':userdata.name,'userdata':userdata})

    else:
        return redirect('login')
    
    
def vend_product(request):
        if 'vendor' in request.session:  #####################################3
            prodata=product()
            catdata=Category.objects.all()
            loggedinuser=vendor.objects.get(email=request.session['vemail'])

            if request.method=='POST' and request.FILES['image']:
                prodata.name=request.POST['name']
                prodata.stock=request.POST['qty']
                prodata.discription=request.POST['discription']
                prodata.price=request.POST['price']
                prodata.image=request.FILES['image']
                catid= request.POST['cat']
                prodata.catagory=Category.objects.get(id=catid)
                prodata.vendorid=loggedinuser
                prodata.save()
#             return render(request,'vendorproduct.html',{'prodata':prodata,'catdata':catdata,'loggedin':loggedinuser.name})
#         else:
#             return redirect('select')

# import razorpay

# RAZOR_KEY_ID = 'rzp_test_7OImT75w0b3T5s'
# RAZOR_KEY_SECRET = '2DyOadFeAUMu9vGCg2RFMXKj'

# razorpay_client = razorpay.Client(
#     auth=(RAZOR_KEY_ID, RAZOR_KEY_SECRET))

# def razorpayment(request):
#     currency = 'INR'
#     amount = int(request.session['amount']) * 100

#     razorpay_order = razorpay_client.order.create(dict(amount=amount,
#                                                        currency=currency,
#                                                        payment_capture='0'))
#     razorpay_order_id = razorpay_order['id']
#     callback_url = 'http://127.0.0.1:8000/paymenthandler/'
#     return render(request,'razorpay.html',{'razorpay_merchant_key':RAZOR_KEY_ID,
#                                            'razorpay_amount':amount,'currency':currency,
#                                            'razorpay_order_id':razorpay_order_id,
#                                            'callback_url':callback_url})


# from django.views.decorators.csrf import csrf_exempt
# from django.http import HttpResponseBadRequest

# @csrf_exempt
# def payemthandler(request):
#     if request.method == "POST":
#         try:
#             payment_id = request.POST.get('razorpay_payment_id', '')
#             razorpay_order_id = request.POST.get('razorpay_order_id', '')
#             signature = request.POST.get('razorpay_signature', '')

#             params_dict = {
#                 'razorpay_order_id': razorpay_order_id,
#                 'razorpay_payment_id': payment_id,
#                 'razorpay_signature': signature
#             }
#             result = razorpay_client.utility.verify_payment_signature(
#                 params_dict)

#             razorpay_client.payment.capture(payment_id, int(request.session['amount']) * 100)
#             loggedinuser = registeration.objects.get(email = request.session['email'])
#             neworder = order()
#             neworder.userid = loggedinuser
#             neworder.proid = request.session['proid']
#             neworder.add = request.session['add']
#             neworder.state = request.session['state']
#             neworder.pincode = request.session['pin']
#             neworder.city = request.session['city']
#             neworder.mobile = request.session['mob']
#             neworder.paymenttype = "onlibne"
#             neworder.total = request.session['amount']
#             neworder.transactionid = payment_id
#             neworder.save()
#             cartdata = cart.objects.filter(userid = loggedinuser.id,orderid = '0')
#             orderid = order.objects.latest('id')
#             for i in cartdata:
#                 i.orderid = orderid.pk
#                 i.save()
#             return render(request,'sucess.html')
#         except:
#             return HttpResponseBadRequest()
#     else:
#         return HttpResponseBadRequest()
###########################################################3 order history check ###############################################################

def orderhistory(request):
    userdata = registeration.objects.get(email = request.session['email'])
    ordereddata = cart.objects.filter(userid = userdata.pk)
    orederlist = []
    for i in ordereddata:
        if i.orderid != "0":
            productdetails = product.objects.get(id = i.proid)
            orderid = order.objects.get(id = i.orderid)
            prodict = {'proimg':productdetails.image,'proname':productdetails.name,
                       'prodes':productdetails.discription,'proprice':productdetails.price,
                       'orderid':orderid.pk,'total':orderid.total,'datetime':orderid.datetime,
                       'qty':i.qty} 
            orederlist.append(prodict)
    return  render(request,'orderhistory.html',{'loggedin':userdata,'orderlist':orederlist})


from django.core.mail import send_mail

def email_send(request):
    if request.method == 'POST':
        reciever = request.POST['email']
        send_mail(## using for all
            'This mail is for authentication',
            "You've been varified",## your massage
            'pqr6997@gmail.com',## email
            [reciever],## recever variable
            fail_silently = True
        )
        return render(request, 'sendemail.html', {'message': 'Email sent successfully!'})
    return render(request,'sendemail.html')

########################################################### email and otp ##########################################################
import random

# def send_otp(request):
#     otp = random.randint(0000, 9999)
#     reciever = request.session['email'] ## loginpage ma session create karyu tena mate
#     request.session['otp'] = otp  ## check otp mate teno upyog karvama avrche

#     send_mail(
#         'this is otp verification mail..',
#         f'Your OTP is{otp}',
#         'pqr699@gmail.com',
#         [reciever],
#         fail_silently = True
#     )
#     print(1555555515551151515151)
#     return redirect('check_otp')

def send_otp(request):
    otp = random.randint(1000, 9999)  # Ensure 4-digit OTP
    reciever = request.session.get('email')  # Safely get email from session

    if not reciever:
        return redirect('login')  # Redirect to login if session email is missing

    request.session['otp'] = otp  # Save OTP in session

    try:
        send_mail(
            'OTP Verification',
            f'Your OTP is: {otp}',
            settings.DEFAULT_FROM_EMAIL,  # Use configured email
            [reciever],
            fail_silently=False  # Fail loudly for better debugging
        )
    except Exception as e:
        print(f"Error sending OTP email: {e}")  # Log error
        return render(request, 'error.html', {'error': 'Failed to send OTP. Please try again.'})

    return redirect('check_otp')


# def check_otp(request):
#     if request.method == 'POST':
#         print(11111111111111111111)
#         userotp = request.POST['otp']
#         if int(userotp) == int(request.session['otp']):## 
#             print(222222222222222222222)
#             return redirect('index')
#         else:
#             print(333333333333333333333)
#             return render(request,'sendemail.html',{'invalid':"enter valid OTP"})
#     else:
#         print(444444444444444444444)
#         return render(request,'sendemail.html')


from django.shortcuts import render, redirect
import datetime

def check_otp(request):
    if request.method == 'POST':
        userotp = request.POST.get('otp')

        if not userotp:
            return render(request, 'sendemail.html', {'invalid': "OTP cannot be empty"})

        session_otp = request.session.get('otp')
        otp_expiry = request.session.get('otp_expiry')  # Add expiry mechanism

        if not session_otp or not otp_expiry:
            return render(request, 'sendemail.html', {'invalid': "OTP has expired. Please request a new one."})

        # Check OTP and expiration
        if datetime.datetime.now() > otp_expiry:
            return render(request, 'sendemail.html', {'invalid': "OTP has expired. Please request a new one."})
        if int(userotp) == int(session_otp):
            return redirect('index')
        else:
            return render(request, 'sendemail.html', {'invalid': "Invalid OTP"})
    else:
        return render(request, 'sendemail.html')

# Add OTP expiration during sending





















# -============================ vendor  -=========================== 



def addproduct(request):
    catdata = Category.objects.all()
    prodata = product()
    if request.method == 'POST':
        prodata.name = request.POST['pname']
        prodata.price = request.POST['price']
        prodata.discription = request.POST['description']
        prodata.stock = request.POST['stock']
        catrow = Category.objects.get(id = request.POST['cat'])
        prodata.category = catrow
        print(111111111111111111111111111111111)
        prodata.save()
        print(22222222222222222222)
        return redirect('index')
    else:
        return render(request,'addprod.html',{'catdata':catdata,'loggedin':True})

################################################# for roll selections ####################################################################
def selection(request):
    if request.method == 'POST':
        if request.POST['radiouv'] == 'user':
            request.session['user'] = 1
            return redirect('login')
        elif request.POST['radiouv'] == 'vendor':
            request.session['vendor'] = 1
            return redirect('login')
    else:
        return render(request,'select.html')
    
####################################### new register using ##################################################################################
def newregisterparctice(request):
    
    
    registeruser= register_new()
    registeruser.name = request.GET.get('uname')
    registeruser.email = request.GET.get('email')
    registeruser.mob = request.GET.get('mob')
    registeruser.password = request.GET.get('password')  ##encrept password
    registeruser.add = request.GET.get('add')
    registeruser.save()
    return render(request,'registernewpractice.html')



################################################### search functions #########################################################################
from django.db.models import Q
from django.shortcuts import render

def search(request):
    searchdata = request.GET.get('search', '')  # Get search query or default to an empty string
    datafaund = Q()  # Initialize an empty Q object

    if searchdata:
        search_terms = searchdata.split(" ")  # Split user input by spaces
        
        # Build the query for name, price, stock, and category
        for term in search_terms:
            datafaund |= (
                Q(name__icontains=term) |
                Q(price__icontains=term) |
                Q(stock__icontains=term) |
                Q(category__name__icontains=term)
            )
        
        # Try to parse a price range filter if the search term is a valid number
        try:
            price = float(searchdata)
            lower = price - 100
            upper= price + 100

            # Add price range condition to the query
            datafaund |= Q(price__gte=lower, price__lte=upper)
        except ValueError:
            pass  # Ignore if searchdata is not a valid number

    # Apply the query to filter products
    filter_products = product.objects.filter(datafaund)

    return render(request, "catpro.html", {'prodata': filter_products})

            
           
           
                
              
        # else:
           
        #     return render(request,'registernewpractice.html')
  
        


# from django.db.models import Q
# from django.shortcuts import render
# from app1.models import product

# def search(request):
#     search_ = request.GET.get('search', '').strip()  # convert into list[]
#     if not search_:
#         return render(request, "catpro.html", {'prodata': []})  # input na hoy tyare emty return 

#     # Split search query into terms
#     search = search_.split(" ")

#     # Initialize the Q object
#     query = Q()

#     for i in search:
#         if i.isdigit():  # Handle numeric input
#             number = int(i)
#             query |= Q(price=number) | Q(stock=number)
#         else:  # Handle string input
#             query |= Q(name__icontains=i) | Q(category__name__icontains=i)

#     # Fetch matching products
#     filtered_products = product.objects.filter(query)

#     return render(request, "catpro.html", {'prodata': filtered_products})
from .form import *
def blogformview(request):
    obj = blogform(request.POST)
    if obj.is_valid():
        obj.save()
        return render(request,'log.html')
    else:
        return render(request,'log.html')

from rest_framework.decorators import api_view
from rest_framework.response import Response
@api_view(['POST'])
def api_data(request):
    return Response({'1':"hello",'2':"world"})