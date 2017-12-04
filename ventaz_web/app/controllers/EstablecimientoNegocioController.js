ventazApp

.controller("EstablecimientoNegocioController", function($scope, API, $window, $mdDialog) {
    
    $scope.d_list = [];
    $scope.establecimientonegocio = {};

    list = function() {
        API.EstablecimientoNegocio.query(function(r) {
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
        $scope.establecimientonegocio.id=null;
        $mdDialog.show({
            scope: $scope.$new(),
            templateUrl: 'app/views/EstablecimientoNegocio/form.html',
            parent: angular.element(document.body),
            clickOutsideToClose:true
        }).then(function(){
            $scope.list($scope.page);
            $scope.establecimientonegocio={};
        }, function(){
        });
    };

    $scope.get = function(d) {
        $scope.establecimientonegocio = API.EstablecimientoNegocio.get({id : d.id});
        $mdDialog.show({
            scope: $scope.$new(),
            templateUrl: 'app/views/EstablecimientoNegocio/form.html',
            parent: angular.element(document.body),
            clickOutsideToClose:true
        }).then(function(){
            $scope.list($scope.page);
            $scope.establecimientonegocio={};
        }, function(){
        });
    };

    $scope.save = function() {
        if ($scope.establecimientonegocio.id) {
            API.EstablecimientoNegocio.update({ id: $scope.establecimientonegocio.id }, $scope.establecimientonegocio).$promise.then(function(r) {
                console.log(r);
                list();
                $mdDialog.hide();
            }, function(error) {
                console.log("Error  " + error);
            });
        } else {
            API.EstablecimientoNegocio.save($scope.establecimientonegocio).$promise.then(function(r) {
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
            API.EstablecimientoNegocio.delete({ "id": d.id }).$promise.then(function (r) {
                console.log(r);
                list();
            }, function (error) {
                console.log(error);
            });
        }
    };

});