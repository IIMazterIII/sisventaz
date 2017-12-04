ventazApp
.factory("API", function($resource) {
    return {
        Almacen:  $resource('http://localhost:8000/accounts/almacens'+'/:id/', {'id': "@id"},
        {
            'update': { method:'PUT' },
            'get': { method:'GET' },
            'query':  {method:'GET', isArray:true},
            'save':   {method:'POST'},
            'remove': {method:'DELETE'},
            'delete': {method:'DELETE'}
        }),
        Categoria:  $resource('http://localhost:8000/accounts/categorias'+'/:id/', {'id': "@id"},
        {
            'update': { method:'PUT' },
            'get': { method:'GET' },
            'query':  {method:'GET', isArray:true},
            'save':   {method:'POST'},
            'remove': {method:'DELETE'},
            'delete': {method:'DELETE'}
        }),
        Cliente:  $resource('http://localhost:8000/accounts/clientes'+'/:id/', {'id': "@id"},
        {
            'update': { method:'PUT' },
            'get': { method:'GET' },
            'query':  {method:'GET', isArray:true},
            'save':   {method:'POST'},
            'remove': {method:'DELETE'},
            'delete': {method:'DELETE'}
        }),
        EstablecimientoNegocio:  $resource('http://localhost:8000/accounts/establecimientonegocios'+'/:id/', {'id': "@id"},
        {
            'update': { method:'PUT' },
            'get': { method:'GET' },
            'query':  {method:'GET', isArray:true},
            //'get': { method:'GET', cache: true },
            //'create': { method:'POST' },
            'save':   {method:'POST'},
            'remove': {method:'DELETE'},
            'delete': {method:'DELETE'}
        }),
        Ingreso:  $resource('http://localhost:8000/accounts/ingresos'+'/:id/', {'id': "@id"},
        {
            'update': { method:'PUT' },
            'get': { method:'GET' },
            'query':  {method:'GET', isArray:true},
            'save':   {method:'POST'},
            'remove': {method:'DELETE'},
            'delete': {method:'DELETE'}
        }),
        Producto:  $resource('http://localhost:8000/accounts/productos'+'/:id/', {'id': "@id"},
        {
            'update': { method:'PUT' },
            'get': { method:'GET' },
            'query':  {method:'GET', isArray:true},
            'save':   {method:'POST'},
            'remove': {method:'DELETE'},
            'delete': {method:'DELETE'}
        }),
        Proveedor:  $resource('http://localhost:8000/accounts/proveedors'+'/:id/', {'id': "@id"},
        {
            'update': { method:'PUT' },
            'get': { method:'GET' },
            'query':  {method:'GET', isArray:true},
            'save':   {method:'POST'},
            'remove': {method:'DELETE'},
            'delete': {method:'DELETE'}
        }),
        Trabajador:  $resource('http://localhost:8000/accounts/trabajadors'+'/:id/', {'id': "@id"},
        {
            'update': { method:'PUT' },
            'get': { method:'GET' },
            'query':  {method:'GET', isArray:true},
            'save':   {method:'POST'},
            'remove': {method:'DELETE'},
            'delete': {method:'DELETE'}
        }),
        Venta:  $resource('http://localhost:8000/accounts/ventas'+'/:id/', {'id': "@id"},
        {
            'update': { method:'PUT' },
            'get': { method:'GET' },
            'query':  {method:'GET', isArray:true},
            'save':   {method:'POST'},
            'remove': {method:'DELETE'},
            'delete': {method:'DELETE'}
        }),
    };

});
