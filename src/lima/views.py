from django.http import HttpResponse
from django.shortcuts import render
import pathlib
from visits.models import PageVisits

this_dir = pathlib.Path(__file__).resolve().parent

def home_view(request, *args, **kwargs):
    return about_view(request, *args, **kwargs)



def about_view(request, *args, **kwargs):
    queryset = PageVisits.objects.all()
    page_qs = PageVisits.objects.filter(path = request.path)

    try:
        percent = (page_qs.count()*100.0 / queryset.count())
    except:
        percent = 0

    print("the paths", request.path)
    title = "SaaS"
    html_template= "home.html"

    my_context = {
         "page_title": title,
         "page_visits_count": page_qs.count(),
         "percent": percent,
         "total_visits": queryset.count()
    }

    PageVisits.objects.create(path = request.path)
    return render(request, html_template, my_context)












def old_home_page_view(request, *args, **kwargs):
    title = "Home"

    # my_context = {
    #      "page_title": title
    # }

    # html_ = """
    # <!DOCTYPE html>
    # <html>
    # <head>
    #     <body>
    #     <h1>This is the {page_title} page</h1>
    #     </body>
    # </html>
    # """.format(**my_context)


#=========alt 2====================
    html_ = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <body>
        <h1>This is the {title} page</h1>
        </body>
    </html>
    """
    
    # html_file_path = this_dir / "home.html"
    # html_ = html_file_path.read_text()
    return HttpResponse(html_) 