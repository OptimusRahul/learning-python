from typing import List, Optional
from pydantic import BaseModel

class Comment(BaseModel):
    id: int
    content: str
    replies: Optional[List['Comment']] = None

Comment.model_rebuild()

comment = Comment(id=1, content="This is a comment", replies=[Comment(id=2, content="This is a reply", replies=[Comment(id=3, content="This is a reply to a reply")])])
print(comment)