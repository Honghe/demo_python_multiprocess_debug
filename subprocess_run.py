# -*- coding: utf-8 -*-
from datetime import date

from pudb.remote import set_trace


def example_run():
    today = date.today()
    set_trace()
    print('today is data: {}'.format(today))


if __name__ == '__main__':
    example_run()
