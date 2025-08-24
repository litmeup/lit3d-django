# yourapp/templatetags/gallery.py
from django import template
from django.contrib.staticfiles import finders

register = template.Library()

@register.simple_tag(takes_context=True)
def project_image_range(context, slug=None):
    """
    Возвращает range(1..N) для static/projects/<slug>/{1..N}.jpg.
    Если slug не передали, попробует достать из:
      - context['slug']
      - context['project'].slug
      - context['object'].slug
      - request.resolver_match.kwargs['slug']  (нужно иметь request в контексте)
    """
    # ---------- автоопределение slug ----------
    if not slug:
        slug = (context.get("slug")
                or getattr(context.get("project", None), "slug", None)
                or getattr(context.get("object", None), "slug", None))
        if not slug:
            req = context.get("request")
            if req and getattr(req, "resolver_match", None):
                slug = req.resolver_match.kwargs.get("slug")

    if not slug:
        return range(0)  # нечего рендерить

    # ---------- поиск 1..N через finders ----------
    i, nmax = 1, 0
    while True:
        found = (finders.find(f"projects/{slug}/{i}.jpg")
                 or finders.find(f"projects/{slug}/{i}.jpeg")
                 or finders.find(f"projects/{slug}/{i}.JPG")
                 or finders.find(f"projects/{slug}/{i}.JPEG"))
        if not found:
            break
        nmax = i
        i += 1
    return range(1, nmax + 1)
