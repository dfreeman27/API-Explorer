import requests

response = requests.get("https://jsonplaceholder.typicode.com/users/") 

users = response.json()

# GET all users and print each user's name and email
print(f"\nAll Users: {len(users)} ")

for user in users:
        print(f"{user['name']} - {user['email']}")

print(f"Status Code: {response.status_code}")
print("="*50)

# GET all posts by user #3 (use query parameters)

response = requests.get(
    "https://jsonplaceholder.typicode.com/posts",
    params={"userId": 3}
    ) 
posts = response.json()

print(f"\nUser 3 has {len(posts)} posts:")

for post in posts:
    print(f" [{post['id']}] {post['body'][0:50]}...")

print(f"Status Code: {response.status_code}")
print("="*50)

# GET all comments on post #1 (endpoint: /posts/1/comments)

response = requests.get("https://jsonplaceholder.typicode.com/posts/1/comments") 

comments = response.json()

print(f"Comments on post 1: {len(comments)}")

for comment in comments:
      print(f"{comment['id']} - {comment['body'][0:50]}...")

print(f"Status Code: {response.status_code}")
print("="*50)

# POST a new post (simulated) and print the response
new_post = {
    "title": "My time with API",
    "body": "This was created by sending a post request",
    "userId": 3
}

response = requests.post(
    "https://jsonplaceholder.typicode.com/posts", json=new_post
)

created = response.json()
print(f"Created post with id: {created['id']}")
print(f"Title: {created['title']}")
print(f"Status Code: {response.status_code}")
print("="*50)