
from django.shortcuts import get_object_or_404, redirect, render
from django.http import JsonResponse
from marketing.models import *
from marketing.forms import CallUsForm
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.conf import settings


def home(request):
     information = Information.objects.all()
     about = About.objects.all()
     services = Service.objects.filter(active=True)
     reviews = Reviews.objects.all()
     customers = Ourcustomers.objects.all()
     slide= Slide.objects.all()
     blog = Blog.objects.filter(active=True).order_by('-id')[:3]
     # chooseus = ChooseUs.objects.all()

     pricing_object = pricing.objects.first()
     golden_package = Golden_package.objects.all()
     silver_package = Silver_package.objects.all()
     bronze_package = Bronze_package.objects.all()
     if request.method == 'POST':
        form = CallUsForm(request.POST)
        if form.is_valid():

            form.save()
            return redirect('marketing:conform')

     else:
        form = CallUsForm()

     context = {
     'information':information,
     'slide':slide,
     'about':about,

     'services':services,
     'reviews':reviews,
     'customers':customers,
     'blog':blog,
     'form': form,
     'pricing_object':pricing_object,
     'golden_package':golden_package,
     'silver_package':silver_package,
     'bronze_package':bronze_package,

        }
     return render(request, 'home.html', context)



# def landing_page(request):
#      information = Information.objects.all()
#
#      context = {'information':information }
#      return render(request, 'landing_page.html', context)
#

def privacy_policy(request):
    information = Information.objects.all()
    policies = Policies.objects.all()  # Renamed the variable to 'policies'
    context = {'information': information, 'policies': policies}  # Updated variable name in the context
    return render(request, 'Privacy.html', context)

def about(request):
     about = About.objects.all()
     customers = Ourcustomers.objects.all()
     team = Team.objects.all()
     information = Information.objects.all()
     reviews = Reviews.objects.all()

     context = {
     'about':about,
     'information':information,
     'customers':customers,
     'reviews':reviews,
     'team':team

}
     return render(request, 'AboutUs.html', context)





def CallUs(request):
    information = Information.objects.all()
    if request.method == 'POST':
        form = CallUsForm(request.POST)
        if form.is_valid():
            form.save()
            # # Send email
            # name = form.cleaned_data['Name']
            # phone_number = form.cleaned_data['phone_number']
            # message = form.cleaned_data['Description']
            # subject = 'New CallUs Submission'
            # email_message = f"Name: {name}\nPhone Number: {phone_number}\nMessage: {message}"
            # send_mail(subject, email_message, settings.DEFAULT_FROM_EMAIL, ['amer66965@gmail.com'])
            # # Handle successful form submission (e.g., redirect or display a success message)
            return redirect('marketing:conform')
    else:
        form = CallUsForm()

    context = {'information': information, 'form': form}
    return render(request, 'CallUs.html', context)










def blog(request):
    blog_obj = Blog.objects.filter(active=True)
    paginator = Paginator(blog_obj, 2)  # Display 2 blog posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    information = Information.objects.all()
    context = {
        'page_obj': page_obj,
        'information': information
    }
    return render(request, 'blog.html', context)




def BlogDetails(request, id):
    blog_obj = get_object_or_404(Blog, id=id)
    information = Information.objects.all()
    category_id = blog_obj.category_id
    filtered_blogs = Blog.objects.filter(category_id=category_id)
    blog = filtered_blogs.exclude(id=id).order_by('-id')[:3]
    context = {
        'blog_obj': blog_obj,
        'information': information,
        'blog': blog,
    }
    return render(request, 'blog-details.html', context)

def service_all(request):
    services=Service.objects.filter(active=True)
    information = Information.objects.all()
    pricing_object = pricing.objects.first()
    golden_package = Golden_package.objects.all()
    silver_package = Silver_package.objects.all()
    bronze_package = Bronze_package.objects.all()
    context = {
     'services':services ,
     'information':information,
     'pricing_object':pricing_object,
     'golden_package':golden_package,
     'silver_package':silver_package,
     'bronze_package':bronze_package,
  }
    return render(request, 'Service.html', context)

def conform(request):
    services=Service.objects.filter(active=True)
    information = Information.objects.all()
    pricing_object = pricing.objects.first()
    golden_package = Golden_package.objects.all()
    silver_package = Silver_package.objects.all()
    bronze_package = Bronze_package.objects.all()
    context = {
     'services':services ,
     'information':information,
     'pricing_object':pricing_object,
     'golden_package':golden_package,
     'silver_package':silver_package,
     'bronze_package':bronze_package,
  }
    return render(request, 'conform.html', context)




def Works (request):
    works=work.objects.filter(active=True)
    information = Information.objects.all()
    context = { 'works':works ,'information':information }
    return render(request, 'Work.html', context)


def WorkDetails(request, id):
    Work = get_object_or_404(work, id=id)
    information = Information.objects.all()
    category_id = Work.category_id
    filtered_work = work.objects.filter(category=category_id,active=True)
    works = filtered_work.exclude(id=id).order_by('-id')[:3]
    context = {'work': Work, 'works': works, 'information': information}
    return render(request, 'Work-details.html', context)

def Career (request):
    job=JOB.objects.all()
    information = Information.objects.all()
    context = { 'job':job ,'information':information }
    return render(request, 'Career.html', context)



def ServiceDetails(request,id):
     service= get_object_or_404(Service,id=id)
     service_all=Service.objects.filter(active=True)
     information = Information.objects.all()
     context = {
     'service_all':service_all,
     'information':information,
     'service':service,
    }
     return render(request, 'service-details.html', context)



def Link_In_Bio(request):
    information = Information.objects.all()
    context = { 'information':information }
    return render(request, 'Link.html', context)
