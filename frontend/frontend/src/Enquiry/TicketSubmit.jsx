import axios from "axios";
import { useState } from "react";

function TicketSubmit() {
    const url ='http://localhost:8000/api/create/ticket'
    const [name ,setName]=useState('')
    const [email ,setEmail]=useState('')
    const [phone ,setPhone]=useState('')
    const [query ,setQuery]=useState('')

    const handleSubmit = ()=>{
    console.log(

        {
            'name':name,
            'email':email,
            'phone':phone,
            'query':query
        }
    )
    axios.post(url,{
        'name':name,
        'email':email,
        'phone':phone,
        'query':query
    }).then((resp)=>{

        console.log(">>>>>>>>>>>>>>>>>>",resp)
    })
    alert("dfdg")
    }

    return ( <div className="container">
      
<br></br>

<div class="list-group">
 
  <a  class="list-group-item list-group-item-action flex-column ">
    <h1>Customer Enquiry</h1>
  <br></br>
  <br></br>

  <form onSubmit={(e)=>handleSubmit()}>

    
  <div class="form-group">
    <div className="row">
    <div className="col-1">Name</div>
    <div className="col"><input type="text" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Enter Name"
    
    onChange={(e)=>setName(e.target.value)}
    required/>
</div>
</div>
<br></br>

<div className="row">
    <div className="col-1">Email</div>
    <div className="col"><input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Enter Email"
    
    onChange={(e)=>setEmail(e.target.value)}

    
    required/>
</div>
</div>
<br></br>
<div className="row">
    <div className="col-1">Phone</div>
    <div className="col"><input type="text"     onChange={(e)=>setPhone(e.target.value)}
 class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Enter Phone" required/>
</div>
</div>
<br></br>

<div className="row">
    <div className="col-1">Query</div>
    <div className="col"><textarea 
        onChange={(e)=>setQuery(e.target.value)}

    class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Enter Query" required/>
</div>
</div>



   <br></br>
 
   <button type="submit" class="btn btn-primary" >Submit</button>

  </div>
  
</form>
  </a>
</div>







    
    </div> );
}

export default TicketSubmit;