from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic, View
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.forms import inlineformset_factory
from django.views.generic import CreateView, UpdateView, DeleteView

from .models import Post, PostImage, Comment
from .forms import PostForm, PostImagesForm, CommentForm

class PostListView(generic.ListView):
    model = Post
    template_name = 'waste/news.html'
    context_object_name = "news"

class PostDetailView(View):
    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        comments = post.comments.all()
        form = CommentForm()
        return render(request, 'waste/post.html', {'post': post, 'comments': comments, 'form': form})

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
        comments = post.comments.all()
        return render(request, 'waste/post.html', {'post': post, 'comments': comments, 'form': form})



class PostCreateView(generic.CreateView):
    model = Post
    form_class = PostForm
    template_name = 'news_create.html'
    success_url = '/'
    extra = 3

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['formset'] = inlineformset_factory(Post, PostImage, form=PostImagesForm, extra=self.extra)(
                self.request.POST, self.request.FILES, instance=self.object
            )
        else:
            data['formset'] = inlineformset_factory(Post, PostImage, form=PostImagesForm, extra=self.extra)()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        if formset.is_valid():
            form.instance.owner = self.request.user
            self.object = form.save()
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)

class PostUpdateView(generic.UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'news_update.html'
    success_url = reverse_lazy('/')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['formset'] = inlineformset_factory(Post, PostImage, form=PostImagesForm, extra=self.extra)(
                self.request.POST, self.request.FILES, instance=self.object
            )
        else:
            data['formset'] = inlineformset_factory(Post, PostImage, form=PostImagesForm, extra=self.extra)()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        if formset.is_valid():
            form.instance.owner = self.request.user
            self.object = form.save()
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)

class PostDeleteView(generic.DeleteView):
    model = Post
    success_url = reverse_lazy('/')

class CommentListView(generic.ListView):
    model = Comment
    template_name = 'post.html'
    context_object_name = "comments"


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        post = get_object_or_404(Post, id=self.kwargs['post_id'])
        form.instance.post = post
        form.instance.user = self.request.user

        replay_comment_id = self.request.POST.get('replay_comment')
        if replay_comment_id:
            form.instance.replay_comment = Comment.objects.get(id=replay_comment_id)

        self.object = form.save()

        if self.request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            response_data = {
                'success': True,
                'id': self.object.id,
                'username': self.object.user.username,
                'text': self.object.text,
                'created_at': self.object.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                'replay_comment': self.object.replay_comment.id if self.object.replay_comment else None,
            }
            return JsonResponse(response_data)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.kwargs['post_id']})


class CommentUpdateView(LoginRequiredMixin, UpdateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        self.object = form.save()
        if self.request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({'success': True, 'text': self.object.text})
        return super().form_valid(form)

    def form_invalid(self, form):
        if self.request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({'success': False})
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.object.post.id})


class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()

        # Ensure only administrators can delete any comment, while authors can only delete their own comments
        if request.user.is_superuser or self.object.user == request.user:
            self.object.delete()
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({'success': True})
            return redirect(success_url)
        else:
            # Handle unauthorized deletion attempt
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({'success': False, 'error': 'Unauthorized'})
            # You may choose to raise a 403 Forbidden or redirect to an error page
            return redirect(success_url)  # Redirect to success URL as fallback

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.object.post.id})


class ReplyCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        parent_comment = get_object_or_404(Comment, id=self.kwargs['parent_id'])
        form.instance.post = parent_comment.post  # Link reply to the parent post
        form.instance.user = self.request.user
        form.instance.replay_comment = parent_comment  # Set the parent comment for reply

        self.object = form.save()

        if self.request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            response_data = {
                'success': True,
                'id': self.object.id,
                'username': self.object.user.username,
                'text': self.object.text,
                'created_at': self.object.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                'replay_comment': self.object.replay_comment.id if self.object.replay_comment else None,
            }
            return JsonResponse(response_data)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.object.post.id})


class ReplyUpdateView(LoginRequiredMixin, UpdateView):
    model = Comment
    form_class = CommentForm

    def get_object(self, queryset=None):
        return get_object_or_404(Comment, id=self.kwargs['reply_id'])

    def form_valid(self, form):
        self.object = form.save()

        if self.request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({'success': True, 'text': self.object.text})
        return super().form_valid(form)

    def form_invalid(self, form):
        if self.request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({'success': False})
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.object.post.id})


class ReplyDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()

        # Ensure only administrators can delete any reply, while authors can only delete their own replies
        if request.user.is_superuser or self.object.user == request.user:
            self.object.delete()
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({'success': True})
            return redirect(success_url)
        else:
            # Handle unauthorized deletion attempt
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({'success': False, 'error': 'Unauthorized'})
            # You may choose to raise a 403 Forbidden or redirect to an error page
            return redirect(success_url)  # Redirect to success URL as fallback

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.object.post.id})



class CommentDetailView(generic.DetailView):
    model = Comment
    template_name = 'comment_detail.html'
    pk_url_kwarg = 'pk'






# @require_POST
# def post_detail(request, post_id):
#     post = get_object_or_404(Post, pk=post_id)
#     text = request.POST.get('text')
#     Comment.objects.create(post=post, user=request.user, text=text)
#     return redirect('post_detail', pk=post_id)


