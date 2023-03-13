from django.shortcuts import render

# Create your views here.
from django.template.loader import render_to_string, get_template
from django.http import HttpResponse, FileResponse, StreamingHttpResponse
import io
from weasyprint import HTML, CSS

def index(request):
    # return HttpResponse("Hello, world.")
    return render(request, 'weasyprint_sample/sample_index.html')

def weasy_test(request):
    message = 'completed'

    # html_template = get_template('http://abehiroshi.la.coocan.jp/')

    pdf_file = HTML('http://abehiroshi.la.coocan.jp/').write_pdf(
        # target=stream
        # この中でcssを指定する
        # stylesheets=[CSS('cms/static/css/pdf.css')]
    )
    stream = io.BytesIO(pdf_file)

    # return HttpResponse(message)
    # return FileResponse(stream, as_attachment=True, filename='sample.pdf')
    return FileResponse(pdf_file, as_attachment=True, filename='sample_x.pdf')