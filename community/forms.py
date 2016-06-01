from django.forms import ModelForm, Textarea, CharField
from .models import Post, Comment


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'topic']

        error_messages = {
            'title': {
                'max_length': "标题过长，最多70个字。"
            }
        }

        # widgets = {
        #     'title': CharField(),
        #     'body': Textarea(),
        # }

    def __init__(self, *args, **kwargs):
        # form 实例化是需要视图函数提供 user 参数
        self.user = kwargs.pop('user')
        super(PostForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        post = super(PostForm, self).save(commit=False)
        post.author = self.user
        post.save()
        return post


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

        # widgets = {
        #     'content': Textarea()
        # }

    def __init__(self, *args, **kwargs):
        # form 实例化是需要视图函数提供 user 参数
        self.user = kwargs.pop('user')
        super(CommentForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        comment = super(CommentForm, self).save(commit=False)
        comment.reply_user = self.user
        comment.save()
        return comment
