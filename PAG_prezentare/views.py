from PAG_prezentare.models import Prezentare
from django.shortcuts import render

def prezentare(request,prezentare_id):
	prezentare = Prezentare.objects.get(pk=prezentare_id)
	if prezentare is not None:
		return render (request,'prezentare/prezentare.html', {'prezentare':prezentare})
	else:
		raise Http404('Prezentarea nu exista')