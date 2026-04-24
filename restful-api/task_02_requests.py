import requests
import csv
r = requests.get('https://jsonplaceholder.typicode.com/posts')
def fetch_and_print_posts():
    for post in r.json():
        print('Post ID: {}, Title: {}'.format(post.get('id'), post.get('title')))
        status_code = r.status_code
        print('Status Code: {}'.format(status_code))

def fetch_and_save_posts():

    posts = r.json()

    data_to_save = []
    for post in posts:
        data_to_save.append({
            'id': post['id'],
            'title': post['title'],
            'body': post['body']
        })

    with open('posts.csv', 'w', newline='', encoding='utf-8') as f:
        fieldnames = ['id', 'title', 'body']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        
        writer.writeheader()
        writer.writerows(data_to_save)
