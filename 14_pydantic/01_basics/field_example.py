from pydantic import BaseModel
from typing import List, Dict, Optional

class Cart(BaseModel):
    user_id: int
    items: List[str]
    quantities: Dict[str, int]

class BlogPost(BaseModel):
    title: str
    content: str
    image_url: Optional[str] = None

cart_data = {
    "user_id": 1,
    "items": ["Chai", "Coffee"],
    "quantities": {"Chai": 2, "Coffee": 1}
}

cart = Cart(**cart_data)
print(cart)

blog_post_data = {
    "title": "My Blog Post",
    "content": "This is my blog post content",
    "image_url": "https://example.com/image.jpg"
}

blog_post = BlogPost(**blog_post_data)
print(blog_post)