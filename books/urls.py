from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('chart/',             views.chart,    name='chart'),
    path('reporte_personas_pdf/',views.ReportePersonasPDF.as_view(), name="reporte_personas_pdf"),
    path('Pdf',       views.Pdf.as_view(),   name='Pdf'),

 



    path('book_list',       views.BookList.as_view(),   name='book_list'),
    path('view/<int:pk>',   views.BookView.as_view(),   name='book_view'),
    path('new',             views.BookCreate.as_view(), name='book_new'),
    path('view/<int:pk>',   views.BookView.as_view(),   name='book_view'),
    path('edit/<int:pk>',   views.BookUpdate.as_view(), name='book_edit'),
    path('delete/<int:pk>', views.BookDelete.as_view(), name='book_delete'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,  document_root=settings.MEDIA_ROOT)
