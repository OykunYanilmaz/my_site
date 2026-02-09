from django.shortcuts import render
from datetime import date

all_posts = [
    {
        "slug": "hike-in-the-mountains",
        "image": "mountains.jpg",
        "author": "Oykun",
        "date": date(2025, 2, 9),
        "title": "Mountain Hiking",
        "excerpt": "There is nothing like the views you get when hiking in the mountains! And I wasn't even prepared for what happened whilst I was enjoying the view!",
        "content": """
            Lorem ipsum dolor sit amet consectetur adipisicing elit. 
            Animi officia harum dolores aut doloremque at suscipit totam adipisci? 
            Fugiat quam enim necessitatibus, sint facere dolores quae quis magni dicta consectetur.

            Lorem ipsum dolor sit amet consectetur adipisicing elit. 
            Animi officia harum dolores aut doloremque at suscipit totam adipisci? 
            Fugiat quam enim necessitatibus, sint facere dolores quae quis magni dicta consectetur.

            Lorem ipsum dolor sit amet consectetur adipisicing elit. 
            Animi officia harum dolores aut doloremque at suscipit totam adipisci? 
            Fugiat quam enim necessitatibus, sint facere dolores quae quis magni dicta consectetur.
        """
    },
    {
        "slug": "programming-is-fun",
        "image": "coding.jpg",
        "author": "Oykun",
        "date": date(2025, 11, 11),
        "title": "Programming Is Great!",
        "excerpt": "Did you ever spend hours searching that one error in your Code!",
        "content": """
            Lorem ipsum dolor sit amet consectetur adipisicing elit. 
            Animi officia harum dolores aut doloremque at suscipit totam adipisci? 
            Fugiat quam enim necessitatibus, sint facere dolores quae quis magni dicta consectetur.

            Lorem ipsum dolor sit amet consectetur adipisicing elit. 
            Animi officia harum dolores aut doloremque at suscipit totam adipisci? 
            Fugiat quam enim necessitatibus, sint facere dolores quae quis magni dicta consectetur.

            Lorem ipsum dolor sit amet consectetur adipisicing elit. 
            Animi officia harum dolores aut doloremque at suscipit totam adipisci? 
            Fugiat quam enim necessitatibus, sint facere dolores quae quis magni dicta consectetur.
        """
    },
    {
        "slug": "into-the-woods",
        "image": "woods.jpg",
        "author": "Oykun",
        "date": date(2026, 1, 28),
        "title": "Nature At Its Best",
        "excerpt": "Nature is Amazing!",
        "content": """
            Lorem ipsum dolor sit amet consectetur adipisicing elit. 
            Animi officia harum dolores aut doloremque at suscipit totam adipisci? 
            Fugiat quam enim necessitatibus, sint facere dolores quae quis magni dicta consectetur.

            Lorem ipsum dolor sit amet consectetur adipisicing elit. 
            Animi officia harum dolores aut doloremque at suscipit totam adipisci? 
            Fugiat quam enim necessitatibus, sint facere dolores quae quis magni dicta consectetur.

            Lorem ipsum dolor sit amet consectetur adipisicing elit. 
            Animi officia harum dolores aut doloremque at suscipit totam adipisci? 
            Fugiat quam enim necessitatibus, sint facere dolores quae quis magni dicta consectetur.
        """
    }
]


def get_date(post):
    return post['date']

def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })


def posts(request):
    return render(request, "blog/all-posts.html", {
        "all_posts": all_posts
    })


def post_detail(request, slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, "blog/post-detail.html", {
        "post": identified_post
    })
