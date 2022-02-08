from django.shortcuts import render
from .models import *
import json as simplejson
from django.http import HttpResponse


# Create your views here.

def index(request):
    END_USER_CHOICES = EndUser.objects.all()
    FABRIC = Fabric.objects.all()
    MATERIAL = Material.objects.all()
    
    return render(request, 'index.html', { 'END_USER_CHOICES': END_USER_CHOICES, 'FABRIC': FABRIC, 'MATERIAL': MATERIAL })

def CostCalculator(request):
    endUser = request.POST['endUser']
    fabric = request.POST['fabric']
    material = request.POST['material']
    fabric_type = request.POST['fabricType']
    blend1 = request.POST['blend1']
    blend2 = request.POST['blend2']
    gsm = request.POST['GSM']
    wrapcount = request.POST['wrapcount']
    # weftcount = request.POST['weftcount']
    Ends = request.POST['Ends']
    picks = request.POST['picks']
    Yarnquality = request.POST['Yarnquality']
    Dyeingtype = request.POST['Dyeingtype']
    colorDepth =    request.POST['colorDepth']
    Texture = request.POST['Texture']
    Direction = request.POST['Direction']
    ReapetSize = request.POST['ReapetSize']
    PreTreatment = request.POST['PreTreatment']
    FinishingType = request.POST['FinishingType']
    Waste = request.POST['Waste']
    Branding = request.POST['Branding']
    Width = request.POST['Width']
    OrderQuantity = request.POST['OrderQuantity']

    # result_set = (endUser,fabric,material,fabric_type,blend1,blend2,gsm,wrapcount,Ends,picks,Yarnquality,Dyeingtype,colorDepth,Texture,Direction,ReapetSize,PreTreatment,FinishingType,Waste,Branding,Width,OrderQuantity)
    
    AddBlend = float(blend1)//float(blend2)
    CalculateGSM =  (float(gsm) * float(wrapcount))
    CalculateEnds = (float(Ends) * float(picks))
    CalculateYarn = (float(Yarnquality) * float(Dyeingtype))
    CalculateColor = (float(colorDepth) * float(Texture))
    CalculateDirection = (float(Direction) * float(ReapetSize))
    CalculatePreTreatment = (float(PreTreatment) * float(FinishingType))
    CalculateWaste = (float(Waste) * float(Branding))
    CalculateWidth = (float(Width) * float(OrderQuantity))
    fabricCost = (float(CalculateGSM) + float(CalculateEnds) + float(CalculateYarn) + float(CalculateColor) + float(CalculateDirection) + float(CalculatePreTreatment) + float(CalculateWaste) + float(CalculateWidth))

    bill = {
        'endUser': endUser,
        'fabric': fabric,
        'material': material,
        'fabric_type': fabric_type,
        'blend': AddBlend,
        'gsm': CalculateGSM,
        'ends': CalculateEnds,
        'yarn': CalculateYarn,
        'color': CalculateColor,
        'direction': CalculateDirection,
        'pretreatment': CalculatePreTreatment,
        'waste': CalculateWaste,
        'width': CalculateWidth,
        'fabricCost': fabricCost
        
    }
    return render(request, 'costCalculator.html', {'result_set':bill })
  


def getdetails(request):

    fabricname = request.GET['cnt']
    
    result_set = []
    all_fabric_type = []
    all_fabric_type = Fabricprop.objects.all()
    for fabric_type in all_fabric_type:
        
        if(fabric_type.fabric.name == fabricname):
            result_set.append(fabric_type.fabric_Type)

    return HttpResponse(simplejson.dumps(result_set), content_type='application/json')
 
