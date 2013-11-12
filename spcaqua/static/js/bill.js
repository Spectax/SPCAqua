function initTable(numRows)
{
	for(var i=0;i<numRows;i++)
		addRow();
}

function addRow()
{
	var table=document.getElementById('billTable');
	var noOfRows = table.rows.length;
	var row=table.insertRow(-1);
	for(var i=0;i<6;i++)
	{
		var cell = row.insertCell(i);
		if(i==0)
			cell.innerHTML = '<input id="'+noOfRows+'0" class="bill-input" type="text" value="'+noOfRows+'." />';
		else if(i==1)
			cell.innerHTML='<input id="'+noOfRows+'1" class="bill-input" type="text" />';
		else if(i==2)
			cell.innerHTML='<input id="'+noOfRows+'2" onkeyup="calculateRupees(this)" class="bill-input" type="text" />';
		else if(i==3)
			cell.innerHTML='<input id="'+noOfRows+'3" onkeyup="calculateRupees(this)" class="bill-input" type="text" />';
		else if(i==4)
			cell.innerHTML = '<input id="'+noOfRows+'4" class="bill-input" type="text" value="" />';
		else if(i==5)
			cell.innerHTML = '<button id="'+noOfRows+'5" class="bill-button" onclick="delRow('+noOfRows+')">Delete</button>';
	}
}
function delRow(rowNum)
{
	var table=document.getElementById('billTable');
	var noOfRows = table.rows.length;
	
	table.deleteRow(parseInt(rowNum));
	for(var r=parseInt(rowNum)+1;r<noOfRows;r++)
	{
		for(var i=0;i<6;i++)
		{
			var cell = document.getElementById((r+'')+i);
			if(i==0)
			{
				cell.setAttribute('id',(r-1)+'0');
				cell.value=(r-1)+'.';
			}
			else if(i==1)
			{
				cell.setAttribute('id',(r-1)+'1');
			}
			else if(i==2)
			{
				cell.setAttribute('id',(r-1)+'2');
			}
			else if(i==3)
			{
				cell.setAttribute('id',(r-1)+'3');
			}
			else if(i==4)
			{
				cell.setAttribute('id',(r-1)+'4');
			}
			else if(i==5)
			{
				cell.setAttribute('id',(r-1)+'5');
                cell.setAttribute('onclick','delRow('+(r-1)+')');
			}
		}
	}
}
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