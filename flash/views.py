from django.shortcuts import render, redirect
from .form import CardForm, TagForm
from .models import Card, Tag
from django.http import JsonResponse

# Create your views here.

def home_view(request, word_id, *args, **kwargs):
     if word_id == 0:
          context = {
               'word' : None
          }
     else:
          card = Card.objects.get(id = word_id)
          context =  card.serialize()
          tagSet = Tag.objects.filter( word = card )
          context['tags'] = list(set(q.tag for q in tagSet))
          
     return render(request, 'home.html', context)

def redirect_view(request,*args, **kwargs):
     print('REQUEST',request.POST)
     if request.method == 'POST':
          try:
               next = request.POST.get('next')
               print('NEXT: ', next)
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

def create_word(request, *args, **kwargs):
     form = CardForm(request.POST or None)
     print(form)
     if request.method == 'POST':
          obj = form.save(commit = False)
          obj.save()
          word_id = obj.id
          return redirect(f'../{word_id}')

     form = CardForm()
     context = {
          'form' : form
     }
     return render(request, 'create_word.html', context)

def create_tag(request, *args, **kwargs):
     if request.method == 'POST':
          requestWord = request.POST.get('id')
          cards = Card.objects.filter(id=requestWord)
          tag = request.POST.get('tag')
          instance = Tag.objects.create( tag = tag )

          for card in cards:
               instance.word.add(card)
          return redirect(f'../{requestWord}/')

     form = TagForm()
     context = {
          'form' : form
     }
     return render(request, 'create_tag.html', context)