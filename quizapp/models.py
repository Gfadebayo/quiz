from django.db import models

# Create your models here.

#Section -> Category -> Question -> Option

#Each Section holds several Categories and each Category holds several Questions
#finally, each Question holds several Option




class Section(models.Model):
    name = models.CharField(max_length=128)

    #Description might be nice
    #description

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=128)

    section = models.ForeignKey(Section, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"

class Question(models.Model):
    name = models.TextField()

    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    summary = models.TextField()

    keyword = models.TextField()

    def __str__(self):
        return self.name



class Option(models.Model):

    name = models.CharField(max_length=200)

    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    correct = models.BooleanField()

    def __str__(self):
        return self.name

class UserQuestion(models.Model):

    question_no = models.IntegerField(default=0)

    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    #An IntegerField is used instead of ForeignKey due to the fact that when the random Questions
    #are created, The user would definitely not have an answer ready
    selected_option_id = models.IntegerField(default=0)

    def __str__(self):
        return f"Question no {self.question_no}: {self.question.name}"


class Statistics():
    category = models.ForeignKey(Category, on_delete=models.CASCADE)



#Consider creating anoteher table order which will preserve the order in which questions were presented
#This is in case the user trues to go to a previous question so we wont show an entirely new one in its place

#class Order(models.Model):
#    #Field should be:
#
#    The question number that is displayed to the user. This will be attached to various options
#    question_number
#
#    The position it appeared in the question that is displayed to the user
#    position
#
#    We can use the option to get the Question they belong to
#    option_id
