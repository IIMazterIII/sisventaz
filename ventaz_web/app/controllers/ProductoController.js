ventazApp

.controller("ProductoController", function($scope, API, $window, $mdDialog) {

    API.Categoria.query(function(r) {
        $scope.nombre_categoria_list = r;
    }, function(error) {
        console.log("Errorum  " + error);
    });

    $scope.d_list = [];
    $scope.producto = {};

    list = function() {
        API.Producto.query(function(r) {
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
        $scope.producto.id=null;
        $mdDialog.show({
            scope: $scope.$new(),
            templateUrl: 'app/views/Producto/form.html',
            parent: angular.element(document.body),
            clickOutsideToClose:true
        }).then(function(){
            $scope.list($scope.page);
            $scope.producto={};
        }, function(){
        });
    };

    $scope.get = function(d) {
        $scope.producto = API.Producto.get({id : d.id});
        $mdDialog.show({
            scope: $scope.$new(),
            templateUrl: 'app/views/Producto/form.html',
            parent: angular.element(document.body),
            clickOutsideToClose:true
        }).then(function(){
            $scope.list($scope.page);
            $scope.producto={};
        }, function(){
        });
    };

    $scope.save = function() {
        if ($scope.producto.id) {
            API.Producto.update({ id: $scope.producto.id }, $scope.producto).$promise.then(function(r) {
                console.log(r);
                list();
                $mdDialog.hide();
            }, function(error) {
                console.log("Error  " + error);
            });
        } else {
            API.Producto.save($scope.producto).$promise.then(function(r) {
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
            API.Producto.delete({ "id": d.id }).$promise.then(function (r) {
                console.log(r);
                list();
            }, function (error) {
                console.log(error);
            });
        }
    };

});
