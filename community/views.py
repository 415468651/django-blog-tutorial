from django.views.generic import FormView
from django.views import generic
import markdown2
from .forms import PostForm, CommentForm
from .models import Post, Comment


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


class CommentCreateView(FormView):
    template_name = ''
    form_class = CommentForm
    success_url = '/'

    def get_form_kwargs(self):
        kwargs = super(CommentCreateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.save()
        return super(CommentCreateView, self).form_valid(form)


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
        kwargs['post_list'] = Post.objects.all().order_by('-modified_date')
        return super(IndexView, self).get_context_data(**kwargs)


class PostDetailView(generic.DetailView):
    pass
