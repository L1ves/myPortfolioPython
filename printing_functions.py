# Список моделей, которые необходимо напечатать.
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
# Цикл последовательно печатает каждую модель до конца списка.
# После печати каждая модель перемещается в список completed_models.
while unprinted_designs:
    current_design = unprinted_designs.pop()
# Печать модели на 3D-принтере.
    print("Printing model: " + current_design)
    completed_models.append(current_design)
# Вывод всех готовых моделей.
    print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model.title())


def print_models(unprinted_designs, completed_models):
    """Имитирует печать моделей, пока список не станет пустым.
    Каждая модель после печати перемещается в completed_models.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        # Имитация печати модели на 3D-принтере.
        print("Printing model: " + current_design)
completed_models.append(current_design)
def show_completed_models(completed_models):
    """Выводит информацию обо всех напечатанных моделях."""
    print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)
    unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
    completed_models = []
    print_models(unprinted_designs, completed_models)
    show_completed_models(completed_models)
