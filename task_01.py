#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" dictionary task"""

def sum_orders(customers,orders):
    """ parameters that get together to form a single dictionary

    Args:
        costumers (dict): a dictionary of customers keyed by costumer_id
        orders (dict): a dictionary of orders keyed by order id

    Returns:
        combined dictionary

    Exampless:
        {
    customer_id: {'name': 'Some Name', 'email': 'some@email.com'},
    }
    {
    order_id: {'customer_id': customer_id, 'total': order_total},
    }
    >>> ORDERS = {1: {'customer_id': 2, 'total': 10},
              3: {'customer_id': 2, 'total': 10},
              4: {'customer_id': 3, 'total': 15}}
    >>> CUSTOMERS = {2: {'name': 'Person One', 'email': 'email@one.com'},
                 3: {'name': 'Person Two', 'email': 'email@two.com'}}
    >>> sum_orders(customers=CUSTOMERS, orders=ORDERS)
    {2: {'name': 'Person One',
     'email': 'email@one.com',
     'orders': 2,
     'total': 20}
     3: {'name': 'Person Two',
     'email': 'email@two.com',
     'orders': 1,
     'total': 15}}
"""
    person = {}
    for key, value in person.iteritems():
        total_orders = 0
        number_orders = 0
        for request in orders.values():
            total_orders += request['costumer_id']
            number_orders += 1
            person[key] = {'name': value['name'],
                              'email': value['email'],
                              'orders': number_orders,
                              'total': total_orders}
    return person 
     
