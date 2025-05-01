# myapp/views.py
from django.shortcuts import render

def home(request):
    return render(request, 'lit3d/index.html')

def so(request):
    return render(request, 'lit3d/project.html')

def portfolio_page(request, slug):
    page = get_object_or_404(PortfolioPage, slug=slug, is_active=True)
    pages = PortfolioPage.objects.filter(is_active=True).order_by('order')
    
    return render(request, 'portfolio/page.html', {
        'page': page,
        'pages': pages,
    })