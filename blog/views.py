from django.shortcuts import render

posts = [
  {
    'author': 'andy',
    'title': 'title_1',
    'content': 'content 1',
    'date_posted': '2/18/2020'
  },
    {
    'author': 'andy',
    'title': 'title_2',
    'content': 'content 2',
    'date_posted': '2/18/2021'
  }
]

def home(request):
  return render(request, 'blog/home.html', { 'posts': posts })

def about(request):
  return render(request, 'blog/about.html', {'title': 'About'})
