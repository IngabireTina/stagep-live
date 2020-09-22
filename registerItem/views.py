from django.shortcuts import render, redirect
from .models import Item
from .forms import ItemForm, ReportItemForm
from .forms import StockForm
from .models import Stock
from django.contrib import messages
from .filters import StockFilter, ItemFilter, SectorReportFilter


# Create your views here.

def recordItem(request, pk):
    device = Stock.objects.get(id=pk)
    form = ItemForm(request=request, initial={'device': device})
    if request.method == 'POST':
        # form = ItemForm(request.POST, request=request)
        form = ItemForm(request.POST, request=request, initial={'device': device})
        if form.is_valid():
            form.save()
            Stock.objects.filter(id=device.id).update(availability='Given')

            return redirect('available_stock')

    items = Item.objects.all()

    context = {'form': form, 'items': items}
    return render(request, 'registerItem.html', context)


# available device to be assigned ############################

def availableDevice(request):
    stocks = Stock.objects.filter(availability='Available')
    sFilter = StockFilter(request.GET, queryset=stocks)
    stocks = sFilter.qs

    context = {'stocks': stocks, 'sFilter': sFilter}
    return render(request, 'stock/available_device.html', context)


def allItem(request):
    items = Item.objects.all()
    sFilter = ItemFilter(request.GET, queryset=items)
    items = sFilter.qs
    context = {'items': items, 'sFilter': sFilter}
    return render(request, 'allItem.html', context)


def updateItem(request, pk):
    item = Item.objects.get(id=pk)
    form = ItemForm(instance=item)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('all_item')

    context = {'form': form}
    return render(request, 'updateItem.html', context)


def deleteItem(request, pk):
    item = Item.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('all_item')

    context = {'item': item}
    return render(request, 'deleteItem.html', context)


# the stock record ##############################3
def recordStock(request):
    form = StockForm()
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = StockForm(request.POST)
            if form.is_valid():
                device_name = form.cleaned_data.get('name')
                form.save()
                messages.success(request, 'The Stock was successful created' + device_name)
                return redirect('allstock')

    context = {'form': form}
    return render(request, 'stock/recordStock.html', context)


def allStock(request):
    stocks = Stock.objects.all()

    sFilter = StockFilter(request.GET, queryset=stocks)
    stocks = sFilter.qs

    context = {'stocks': stocks, 'sFilter': sFilter}
    return render(request, 'stock/allStock.html', context)


def updateStock(request, pk):
    stock = Stock.objects.get(id=pk)
    form = StockForm(instance=stock)
    if request.method == 'POST':
        form = StockForm(request.POST, instance=stock)
        if form.is_valid():
            form.save()
            return redirect('allstock')

    context = {'form': form}
    return render(request, 'stock/updateStock.html', context)


def deleteStock(request, pk):
    form = Stock.objects.get(id=pk)
    if request.method == 'POST':
        form.delete()
        return redirect('allstock')

    context = {'form': form}
    return render(request, 'stock/deleteStock.html', context)


#
def sectorLaptop(request):
    data = Item.objects.filter(device__category='Computer Laptop').filter(address=request.user.address)
    rFilter = SectorReportFilter(request.GET, queryset=data)
    data = rFilter.qs

    context = {'data': data, 'rFilter': rFilter}
    return render(request, 'sector/sector_laptop.html', context)


def sectorDesktop(request):
    data = Item.objects.filter(device__category='Computer Desktop').filter(address=request.user.address)
    rFilter = SectorReportFilter(request.GET, queryset=data)
    data = rFilter.qs

    context = {'data': data, 'rFilter': rFilter}
    return render(request, 'sector/sector_desktop.html', context)


def sectorPrinter(request):
    data = Item.objects.filter(device__category='Printer').filter(address=request.user.address)
    rFilter = SectorReportFilter(request.GET, queryset=data)
    data = rFilter.qs

    context = {'data': data, 'rFilter': rFilter}
    return render(request, 'sector/sector_printer.html', context)


def sectorRouter(request):
    data = Item.objects.filter(device__category='4G Router').filter(address=request.user.address)
    rFilter = SectorReportFilter(request.GET, queryset=data)
    data = rFilter.qs

    context = {'data': data, 'rFilter': rFilter}
    return render(request, 'sector/sector_router.html', context)


def sectorScanner(request):
    data = Item.objects.filter(device__category='Scanner').filter(address=request.user.address)
    rFilter = SectorReportFilter(request.GET, queryset=data)
    data = rFilter.qs

    context = {'data': data, 'rFilter': rFilter}
    return render(request, 'sector/sector_scanner.html', context)


def sectorTelevision(request):
    data = Item.objects.filter(device__category='Television').filter(address=request.user.address)
    rFilter = SectorReportFilter(request.GET, queryset=data)
    data = rFilter.qs

    context = {'data': data, 'rFilter': rFilter}
    return render(request, 'sector/sector_television.html', context)


def sectorDecoder(request):
    data = Item.objects.filter(device__category='Decoder').filter(address=request.user.address)
    rFilter = SectorReportFilter(request.GET, queryset=data)
    data = rFilter.qs

    context = {'data': data, 'rFilter': rFilter}
    return render(request, 'sector/sector_decoder.html', context)


def sectorLaptopUpdate(request, pk):
    data = Item.objects.get(id=pk)
    form = ReportItemForm(request.POST or None, instance=data)
    if request.method == 'POST':
        form = ReportItemForm(request.POST or None, instance=data)
        if form.is_valid():
            form.save()
            # device = form.cleaned_data.get('serialNumber')
            #
            # messages.success(request, 'The Device was successful Updated' + device)
            return redirect('sector_laptop')
    context = {'form': form}
    return render(request, 'sector/sector_update.html', context)


def sectorDesktopUpdate(request, pk):
    data = Item.objects.get(id=pk)
    form = ReportItemForm(request.POST or None, instance=data)
    if request.method == 'POST':
        form = ReportItemForm(request.POST or None, instance=data)
        if form.is_valid():
            form.save()
            return redirect('sector_desktop')
    context = {'form': form}
    return render(request, 'sector/sector_update.html', context)


def sectorPrinterUpdate(request, pk):
    data = Item.objects.get(id=pk)
    form = ReportItemForm(request.POST or None, instance=data)
    if request.method == 'POST':
        form = ReportItemForm(request.POST or None, instance=data)
        if form.is_valid():
            form.save()
            return redirect('sector_printer')
    context = {'form': form}
    return render(request, 'sector/sector_update.html', context)


def sectorRouterUpdate(request, pk):
    data = Item.objects.get(id=pk)
    form = ReportItemForm(request.POST or None, instance=data)
    if request.method == 'POST':
        form = ReportItemForm(request.POST or None, instance=data)
        if form.is_valid():
            form.save()
            return redirect('sector_router')
    context = {'form': form}
    return render(request, 'sector/sector_update.html', context)


def sectorScannerUpdate(request, pk):
    data = Item.objects.get(id=pk)
    form = ReportItemForm(request.POST or None, instance=data)
    if request.method == 'POST':
        form = ReportItemForm(request.POST or None, instance=data)
        if form.is_valid():
            form.save()
            return redirect('sector_scanner')
    context = {'form': form}
    return render(request, 'sector/sector_update.html', context)


def sectorTelevisionUpdate(request, pk):
    data = Item.objects.get(id=pk)
    form = ReportItemForm(request.POST or None, instance=data)
    if request.method == 'POST':
        form = ReportItemForm(request.POST or None, instance=data)
        if form.is_valid():
            form.save()
            return redirect('sector_television')
    context = {'form': form}
    return render(request, 'sector/sector_update.html', context)


def sectorDecoderUpdate(request, pk):
    data = Item.objects.get(id=pk)
    form = ReportItemForm(request.POST or None, instance=data)
    if request.method == 'POST':
        form = ReportItemForm(request.POST or None, instance=data)
        if form.is_valid():
            form.save()
            return redirect('sector_decoder')
    context = {'form': form}
    return render(request, 'sector/sector_update.html', context)


# view for displaying Sector Report###########################################

def gishamvuReport(request):
    data = Item.objects.filter(address__name='Gishamvu')
    rFilter = SectorReportFilter(request.GET, queryset=data)
    data = rFilter.qs

    context = {'data': data, 'rFilter': rFilter}
    return render(request, 'sector/gishamvu_report.html', context)


def huyeReport(request):
    data = Item.objects.filter(address__name='Huye')
    rFilter = SectorReportFilter(request.GET, queryset=data)
    data = rFilter.qs

    context = {'data': data, 'rFilter': rFilter}
    return render(request, 'sector/huye/huye_report.html', context)


def karamaReport(request):
    data = Item.objects.filter(address__name='Karama')
    rFilter = SectorReportFilter(request.GET, queryset=data)
    data = rFilter.qs

    context = {'data': data, 'rFilter': rFilter}
    return render(request, 'sector/karama/karama_report.html', context)


def kigomaReport(request):
    data = Item.objects.filter(address__name='Kigoma')
    rFilter = SectorReportFilter(request.GET, queryset=data)
    data = rFilter.qs

    context = {'data': data, 'rFilter': rFilter}
    return render(request, 'sector/kigoma/kigoma_report.html', context)


def kinaziReport(request):
    data = Item.objects.filter(address__name='Kinazi')
    rFilter = SectorReportFilter(request.GET, queryset=data)
    data = rFilter.qs

    context = {'data': data, 'rFilter': rFilter}
    return render(request, 'sector/kinazi/kinazi_report.html', context)


def marabaReport(request):
    data = Item.objects.filter(address__name='Maraba')
    rFilter = SectorReportFilter(request.GET, queryset=data)
    data = rFilter.qs

    context = {'data': data, 'rFilter': rFilter}
    return render(request, 'sector/maraba/maraba_report.html', context)


def mbaziReport(request):
    data = Item.objects.filter(address__name='Mbazi')
    rFilter = SectorReportFilter(request.GET, queryset=data)
    data = rFilter.qs

    context = {'data': data, 'rFilter': rFilter}
    return render(request, 'sector/mbazi/mbazi_report.html', context)


def mukuraReport(request):
    data = Item.objects.filter(address__name='Mukura')
    rFilter = SectorReportFilter(request.GET, queryset=data)
    data = rFilter.qs

    context = {'data': data, 'rFilter': rFilter}
    return render(request, 'sector/mukura/mukura_report.html', context)


def ngomaReport(request):
    data = Item.objects.filter(address__name='Ngoma')
    rFilter = SectorReportFilter(request.GET, queryset=data)
    data = rFilter.qs

    context = {'data': data, 'rFilter': rFilter}
    return render(request, 'sector/ngoma/ngoma_report.html', context)


def ruhashyaReport(request):
    data = Item.objects.filter(address__name='Ruhashya')
    rFilter = SectorReportFilter(request.GET, queryset=data)
    data = rFilter.qs

    context = {'data': data, 'rFilter': rFilter}
    return render(request, 'sector/ruhashya/ruhashya_report.html', context)


def rusatiraReport(request):
    data = Item.objects.filter(address__name='Rusatira')
    rFilter = SectorReportFilter(request.GET, queryset=data)
    data = rFilter.qs

    context = {'data': data, 'rFilter': rFilter}
    return render(request, 'sector/rusatira/rusatira.html', context)


def rwaniroReport(request):
    data = Item.objects.filter(address__name='Rwaniro')
    rFilter = SectorReportFilter(request.GET, queryset=data)
    data = rFilter.qs

    context = {'data': data, 'rFilter': rFilter}
    return render(request, 'sector/rwaniro/rwaniro_report.html', context)


def simbiReport(request):
    data = Item.objects.filter(address__name='Simbi')
    rFilter = SectorReportFilter(request.GET, queryset=data)
    data = rFilter.qs

    context = {'data': data, 'rFilter': rFilter}
    return render(request, 'sector/simbi/simbi_report.html', context)


def tumbaReport(request):
    data = Item.objects.filter(address__name='Tumba')
    rFilter = SectorReportFilter(request.GET, queryset=data)
    data = rFilter.qs

    context = {'data': data, 'rFilter': rFilter}
    return render(request, 'sector/tumba/tumba_report.html', context)


def districtOfficeReport(request):
    data = Item.objects.filter(address__name='Huye District Office')
    rFilter = SectorReportFilter(request.GET, queryset=data)
    data = rFilter.qs

    context = {'data': data, 'rFilter': rFilter}
    return render(request, 'sector/huyedistrict/huyedistrictofficereport.html', context)


# Report Tables for Sector #########################

def tableReport(request):
    data = Item.objects.filter(address=request.user.address)
    rFilter = SectorReportFilter(request.GET, queryset=data)
    data = rFilter.qs

    context = {'data': data, 'rFilter': rFilter}
    return render(request, 'sector_report.html', context)
