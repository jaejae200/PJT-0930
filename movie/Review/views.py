from django.shortcuts import render, redirect
from .models import Review

# Create your views here.


def index(request):
    Reviews = Review.objects.all()

    context = {
        "Reviews": Reviews,
    }

    return render(request, "Review/index.html", context)


def detail(request, pk):
    detail = Review.objects.get(pk=pk)

    context = {
        "detail": detail,
    }

    return render(request, "Review/detail.html", context)


def new(request):
    return render(request, "Review/new.html")


def create(request):
    title = request.GET.get("title")
    content = request.GET.get("content")

    Review.objects.create(title=title, content=content)

    return redirect("Review:index")


def edit(request, pk):
    edit = Review.objects.get(pk=pk)

    context = {
        "edit": edit,
    }

    return render(request, "Review/edit.html", context)


def update(request, pk):
    update = Review.objects.get(pk=pk)
    title = request.GET.get("title")
    content = request.GET.get("content")

    update.title = title
    update.content = content

    update.save()

    return redirect("Review:detail", update.pk)


def delete(request, pk):
    Review.objects.get(pk=pk).delete()

    return redirect("Review:index")
