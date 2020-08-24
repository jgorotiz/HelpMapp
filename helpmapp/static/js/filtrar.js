function capturar(){
    $.ajax({
        url : "/static/data/provincias.json",// the endpoint
        contentType: "application/json; charset=utf-8",
        type:"get",

        // handle a successful response
        success : function(json) {
            
            console.log(json); // log the returned json to the console
            console.log("success"); // another sanity check
            let opcion = $('<option></option>');
            opcion.attr("value", "")
            opcion.text("Provincia");
            $("#province").append(opcion)
            $.each(json["rows"], function(key,val) {
                let nombre = val["nombre"];
                let opcion = $('<option></option>');
                opcion.attr("value", val["id_provincia"])
                opcion.text(nombre);
                 $("#province").append(opcion);
            });
       }
    });

    // $.getJSON("provicias.json", function(data) {
    	// let opcion = $('<option></option>');
     //    opcion.attr("value", "")
     //    opcion.text("Provincia");
     //    $("#province").append(opcion)
     //    alert("entrooo");
     //    $.each(data["rows"], function(key,val) {
     //        let nombre = val["nombre"];
     //        let opcion = $('<option></option>');
     //        opcion.attr("value", val["id_provincia"])
     //        opcion.text(nombre);
     //         $("#province").append(opcion);

    //     });
    // });
    
}

function cargarCiudades(){
	$('#province').click(function(){
        var valor = $("#province").val();
        $("#city").empty();
        $.getJSON("/static/data/ciudades.json", function(data) {
            console.log(data);
        	if(valor != ""){
	        	let opcion = $('<option></option>');
		        opcion.attr("value", "")
		        opcion.text("Ciudad");
		        $("#city").append(opcion);
		        $.each(data["rows"], function(key,val) {
		        	if (valor == val["id_provincia"]){
			            let nombre = val["nombre"];
			            let opcion = $('<option></option>');
			            opcion.attr("value", val["nombre"])
			            opcion.attr("id","ciudad");
			            opcion.text(nombre);
			            $("#city").append(opcion);
		         	}
		        });
		    }
	    });
    });
}


function centrarMapa(){
    $('#city').click(function(){
        var valor = $("#city").val();
        $("#coordenadas").empty();
        $.getJSON("/static/data/coordenadas_ciudades.json", function(data) {
            if(valor != ""){
                $.each(data["rows"], function(key,val) {
                    if (valor == val["id_ciudad"]){
                        let lat = $('<input></input>');
                        let long = $('<input></input>');
                        lat.attr("id", "lat");
                        long.attr("id", "long");
                        lat.attr("type", "hidden");
                        long.attr("type", "hidden");
                        lat.attr("value", "lat");
                        long.attr("value", "long");
                        $("#coordenadas").append(lat);
                        $("#coordenadas").append(long);

                    }
                });
                let button = $('<input></input>');
                button.attr("type", "submit");
                button.attr("id", "hola");
                button.attr("value", "Centrar Mapa");
                $("#coordenadas").append(button);
            }
        });
    });
}




function cargarCentros(){
    $('#btn-submit').click(function(){
        var valor = $("#city").val();
        $("#tabla-upc").empty();
        $.getJSON("../data/centros-acopio.json", function(data) {
            if(valor != ""){
                $.each(data["rows"], function(key,val) {
                    if (valor == val["ciudad"]){
                        let tr = $('<tr></tr>');
                        let td_id = $('<td></td>');
                        let td_nombre = $('<td></td>');
                        let td_ciudad = $('<td></td>');

                        let link = './verCentro.html';

                        let nombre = val["nombre"];
                        let  id = val["id_centro"];
                        let ciudad = valor;

                        td_id.text(id);
                        td_nombre.text(nombre);
                        td_ciudad.text(ciudad);
                        let td_link = $('<td><a href=\"' + link + '\">Ver centro</a></td>');
                        tr.append(td_id);
                        tr.append(td_nombre);
                        tr.append(td_ciudad);
                        tr.append(td_link);

                        $("#tabla-upc").append(tr);
                    }
                });
            }
        });
    });
}

$(window).load(function() {
 	capturar();
 	cargarCiudades();
    centrarMapa();
});