function add(matA, matB){
	if(matA.length != matB.length){
		alert("Your matrices don't have the same number of rows");
		return;
	}
	var result = [];
    try{
        for(var i=0; i<matA.length; i++){
            result[i] = [];
            for(var j=0; j<matA[0].length; j++){
                result[i][j] = matA[i][j] + matB[i][j];
            }
        } 
        return result;
    }
    catch(er){
         alert("Your matrices don't look right, cannot compute");
         return;
    }
}

function subtract(matA, matB){
	if(matA.length != matB.length){
		alert("Your matrices don't have the same number of rows");
		return;
	}
	var result = [];
    try{
        for(var i=0; i<matA.length; i++){
            result[i] = [];
            for(var j=0; j<matA[0].length; j++){
                result[i][j] = matA[i][j] - matB[i][j];
            }
        } 
        return result;
    }
    catch(er){
        alert("Your matrices don't look right, cannot compute");
        return;
    }
    
}

function multiply(matA, matB){
	if(matA[0].length != matB.length){
		alert("Hmm cannot multiply your matrices, the column and row numbers don't look right");
		return;
	}
	var row = matA.length;
	var col = matA[0].length;
	var col2 = matB[0].length;
	var result = [];
    try{
        for(var i=0; i<col; i++){
            result[i] = [];
        }
        var total;
        for(var i=0; i<row; i++){
            for(var k=0; k<col2; k++){
                total = 0;
                for(var j=0; j<col; j++){
                    total += matA[i][j] * matB[j][k];
                }
                result[i][k] = total;
            }
        }
        return result;
    }
    catch(er){
        alert("Your matrices don't look right, cannot compute");
        return;
    }
}

function transpose(matrix){
	var transposed = new Array(matrix[0].length);
	for(var i=0; i<matrix[0].length; i++){
		transposed[i] = new Array(matrix.length);
	}
	for(var i=0; i<matrix.length; i++){
		for(var j=0; j<matrix[0].length; j++){
			transposed[j][i] = matrix[i][j];
		}
	}
	return transposed;
}

function dotProduct(vecA, vecB){
	return mutiply(vecA, transpose(vecB))[0][0];
}

function prettify(matrix, name){
    if(name == null){
        name = 'Answer';
    }
    var row = '';
    for(var i=0; i<matrix.length; i++){
        row += '<mtr>';
        for(var j=0; j<matrix[0].length; j++){
            row += ('<mtd><mi>' + matrix[i][j] + '</mi></mtd>');
        }
        row += '</mtr>';
    }
    var html = '<math xmlns="http://www.w3.org/1998/Math/MathML"><mrow><mi>' + name + '</mi><mo>=</mo><mfenced open="[" close="]"><mtable>' + row + '</mtable></mfenced></mrow></math>';
    return html;
}

function check(matrix){
    var cols = matrix[0].length;
    for(var i=0; i<matrix.length; i++){
        if(matrix[i].length != cols){
            alert("One or more columns need more inputs");
            return false;
        }
    }
    return true; 
}
