from django.shortcuts import render, redirect,Http404
from .models import Post, BlogComment
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# show blog newsfeed
@login_required(login_url='/')
def foxBlog(request):
    try:
        total = Post.objects.all().count()
        allpost = Post.objects.all().order_by('-time')
        context = {'allpost': allpost, 'total': total, 'sbar': 'blog'}
        return render(request, 'blog/blog.html', context)
    except:
        return HttpResponse("Page Not Found ....")

# showing single post in detail
@login_required(login_url='/')
def foxdetailpost(request, slug):
    try:
        postdetail = Post.objects.filter(slug=slug).first()
        comments = BlogComment.objects.filter(
                post=postdetail).order_by('-time')
        totalcomment = BlogComment.objects.filter(post=postdetail).count()
        context = {'sbar':'blog','postdetail': postdetail, 'comments':
                    comments, 'totalcomment': totalcomment,
                    }
        return render(request, 'blog/detailpost.html', context)
    except:
        return HttpResponse("Page Not Found ....")

# commenting on post
@login_required(login_url='/')
def comment_post(request):
    try:
        if request.method == 'POST':
            postSno = request.POST.get('postsno')
            post = Post.objects.get(sno=postSno)
            user = request.user
            comment = request.POST.get('newcomment')
            create_comment = BlogComment.objects.create(
                    comment=comment, post=post, user=user)
            create_comment.save()
            path_red = request.POST.get('next', '/')
            return redirect(path_red)
    except:
        return HttpResponse("Page Not Found ....")