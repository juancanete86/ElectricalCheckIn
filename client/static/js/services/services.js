// Services
app.service('UsersServices', function UsersServices($resource) {
        console.log("userServices");

        return $resource(
            'http://localhost:8000/users', {}, {
                get: {method: 'GET', cache: false, isArray: true}
            });
    });

app.service('SingleUserServices', function UsersServices($resource) {
        console.log("userServices");

        return $resource(
            'http://localhost:8000/users/:id', {}, {
                get: {method: 'GET', cache: false, isArray: true}
            });
    });

app.service('BillsServices', function UsersServices($resource) {
        console.log("BillsServices");

        return $resource(
            'http://localhost:8000/bills', {}, {
                get: {method: 'GET', cache: false, isArray: true}
            });
    });
app.service('BillServices', function UsersServices($resource) {
        console.log("BillServices deleteing!!!");

        return $resource(
            'http://localhost:8000/bills/:id', {}, {
                get: {method: 'GET', cache: false, isArray: false},
                save: {method: 'POST', cache: false, isArray: false},
                update: {method: 'PUT', cache: false, isArray: false},
                delete: {method: 'DELETE', cache: false, isArray: false}
            });
    });