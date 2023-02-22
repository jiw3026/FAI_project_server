from django.db import models
# from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Diagnosis(models.Model):
    diag_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey("user.User", related_name="user", on_delete=models.CASCADE, db_column="user_id")
    diag_date = models.DateField(auto_now_add=True)
    diag_image = models.ImageField(upload_to="diagnosis/images/", null=True, blank=True)
    # diag_percent0 = models.FloatField(validators=[MinValueValidator(0.0),MaxValueValidator(100.0)])
    # diag_percent1 = models.FloatField(validators=[MinValueValidator(0.0),MaxValueValidator(100.0)])
    # diag_percent2 = models.FloatField(validators=[MinValueValidator(0.0),MaxValueValidator(100.0)])
    # diag_percent3 = models.FloatField(validators=[MinValueValidator(0.0),MaxValueValidator(100.0)])
    # diag_percent4 = models.FloatField(validators=[MinValueValidator(0.0),MaxValueValidator(100.0)])
    # diag_percent5 = models.FloatField(validators=[MinValueValidator(0.0),MaxValueValidator(100.0)])
    def __str__(self):
        return self.diag_id
    


# CREATE TABLE diagnosis (
# 	diag_id INT NOT NULL AUTO_INCREMENT,
# 	user_id INT NOT NULL,
# 	diag_name VARCHAR(30) NOT NULL,
# 	diag_date DATE NOT NULL,
# 	diag_image VARCHAR(100) NULL,
# 	diag_percent INT NOT NULL,
# 	primary key(diag_id),
# 	foreign key(user_id) references user(user_id) on delete cascade
# );