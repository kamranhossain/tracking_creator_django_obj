from django.shortcuts import render

# Create your views here.
@login_required
def create_name(request):
    form = NameForm(data=request.POST or None)
    if form.is_valid():
        name = Name.objects.create(english_representation=form.cleaned_data['english_representation'], vernacular_representation=form.cleaned_data['vernacular_representation'])
    return render(request, 'names/name-create.html', {'form': form})