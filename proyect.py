# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 18:05:08 2024

@author: Camilo Gallego B
"""

import re

regex_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
regex_phone = r'^\d{3}-\d{3}-\d{4}$'
regex_date = r'^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}$'
regex_postal_code = r'^\d{5}$'


tests = [
    {"type": "Correo Electrónico", "value": "test@example.com", "regex": regex_email},
    {"type": "Número de Teléfono", "value": "123-456-7890", "regex": regex_phone},
    {"type": "Fecha", "value": "15/08/2024", "regex": regex_date},
    {"type": "Código Postal", "value": "12345", "regex": regex_postal_code}
]


for test in tests:
    if re.match(test['regex'], test['value']):
        print(f"{test['type']}: {test['value']} -> Válido")
    else:
        print(f"{test['type']}: {test['value']} -> No válido")