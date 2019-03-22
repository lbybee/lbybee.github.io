"""
Everything I need to build my website
"""
from feedgen.feed import FeedGenerator
from jinja2 import Template
import subprocess
import os



blog_dir = "/home/lbybee/passepartout/notes/blog"
blog_posts = [os.path.splitext(f) for f in os.listdir(blog_dir)]
blog_posts = [f[0] for f in blog_posts if f[1] == ".org"]
blog_posts = []
