function stampCalculate(stateName, authCapital) {
	var form = null;
	var moa = null;
	var aoa = null;
	var fee = null;
	if (stateName === 'Del') {
		form = 10;
		moa = 200;
		var mid = authCapital * 0.15 / 100
		aoa = (mid) < 2500000 ? (mid) : 2500000;
	}
	if (stateName === 'Har') {
		form = 15;
		moa = 60;
		aoa = authCapital < 100000 ? 60 : 120;
	}
	if (stateName === 'Mah') {
		form = 100;
		moa = 200;
		var mid = Math.floor(authCapital / 500000) * 1000;
		aoa = ((authCapital % 500000 == 0) ? mid : (mid + 1000));
		aoa = aoa < 5000000 ? aoa : 5000000;
	}
	if (stateName === 'Or') {
		form = 10;
		moa = 300;
		aoa = 300;
	}
	if (stateName === 'Ap') {
		form = 20;
		moa = 500;
		var mid = 0.15 * authCapital / 100;
		if (mid < 1000) {
			aoa = 1000;
		}
		else {
			aoa = mid < 500000 ? mid : 500000;
		}
	}
	if(stateName==='Bi'){
		form=20;
		moa=500;
		aoa=1000;
	}
	if (stateName === 'Jh') {
		form = 5;
		moa = 63;
		aoa = 105;
	}
	if (stateName === 'Jk') {
		form = 10;
		moa = 150;
		aoa = authCapital <= 100000 ? 150 : 300;
	}
	if (stateName === 'Tn') {
		form = 20;
		moa = 200;
		aoa = 300;
	}
	if (stateName === 'Pud') {
		form = 10;
		moa = 200;
		aoa = 300;
	}
	if (stateName === 'As') {
		form = 15;
		moa = 200;
		aoa = 310;
	}
	if (stateName === 'Me') {
		form = 10;
		moa = 100;
		aoa = 300;
	}
	if (stateName === 'Ma') {
		form = 10;
		moa = 100;
		aoa = 150;
	}
	if (stateName === 'Na') {
		form = 10;
		moa = 100;
		aoa = 150;
	}
	if (stateName === 'Tr') {
		form = 10;
		moa = 100;
		aoa = 150;
	}
	if (stateName === 'Ar') {
		form = 10;
		moa = 200;
		aoa = 500;
	}
	if (stateName === 'Mi') {
		form = 10;
		moa = 100;
		aoa = 150;
	}
	if (stateName === 'La') {
		form = 25;
		moa = 500;
		aoa = 1000;
	}
	if (stateName === 'Ch') {
		form = 3;
		moa = 500;
		aoa = 1000;
	}
	if (stateName === 'Up') {
		form = 10;
		moa = 500;
		aoa = 500;
	}
	if (stateName === 'Uk') {
		form = 10;
		moa = 500;
		aoa = 500;
	}
	if (stateName === 'Wb') {
		form = 10;
		moa = 60;
		aoa = 300;
	}
	if (stateName === 'Dn') {
		form = 1;
		moa = 15;
		aoa = 25;
	}
	if (stateName === 'And') {
		form = 20;
		moa = 200;
		aoa = 300;
	}
	if (stateName === 'Ke') {
		form = 25;
		moa = 500;
		if (authCapital <= 1000000) {
			aoa = 2000;
		}
		if (authCapital > 1000000 && authCapital <= 2500000) {
			aoa = 5000;
		}
		if (authCapital > 2500000) {
			aoa = 0.5 * authCapital / 100;
		}
	}
	if (stateName === 'Mp') {
		form = 50;
		moa = 2500;
		var mid = 0.15 * authCapital / 100;
		aoa = mid > 5000 ? mid : 5000;
		aoa = aoa < 2500000 ? aoa : 2500000;
	}
	if (stateName === 'Cg') {
		form = 10;
		moa = 500;
		var mid = authCapital * 0.15 / 100;
		aoa = (mid) > 5000 ? mid : 5000;
		aoa = aoa < 500000 ? aoa : 500000;
	}
	if (stateName === 'Rj') {
		form = 10;
		moa = 500;
		aoa = 0.5 * authCapital / 100;
	}
	if (stateName === 'Pu') {
		form = 25;
		moa = 5000;
		aoa = authCapital <= 100000 ? 5000 : 10000;
	}
	if (stateName === 'Hp') {
		form = 3;
		moa = 60;
		aoa = authCapital <= 100000 ? 60 : 120;
	}
	if (stateName === 'Kar') {
		form = 20;
		moa = 1000;
		var mid = Math.floor(authCapital / 1000000) * 500;
		aoa = mid + ((authCapital % 1000000) > 0 ? 500 : 0);
	}
	if (stateName === 'Guj') {
		form = 20;
		moa = 100;
		var mid = 0.5 * authCapital / 100;
		aoa = mid < 500000 ? mid : 500000;
	}
	if (stateName === 'Go') {
		form = 50;
		moa = 150;
		var mid = Math.floor(authCapital / 500000) * 1000;
		aoa = mid + ((authCapital % 500000) > 0 ? 1000 : 0);
	}
	if (stateName === 'Dd') {
		form = 20;
		moa = 150;
		var mid = Math.floor(authCapital / 500000) * 1000;
		aoa = mid + ((authCapital % 500000) > 0 ? 1000 : 0);
	}
	return form+moa+aoa;
}