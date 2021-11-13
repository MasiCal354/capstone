from faker import Faker
from faker.config import AVAILABLE_LOCALES
from datetime import timezone
from datetime import datetime
import time
import random
import argparse


def get_locale(lc):
    rnd_country = random.randint(0, len(lc)-1)

    loc = lc[rnd_country].split('_')
    if len(loc) > 1:
        return loc[1].upper()
    else:
        return loc[0].upper()


def main(run_min=1):
    Faker.seed(8711)
    fake = Faker('en_US')
    en_us = get_locale([en for en in AVAILABLE_LOCALES if 'en_' in en])
    keys = ('lat', 'lon', 'location', 'country_ code', 'timezone')
    message = {'device_id': fake.isbn10()}

    print(en_us)

    tic = time.perf_counter()
    while ((time.perf_counter() - tic) / 60) < run_min:
        location = dict(zip(keys, fake.local_latlng(country_code=en_us, coords_only=False)))
        alt_as = {'altitude': random.randint(0, 13000), 'airspeed': random.randint(0, 240),
                  'timestamp': datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S.%f%z')}
        message.update(location)
        message.update(alt_as)
        print(message)
        time.sleep(random.uniform(.1, 2))
    print((time.perf_counter() - tic) / 60)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--run_min', type=int, required=True)
    args = parser.parse_args()
    main(args.run_min)
