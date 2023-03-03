from flask import Flask, request, jsonify
from car import Car 
from carparts import Battery, BrakingSystem, CoolingSystem, Electrical, Engine, Transmission, FuelType, Color, CarBodyStyle, CarPart

app = Flask(__name__)

# dummy car parts
car_parts = [
    CarPart("Windshield", "ABC Windshields"),
    Electrical("Battery"),
    Battery("Battery"),
    BrakingSystem("BrakingSystem"),
    CoolingSystem("CoolingSystem")
    ]

# dummy cars
cars = [
    Car("Tesla", "Model S", "Tesla Motors", 2021, Engine(capacity=1500, num_cylinders=4), Transmission("Automatic"), FuelType("Electric"), Color("Red", "Black"), Color("Black", "Black"), CarBodyStyle(style="Sedan", size="Mid-Size"), car_parts),
    Car("Harley Davidson", "Iron 883", "Harley Davidson", 2020, Engine(capacity=1000, num_cylinders=2), Transmission("Manual"), FuelType("Gasoline"), Color("Black", "Black"), Color("Black", "Black"), CarBodyStyle(style="Cruiser", size="2-Wheeler"), car_parts),
    Car("Porsche", "911 Carrera", "Porsche", 2022, Engine(capacity=500, num_cylinders=3), Transmission("Automatic"), FuelType("Gasoline"), Color("Yellow", "Black"), Color("Black", "Black"), CarBodyStyle(style="Coupe", size="Sport"), car_parts)
]

# car type to the car
car_type_map = {
    "electrical": cars[0],
    "2 wheels": cars[1],
    "sport": cars[2]
}

# route to get a car based on the car type
@app.route('/car', methods=['GET'])
def get_car():
    car_type = request.args.get('type')

    if car_type:
        car = car_type_map.get(car_type.lower())

        if car:
            car_dict = {
                "name": car.name,
                "model": car.model,
                "manufacturer": car.manufacturer,
                "year": car.year,
                "engine": car.engine.capacity if isinstance(car.engine, Engine) else car.engine,
                "transmission": car.transmission.type if isinstance(car.transmission, Transmission) else car.transmission,
                "fuel_type": car.fuel_type.type if isinstance(car.fuel_type, FuelType) else car.fuel_type,
                "exterior_color": car.exterior_color.exterior if isinstance(car.exterior_color, Color) else car.exterior_color,
                "interior_color": car.exterior_color.interior if isinstance(car.exterior_color, Color) else car.exterior_color,
                "car_body_style": car.car_body_style.style if isinstance(car.car_body_style, CarBodyStyle) else car.car_body_style,
                "car_parts": [part.__dict__ for part in car.car_parts] if car.car_parts else None
            }

            return jsonify(car_dict)
        else:
            return jsonify({"error": "Invalid car type"})
    else:
        return jsonify({"error": "Car type not specified"})


if __name__ == '__main__':
    app.run(debug=True)
