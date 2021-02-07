import random
from .models import UserQuestion, Question, Category

#Im having trouble thinking of categories so for now
#ill scrap it but leave the table and instead just use the
#secion the category belongs to to generate the questions
def load_questions(category_id, amount=20):
    """Takes care of loading the UserQuestion table with questios
        that will be displayed to the user"""
    #Clear the table before loading new questions
    UserQuestion.objects.all().delete()

    #section_categories = Category.objects.filter(id=category_id).values_list('id', flat=True)
    question_ids = list(Question.objects.filter(category_id = category_id)[:amount])
    random.shuffle(question_ids)

    print(question_ids)

    return map(lambda i: UserQuestion(question_no=i+1, question=question_ids[i]), range(0, len(question_ids)))
