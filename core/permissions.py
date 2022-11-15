PERMISSIONS_PADRAO = [
    {
        'name': 'Administrador(a)',
        'models_permissions': [
            {
                'permissions': ['view', 'add', 'change', 'delete'],
                'model': 'user'
            },
            {
                'permissions': ['view', 'add', 'change', 'delete'],
                'model': 'agendamento'
            },
            {
                'permissions': ['view', 'add', 'change', 'delete'],
                'model': 'group'
            },
            {
                'permissions': ['view', 'add', 'change', 'delete'],
                'model': 'permission'
            },
            {
                'permissions': ['view', 'add', 'change', 'delete'],
                'model': 'cliente'
            },
            {
                'permissions': ['view', 'add', 'change', 'delete'],
                'model': 'group'
            },
            {
                'permissions': ['view', 'add', 'change', 'delete'],
                'model': 'configuracao'
            },
            {
                'permissions': ['view', 'add', 'change', 'delete'],
                'model': 'disponibilidade'
            },
            {
                'permissions': ['view', 'add', 'change', 'delete'],
                'model': 'horario'
            },
            {
                'permissions': ['view', 'add', 'change', 'delete'],
                'model': 'funcionario'
            },
            {
                'permissions': ['view', 'add', 'change', 'delete'],
                'model': 'servico'
            },
        ]
    },
    {
        'name': 'Funcionário(a)',
        'models_permissions': [
            {
                'permissions': ['view', 'add', 'change', 'delete'],
                'model': 'agendamento'
            },
            {
                'permissions': ['view'],
                'model': 'cliente'
            },
            {
                'permissions': ['view', 'change'],
                'model': 'disponibilidade'
            },
            {
                'permissions': ['view', 'change'],
                'model': 'horario'
            },
            {
                'permissions': ['view'],
                'model': 'funcionario'
            },
            {
                'permissions': ['view'],
                'model': 'servico'
            },
        ]
    },
    {
        'name': 'Secretário(a)',
        'models_permissions': [
            {
                'permissions': ['view', 'add', 'change', 'delete'],
                'model': 'user'
            },
            {
                'permissions': ['view', 'add', 'change', 'delete'],
                'model': 'agendamento'
            },
            {
                'permissions': ['view', 'add', 'change', 'delete'],
                'model': 'cliente'
            },
            {
                'permissions': ['view', 'add', 'change', 'delete'],
                'model': 'disponibilidade'
            },
            {
                'permissions': ['view', 'add', 'change', 'delete'],
                'model': 'horario'
            },
            {
                'permissions': ['view', 'add', 'change', 'delete'],
                'model': 'funcionario'
            },
            {
                'permissions': ['view', 'add', 'change', 'delete'],
                'model': 'servico'
            },
        ]
    },
]
