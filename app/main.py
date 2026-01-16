from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    result = []

    clear = Cleaner(cleaner)
    for customer in customers:
        mem = Customer(
            name=customer["name"],
            food=customer["food"])
        CinemaBar.sell_product(product=customer["food"] , customer=mem)
        result.append(mem)
    hall = CinemaHall(hall_number)
    hall.movie_session(movie, result, clear)
