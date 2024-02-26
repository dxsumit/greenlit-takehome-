from __future__ import annotations


define_tags = [
    # {
    #     'name': 'User Management',
    #     'description': 'User authentication(login and logout) and New user Creation Endpoints',
    # },
    {
        'name': 'Upload Payslip and Form26as',
        'description': 'Endpoint to upload payslip and form26as at the same time'
    },
    {
        'name': 'Upload W2 Documents',
        'description': "Endpoint to Upload W2 documents"
    },
    {
        'name': 'Case List',
        'description': 'To access documents status uploaded by user'
    },
    {
        'name': 'Callback',
        'description': 'Callbacks are used by Fintech Backend to initiate excel generation and zipping'
    },
    {
        'name': 'Download Report',
        'description': 'Zip File Generation based on Id as a parameter'
    },
    {
        'name':'Download client usage statistics',
        'description':'excel sheet genration with statistics for a given date range'
    }
]

description = """  
             """

title = 'Ventura Pranas'
description = description
version = 'V1'

openapi_tags = define_tags
