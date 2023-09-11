from django.urls import path
from marketing.views import *
from django.conf import settings
from django.conf.urls.static import static
app_name='marketing'

urlpatterns = [

  path('',home, name="home"),
  path('Team',Team, name="Team"),
  path('About',about, name="About"),
  path('CallUs',CallUs, name="CallUs"),

  path('Bio',Link_In_Bio, name="Link_In_Bio"),
  path('portfolio',Works, name="Work"),
  path('conform',conform, name="conform"),
  path('Careers',Career, name="Career"),
  # path('landing',landing_page, name="landing_page"),
  path('blog',blog, name="blogAll"),
  path('Service',service_all, name="service_all"),
  path('Policies',privacy_policy, name="privacy_policy"),
  path('portfolio/<int:id>/',WorkDetails, name="WorkDetails"),
  path('Blog/<int:id>/',BlogDetails, name="blogdetails"),
  path('Service/<int:id>/',ServiceDetails, name="servicedetails"),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
