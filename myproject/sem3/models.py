from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    biography = models.TextField()
    birthday = models.DateTimeField()

    def __str__(self):
        return f'Full name: {self.last_name} {self.name}'


class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    public_date = models.DateTimeField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    view_count = models.IntegerField(default=0)
    published = models.BooleanField(default=False)


class Comment(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    article = models.OneToOneField(Article, on_delete=models.CASCADE)
    content = models.TextField
    make_date = models.DateTimeField(auto_now=True)
    modify_date = models.DateTimeField(auto_now=True)


