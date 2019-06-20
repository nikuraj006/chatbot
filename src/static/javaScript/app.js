var app = angular.module("myApp", []);
app.controller("myCtrl", function($scope,$http) {
	$scope.data = "Some thing";
	 var d = new Date();
     var hour = d.getHours();
     if(hour <=12){
          $scope.actionTime ="Good Morning";
     }else if(hour <=16){
          $scope.actionTime = "Good Afternoon";
     }else{
          $scope.actionTime = "Good Evening";
     }
     $scope.currentAction = $scope.actionTime;
     $scope.firstQuestion = "How can I help you?";
     var template = "<tr><td>"+$scope.currentAction+"</td></tr><tr align='right'><td>"+$scope.firstQuestion+"</td></tr>";
                 $('#chatData').append(template);

    $scope.myFunc = function () {
		//alert($scope.clientData);
		console.log($scope.clientData);
		var postData={user: $scope.clientData}

		$.ajax({
            url: '/chatting',
            data: postData,
            type: 'POST',
            success: function(response) {
                console.log(response);
                console.log(response.data.in_response_to);
                console.log(response.data.created_at);
                console.log(response.data.text);
                $scope.data = response.data.text;
                var html = "<tr><td>"+response.data.in_response_to+"</td></tr><tr align='right'><td>"+response.data.text+"</td></tr>";
                 $('#chatData').append(html);
                 $('#clientData').val('');

            },
            error: function(error) {
                console.log(error);
            }
        });

    }
    console.log("response data-----"+$scope.data);
    console.log("response data-----"+$scope.currentAction);
    console.log("response data-----"+$scope.firstQuestion);
});