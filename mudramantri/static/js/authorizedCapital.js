function authCapitals(authCapc)
{
	//var theForm = document.forms["calculator"];
	//var authCapital = theForm.elements["capitalvalue"];
	var moa = 5000;
	var form = null;
	var aoa = null;
	var fee = null;
	var fee_min=5600;
	var authCapital = authCapc;
	
	if(authCapital==100000){
		fee = fee_min;
	}
	if(authCapital>100000){
		form = 300;
		aoa = 300;
		var mid1=authCapital-100000;
		var mx = (Math.floor((mid1)/10000))>40?40:(Math.floor((mid1)/10000));
		moa= moa + mx*400;
		if(mid1%10000!==0){
			moa=moa+400;
		}
		fee = fee_min+form+aoa+moa;
	}
	if(authCapital>500000){
		form=400;
		aoa=400;
		var mid2=authCapital-500000;
		var mx = (Math.floor((mid1)/10000))>50?50:(Math.floor((mid2)/10000));
		moa= moa +mx*300;
		if(mid2%10000!==0){
			moa=moa+300;
		}
		fee = form+aoa+moa;
	}
	if(authCapital>2500000){
		form=500;
		aoa=500;
		var mid3=authCapital-2500000;
		var mx = (Math.floor((mid1)/10000))>450?450:(Math.floor((mid3)/10000));
		moa= moa + mx*300;
		if(mid3%10000!==0){
			moa=moa+300;
		}
		fee = form+aoa+moa;
	}
	if(authCapital>5000000){
		form=600;
		aoa=600;
		var mid4=authCapital-5000000;
		var mx = (Math.floor((mid1)/10000))>500?500:(Math.floor((mid4)/10000));
		moa= moa + mx*100;
		if(mid4%10000!==0){
			moa=moa+100;
		}
		fee = form+aoa+moa;
	}
	if(authCapital>10000000){
		form=600;
		aoa=600;
		var mid5=authCapital-10000000;
		var mx = (Math.floor((mid1)/10000))>1000?1000:(Math.floor((mid5)/10000));
		moa= moa + mx*75;
		if(mid5%10000!==0){
			moa=moa+75;
		}
		fee = form+aoa+moa;
	}
	if(authCapital>20000000){
		form=600;
		aoa=600;
		var mid6=authCapital-10000000;
		moa= moa + Math.floor((mid6)/10000)*75;
		if(mid6%10000!==0){
			moa=moa+75;
		}
		fee = form+aoa+moa;
	}
	return fee;
}