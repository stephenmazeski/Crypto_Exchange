//This file contains the JavaScript for dashboard.html


//Globals and configuration variables
var tableTimer;
var username;
var order_data = [];


var columns = 3;
var rows = 16;


var currentIndex = 0;
var shiftBy = 2;
var secondsBetweenUpdates = 1;

$(document).ready(function(){

	//If user is not currently logged in, redirect to landing page
	check_if_logged_in();

	username = sessionStorage.getItem("username");
	//console.log(username);
	

	//Get order data for table from server
	get("/get_orders", function(response){

		order_data = response;


		/***********************************************
			Now that order data is correctly formatted:
				1. Create an HTML table
				2. Add order data to table
		************************************************/
		

		/*var table_html = '';

		table_html += ` <thead>
							<tr>
								<th>Column 1</th>
								<th>Column 2</th>
								<th>Column 3</th>
							</tr>
						</thead>
						<tbody>`

		for(let i = 0; i < rows; i++){

			table_html += '<tr>';
			for(let j = 0; j < columns; j++){
				table_html += '<td>' +  +'</td>';
			}
		}*/



		//Create HTML table
		for(let i = 0; i < rows; i++){
			var rowNode = document.createElement("TR");
			for(let j = 0; j < columns; j++){
				var dataCellNode = document.createElement("TD");

				var column_mapping = [4, 2, 5];

				var text = order_data[i][column_mapping[j]];

				var text;
				if(j == 0){
					text = order_data[i][4];
				}

				else if(j == 1){
					text = order_data[i][2];
				}

				else if(j == 2){
					text = order_data[i][5];
				}

				var textNode = document.createTextNode(order_data[i][column_mapping[j]]);
				dataCellNode.appendChild(textNode);
				rowNode.appendChild(dataCellNode);
			}
			document.getElementById("order_table").appendChild(rowNode);
		}
		

		//Call updateTable() every secondsBetweenUpdates seconds
		tableTimer = window.setInterval(updateTable, secondsBetweenUpdates * 1000);
	});


	//Sample graph to build off of
	TESTER = document.getElementById('graph');
	Plotly.plot(TESTER, [{
		x: [1, 2, 3, 4, 5],
		y: [1, 2, 4, 8, 16]
	}], {
		margin: {
		t: 0
	}});
}); 	//end of document.ready
	

//This is the function that's called every x seconds to update the table
var updateTable = function(){
	var currentRow = $("tr").first();
	for(let i = 1; i < rows; i++){

		var currentCell = currentRow.children().first();

		currentCell.text(order_data[currentIndex + i][4]);
		currentCell = currentCell.next();
		currentCell.text(order_data[currentIndex + i][2]);
		currentCell = currentCell.next();
		currentCell.text(order_data[currentIndex + i][5]);

		currentRow = currentRow.next();
	}
	currentIndex += shiftBy;
}


var pauseData = function(){
	clearInterval(tableTimer);
}


var place_order = function(order_type){

    var order_info = {
		amount : document.getElementById('amount').value,
		price : document.getElementById('price').value,
		order_type : order_type
    };

    post('/submit_order', order_info, function(response){
    	console.log(response)
    });
}







/*
//Generate data
var coins = ["BTC", "ETH", "LTC", "XRP", "NEO"];
var orderLimit = 1000;
var orders = [];
for(let i = 0; i < orderLimit; i++){
	var coinIndex = Math.floor(Math.random() * coins.length);
	orders.push({
		coin1: coins[coinIndex],
		amount1: Math.floor(Math.random() * 100),
		coin2: coins[coins.length - 1 - coinIndex],
		amount2: Math.floor(Math.random() * 100)
	});
	//console.log(orders[orders.length - 1]);
}
*/