function addFieldsForm(){
	var container = document.getElementById("nothing");
	var values = document.getElementById("myVar").value;
	for (i=0;i<values;i++){
                // Append a node with a random text
				var div = document.createElement("div");
				div.setAttribute("class","form-group");
                div.style = "padding-bottom: 6%;";


                var photo = document.createElement("input");
                photo.type = "file";
                photo.name = "photo" + i;
				photo.className="form-group";
                photo.style="padding-left:3%;";
				
				var PhotoGraph = document.createElement("label");
				PhotoGraph.setAttribute("class","col-sm-5 control-label label-default");
				PhotoGraph.textContent = "Select Photograph of Partner - "+ (i+1);

                div.appendChild(PhotoGraph);
                div.appendChild(photo);


                var div2 = document.createElement("div");
				div2.setAttribute("class","form-group");
                div2.style = "padding-bottom: 6%;";

				var PanCard = document.createElement("input");
				PanCard.type="file";
				PanCard.name = "pan"+ i;
				PanCard.className="form-group";
                PanCard.style="padding-left:3%;";
				
				var PanCardUpload = document.createElement("label");
				PanCardUpload.setAttribute("class","col-sm-5 control-label label-default");
				PanCardUpload.textContent = "Select Pan Card of Partner - "+ (i+1);

                div2.appendChild(PanCardUpload);
                div2.appendChild(PanCard);

                var div3 = document.createElement("div");
				div3.setAttribute("class","form-group");
                div3.style = "padding-bottom: 6%;";

				var APf = document.createElement("input");
				APf.type="file";
				APf.name="apf"+ i;
				APf.className = "form-group";
                APf.style="padding-left:3%;";
				
				var apfUpload = document.createElement("label");
				apfUpload.setAttribute("class","col-sm-5 control-label label-default");
				apfUpload.textContent = "Select Address proof of Partner - "+ (i+1);

                div3.appendChild(apfUpload);
                div3.appendChild(APf);

				container.appendChild(div);
                container.appendChild(document.createElement("br"));
				container.appendChild(div2);
                container.appendChild(document.createElement("br"));
				container.appendChild(div3);
                container.appendChild(document.createElement("br"));
            }
}