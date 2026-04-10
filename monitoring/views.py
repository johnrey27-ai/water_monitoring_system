from django.shortcuts import render

def dashboard(request):
    data = {
        'temperature': 28,
        'ph': 7.2,
        'status': 'Safe',
        'records': [
            {'temperature': 27, 'ph': 7.0, 'status': 'Safe'},
            {'temperature': 30, 'ph': 6.5, 'status': 'Warning'},
            {'temperature': 32, 'ph': 5.8, 'status': 'Danger'},
        ]
    }
    return render(request, 'monitoring/dashboard.html', data)