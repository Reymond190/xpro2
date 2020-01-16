from django.http import JsonResponse
from django.shortcuts import render ,HttpResponse
from django.views import View
# Create your views here.




# class TimedView(View):
#     template_name = 'session.html'
#     def get(self,request,*args,**kwargs):
#         return render(request, self.template_name)
#
#     def post(self,request,*args,**kwargs):
#         return render(request, self.template_name)
#
#
class AjaxView(View):

    def get(self,request,*args,**kwargs):
        veh = request.GET['dataa']
        print(veh)
        print('hello')
        return JsonResponse('hello',safe=False)

def timedview(request):
    return render(request,'session.html')


# def ajaxx(request):
#     print('hello')
#     veh = request.GET['dataa']
#     print(veh)
#     return JsonResponse(veh,safe=False)