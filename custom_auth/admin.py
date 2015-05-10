from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from custom_auth.models import UserProfile

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class UserProfileInLine(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'User Profiles'

# Define a new User admin
class UserAdmin(UserAdmin):
   def add_view(self, *args, **kwargs):
      self.inlines = []
      return super(UserAdmin, self).add_view(*args, **kwargs)

   def change_view(self, *args, **kwargs):
      self.inlines = [UserProfileInLine]
      return super(UserAdmin, self).change_view(*args, **kwargs)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)