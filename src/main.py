from src import linear_regression, ft_math

def get_thetas() -> list:
    filename = './data/data_prophecy.csv'
    linear_regression.run('data')
    thetas = open(filename, 'r').read()

    return thetas.split(',')


def compute_price(distance: int):
    thetas = get_thetas()
    price = ft_math.linear(distance, thetas)
    print(
        'This car should cost {} euros.\
            \n\tHis kilometrage (distance) is {}\
            \n\tfunction used: price(distance) = {} + {} * distance'
        .format(
            int(price),
            distance,
            thetas[0],
            thetas[1]
        )
    )
