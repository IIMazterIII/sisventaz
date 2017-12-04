ventazApp

.controller("TrabajadorController", function($scope, API, $window, $mdDialog) {
    
    $scope.d_list = [];
    $scope.trabajador = {};

    list = function() {
        API.Trabajador.query(function(r) {
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
        $scope.trabajador.id=null;
        $mdDialog.show({
            scope: $scope.$new(),
            templateUrl: 'app/views/Trabajador/form.html',
            parent: angular.element(document.body),
            clickOutsideToClose:true
        }).then(function(){
            $scope.list($scope.page);
            $scope.trabajador={};
        }, function(){
        });
    };

    $scope.get = function(d) {
        $scope.trabajador = API.Trabajador.get({id : d.id});
        $mdDialog.show({
            scope: $scope.$new(),
            templateUrl: 'app/views/Trabajador/form.html',
            parent: angular.element(document.body),
            clickOutsideToClose:true
        }).then(function(){
            $scope.list($scope.page);
            $scope.trabajador={};
        }, function(){
        });
    };

    $scope.save = function() {
        if ($scope.trabajador.id) {
            API.Trabajador.update({ id: $scope.trabajador.id }, $scope.trabajador).$promise.then(function(r) {
                console.log(r);
                list();
                $mdDialog.hide();
            }, function(error) {
                console.log("Error  " + error);
            });
        } else {
            API.Trabajador.save($scope.trabajador).$promise.then(function(r) {
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
            API.Trabajador.delete({ "id": d.id }).$promise.then(function (r) {
                console.log(r);
                list();
            }, function (error) {
                console.log(error);
            });
        }
    };

});