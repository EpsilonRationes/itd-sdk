from uuid import UUID

from itd.request import fetch

def add_comment(token: str, post_id: UUID, content: str):
    return fetch(token, 'post', f'posts/{post_id}/comments', {'content': content})

def add_reply_comment(token: str, comment_id: UUID, content: str, author_id: UUID):
    return fetch(token, 'post', f'comments/{comment_id}/replies', {'content': content, 'replyToUserId': str(author_id)})

def get_comments(token: str, post_id: UUID, limit: int = 20, cursor: int = 0, sort: str = 'popular'):
    return fetch(token, 'get', f'posts/{post_id}/comments', {'limit': limit, 'sort': sort, 'cursor': cursor})

def like_comment(token: str, comment_id: UUID):
    return fetch(token, 'post', f'comments/{comment_id}/like')

def unlike_comment(token: str, comment_id: UUID):
    return fetch(token, 'delete', f'comments/{comment_id}/like')

def delete_comment(token: str, comment_id: UUID):
    return fetch(token, 'delete', f'comments/{comment_id}')
