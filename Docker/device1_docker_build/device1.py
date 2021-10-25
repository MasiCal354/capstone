from faker import Faker
import time
import random
import argparse


def main(run_min=1):
    Faker.seed(8711)
    fake = Faker('en_US')
    keys = ('lat', 'lon', 'location', 'country_ code', 'timezone')
    message = {'device_id': fake.isbn10()}

    tic = time.perf_counter()
    while ((time.perf_counter() - tic) / 60) < run_min:
        location = dict(zip(keys, fake.location_on_land()))
        message.update(location)
        print(message)
        time.sleep(random.uniform(.1, 2))
    print((time.perf_counter() - tic) / 60)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--run_min', type=int, required=True)
    args = parser.parse_args()
    main(args.run_min)
