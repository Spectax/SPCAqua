$(document).ready(function(){
	for(var i=0;i<5;i++)
	{
		bindKeyUp(i);
	}
});
function bindKeyUp(num)
{
	var i = num;
	$('#id_form-'+i+'-no_of_cans,#id_form-'+i+'-rate').keyup(function(){
		var cans=Number(parseFloat($('#id_form-'+i+'-no_of_cans').val()).toFixed(3));
		var rate=Number(parseFloat($('#id_form-'+i+'-rate').val()).toFixed(3));
		var price = parseFloat(cans)*parseFloat(rate);
		if(!isNaN(price))
			$('#id_form-'+i+'-price').val(Number((price).toFixed(3)));
		else
			$('#id_form-'+i+'-price').val('');
	});
}

function validatePurchaseBill()
{
	var tosubmit = false;
    for(var i=0;i<5;i++)
	{
		var canstr = $('#id_form-'+i+'-no_of_cans').val();
		if(canstr!=='' && canstr!==null && canstr!==undefined)
			tosubmit = true;
        
        var cans=Number(parseFloat($('#id_form-'+i+'-no_of_cans').val()).toFixed(3));
		var rate=Number(parseFloat($('#id_form-'+i+'-rate').val()).toFixed(3));
		if(!isNaN(cans)) $('#id_form-'+i+'-no_of_cans').val(cans);
		if(!isNaN(rate)) $('#id_form-'+i+'-rate').val(rate);
	}
    if(tosubmit)
        return true;
	alert('Empty bill not allowed! Enter atleast one Can!');
	return false;
}