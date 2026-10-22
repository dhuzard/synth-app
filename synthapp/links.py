"""Link helpers of synth-app."""


def post_url(title, slugify):
    """Return the URL path of a post, using the injected slugify callable."""
    slug = slugify(title)
    if not slug:
        raise ValueError("title produces an empty slug")
    return "/posts/" + slug
