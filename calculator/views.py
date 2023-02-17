from django.shortcuts import render


DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 300,
        'сыр, г': 50,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}

def index(request):
    context = {'recipes': DATA.keys()}
    return render(request, 'calculator/index.html', context)


def dish(request, recipe):
    quantity = int(request.GET.get('servings', 1))
    all_amount = dict()
    for ingredient, amount in DATA.get(recipe).items():
        all_amount[ingredient] = quantity * amount

    context = {'name': recipe,
               'quantity': quantity,
               'recipe': all_amount}
    return render(request, 'calculator/dish.html', context)
