from django.shortcuts import render,HttpResponse,redirect
from matplotlib.pyplot import title
from product.models import *
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, request
from django.contrib.auth.models import User
from .models import *
from users.models import address as add
from users.models import payment 
from django.contrib.auth.decorators import login_required, permission_required


def home(request):
    context={}
    user=request.user
    print(user)
    items=carousel.objects.all()[:3]
    products=product.objects.all()[:6]
    if user.is_authenticated:
        if history.objects.filter(user=user.id).exists():
            recomondations=history.objects.filter(user=user.id).latest('id')
            c=recomondations.parent+recomondations.category
            print(c)
            cat=category.objects.get(slug=c)
            pr=product.objects.filter(parent_category=cat.id)[:3]
            print(len(pr))
            context.update({'rec':pr})


           

            print(recomondations.id) 
    else:
        pass
    
       

    context.update({'use':user})
    context.update({'items':items})
    context.update({'products':products})

    

    print(context.keys())
        
    


    
    return render(request,'home/home.html',context)
    
def men(request,catt):
    x=category.objects.get(slug=catt)
    tshirts=product.objects.filter(parent_category=x.id)
   

    
    
  
    context={
        'subc':tshirts,

        
    }
    return render(request,'home/product.html',context)


def login(request):
    return render(request,'home/login.html')


def productdetail(request,the_slug): 
    context={}
    user=request.user
    prod=product.objects.get(slug=the_slug)
    if user.is_authenticated:
        hist=history(user=user,parent=prod.parent_category.parent_category,category=prod.parent_category)
        hist.save()
   
    if request.method!='POST':
        print("notpost")
        x=product.objects.get(slug=the_slug)
        y=images.objects.filter(img_product=x.id)
        key=1
        ok=1
        if x.title=="Full Sleeve T Shirt":
            reco=rec.objects.get(main=x.id)
            context.update({'re':reco})
            context.update({'ok':ok})
    

        if x.des=="yes":
            key1=0
            key=0
            variant=attributes.objects.filter(product=x.id)
            s=attributes.objects.filter(product=x.id,size=variant[0].size)
            sizes = attributes.objects.raw('SELECT * FROM  product_attributes  WHERE product_id=%s GROUP BY size_id',[x.id])
            context.update({'c':s})
            context.update({'q':sizes})
            context.update({'key':key})
            context.update({'key1':key1})

            print(x.content)
            print(context.keys())

        b=x.id
        context.update({'w':x})
        context.update({'i':y})
        context.update({'l':b})
        context.update({'key':key})
        print(key)



    if request.method=='POST':
        print("post")
        key1=0
        name=request.POST.get("id")
        var=attributes.objects.get(id=name)
        imag=img_attributes.objects.filter(product=var.id)
        pr=var.product.id
        key=2
        print(key)
        sizes = attributes.objects.raw('SELECT * FROM  product_attributes  WHERE product_id=%s GROUP BY size_id',[pr])
        s=attributes.objects.filter(product=pr,size=var.size)
        context.update({'i': imag})
        context.update({'w':var})
        context.update({'l':pr})
        context.update({'q':sizes})
        context.update({'c':s})
        context.update({'key':key})
        context.update({'key1':key1})





   
   
    

    print(context.keys())
    return render(request,'home/productdetail.html',context)
@login_required
def cartdispaly(request):
    customer=request.user
    print(customer)
    cartitems=cart.objects.filter(owner=customer.id)
    count=cartitems.count()
    print(count)
    numbers=[1,2,3,4,5,6,7,8,9,10]
    context={
        'c':cartitems,
        'count':count,
        'numbers':numbers,
    }
    return render(request,'home/cart.html',context)




def ajaxdisplay(request):
    if request.POST.get('action') == 'post':
        size_id = request.POST.get('size')
        productid = request.POST.get('productid')
        print(size_id)
        print(productid)
        prod=product.objects.get(id=productid)
        v=attributes.objects.filter(product=productid,size=size_id)
        print(v)
        context={
         'c':v,
         'pr':prod
        }
        return render(request,'home/test.html',context)

@login_required
def addtocart(request):
    user=request.user
    id=request.POST.get('id')
    key=request.POST.get('key')
    print(key)
    
    if key=='1':
        print("ok")
        main_product=product.objects.get(id=id)
        print(main_product.price)
        title=main_product.title
        number=request.POST.get('n')
        a=cart(owner=user,main_product=main_product,quantity=number,title=title)
        a.save()
    if key=='2':
        cart_product=attributes.objects.get(id=id)
        print(cart_product)
        title=cart_product.product
        print(cart_product.price)
        number=request.POST.get('n')
        a=cart(owner=user,cart_product=cart_product,quantity=number,title=title)
        a.save()
    return redirect('showcart')

def cartdelete(request):
    id=request.POST.get('id')
    print(id)
    
    item=cart.objects.get(id=id)
    item.delete()
    return HttpResponseRedirect('/cart')

def paymen(request):
    
    return render(request,'home/payment.html')


def checkout(request):
    user=request.user
    items=cart.objects.filter(owner=user.id)
    print(items)
    for i in items:
        if i.main_product==None:
            print("hello")
            it=attributes.objects.get(id=i.cart_product.id)
            
            p=payment(parent=i.cart_product.parent_category.parent_category,category=i.cart_product.parent_category.title,user=user,cart_product=it)
            p.save()
        else:
            it=product.objects.get(id=i.main_product.id)

            p=payment(parent=i.main_product.parent_category.parent_category,category=i.main_product.parent_category.title,user=user,main_product=it)
            p.save()
    return redirect('home')

    
@login_required
def myorders(request):
    user=request.user
    p=payment.objects.filter(user=user.id)
    count=p.count()
    context={}
    rec=payment.objects.filter(user=user.id).latest('id')

    
    pc=rec.main_product.parent_category.parent_category.title
    c=rec.main_product.parent_category.title
    z= pc+c
    if z=="menshirts":
        pd=category.objects.get(slug="menjeans")
        a=product.objects.filter(parent_category=pd.id)
        context.update({'f':a})
    elif z=="mentshirts":
        pd=category.objects.get(slug="mentrousers")
        a=product.objects.filter(parent_category=pd.id)
        context.update({'f':a})
    elif z=="menjeans":
        pd=category.objects.get(slug="menshirts")
        a=product.objects.filter(parent_category=pd.id)
        context.update({'f':a})
    elif z=="mentrousers":
        pd=category.objects.get(slug="mentshirts")
        a=product.objects.filter(parent_category=pd.id)
        context.update({'f':a})




        
    print(c)
    context.update({'orders':p})
    context.update({'count':c})
    print(context.keys())

    return render(request,'home/myorder.html',context)

def cancellation(request):
    id=request.POST.get('id')
    print(id)
    reason=request.POST.get('reason')
    order=payment.objects.get(id=id)
    print(order)
    order.delete()
    return redirect('home')

