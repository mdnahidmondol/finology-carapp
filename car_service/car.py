class Car:
    def __init__(self, name, model, manufacturer, year, engine, transmission, fuel_type, exterior_color, interior_color, car_body_style, car_parts=None):
        self.name = name
        self.model = model
        self.manufacturer = manufacturer
        self.year = year
        self.engine = engine
        self.transmission = transmission
        self.fuel_type = fuel_type
        self.exterior_color = exterior_color
        self.interior_color = interior_color
        self.car_body_style = car_body_style
        self.car_parts = car_parts or []

