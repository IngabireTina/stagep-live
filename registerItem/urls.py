from django.urls import path
from . import views

urlpatterns = [

    path('recorditem/<int:pk>/', views.recordItem, name='recorditem'),
    path('all_item/', views.allItem, name='all_item'),

    path('updateitem/<str:pk>/', views.updateItem, name='updateitem'),
    path('deleteitem/<str:pk>/', views.deleteItem, name='deleteitem'),

    path('recordstock/', views.recordStock, name='recordstock'),
    path('updatestock/<str:pk>/', views.updateStock, name='updatestock'),
    path('deletestock/<str:pk>/', views.deleteStock, name='deletestock'),
    path('allstock/', views.allStock, name='allstock'),
    path('available_stock/', views.availableDevice, name='available_stock'),


    path('sector-laptop', views.sectorLaptop, name='sector_laptop'),
    path('sector_update_lap/<int:pk>', views.sectorLaptopUpdate, name='sector_update_lap'),

    path('sector_desktop', views.sectorDesktop, name='sector_desktop'),
    path('sector_update_desktop/<int:pk>', views.sectorDesktopUpdate, name='sector_update_desktop'),

    path('sector_printer', views.sectorPrinter, name='sector_printer'),
    path('sector_update_printer/<int:pk>', views.sectorPrinterUpdate, name='sector_update_printer'),

    path('sector_router', views.sectorRouter, name='sector_router'),
    path('sector_update_router/<int:pk>', views.sectorRouterUpdate, name='sector_update_router'),

    path('sector_scanner', views.sectorScanner, name='sector_scanner'),
    path('sector_update_scanner/<int:pk>', views.sectorScannerUpdate, name='sector_update_scanner'),

    path('sector_television', views.sectorTelevision, name='sector_television'),
    path('sector_update_television/<int:pk>', views.sectorTelevisionUpdate, name='sector_update_television'),

    path('sector_decoder', views.sectorDecoder, name='sector_decoder'),
    path('sector_update_decoder/<int:pk>', views.sectorDecoderUpdate, name='sector_update_decoder'),



    path('gishamvu-report/', views.gishamvuReport, name='gishamvu_report'),
    path('huye-report/', views.huyeReport, name='huye_report'),
    path('karama-report/', views.karamaReport, name='karama_report'),
    path('kigoma-report/', views.kigomaReport, name='kigoma_report'),
    path('kinazi-report/', views.kinaziReport, name='kinazi_report'),
    path('maraba-report/', views.marabaReport, name='maraba_report'),
    path('mbazi-report/', views.mbaziReport, name='mbazi_report'),
    path('mukura-report/', views.mukuraReport, name='mukura_report'),
    path('ngoma-report/', views.ngomaReport, name='ngoma_report'),
    path('ruhashya-report/', views.ruhashyaReport, name='ruhashya_report'),
    path('rusatira-report/', views.rusatiraReport, name='rusatira_report'),
    path('rwaniro-report/', views.rwaniroReport, name='rwaniro_report'),
    path('simbi-report/', views.simbiReport, name='simbi_report'),
    path('tumba-report/', views.tumbaReport, name='tumba_report'),
    path('huyedistrict-report/', views.districtOfficeReport, name='huyedistrict_report'),




    path('sector_report/', views.tableReport, name='sector_report'),


]
