from django.shortcuts import render, redirect
from .form import CardForm, TagForm
from .models import Topic, Tag
from django.http import JsonResponse

# Create your views here.

def welcome(request, *args, **kwargs):
     context = {
          'exists': len(Topic.objects.all()) != 0
     }    
     return render(request, 'base.html', context)

def home_view(request, topic_id=1, *args, **kwargs):
     if topic_id == 0:
          context = {
               'topic' : None
          }
     else:
          card = Card.objects.get(id = topic_id)
          context =  card.serialize()
          tagSet = Tag.objects.filter( topic = card )
          context['tags'] = list(set(q.tag for q in tagSet))
          
     return render(request, 'home.html', context)

def redirect_view(request,*args, **kwargs):
     print('REQUEST',request.GET)
     if request.method == 'GET':
          try:
               next = request.GET.get('next')
               print('NEXT: ', next)
               next = next == 0 if next == '' else next
               existing_objs = Card.objects.filter( id__gt = int(next) )
               print('OBJECTS:', existing_objs)

               # hanling last page
               if len(existing_objs)==0:
                    return redirect( f'../{next}' )

               # handling next pages, takes care of missing objects
               else:
                    list_id = [obj.id for obj in existing_objs]
                    print('IDS:', list_id)
                    next_id = list_id[0]
                    next = str( next_id )
                    return redirect( f'../{next}' )

          #handle prev pages
          except:
               prev = request.POST.get('prev')
               if prev!='':
                    prev = str(int(prev) - 1)

               #handle moving back from page 0
               else:
                    prev = str(0)
               return redirect( f'../{prev}' )
                    
     context = {}
     return render(request, 'redirect.html', context)

def create_topic(request, *args, **kwargs):
     form = CardForm(request.POST or None)
     print(form)
     if request.method == 'POST':
          obj = form.save(commit = False)
          obj.save()
          topic_id = obj.id
          return redirect(f'../{topic_id}')

     form = CardForm()
     context = {
          'form' : form
     }
     return render(request, 'create_topic.html', context)

def create_tag(request, *args, **kwargs):
     if request.method == 'POST':
          requestTopic = request.POST.get('id')
          cards = Card.objects.filter(id=requestTopic)
          tag = request.POST.get('tag')
          instance = Tag.objects.create( tag = tag )

          for card in cards:
               instance.topic.add(card)
          return redirect(f'../{requestTopic}/')

     form = TagForm()
     context = {
          'form' : form
     }
     return render(request, 'create_tag.html', context)