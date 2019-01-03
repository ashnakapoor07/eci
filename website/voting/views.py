from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.http import Http404
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.views import generic
from django.views.generic import View
from .models import candidate
from .forms import UserForm
from .forms import CandidateAdd
from django.contrib.auth.decorators import login_required




def index(request):
    all_candidates = candidate.objects.all()
    template=loader.get_template('voting/index.html')
    context={'all_candidates':all_candidates}
    return HttpResponse(template.render(context,request))
def detail(request,candidate_id):
    try:
        candi = candidate.objects.get(pk=candidate_id)
    except candidate.DoesNotExist:
        raise Http404("NO CANDIDATE WITH SPECIFIED ID EXISTS")
    return render(request,'voting/detail.html',{'candidate':candi})


def thankyou(request,candidate_id):
    template_name = "voting/thankyou.html"
    return render(request,template_name)

class AddCandidate(View):
    form_class=CandidateAdd
    template_name = 'voting/candidate_form.html'

    def get(self,request):
          form = self.form_class(None)
          return render(request,'voting/candidate_form.html', {'form':form })


    def post(self,request):

        form = self.form_class(request.POST or None,request.FILES or None)

        if form.is_valid():
              Candidate = form.save(commit=False)
              Candidate.save()
              return render(request, 'voting/index.html',{'all_candidates': candidate.objects.all()})


class CandidateUpdate(UpdateView):
    model = candidate
    fields=['name','logo','political_party','quote','photo','area']

@login_required
def delete(request,pk):
    if request.user.is_superuser:
     Candidate = candidate.objects.get(pk=pk)
     Candidate.delete()
     all_candidates = candidate.objects.all()
     return render(request, 'voting/index.html', {'all_candidates': all_candidates ,'error_message':"Successfully deleted candidate"})
    else:
     raise Http404("YOU ARE NOT AUTHORIZED TO DELETE THE CANDIDATE")



class UserFormView(View):
    form_class = UserForm
    template_name='voting/registration_form.html'

    #display blank form
    def get(self,request):
       form=self.form_class(None)
       return render(request,self.template_name,{'form':form})

    #process form data
    def post(self,request):
        form=self.form_class(request.POST)

        if form.is_valid():
            users=form.save(commit=False)
            #cleaned normalized data
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            users.set_password(password)
            users.save()

            #returns user objects if credentials are correct
            users=authenticate(username=username,password=password)
            if users is not None:
                if users.is_active:
                  login(request,users)
                  #return redirect('voting:index')
                  return render(request, 'voting/index2.html', {'all_candidates': candidate.objects.all()})

        return render(request,self.template_name,{'form':form})



