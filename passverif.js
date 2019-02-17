function passStr() {
	var password = document.getElementById("myPwd").value;
	var passwordCfm = document.getElementById("myPwdCfm").value;
	
	if (password != passwordCfm) {
		alert("Passwords do not match.");
		exit();
	}
	
	var hasUpp = 0;
	var hasNum = 0;
	
	var i;
	
	for (i in password) {
		var x = password.charAt(i);
		if (isNaN(x) && x == x.toUpperCase()) {;
			hasUpp += 1;
		}
		
		if (!isNaN(x)) {
			hasNum += 1;
		}
		
	}
	
	if (password.length < 8) {
		alert("Your password must be at least 8 characters.");
		exit();
	}
	
	if (hasUpp < 1) {
		alert("Your psasword must contain an uppercase letter.");
		exit();
	}
		
	if (hasNum < 1) {
		alert("Your password must contain a number.");
		exit();
	}
	
	alert("User successfully created.");
	
}