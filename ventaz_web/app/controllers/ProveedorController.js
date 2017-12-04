ventazApp

.controller("ProveedorController", function($scope, API, $window, $mdDialog) {
    
    $scope.d_list = [];
    $scope.proveedor = {};

    list = function() {
        API.Proveedor.query(function(r) {
            $scope.d_list = r;
        }, function(error) {
            console.log("Error  " + error);
        });

    };
    list();

    $scope.cancel = function() {
        //$mdDialog.hide();
        $mdDialog.cancel();
    };

    $scope.new = function() {
        $scope.proveedor.id=null;
        $mdDialog.show({
            scope: $scope.$new(),
            templateUrl: 'app/views/Proveedor/form.html',
            parent: angular.element(document.body),
            clickOutsideToClose:true
        }).then(function(){
            $scope.list($scope.page);
            $scope.proveedor={};
        }, function(){
        });
    };

    $scope.get = function(d) {
        $scope.proveedor = API.Proveedor.get({id : d.id});
        $mdDialog.show({
            scope: $scope.$new(),
            templateUrl: 'app/views/Proveedor/form.html',
            parent: angular.element(document.body),
            clickOutsideToClose:true
        }).then(function(){
            $scope.list($scope.page);
            $scope.proveedor={};
        }, function(){
        });
    };

    $scope.save = function() {
        if ($scope.proveedor.id) {
            API.Proveedor.update({ id: $scope.proveedor.id }, $scope.proveedor).$promise.then(function(r) {
                console.log(r);
                list();
                $mdDialog.hide();
            }, function(error) {
                console.log("Error  " + error);
            });
        } else {
            API.Proveedor.save($scope.proveedor).$promise.then(function(r) {
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
            API.Proveedor.delete({ "id": d.id }).$promise.then(function (r) {
                console.log(r);
                list();
            }, function (error) {
                console.log(error);
            });
        }
    };

});