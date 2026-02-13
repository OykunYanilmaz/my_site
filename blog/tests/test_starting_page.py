import pytest
from django.urls import reverse
from http import HTTPStatus
from blog.models import Post, Tag
from datetime import date, timedelta

def create_post(title, slug, tag):
    post = Post.objects.create(
        title=title,
        excerpt="some excerpt",
        slug=slug,
        content="0123456789X",
    )
    post.tags.add(tag)
    return post

@pytest.mark.django_db
class TestStartingPage:
    def test_starting_page_returns_200(self, client):
        response = client.get(reverse("starting-page"))
        # assert response.status_code == 200
        assert response.status_code == HTTPStatus.OK

    def test_starting_page_has_posts_in_context(self, client):
        response = client.get(reverse("starting-page"))
        assert "posts" in response.context

    def test_uses_correct_template(self, client):
        response = client.get(reverse("starting-page"))
        templates = [t.name for t in response.templates]
        assert "blog/index.html" in templates

    def test_limits_posts_to_three(self, client):
        tag = Tag.objects.create(caption="general")
        for i in range(4):
            create_post(
                title=f"Post {i}",
                slug=f"post-{i}",
                tag=tag
            )

        response = client.get(reverse("starting-page"))

        assert len(response.context["posts"]) == 3

    def test_shows_latest_three_posts_by_date(self, client, db):
        tag = Tag.objects.create(caption="general")
        p1 = create_post("Post 1", "post-1", tag)
        p2 = create_post("Post 2", "post-2", tag)
        p3 = create_post("Post 3", "post-3", tag)
        p4 = create_post("Post 4", "post-4", tag)
        p5 = create_post("Post 5", "post-5", tag)
        today = date.today()
        Post.objects.filter(pk=p1.pk).update(date=today - timedelta(days=4))
        Post.objects.filter(pk=p2.pk).update(date=today - timedelta(days=3))
        Post.objects.filter(pk=p3.pk).update(date=today - timedelta(days=2))
        Post.objects.filter(pk=p4.pk).update(date=today - timedelta(days=1))
        Post.objects.filter(pk=p5.pk).update(date=today)

        response = client.get(reverse("starting-page"))

        posts = list(response.context["posts"])
        slugs = [p.slug for p in posts]
        assert len(posts) == 3
        assert slugs == ["post-5", "post-4", "post-3"]
