function addFieldsForm(){
	var container = document.getElementById("nothing");
	var values = document.getElementById("myVar").value;
	for (i=0;i<values;i++){

                var div0 = document.createElement("div");
                div0.setAttribute("class","span well");

                // Append a node with a random text
				var div = document.createElement("div");
				div.setAttribute("class","form-group");


                var photo = document.createElement("input");
                photo.type = "file";
                photo.name = "photo" + i;
				photo.className="form-group col-md-7";

				
				var PhotoGraph = document.createElement("label");
				PhotoGraph.setAttribute("class","col-md-5 control-label label-default");
				PhotoGraph.textContent = "Photograph";

                div.appendChild(PhotoGraph);
                div.appendChild(photo);


                var div2 = document.createElement("div");
				div2.setAttribute("class","form-group");


				var PanCard = document.createElement("input");
				PanCard.type="file";
				PanCard.name = "pan"+ i;
				PanCard.className="form-group col-md-7";

				
				var PanCardUpload = document.createElement("label");
				PanCardUpload.setAttribute("class","col-md-5 control-label label-default");
				PanCardUpload.textContent = "Pan Card";

                div2.appendChild(PanCardUpload);
                div2.appendChild(PanCard);

                var div3 = document.createElement("div");
				div3.setAttribute("class","form-group");

				var APf = document.createElement("input");
				APf.type="file";
				APf.name="apf"+ i;
				APf.className = "form-group col-md-7";


				var apfUpload = document.createElement("label");
				apfUpload.setAttribute("class","col-md-5 control-label label-default");
				apfUpload.textContent = "Address proof";

                div3.appendChild(apfUpload);
                div3.appendChild(APf);

                var text = document.createElement("div");
                text.innerHTML = "Documents for Director "+(i+1);
                container.appendChild(text);
				div0.appendChild(div);
                div0.appendChild(document.createElement("br"));
				div0.appendChild(div2);
                div0.appendChild(document.createElement("br"));
				div0.appendChild(div3);
                div0.appendChild(document.createElement("br"));
                container.appendChild(div0)
            }
}