"""
Everything I need to build my website
"""
from feedgen.feed import FeedGenerator
from bs4 import BeautifulSoup
from jinja2 import Template
from toolbelt import spbash
import os


def pop_blog(f, blog_dir, post_dict, blog_feed, blog_template, main_template):
    """populates an html page from an org blog post

    Parameters
    ----------
    f : str
        basename for org file
    blog_dir : str
        location where org blog posts are located
    post_dict : dict
        dictionary of posts mapping titles to urls
    blog_feed : FeedGenerator instance
        blog feed instance for RSS
    blog_template : jinja2 Template instance
        template containing content for blog post
    main_template : jinja2 Template instnace
        template for adding style to blog post

    Returns
    -------
    tuple
        containing updated post_dict and blog_feed
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
    cmd = ("pandoc -r org -t html --mathjax --standalone %s "
           "-o /dev/stdout")

    html = spbash(cmd % full_path)
    html = post_template.render(date=date, pandoc_html=html)
    # remove pandoc body
    html = str(BeautifulSoup(html, features="lxml").body)
    html = html.replace("<body>", "").replace("</body>", "")
    html = main_template.render(title=title, content_html=html)


    with open(html_f, "w") as fd:
        fd.write(html)

    # add to rss feed
    fe = blog_feed.add_entry()
    fe.id(url)
    fe.title(full_title)
    fe.description("some stuff here")
    fe.link(href=url)

    # update content dict
    post_dict[full_title] = url

    return post_dict, blog_feed


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

# prep blog_feed
blog_feed = FeedGenerator()
blog_feed.id("https://lbybee.github.io")
blog_feed.title("Leland's Blog")
blog_feed.author({"name": "Leland Bybee"})
blog_feed.link(href="https://lbybee.github.io")
blog_feed.description("My Blog")
blog_feed.language("en")

# prep blog posts
post_dict = {}
blog_dir = "/home/lbybee/passepartout/notes/blog"
blog_posts = [f for f in os.listdir(blog_dir)
              if os.path.splitext(f)[1] == ".org"]
for f in blog_posts:
    post_dict, blog_feed = pop_blog(f, blog_dir, post_dict, blog_feed,
                                    post_template, main_template)

# build index page
html = home_template.render(posts=post_dict)
html = main_template.render(title="Blog Posts", content_html=html)
with open("index.html", "w") as fd:
    fd.write(html)

# build rss page
blog_feed.rss_file("rss.xml")
blog_feed.atom_file("atom.xml")
