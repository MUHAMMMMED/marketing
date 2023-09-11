
from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField



class Information(models.Model):#
   LOGO = models.FileField(upload_to = "files/images/Home/Information/Image/%Y/%m/%d/",blank=True, null=True)
   FaviconIco= models.FileField(upload_to = "files/images/Home/Information/Image/%Y/%m/%d/",blank=True, null=True)
   WebName= models.CharField(max_length = 300 ,blank=True, null=True)
   Description = models.CharField(max_length = 300 , null = True)
   Address= models.CharField(max_length=300, blank=True, null=True)
   Map_Address= models.CharField(max_length=500,blank=True, null=True)
   Gmail= models.CharField(max_length = 300 ,blank=True, null=True)
   PHONE = models.CharField(max_length = 20 ,blank=True, null=True)
   Twitterlinke= models.CharField(max_length=500,blank=True, null=True)
   instagramlinke= models.CharField(max_length=500,blank=True, null=True)
   facebooklinke= models.CharField(max_length=500,blank=True, null=True)
   Youtubelinke= models.CharField(max_length=500,blank=True, null=True)
   linkedinlinke= models.CharField(max_length=500,blank=True, null=True)
   Whatsapp= models.CharField(max_length=20,blank=True, null=True)
   snapchat= models.CharField(max_length=200,blank=True, null=True)
   pixal_id= models.CharField(max_length=200,blank=True, null=True)
   Copyright = models.CharField(max_length = 200 ,blank=True, null=True)

   def __str__(self):
         return self.WebName

class CallUs(models.Model):
     Name = models.CharField(max_length=100, blank=True, null=True)
     phone_number= models.CharField(max_length = 20 ,blank=True, null=True)
     Description = models.CharField(max_length = 1000 , null = True)
     def __str__(self):
         return self.Name

class Categories(models.Model):
    Name = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return self.Name


class Slide(models.Model):
     Image = models.FileField(upload_to = "files/images/Slide/Image/%Y/%m/%d/",blank=True, null=True)
     Titel= models.CharField(max_length = 300 , null = True)
     Description = models.CharField(max_length = 300 , null = True)
     Customers= models.IntegerField(default=0, blank=True, null=True)
     Projects= models.IntegerField(default=0, blank=True, null=True)
     team= models.IntegerField(default=0, blank=True, null=True)
     def __str__(self):
        return self.Titel



class About(models.Model):
     Image = models.FileField(upload_to = "files/images/About/photos/Image/%Y/%m/%d/",blank=True, null=True)
     Titel= models.CharField(max_length = 300 , null = True)
     Description = models.CharField(max_length = 300 , null = True)
     Point1 = models.CharField(max_length = 300 , null = True)
     Point2 = models.CharField(max_length = 300 , null = True)
     Point3 = models.CharField(max_length = 300 , null = True)
     Point4 = models.CharField(max_length = 300 , null = True)
     Point5 = models.CharField(max_length = 300 , null = True)
     def __str__(self):
        return self.Titel




# class ChooseUs(models.Model):
#      Experience = models.CharField(max_length = 300 , null = True)
#      CustomSolutions= models.CharField(max_length = 300 , null = True)
#      StrongNetwork= models.CharField(max_length = 300 , null = True)
#      Customers= models.IntegerField(default=0, blank=True, null=True)
#      Projects= models.IntegerField(default=0, blank=True, null=True)
#      Hours_of_support= models.IntegerField(default=0, blank=True, null=True)
#      team= models.IntegerField(default=0, blank=True, null=True)
#      def __str__(self):
#         return self.Experience





class Service(models.Model):
      created_at = models.DateTimeField(auto_now_add=True)
      active = models.BooleanField(default = False)
      keywords = models.CharField(max_length=300, blank=True, null=True)
      category=models.ForeignKey(Categories,on_delete=models.CASCADE, related_name='Service', blank=True, null=True)
      Image = models.FileField(upload_to = "files/images/Service/photos/Image/%Y/%m/%d/",blank=True, null=True)
      Title= models.CharField(max_length = 300 , null = True)
      Description= models.CharField(max_length = 300 , null = True)
      slideImage =models.FileField(upload_to = "files/images/Service/slideImage/%Y/%m/%d/",blank=True, null=True)
      slideVideo= models.CharField(max_length=300,blank=True, null=True)
      body= RichTextField()
      def __str__(self):
        return self.Title

class work(models.Model):
      created_at = models.DateTimeField(auto_now_add=True)
      active = models.BooleanField(default = False)
      keywords = models.CharField(max_length=300, blank=True, null=True)
      category=models.ForeignKey(Categories,on_delete=models.CASCADE, related_name='work', blank=True, null=True)
      Image = models.FileField(upload_to = "files/images/work/photos/Image/%Y/%m/%d/",blank=True, null=True)
      Image1 = models.FileField(upload_to = "files/images/work/photos/Image/%Y/%m/%d/",blank=True, null=True)
      Image2 = models.FileField(upload_to = "files/images/work/photos/Image/%Y/%m/%d/",blank=True, null=True)
      Image3 = models.FileField(upload_to = "files/images/work/photos/Image/%Y/%m/%d/",blank=True, null=True)
      Image4 = models.FileField(upload_to = "files/images/work/photos/Image/%Y/%m/%d/",blank=True, null=True)
      Image5 = models.FileField(upload_to = "files/images/work/photos/Image/%Y/%m/%d/",blank=True, null=True)
      Title= models.CharField(max_length = 300 , null = True)
      Client= models.CharField(max_length = 300 , null = True)
      Location= models.CharField(max_length = 400 , null = True)
      body= RichTextField()

      def __str__(self):
        return self.Client


class pricing(models.Model):
      Silver_package= models.CharField(max_length = 50 , null = True)
      Golden_package= models.CharField(max_length = 50 , null = True)
      Bronze_package= models.CharField(max_length = 50 , null = True)

class Golden_package(models.Model):
      Description= models.CharField(max_length = 300 , null = True)
      def __str__(self):
        return self.Description

class Silver_package(models.Model):
      Description= models.CharField(max_length = 300 , null = True)
      def __str__(self):
        return self.Description

class Bronze_package(models.Model):
      Description= models.CharField(max_length = 300 , null = True)
      def __str__(self):
        return self.Description

# class businessplan(models.Model):
#       Description= models.CharField(max_length = 300 , null = True)
#       def __str__(self):
#         return self.Description

class Reviews(models.Model):
     Image1 = models.FileField(upload_to = "files/images/Reviews/photos/Image/%Y/%m/%d/",blank=True, null=True)
     Description1 = models.CharField(max_length = 500 , null = True)
     Image2 = models.FileField(upload_to = "files/images/Reviews/photos/Image/%Y/%m/%d/",blank=True, null=True)
     Description2 = models.CharField(max_length = 500 , null = True)
     Image3 = models.FileField(upload_to = "files/images/Reviews/photos/Image/%Y/%m/%d/",blank=True, null=True)
     Description3 = models.CharField(max_length = 500 , null = True)
     Image4 = models.FileField(upload_to = "files/images/Reviews/photos/Image/%Y/%m/%d/",blank=True, null=True)
     Description4 = models.CharField(max_length = 500 , null = True)
     # def __str__(self):
     #    return self.Name

class Ourcustomers(models.Model):
     Title= models.CharField(max_length = 300 , null = True)
     Image = models.FileField(upload_to = "files/images/Reviews/photos/Image/%Y/%m/%d/",blank=True, null=True)
     def __str__(self):
        return self.Title


class Team(models.Model):
     Image = models.FileField(upload_to = "files/images/team/photos/Image/%Y/%m/%d/",blank=True, null=True)
     Name = models.CharField(max_length=100,blank=True, null=True)
     jobtitel= models.CharField(max_length = 300 , null = True)
     def __str__(self):
        return self.Name


class Blog(models.Model):
   created_at = models.DateTimeField(auto_now_add=True)
   active = models.BooleanField(default = False)
   keywords = models.CharField(max_length=300, blank=True, null=True)
   category=models.ForeignKey(Categories,on_delete=models.CASCADE, related_name='Blog', blank=True, null=True)
   Image = models.FileField(upload_to = "files/images/Blog/Image/%Y/%m/%d/",blank=True, null=True)
   Titel= models.CharField(max_length = 300 , null = True)
   slideImage =models.FileField(upload_to = "files/images/Blog/slideImage/%Y/%m/%d/",blank=True, null=True)
   slideVideo= models.CharField(max_length=300,blank=True, null=True)
   body= RichTextField()

   def __str__(self):
        return self.Titel




class Policies(models.Model):
   body= RichTextField()



class JOB(models.Model):
    remote_work = 'العمل عن بعد'
    available = 'متاحة'
    Hired = 'تم التوظيف'
    FullTime = 'دوام كامل'
    partTime = 'دوام جزئي'
    Undefined = 'غير مذكور'
    CHOICES_available = (
        (available, 'متاحة'),
        (Hired, 'تم التوظيف'),
    )
    CHOICES_Job_type = (
        (FullTime, 'دوام كامل'),
        (partTime, 'دوام جزئي'),
        (remote_work, 'العمل عن بعد' ),
        (Undefined, 'غير مذكور'),
    )
    created_at = models.DateTimeField(auto_now_add=True)
    Jobtitel = models.CharField(max_length=300, null=True)
    Job_type = models.CharField(max_length=30, choices=CHOICES_available, default=FullTime)
    job_type_available = models.CharField(max_length=30, choices=CHOICES_Job_type, default=available)

    def __str__(self):
        return self.Jobtitel
