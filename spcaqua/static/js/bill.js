function calculateRupees(tag)
{
	var row = tag.id[0];
	var qty = document.getElementById(row+'2').value;
	var rate = document.getElementById(row+'3').value;
	
	var rupees = parseFloat(qty)*parseFloat(rate);
	if(!isNaN(rupees))
		document.getElementById(row+'4').value=rupees;
	else
		document.getElementById(row+'4').value='';
	//console.log('calculateRupees Called for '+tag);
}


$(document).ready(function(){
	for(var i=0;i<12;i++)
	{
		bindKeyUp(i);
	}
});
function bindKeyUp(num)
{
	var i = num;
	$('#id_form-'+i+'-quantity,#id_form-'+i+'-rate').keyup(function(){
		var qty=Number(parseFloat($('#id_form-'+i+'-quantity').val()).toFixed(3));
		var rate=Number(parseFloat($('#id_form-'+i+'-rate').val()).toFixed(3));
		//if(!isNaN(qty)) $('#id_form-'+i+'-quantity').val(qty);
		//if(!isNaN(rate)) $('#id_form-'+i+'-rate').val(rate);
		var price = parseFloat(qty)*parseFloat(rate);
		if(!isNaN(price))
			$('#id_form-'+i+'-price').val(Number((price).toFixed(3)));
		else
			$('#id_form-'+i+'-price').val('');
	});
}

function validateBill()
{
	var tosubmit = false;
    for(var i=0;i<12;i++)
	{
		var qtystr = $('#id_form-'+i+'-quantity').val();
		if(qtystr!=='' && qtystr!==null && qtystr!==undefined)
			tosubmit = true;
        
        var qty=Number(parseFloat($('#id_form-'+i+'-quantity').val()).toFixed(3));
		var rate=Number(parseFloat($('#id_form-'+i+'-rate').val()).toFixed(3));
		if(!isNaN(qty)) $('#id_form-'+i+'-quantity').val(qty);
		if(!isNaN(rate)) $('#id_form-'+i+'-rate').val(rate);
	}
    if(tosubmit)
        return true;
	alert('Empty bill not allowed! Enter atleast one Quantity');
	return false;
}
