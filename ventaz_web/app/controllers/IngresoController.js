ventazApp

.controller("IngresoController", function($scope, API, $window, $mdDialog) {

    API.Almacen.query(function(r) {
        $scope.nombre_almacen_list = r;
    }, function(error) {
        console.log("Errorum  " + error);
    });

    API.Proveedor.query(function(r) {
        $scope.razon_social_list = r;
    }, function(error) {
        console.log("Errorum  " + error);
    });

    API.Producto.query(function(r) {
        $scope.nombre_producto_list = r;
    }, function(error) {
        console.log("Errorum  " + error);
    });

    $scope.d_list = [];
    $scope.ingreso = {};

    list = function() {
        API.Ingreso.query(function(r) {
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
        $scope.ingreso.id=null;
        $mdDialog.show({
            scope: $scope.$new(),
            templateUrl: 'app/views/Ingreso/form.html',
            parent: angular.element(document.body),
            clickOutsideToClose:true
        }).then(function(){
            $scope.list($scope.page);
            $scope.ingreso={};
        }, function(){
        });
    };

    $scope.get = function(d) {
        $scope.ingreso = API.Ingreso.get({id : d.id});
        $mdDialog.show({
            scope: $scope.$new(),
            templateUrl: 'app/views/Ingreso/form.html',
            parent: angular.element(document.body),
            clickOutsideToClose:true
        }).then(function(){
            $scope.list($scope.page);
            $scope.ingreso={};
        }, function(){
        });
    };

    $scope.save = function() {
        if ($scope.ingreso.id) {
            API.Ingreso.update({ id: $scope.ingreso.id }, $scope.ingreso).$promise.then(function(r) {
                console.log(r);
                list();
                $mdDialog.hide();
            }, function(error) {
                console.log("Error  " + error);
            });
        } else {
            API.Ingreso.save($scope.ingreso).$promise.then(function(r) {
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
            API.Ingreso.delete({ "id": d.id }).$promise.then(function (r) {
                console.log(r);
                list();
            }, function (error) {
                console.log(error);
            });
        }
    };

});