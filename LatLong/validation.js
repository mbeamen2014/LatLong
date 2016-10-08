function validateForm() {
		var item = document.getElementById("firstlat");
		if ( check_non_empty(item) == false ) {
            item.focus();
            return false;
        }
		if ( check_lat(item) == false ) {
			item.focus();
			return false;
		}
		
		var item = document.getElementById("firstlong");
		if ( check_non_empty(item) == false ) {
            item.focus();
            return false;
        }
		if ( check_long(item) == false ) {
			item.focus();
			return false;
		}
		
		var item = document.getElementById("secondlat");
		if ( check_non_empty(item) == false ) {
            item.focus();
            return false;
        }
		if ( check_lat(item) == false ) {
			item.focus();
			return false;
		}
		
		var item = document.getElementById("secondlong");
		if ( check_non_empty(item) == false ) {
            item.focus();
            return false;
        }
		if ( check_long(item) == false ) {
			item.focus();
			return false;
		}
		
        return true;
    }


    function check_non_empty(item) {
        if (item.value == "") {
            alert("The " + item.name + " was left empty.");
            return false;
        }
        return true;
    }
	
	function check_long(item) {
  
        if ((item.value > 180 || item.value < -180) || isNaN(item.value) == true) {
            alert("Enter a number between 180 and -180 in the " + item.name + " field.");
            return false;
        }
        return true;
    }
	
	function check_lat(item) {
  
        if ((item.value > 90 || item.value < -90) || isNaN(item.value) == true) {
            alert("Enter a number between 90 and -90 in the " + item.name + " field.");
            return false;
        }
        return true;
    }