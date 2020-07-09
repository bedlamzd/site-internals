import os


def has_tag(article, tag_name):
    try:
        tags = getattr(article, 'tags')
    except AttributeError:
        try:
            tags = getattr(article, 'tag')
        except AttributeError:
            return False
    return tag_name in [tag.name for tag in tags]


def folder(path: str):
    return os.path.split(path)[0]

def strip_ext(path: str):
    return os.path.splitext(path)[0]
