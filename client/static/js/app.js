app = angular.module ('billApp', ['ngResource','ngRoute', 'ngCookies']);

app.config(['$routeProvider', function ($routeProvider) {
        $routeProvider
            .when('/users',{
                templateUrl:'user.html',
                controller:'UserCtrl'
            })
            .when('/users/:id',{
                templateUrl:'user-info.html',
                controller:'CurrentUserCtrl'
            })
            .when('/billsdel/:id',{
                templateUrl:'bill.html',
                controller:'CurrentBillDelCtrl'
            })
            .when('/bill-edit/:id',{
                templateUrl:'bill-new.html',
                controller:'CurrentBillEditCtrl'
            })
            .when('/bills',{
                templateUrl:'bill.html',
                controller:'SetBillsCtrl'
            })
            .when('/userbills/:id',{
                templateUrl:'bill.html',
                controller:'BillCtrl'
            })
            .when('/bill-new', {
              templateUrl: 'bill-new.html',
              controller: 'NewBillCtrl'
            })
            .otherwise({
                redirectTo: '/'
            })
    }]);

app.config(['$httpProvider', function ($httpProvider) {
        $httpProvider.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';
        $httpProvider.defaults.xsrfCookieName = 'csrftoken';
        $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
}]);