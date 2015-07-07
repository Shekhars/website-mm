/**
 * Created by shesharma on 6/7/2015.
 */
function addRowsForm16(){
    var container = document.getElementById("nothing");
    container.innerHTML="";
    noForm = document.getElementById("noform16").value;
    document.getElementById('totalcost').innerHTML ='&#8377;'+ 300 +'/-'
    document.getElementById('cost').value = 300;
    for(i=0;i<document.getElementById("noform16").value;i++){
        var div1 = document.createElement("div");
        div1.setAttribute("class","form-group");

        var labelForm = document.createElement("label");
        labelForm.setAttribute("class","col-sm-5 control-label label-default");
        labelForm.textContent = "Select form-16";
        var form = document.createElement("input");
        form.type="file";
        form.name="form16_"+i;
        form.id="form16_"+i;
        form.style.paddingLeft='3%';


        var div2 = document.createElement("div");
        div2.setAttribute("class","form-group");
        div2.style="padding-bottom: 12%;";

        var labelPass = document.createElement("label");
        labelPass.setAttribute("class","col-sm-5 control-label label-default");
        labelPass.textContent = "Password for Form-16(if any)";

        var div3 = document.createElement("div");
        div3.setAttribute("class","col-sm-7");

        var textBox = document.createElement("input");
        textBox.type = "password";
        textBox.name = "password_"+i;
        textBox.id = "password_"+i;
        textBox.setAttribute("class","form-control");
        textBox.style.marginBottom='3%'

        div1.appendChild(labelForm);
        div1.appendChild(form);

        div3.appendChild(textBox);
        div2.appendChild(labelPass);
        div2.appendChild(div3);


        container.appendChild(div1);
        container.appendChild(div2);
        container.appendChild(document.createElement("br"));
        container.style="margin:2%;"
    }
}
/*
<div class="form-group"> div1
<label for="fileUploadForm16" class="col-sm-5 control-label label-default">Select form-16</label>
<input type="file" id="exampleInputFile" style="
padding-left: 3%;
">
</div>
<div class="form-group" style="padding-bottom: 12%;"> div 2
<label label-default="" class="col-sm-5 control-label label-default">Passwordr</label>
<div class="col-sm-7"> div 3
        <input type="text" class="form-control" id="bankAccount" placeholder="">
</div>
</div>
 */

/*
    <div class="form-group" style="padding-bottom: 12%;">
    <label label-default="" for="BankAccountNumber" class="col-sm-5 control-label label-default">Password?(optional)</label>
    <div class="col-sm-7">
    <input type="text" class="form-control" id="bankAccount" placeholder="">
    </div>
    </div>

    <div class="form-group" style="padding-bottom: 12%;">
                        <label label-default="" for="BankAccountNumber" class="col-sm-5 control-label label-default">Account Number</label>
                        <div class="col-sm-7">
                                <input type="text" class="form-control" id="bankAccount" placeholder="">
                        </div>
                    </div>
 */