def print_models(unprinting, completed):
    while unprinting:
        current_design = unprinting.pop()
        print(f"Wydruk modelu: {current_design}")
        completed.append(current_design)


def show_completed(completed):
    print("Wydrukowane zostały modele.")
    for model in completed:
        print(model)
