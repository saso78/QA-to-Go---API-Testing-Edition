# tests/test_posts.py

from utils.request_handler import RequestHandler

handler = RequestHandler()

def test_create_post():
    new_post = {
        "title": "QA to Go Test Post",
        "body": "This is a sample post created by the API Testing Kit.",
        "userId": 1
    }

    response = handler.post("/posts", new_post)

    assert response.status_code == 201
    post = response.json()

    print("\n📝 Created Post:")
    print(f"ID: {post.get('id')} - Title: {post.get('title')}")
    assert post["title"] == new_post["title"]
    assert post["body"] == new_post["body"]
    assert post["userId"] == new_post["userId"]
