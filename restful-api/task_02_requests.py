#!/usr/bin/python3
"""
Module for RESTful API
"""
import requests
import csv


def fetch_and_print_posts():
    """
    Fetch posts from JSONPlaceholder and print titles
    """
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        posts = response.json()
        for i in posts:
            print(i["title"])

def fetch_and_save_posts():
    """
    Fetch posts from JSONPlaceholder and save to file
    """
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    
    if response.status_code == 200:
        posts = response.json()
        posts_dict = [
            {"id": i['id'],
             "title": i['title'],
             "body": i['body']}
                for i in posts]

        with open("posts.csv", "w", newline="", encoding="utf-8") as f:
            csv_writer = csv.DictWriter(f, fieldnames=["id", "title", "body"])
            csv_writer.writeheader()
            csv_writer.writerows(posts_dict)
