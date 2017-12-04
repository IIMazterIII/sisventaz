ventazApp

.controller("AlmacenController", function($scope, API, $window, $mdDialog) {
    
    $scope.d_list = [];
    $scope.almacen = {};

    list = function() {
        API.Almacen.query(function(r) {
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
        $scope.almacen.id=null;
        $mdDialog.show({
            scope: $scope.$new(),
            templateUrl: 'app/views/Almacen/form.html',
            parent: angular.element(document.body),
            clickOutsideToClose:true
        }).then(function(){
            $scope.list($scope.page);
            $scope.almacen={};
        }, function(){
        });
    };

    $scope.get = function(d) {
        $scope.almacen = API.Almacen.get({id : d.id});
        $mdDialog.show({
            scope: $scope.$new(),
            templateUrl: 'app/views/Almacen/form.html',
            parent: angular.element(document.body),
            clickOutsideToClose:true
        }).then(function(){
            $scope.list($scope.page);
            $scope.almacen={};
        }, function(){
        });
    };

    $scope.save = function() {
        if ($scope.almacen.id) {
            API.Almacen.update({ id: $scope.almacen.id }, $scope.almacen).$promise.then(function(r) {
                console.log(r);
                list();
                $mdDialog.hide();
            }, function(error) {
                console.log("Error  " + error);
            });
        } else {
            API.Almacen.save($scope.almacen).$promise.then(function(r) {
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
            API.Almacen.delete({ "id": d.id }).$promise.then(function (r) {
                console.log(r);
                list();
            }, function (error) {
                console.log(error);
            });
        }
    };

});