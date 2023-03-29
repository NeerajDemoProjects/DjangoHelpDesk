import axios from "axios";
import { useEffect, useState } from "react";
import Chatter from "../Enquiry/Chatter";
import ChatterView from "./ChatterView";

function EnquiryFormView() {
    const [ticket,setTicket]=useState([])
    const  baseURL ='http://localhost:8000/api/get/client/ticket?id=3'

    useEffect(() => {
        axios.get(baseURL).then((response) => {
            setTicket(response.data);
        });
      }, []);

    return (<>
    {ticket.map((ticket)=>(


<div className="container">
<div class="list-group">

<a href="#" class="list-group-item list-group-item-action flex-column align-items-start">
<div class="d-flex w-100 justify-content-between">
<h5 class="mb-1">{ticket.number}</h5>
<small class="text-muted">{ticket.created_at}</small>
<button type="button" class="btn btn-info">Info</button>

</div>
<p class="mb-1">{ticket.contact_id.name}</p>
<small class="text-muted">Phone : {ticket.contact_id.phone}</small><br></br>
<small class="text-muted">Email : {ticket.contact_id.email}</small><br></br>

<small class="text-muted">Query : {ticket.contact_id.query}</small><br></br>

</a>



<ChatterView ticket={ticket}></ChatterView>








</div>

<Chatter ticket={ticket}></Chatter>



</div>


    ))}
   
    <br></br>
    </>  );
}

export default EnquiryFormView;