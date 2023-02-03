from django.shortcuts import render
from .models import *

# Create your views here.


def forums (request):
    forums =Forums.objects.filter(forum_is_active=True)
    return render (request,"forums/forums.html",{
        "forums":forums,
    })

def posts (request,pk):
    forum =Forums.objects.get(pk=pk)
    posts =Forums_posts.objects.filter(post_forum=forum,post_is_active=True).order_by("-post_published_in")
    if request.method=="POST":
        if "title" in request.POST:
            title =request.POST ["title"]
        if "added_by" in request.POST:
            added_by =request.POST ["added_by"]
        if "content" in request.POST:
            content =request.POST ["content"]
        add_post =Forums_posts (post_name=title,post_forum=forum,post_content=content,posted_by=added_by)
        add_post.save()
    return render (request,"forums/posts.html",{
        "forum":forum,
        "posts":posts,
    })

def post (request,pk):
    post =Forums_posts.objects.get(pk=pk)
    comments =Forums_comments.objects.filter(comment_post=post,comment_is_active=True).order_by("-comment_published_in")
    if request.method=="POST":
        if "added_by" in request.POST:
            commented_by =request.POST ["added_by"]
        if "content" in request.POST:
            comment =request.POST ["content"]
        add_comment =Forums_comments(comment_forum=post.post_forum,comment_post=post,comment_content=comment,commented_by=commented_by)
        add_comment.save()
    return render (request,"forums/post.html",{
        "post":post,
        "comments":comments,
    })

def replies (request,pk):
    comment =Forums_comments.objects.get(pk=pk)
    replies =Forums_replies.objects.filter(reply_comment=comment,reply_is_active=True)
    if request.method=="POST":
        if "added_by" in request.POST:
            replyed_by =request.POST ["added_by"]
        if "content" in request.POST:
            reply =request.POST ["content"]
        add_reply =Forums_replies(reply_forum=comment.comment_forum,reply_post=comment.comment_post,reply_comment=comment,reply_content=reply,replyed_by=replyed_by)
        add_reply.save()
    return render (request,"forums/replies.html",{
        "comment":comment,
        "replies":replies,
    })
    
