
from .render import Render
from django.utils import timezone

from django.conf import settings
from io import BytesIO
from reportlab.pdfgen import canvas
from django.views.generic import View

from django.db.models import Count, Q
from django.shortcuts import render

from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from books.models import Book, Contact
from .models import Passenger

from .forms import ContactForm

class ReportePersonasPDF(View):

    def cabecera(self,pdf):
            #Utilizamos el archivo logo_django.png que está guardado en la carpeta media/imagenes
            archivo_imagen = settings.MEDIA_ROOT+"/logo.png"
            #Definimos el tamaño de la imagen a cargar y las coordenadas correspondientes
            pdf.drawImage(archivo_imagen, 40, 750, 120, 90,preserveAspectRatio=True)
            #Establecemos el tamaño de letra en 16 y el tipo de letra Helvetica
            pdf.setFont("Helvetica", 16)
            #Dibujamos una cadena en la ubicación X,Y especificada
            pdf.drawString(230, 790, u"PYTHON PDF")
            pdf.setFont("Helvetica", 14)
            pdf.drawString(200, 770, u"REPORTE DE PERSONAS")
            
    def get(self, request, *args, **kwargs):
            #Indicamos el tipo de contenido a devolver, en este caso un pdf
            response = HttpResponse(content_type='application/pdf')
            #La clase io.BytesIO permite tratar un array de bytes como un fichero binario, se utiliza como almacenamiento temporal
            buffer = BytesIO()
            #Canvas nos permite hacer el reporte con coordenadas X y Y
            pdf = canvas.Canvas(buffer)
            #Llamo al método cabecera donde están definidos los datos que aparecen en la cabecera del reporte.
            self.cabecera(pdf)
            #Con show page hacemos un corte de página para pasar a la siguiente
            pdf.showPage()
            pdf.save()
            pdf = buffer.getvalue()
            buffer.close()
            response.write(pdf)
            return response

class bookPdf(View):

    def get(self, request):
        book = Book.objects.all()

        today = timezone.now()
        params = {
            'today': today,
            'book': book,
            'request': request
        }
        return Render.render('books/book_pdf.html', params)


def chart(request):
    dataset = Passenger.objects \
        .values('ticket_class') \
        .annotate(survived_count=Count('ticket_class', filter=Q(survived=True)),
                  not_survived_count=Count('ticket_class', filter=Q(survived=False))) \
        .order_by('ticket_class')
    return render(request, 'chart/chart.html', {'dataset': dataset})

class BookList(ListView):
    model = Book

class BookView(DetailView):
    model = Book

class BookCreate(CreateView):
    model = Book
    fields = ['name','author', 'pages','image']
    success_url = reverse_lazy('book_list')

class BookUpdate(UpdateView):
    model = Book
    fields = ['name','author', 'pages','image']
    success_url = reverse_lazy('book_list')

class BookDelete(DeleteView):
    model = Book
    #messages.add_message(request, messages.INFO, 'Data Delete Successfully')
    success_url = reverse_lazy('book_list')

class ContactCreate(CreateView):
    model = Contact
    template_name="contact/contact_form.html"
    fields = ['first_name','last_name', 'email','message']
    success_url = reverse_lazy('home')

class PassengerCreate(CreateView):
    model = Passenger
    template_name="chart/passenger_form.html"
    fields = ['name', 'survived','ticket_class']
    success_url = reverse_lazy('chart')

class PassengerList(ListView):
    model = Passenger
class ContactList(ListView):
    model = Contact
#    template_name = "contact/contact_list.html"
