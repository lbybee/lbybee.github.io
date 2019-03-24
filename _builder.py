"""
Everything I need to build my website
"""
from rfeed import Feed, Item, Guid
from dateutil.parser import parse
from datetime import datetime
from jinja2 import Template
from toolbelt import spbash
import os


def pop_blog(f, blog_dir, post_dict, post_template, main_template):
    """populates an html page from an org blog post

    Parameters
    ----------
    f : str
        basename for org file
    blog_dir : str
        location where org blog posts are located
    post_dict : dict
        dictionary of posts mapping titles to urls
    post_template : jinja2 Template instance
        template containing content for blog post
    main_template : jinja2 Template instnace
        template for adding style to blog post

    Returns
    -------
    tuple
        containing updated post_dict and item to add to rss feed
    """

    # prep inputs
    bn, ext = os.path.splitext(f)
    comp = bn.split("-")
    date = "-".join(comp[:3])
    title = " ".join(comp[3:])
    full_title = "%s %s" % (date, title)
    full_path = os.path.join(blog_dir, f)
    html_f = os.path.join("posts", bn + ".html")
    url = "https://lbybee.github.io/%s" % html_f

    # build html
    cmd = "pandoc -r org -t html --mathjax %s -o /dev/stdout"

    html = spbash(cmd % full_path)
    html = post_template.render(date=date, pandoc_html=html)
    html = main_template.render(title=title, content_html=html)


    with open(html_f, "w") as fd:
        fd.write(html)

    # add to rss feed
    item = Item(title=full_title,
                link=url,
                author="Leland Bybee",
                description=" ",
                guid=Guid(url),
                pubDate=parse(date))

    # update content dict
    post_dict[full_title] = url

    return post_dict, item


# load templates
with open("templates/_page.html", "r") as fd:
    main_template = Template(fd.read())
with open("templates/_post.html", "r") as fd:
    post_template = Template(fd.read())
with open("templates/_home.html", "r") as fd:
    home_template = Template(fd.read())

# remove existing html files
html_files = os.listdir(".")
for f in html_files:
    if os.path.splitext(f)[1] == ".html":
        os.remove(f)

# prep blog posts
post_dict = {}
items = []
blog_dir = "/home/lbybee/passepartout/notes/blog"
blog_posts = [f for f in os.listdir(blog_dir)
              if os.path.splitext(f)[1] == ".org"]
for f in blog_posts:
    post_dict, item = pop_blog(f, blog_dir, post_dict, post_template,
                               main_template)
    items.append(item)

# build index page
html = home_template.render(posts=post_dict)
html = main_template.render(title="Blog Posts", content_html=html)
with open("index.html", "w") as fd:
    fd.write(html)

# build rss page
feed = Feed(title="Leland's Blog",
            link="https://lbybee.github.io",
            description="My personal blog",
            language="en-US",
            lastBuildDate = datetime.now(),
            items=items)
rss = feed.rss()
with open("rss.xml", "w") as fd:
    fd.write(rss)
