from django.shortcuts import render
from django.views.generic import FormView
from community.forms import PostForm, ReplyForm
from django.views import generic
from community.models import Post, Comment
import markdown2


# Create your views here.
class PostCreateView(FormView):
    template_name = 'community/post_create.html'
    form_class = PostForm
    success_url = '/'

    def get_form_kwargs(self):
        kwargs = super(PostCreateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.save()
        return super(PostCreateView, self).form_valid(form)


class ReplyCreateView(FormView):
    template_name = ''
    form_class = ReplyForm
    success_url = '/'

    def get_form_kwargs(self):
        kwargs = super(ReplyCreateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.save()
        return super(ReplyCreateView, self).form_valid(form)


class IndexView(generic.ListView):
    model = Post
    template_name = "community/index.html"
    context_object_name = "post_list"

    # def get_queryset(self):
    #     post_list = Post.objects.filter(is_published=True)
    #     for post in post_list:
    #         post.body = markdown2.markdown(post.body, extras=['fenced-code-blocks'], )
    #     return post_list

    def get_context_data(self, **kwargs):
        kwargs['post_list'] = Post.objects.all().order_by('-last_modified_time')
        return super(IndexView, self).get_context_data(**kwargs)


class PostDetailView(generic.DetailView):
    pass
