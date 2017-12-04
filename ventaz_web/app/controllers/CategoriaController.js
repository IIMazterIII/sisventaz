ventazApp

.controller("CategoriaController", function($scope, API, $window, $mdDialog) {
    
    $scope.d_list = [];
    $scope.categoria = {};

    list = function() {
        API.Categoria.query(function(r) {
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
        $scope.categoria.id=null;
        $mdDialog.show({
            scope: $scope.$new(),
            templateUrl: 'app/views/Categoria/form.html',
            parent: angular.element(document.body),
            clickOutsideToClose:true
        }).then(function(){
            $scope.list($scope.page);
            $scope.categoria={};
        }, function(){
        });
    };

    $scope.get = function(d) {
        $scope.categoria = API.Categoria.get({id : d.id});
        $mdDialog.show({
            scope: $scope.$new(),
            templateUrl: 'app/views/Categoria/form.html',
            parent: angular.element(document.body),
            clickOutsideToClose:true
        }).then(function(){
            $scope.list($scope.page);
            $scope.categoria={};
        }, function(){
        });
    };

    $scope.save = function() {
        if ($scope.categoria.id) {
            API.Categoria.update({ id: $scope.categoria.id }, $scope.categoria).$promise.then(function(r) {
                console.log(r);
                list();
                $mdDialog.hide();
            }, function(error) {
                console.log("Error  " + error);
            });
        } else {
            API.Categoria.save($scope.categoria).$promise.then(function(r) {
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
            API.Categoria.delete({ "id": d.id }).$promise.then(function (r) {
                console.log(r);
                list();
            }, function (error) {
                console.log(error);
            });
        }
    };

});