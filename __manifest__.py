# -*- coding: utf-8 -*-
{
    'name': "Demodaten",

    'summary': """
        Demodata of the Mint System GmbH.
    """,

    'description': """
        Automatically installs demo datasets and apps.
    """,

    'author': "Mint System GmbH",
    'website': "https://www.mint-system.ch",
    'category': 'Customization',
    'version': '14.0.1.0.0',

    'depends': ['hr_contract'],

    'data': [
        'data/resource.calendar.csv'
        'data/hr.departemnt.csv'
        'data/hr.job.csv'
        'data/res.user.csv',
        'data/hr.employee.csv',
        'data/hr.contract.csv'
    ],

    'installable': True,
    'application': False,
}