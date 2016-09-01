var module = angular.module("sampleApp", ['ngRoute','ngResource','ngSanitize','ngTouch','chart.js']);
module.config(function ($interpolateProvider) {
    $interpolateProvider.startSymbol('[[').endSymbol(']]');
})
module.config(['$routeProvider',
    function($routeProvider) {
        $routeProvider.
            when('/route1', {
                templateUrl: static_url + 'angularapp/html/test1.html',
                controller: 'UserCtrl'
            }).
            when('/route2', {
                templateUrl: static_url + 'angularapp/html/test2.html',
                controller: 'RouteController2'
            }).
            otherwise({
                redirectTo: '/'
            });
    }]);

module.service('myService', ['$resource', function ($resource) {
    console.log("userServices");

    return $resource(
        'http://rest-service.guides.spring.io/greeting', {}, {
            get: {method: 'GET', cache: false, isArray: true}
        });
}]);

module.controller("UserCtrl",  function($scope) {
    //$scope.test="This is working test1"
    $scope.users = [];

    console.log("UserCtrl 11111")
    service = angular.element(document.body).injector().get('myService');

    service.get({},
        function success(response) {
            console.log("UserCtrl success: " + JSON.stringify(response));
            $scope.users = response;

            console.log("UserCtrl success: " + JSON.stringify($scope.users));
        }, function error(errorResponse) {
            console.log("Error: " + JSON.stringify(errorResponse))
        });
});
module.controller("RouteController2", function($scope) {
    $scope.test="This is working test2"
});

module.controller("LineCtrl", function($scope){
  $scope.labels = ["January", "February", "March", "April", "May", "June", "July"];
  $scope.series = ['Series A', 'Series B'];
  $scope.data = [
    [65, 59, 80, 81, 56, 55, 40],
    [28, 48, 40, 19, 86, 27, 90]
  ];
  $scope.onClick = function (points, evt) {
    console.log(points, evt);
  };
  $scope.datasetOverride = [{ yAxisID: 'y-axis-1' }, { yAxisID: 'y-axis-2' }];
  $scope.options = {
    scales: {
      yAxes: [
        {
          id: 'y-axis-1',
          type: 'linear',
          display: true,
          position: 'left'
        },
        {
          id: 'y-axis-2',
          type: 'linear',
          display: true,
          position: 'right'
        }
      ]
    }
  };
});
