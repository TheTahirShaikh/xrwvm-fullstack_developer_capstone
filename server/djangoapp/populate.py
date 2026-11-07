from .models import CarMake, CarModel


def initiate():
    car_make_data = [
        ("NISSAN", "Great cars. Japanese technology"),
        ("Mercedes", "Great cars. German technology"),
        ("Audi", "Great cars. German technology"),
        ("Kia", "Great cars. Korean technology"),
        ("Toyota", "Great cars. Japanese technology"),
    ]

    car_make_instances = []
    for name, description in car_make_data:
        car_make_instances.append(
            CarMake.objects.create(name=name, description=description)
        )

    # (model name, type, index of its make in the list above)
    car_model_data = [
        ("Pathfinder", "SUV", 0),
        ("Qashqai", "SUV", 0),
        ("XTRAIL", "SUV", 0),
        ("A-Class", "SUV", 1),
        ("C-Class", "SUV", 1),
        ("E-Class", "SUV", 1),
        ("A4", "SUV", 2),
        ("A5", "SUV", 2),
        ("A6", "SUV", 2),
        ("Sorrento", "SUV", 3),
        ("Carnival", "SUV", 3),
        ("Cerato", "Sedan", 3),
        ("Corolla", "Sedan", 4),
        ("Camry", "Sedan", 4),
        ("Kluger", "SUV", 4),
    ]

    for name, car_type, make_index in car_model_data:
        CarModel.objects.create(
            name=name,
            type=car_type,
            year=2023,
            car_make=car_make_instances[make_index],
        )
