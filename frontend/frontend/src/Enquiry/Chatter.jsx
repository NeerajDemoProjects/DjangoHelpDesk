import axios from "axios";
import { useState } from "react";

function Chatter(props) {
    const [message,setMessage]=useState()

    const handlemessage = ()=>{
     
        axios.put('http://localhost:8000/api/create/ticket',{
            'id': props.ticket.id,
            'message':message
        


        })
        window.location.reload();

    }
    return (  <>
    <br></br>
    <form onSubmit={(e)=>handlemessage()}>
    <div className="container">
    <div class="list-group">


<a href="#" class="list-group-item list-group-item-action flex-column align-items-start">
<div className="col"><input type="text" onChange={(e)=>{setMessage(e.target.value)}} class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Enter Message"/></div>
<button type="submit" class="btn btn-info">Send</button>


</a>
</div>

    </div>
    </form>
    
   
    
    </>);
}

export default Chatter;