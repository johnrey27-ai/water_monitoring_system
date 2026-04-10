from django.shortcuts import render


def calculate_predicted_do(temperature, ph, turbidity):
    """Predict dissolved oxygen from temperature, pH, and turbidity."""
    predicted = 14.6 - 0.28 * temperature - 0.18 * (ph - 7) - 0.05 * turbidity
    return max(0.0, round(predicted, 2))


def dashboard(request):
    records = [
        {'temperature': 27, 'ph': 7.0, 'turbidity': 4, 'status': 'Safe'},
        {'temperature': 30, 'ph': 6.5, 'turbidity': 8, 'status': 'Warning'},
        {'temperature': 32, 'ph': 5.8, 'turbidity': 12, 'status': 'Danger'},
    ]

    for record in records:
        record['predicted_do'] = calculate_predicted_do(record['temperature'], record['ph'], record['turbidity'])

    data = {
        'temperature': 28,
        'ph': 7.2,
        'turbidity': 5,
        'predicted_do': calculate_predicted_do(28, 7.2, 5),
        'status': 'Safe',
        'records': records,
    }
    return render(request, 'monitoring/dashboard.html', data)