import pytest
from django.urls import reverse
from http import HTTPStatus
from blog.models import Post, Tag

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
