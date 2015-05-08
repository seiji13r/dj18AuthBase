from django.test import TestCase

# Create your tests here.

from django.contrib.auth.models import User
from custom_auth.models import UserProfile
from django.core.exceptions import ObjectDoesNotExist


class CompletedProfiles(TestCase):
    def printing_users(self):
        """This Function List all Users"""
        print("\nPrinting Users: ")
        for user in User.objects.all():
            print("User: " , user.username)
            
    def check_profiles(self):
        """This Function For Profiles Set to Users"""
        print("\nChecking User Profiles: ")
        for user in User.objects.all():
            try:
                print(user," has a ",user.userprofile)
            except ObjectDoesNotExist:
                print(user, "has no User Profile Set")

    def create_missing_profiles(self):
        """This Function Fix Missing User Profile Objects"""
        print("Creating Missing User Profiles: ")
        for xuser in User.objects.all():
            try:
                print(xuser," has an",xuser.userprofile)
            except ObjectDoesNotExist:
                print(xuser, "Has no User Profile Set")
                current_profile = UserProfile( user = xuser)
                current_profile.save()

MyTest = CompletedProfiles()
MyTest.printing_users()
MyTest.check_profiles()
#MyTest.create_missing_profiles()