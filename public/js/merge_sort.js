
function merge_sort(array) {
	if(array.length <= 1) {
		return array;
	}
	var middle = Math.round(array.length/2);
	var left = [];
	var right = [];
	for(var i = 0; i < middle; i++){
		left.push(array[i]);
	}
	for(var j = middle; j < array.length; j++){
		right.push(array[j]);
	}
	left = merge_sort(left);
	right = merge_sort(right);
	var result = merge(left, right);
	return result;
}

function merge(left,right) {
	var result = [];
	while(left.length > 0 || right.length > 0){
		if(left.length > 0 && right.length > 0){
			if(left[0] <right[0]){
				result.push(left[0]);
				left.shift();
			}else{
				result.push(right[0]);
				right.shift();
			}
		}else if(left.length > 0){
			result.push(left[0]);
			left.shift();
		}else if(right.length > 0){
			result.push(right[0]);
			right.shift();
		}
	}
		return result;
}

function display(){
	var test = [5,4,3,2,1];
    $("#demo").html('Sorted list: ' + merge_sort(test).join(", "));
}

