from django.shortcuts import render
from .models import Lista, BranzaForm, KrajForm

def database(request):
	lista=Lista.objects.all()
	if request.method == 'POST':
		form=BranzaForm(request.POST)
		form_kraj=KrajForm(request.POST)
		Kategoria=request.POST['branza']
		kraj=request.POST['kraj']
		#if form.is_valid():
			#miasto=form.cleaned_data['miasto']
			#Kategoria=form.cleaned_data['branza']
		lista=Lista.objects.all().filter(branza=Kategoria,kraj=kraj)
		if request.POST['branza']=='11':
			lista=Lista.objects.all().filter(kraj=kraj)
		if request.POST['kraj']=='3':
			lista=Lista.objects.all().filter(branza=Kategoria)
		if request.POST['kraj']=='3' and request.POST['branza']=='11':
			lista=Lista.objects.all()
	else:
		lista=Lista.objects.all()
		form=BranzaForm(initial={"branza": "11"})
		form_kraj=KrajForm(initial={"kraj": "3"})
	return render(request,'database.html',{'lista':lista,'form':form,'form_kraj':form_kraj})