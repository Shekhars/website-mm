function totalCostCal() {
	var noOfPartners = document.getElementById('noOfPartners').value;
	var authCapital = document.getElementById('authCapital').value;
	var stateName = document.getElementById('stateName').value;
	var ROC = authCapitals(authCapital);
	var stamp = stampCalculate(stateName);
	var misc = 9400;
	var total =  ROC +stamp + misc + (1300*noOfPartners) ;
	document.getElementById('actualCost').innerText='₹ '+ total + '/-';
    document.getElementById('cost').value = total;
    document.getElementById('submitbut').disabled = false;
}