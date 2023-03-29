import axios from "axios";
import { useEffect, useState } from "react";
import Kanban from "./Kanban";

function Main() {
    const [ticket ,setTicket] = useState([])
    const baseURL = 'http://localhost:8000/api/get/ticket'
    useEffect(() => {
        axios.get(baseURL).then((response) => {
            setTicket(response.data);
        });
      }, []);
      console.log(ticket)
    return (
        
        <div className="row">
            {ticket.map((ticket)=>(

<Kanban ticket={ticket}></Kanban>



            ))}
      


        </div>
       );
}

export default Main;