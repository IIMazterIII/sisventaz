ventazApp
.config(function ($httpProvider) {
    $httpProvider.interceptors.push('authInterceptorService');
})

.run(
    ['$rootScope', '$state', '$stateParams','authService','$location','$window',
      function ( $rootScope,   $state,   $stateParams, authService,$location, $window) {
        $rootScope.$state = $state;
        $rootScope.$stateParams = $stateParams;     
        /*******************************agregado**************************/
        authService.fillAuthData(); 
        if(authService.authentication.isAuth==false){
            //$window.location="../skyend_accounts";
        }       
        /******************************************************************/
      }
    ]
  )

.config(['$stateProvider', '$urlRouterProvider', function($stateProvider,   $urlRouterProvider) {
  $stateProvider
    //------------------------------
    // HOME
    //------------------------------
    .state('app', {
      url: '/',
      templateUrl: 'app/views/Home.html'
    })
    //------------------------------
    // Inicio
    //------------------------------
    .state('Inicio', {
      url: '/Inicio',
      templateUrl: 'app/views/Inicio.html'
    })
/*
    //------------------------------
    // HOME
    //------------------------------
    .state('app', {
      url: '/',
      templateUrl: 'partials/home.tmpl.html'
    })
    //------------------------------
    // inicio page http://plnkr.co/edit/u18KQc?p=preview
    //------------------------------
    .state('getting-started', {
      url: '/getting-started',
      templateUrl: 'partials/getting-started.tmpl.html'
    })
*/

    $stateProvider
    //------------------------------
    // Cajaingreso
    //------------------------------
    .state('Almacen', {
      url: '/Almacen',
      templateUrl: 'app/views/Almacen/index.html'
    })
    //------------------------------
    // Citahistorial
    //------------------------------
    .state('Categoria', {
      url: '/Categoria',
      templateUrl: 'app/views/Categoria/index.html'
    })
    //------------------------------
    // Citainscripcion
    //------------------------------
    .state('Cliente', {
      url: '/Cliente',
      templateUrl: 'app/views/Cliente/index.html'
    })
    //------------------------------
    // Cliente
    //------------------------------
    .state('EstablecimientoNegocio', {
      url: '/EstablecimientoNegocio',
      templateUrl: 'app/views/EstablecimientoNegocio/index.html'
    })
    //------------------------------
    // Cuentausuario
    //------------------------------
    .state('Ingreso', {
      url: '/Ingreso',
      templateUrl: 'app/views/Ingreso/index.html'
    })
    //------------------------------
    // Especialidad
    //------------------------------
    .state('Producto', {
      url: '/Producto',
      templateUrl: 'app/views/Producto/index.html'
    })
    //------------------------------
    // Especialidad
    //------------------------------
    .state('Proveedor', {
      url: '/Proveedor',
      templateUrl: 'app/views/Proveedor/index.html'
    })//------------------------------
    // Especialidad
    //------------------------------
    .state('Trabajador', {
      url: '/Trabajador',
      templateUrl: 'app/views/Trabajador/index.html'
    })
    //------------------------------
    // Odontologo
    //------------------------------
    .state('Venta', {
      url: '/Venta',
      templateUrl: 'app/views/Venta/index.html'
    });

    $urlRouterProvider.otherwise('/');

  }]);