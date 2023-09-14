from django.contrib import admin
from .models import Blog,Category,Like,Comment

# Register your models here.

class LikeAdmin(admin.ModelAdmin):
    list_display = ('blog', 'user')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name','email','blog','text','created_at', 'updated_at')


# class BlogAdmin(admin.ModelAdmin):
#     list_display = ('title', 'author', 'category', 'created_at')
#     filter_horizontal = ()  # Keep the likes field with filter_horizontal

#     def get_urls(self):
#         from django.urls import path

#         # Add a custom URL pattern for the change view
#         info = self.model._meta.app_label, self.model._meta.model_name
#         urlpatterns = super().get_urls()
#         urlpatterns += [
#             path('<int:object_id>/comments/', self.admin_site.admin_view(self.comments_view), name='%s_%s_comments' % info),
#         ]
#         return urlpatterns

#     def comments_view(self, request, object_id):
#         # Custom view to display comments for the selected blog post
#         blog = self.get_object(request, object_id)
#         if blog is not None:
#             comments = blog.comment_set.all()  # Get all comments related to this blog
#             return self.render_change_form(
#                 request,
#                 context={'title': f'Comments for "{blog}"', 'comments': comments},
#             )
#         return self.response_404(request, object_id)


admin.site.register(Blog)
admin.site.register(Category)
admin.site.register(Like, LikeAdmin)
admin.site.register(Comment, CommentAdmin)
