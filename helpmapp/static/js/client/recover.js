
$( "#campo" ).on("keypress",function(){
	let value=$.trim($("#id_correo").val());
	if(value.length>0){
		$("#enviar").removeAttr("disabled"); 
  	}});
