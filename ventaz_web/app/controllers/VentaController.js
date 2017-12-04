ventazApp

.controller("VentaController", function($scope, API, $window, $mdDialog) {

    API.Cliente.query(function(r) {
        $scope.apellidos_cliente_list = r;
    }, function(error) {
        console.log("Errorum  " + error);
    });

    API.EstablecimientoNegocio.query(function(r) {
        $scope.nombre_en_list = r;
    }, function(error) {
        console.log("Errorum  " + error);
    });

    API.Ingreso.query(function(r) {
        $scope.producto_str_list = r;
    }, function(error) {
        console.log("Errorum  " + error);
    });

    $scope.d_list = [];
    $scope.venta = {};

    list = function() {
        API.Venta.query(function(r) {
            $scope.d_list = r;
        }, function(error) {
            console.log("Error  " + error);
        });
    };
    list();

    $scope.cancel = function() {
        $mdDialog.cancel();
    };

    $scope.new = function() {
        $scope.venta.id=null;
        $mdDialog.show({
            scope: $scope.$new(),
            templateUrl: 'app/views/Venta/form.html',
            parent: angular.element(document.body),
            clickOutsideToClose:true
        }).then(function(){
            $scope.list($scope.page);
            $scope.venta={};
        }, function(){
        });
    };

    $scope.get = function(d) {
        $scope.venta = API.Venta.get({id : d.id});
        $mdDialog.show({
            scope: $scope.$new(),
            templateUrl: 'app/views/Venta/form.html',
            parent: angular.element(document.body),
            clickOutsideToClose:true
        }).then(function(){
            $scope.list($scope.page);
            $scope.venta={};
        }, function(){
        });
    };

    $scope.save = function() {
        if ($scope.venta.id) {
            API.Venta.update({ id: $scope.venta.id }, $scope.venta).$promise.then(function(r) {
                console.log(r);
                list();
                $mdDialog.hide();
            }, function(error) {
                console.log("Error  " + error);
            });
        } else {
            API.Venta.save($scope.venta).$promise.then(function(r) {
                console.log(r);
                list();
                $mdDialog.hide();
            }, function(error) {
                console.log("Error  " + error);
            });
        }
    };
    
    $scope.delete = function(d){
        if ($window.confirm('Confirm delete')) {
            API.Venta.delete({ "id": d.id }).$promise.then(function (r) {
                console.log(r);
                list();
            }, function (error) {
                console.log(error);
            });
        }
    };

});