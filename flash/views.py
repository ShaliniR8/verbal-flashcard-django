from django.shortcuts import render, redirect,  get_object_or_404
from django.db.models import Q
from .form import TopicForm, TagForm, UseCaseForm, ComparisonForm, ComparisonRowForm
from .serializers import ComparisonRowSerializer
from django.forms import inlineformset_factory
from .models import Topic, Tag, UseCase, Comparison, ComparisonRow
from django.http import JsonResponse

# Create your views here.

def welcome(request, *args, **kwargs):
     if len(Topic.objects.all()) != 0:
          context = {
               'topic_id': Topic.objects.first().id
          }    
     else:
          context = {
               'topic_id': None
          }  
     return render(request, 'base.html', context)

# ------------------------------------------------------------------------------------------
# TOPIC
# ------------------------------------------------------------------------------------------

def home_view(request, topic_id, *args, **kwargs):
     try: 
          topic = Topic.objects.get(id = topic_id)
          context =  topic.serialize()
          tagSet = Tag.objects.filter( topic = topic )
          useCaseSet = topic.use_cases.all()
          compairsonSet = topic.comparisons.all()
          context['tags'] = list(set(q.tag for q in tagSet))
          context['is_topic'] = ["true" if Topic.objects.filter(topic = tag).exists() else "false" for tag in context['tags'] ]
          context['use_cases'] = useCaseSet if useCaseSet.exists() else None
          context['comparisons'] = compairsonSet if compairsonSet.exists() else None
          return render(request, 'home.html', context)
     except Exception as e:
          print(e)
          return redirect('welcome')

def redirect_view(request,*args, **kwargs):
     if request.method == 'GET':
          try:
               next = request.GET.get('next')
               next = next == 0 if next == '' else next
               existing_objs = Topic.objects.filter( id__gt = int(next) )
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
               prev = request.GET.get('prev')
               if prev!='':
                    prev = str(int(prev) - 1)

               #handle moving back from page 0
               else:
                    prev = str(0)
               return redirect( f'../{prev}' )
                    
     context = {}
     return render(request, 'redirect.html', context)

def create_topic(request, *args, **kwargs):
     if request.method == 'POST':
          form = TopicForm(request.POST or None)
          obj = form.save()
          topic_id = obj.id
          return redirect('topic-page', topic_id=topic_id)

     context = {'topic' : ""}
     if 'tag' in kwargs:
          topic = Topic.objects.filter(topic=kwargs['tag'])
          if topic.exists():
               return redirect('topic-page', topic_id=topic.first().id)
          else:
               context['topic'] = kwargs['tag']

     context['form'] = TopicForm()
     return render(request, 'create_topic.html', context)

def edit_topic(request, *args, **kwargs):
     topic_id = request.POST.get('id')
     request_form = request.POST
     topic = Topic.objects.get(id = topic_id)
     form = TopicForm(request_form, instance = topic)
     if form.is_valid():
          form.save()
          return JsonResponse({'message': 'Success!', 'tag': 'success'})
     else:
          return JsonResponse({'message': 'Failed to edit that.', 'tag': 'warning'})

def delete_topic(request):
     topic_id = request.POST.get('id')
     Topic.objects.get(id = topic_id).delete()
     return JsonResponse({'message': 'go back!'})
      
     

def create_tag(request, *args, **kwargs):
     if request.method == 'POST':
          topic_id = request.POST.get('id')
          tag_text = request.POST.get('tag')

          tag_instance, created = Tag.objects.get_or_create(tag=tag_text)
          topic = Topic.objects.get(id=topic_id)

          # Check if the topic is already associated with the tag
          if not tag_instance.topic.filter(id=topic.id).exists():
               tag_instance.topic.add(topic)

          return JsonResponse({'result': "Success"})

     form = TagForm()
     context = {
          'form' : form
     }
     return render(request, 'create_tag.html', context)

def remove_tag(request, *args, **kwargs):
     print(request)
     if request.method == 'POST':
          topic_id = request.POST.get('id')
          tag_text_to_remove = request.POST.get('tag')

          if not topic_id or not tag_text_to_remove:
               return JsonResponse({'result': "Missing Data"})
          try:
               topic = Topic.objects.get(id=topic_id)
          except Topic.DoesNotExist:
               topic = None
          tag_instance = Tag.objects.get(tag=tag_text_to_remove)
          
          if topic is not None:
               tag_instance.topic.remove(topic)
     return JsonResponse({'result': "Success"})

# ------------------------------------------------------------------------------------------
# USE CASE
# ------------------------------------------------------------------------------------------

def add_use_case(request, topic_id):
     topic = get_object_or_404(Topic, id=topic_id)
     if request.method == 'POST':
          form = UseCaseForm(request.POST)
          use_case = form.save(commit=False)
          use_case.topic = topic
          use_case.save()
          return redirect('topic-page', topic_id=topic_id)
     else:
          form = UseCaseForm()
          return render(request, 'use_case/add_use_case.html', {'form': form, 'topic': topic})

def edit_use_case(request, *args, **kwargs):
     use_case_id = request.POST.get('id')
     request_form = request.POST
     use_case = UseCase.objects.get(id = use_case_id)
     form = UseCaseForm(request_form, instance = use_case)
     if form.is_valid():
          form.save()
     return JsonResponse({'result': request.method})

def delete_use_case(request, *args, **kwargs):
     if request.method == 'POST':
          topic_id = request.POST.get('id')
          use_case_id_to_remove = request.POST.get('use_case_id')

          if not topic_id or not use_case_id_to_remove:
               return JsonResponse({'result': "Missing Data"})
          UseCase.objects.get(id=use_case_id_to_remove).delete()
     return JsonResponse({'result': request.method})

# ------------------------------------------------------------------------------------------
# COMPARISON
# ------------------------------------------------------------------------------------------

ComparisonRowFormSet = inlineformset_factory(
    Comparison,
    ComparisonRow,
    fields=('row1', 'row2'),
    can_delete=True  # Allow the deletion of form instances
)

def add_comparison(request, topic_id):
     if request.method == 'POST':
          topic = get_object_or_404(Topic, id = topic_id)
          form = ComparisonForm(request.POST)
          parent = form.save(commit=False)
          parent.topic = topic 
          parent.save()
          child_formset = ComparisonRowFormSet(request.POST, instance=parent)
          if child_formset.is_valid():
               child_formset.save()
          return redirect('topic-page', topic_id=topic_id)
     else:
          form = Comparison()
          child_formset = ComparisonRowFormSet(instance=Comparison())
          options = list(topic.topic for topic in Topic.objects.all()) + list(tag.tag for tag in Tag.objects.all())
          return render(request, 'comparisons/add_comparison.html', {
          'form': form,
          'child_formset': child_formset,
          'options': options})

def comparison_datatable(request, comparison_id):
     # Extracting DataTable request parameters
     draw = int(request.GET.get('draw', 1))  # Unique ID for each request
     start = int(request.GET.get('start', 0))
     length = int(request.GET.get('length', 10))  # Page size
     search_value = request.GET.get('search[value]', '')
     comparison = get_object_or_404(Comparison, id = comparison_id)

     queryset = comparison.comparison_rows.all()
     if search_value:
          queryset = comparison.comparison_rows.filter(Q(row1__icontains=search_value) | Q(row2__icontains=search_value))

     # Total record count before filtering
     total = queryset.count()

     # Sorting and pagination
     queryset = queryset[start:start + length]

     # Serialization
     serializer = ComparisonRowSerializer(queryset,  many=True)
     data = serializer.data

     # Preparing the response
     response = {
          "draw": draw,
          "recordsTotal": total,
          "recordsFiltered": total,
          "data": data
     }

     return JsonResponse(response)


def edit_comparison(request, comparison_id):
     comparison = Comparison.objects.get(id=comparison_id)
     if request.method == 'POST':
          topic = comparison.topic
          child_formset = ComparisonRowFormSet(request.POST, instance=comparison)
          if child_formset.is_valid():
               child_formset.save()
          return redirect('topic-page', topic_id=topic.id)
     else:
          form = ComparisonForm(instance=comparison)
          child_formset = ComparisonRowFormSet(instance=comparison)
          return render(request, 'comparisons/edit_comparison.html', {
          'comparison' : comparison,
          'child_formset': child_formset})

def delete_comparison(request):
     id = request.POST.get('id')
     comparison = Comparison.objects.get(id = id)
     if comparison is not None:
          comparison.delete()

     return JsonResponse({'result': 'deleted'})