from django.db import models
from accounts.models import CustomUser
from posts.models import Post


class Profile(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    



class SavedHome(models.Model): 
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)

    def __str__(self): 
        return f'{self.user} liked {self.post}'


class Vote(models.Model): 
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)



class Recommendation(models.Model): 
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)

    def __str__(self):
        return f"{self.user.email} is suggested with postid {self.post.id} at time {self.created_at}"

    class Meta: 
        ordering = ['-created_at']



