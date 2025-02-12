{
    'name': 'Gestion des Recours',
    'version': '1.0',
    'summary': 'Module de gestion des recours pour la CNR',
    'description': """
        Ce module permet la gestion complète des recours, incluant :
        - Le dépôt de recours par les assurés
        - Le suivi des recours
        - ...
    """,
    'author': 'MEBARKI Aicha Aya',
    'category': 'CNR',
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/recours.xml',
        'views/agence.xml'
    ]
}
