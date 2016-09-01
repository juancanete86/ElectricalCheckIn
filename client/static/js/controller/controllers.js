// Controllers
app.controller('UserCtrl',  function ($scope) {
    $scope.users = [];

    service = angular.element(document.body).injector().get('UsersServices');

    service.get({},
        function success(response) {
            $scope.users = response;
        }, function error(errorResponse) {
            console.log("Error: " + JSON.stringify(errorResponse))
        })
});

app.controller('CurrentUserCtrl',  ['$scope', '$http', '$routeParams',
    function ($scope, $http, $routeParams) {
    service = angular.element(document.body).injector().get('SingleUserServices');
        service.get({},function success(response) {
            $scope.users = response
        });
}]);

//Controller to get a set of bills
app.controller('SetBillsCtrl',  ['$scope','BillsServices',
    function ($scope, service) {
        $scope.bills = [];

        service.get({},
            function success(response) {
                $scope.bills = response;

                console.log("BillCtrl success: " + JSON.stringify($scope.bills));
            }, function error(errorResponse) {
                console.log("Error: " + JSON.stringify(errorResponse))
            })
}]);

//Controller to get information of a single bill
app.controller('BillCtrl',  ['$scope','$routeParams','$location','BillsServices',
    function ($scope, $routeParams, $location, service) {
        $scope.bills = [];

        service.get({},
            function success(response) {
                $scope.bills = response;
            }, function error(errorResponse) {
                console.log("Error: " + JSON.stringify(errorResponse))
            })
}]);

app.controller('CurrentBillDelCtrl',  ['$scope', '$http', '$routeParams',
    function ($scope, $http, $routeParams) {
        $http({
                url: '/bills/' + $routeParams.id,
                method: 'DELETE'
                }).success(function(out_data) {
                    console.log("Deleted.")
                });
}]);

app.controller('CurrentBillEditCtrl',  ['$scope', '$http', '$routeParams',
    function ($scope, $http, $routeParams) {
        $http({
                url: '/bills/' + $routeParams.id,
                method: 'GET'
                }).success(function(out_data) {
                    $scope.bill = out_data
                });
}]);

app.controller('NewBillCtrl',  ['$scope','$http','$cookies','BillsServices',
    function ($scope, $http, $cookies, service) {
        $http.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';

        // To send the csrf code.
        $http.defaults.headers.post['X-CSRFToken'] = $cookies.csrftoken;

        // This function is called when the form is submitted.
        $scope.submit = function ($event) {
            // Prevent page reload.
            $event.preventDefault();

            // Send the data.
            var in_data = jQuery.param({'identifier':$scope.bill.identifier,'amount_price': $scope.bill.amount_price,
                'taxes': $scope.bill.taxes, 'power_consumed':$scope.bill.power_consumed,
                'csrfmiddlewaretoken': $cookies.csrftoken});

            $http({
                url: 'addbill',
                method: 'POST',
                data: in_data
                }).success(function(out_data) {
                    $scope.bill = angular.copy({});
                });
        }
}]);