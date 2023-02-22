from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_email = models.CharField(max_length=50)
    user_name = models.CharField(max_length=20)
    user_password = models.CharField(max_length=20)
    def __str__(self):
        return self.user_email







# CREATE TABLE user (
# 	user_id	INT	NOT NULL AUTO_INCREMENT,
# 	user_email	VARCHAR(50)	NOT NULL,
# 	user_name	VARCHAR(20)	NOT NULL,
# 	user_password	VARCHAR(20)	NOT NULL,
# 	primary key(user_id)
# );