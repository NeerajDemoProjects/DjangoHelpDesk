import SentimentSatisfiedAltIcon from '@mui/icons-material/SentimentSatisfiedAlt';
import SentimentVeryDissatisfiedIcon from '@mui/icons-material/SentimentVeryDissatisfied';
import axios from 'axios';
import { useEffect, useState } from 'react';
function CustomerRating() {
const URL ='http://localhost:8000/api/get/rating/ticket'
const [is_not_expired,setIsnotExpired]= useState([false])



const baseURL = 'http://localhost:8000/api/get/rating/ticket?id=3'
    useEffect(() => {
        axios.get(baseURL).then((response) => {
            setIsnotExpired(response.data);
        });
      }, []);

      console.log(is_not_expired)
const handlesatisfy = ()=>{
    alert("handlesatisfy")
    axios.put(URL,{'id':3,'rating':'satisfied'})

}

const handleunsatisfy = ()=>{
    alert("handleunsatisfy")

    axios.put(URL,{'id':3,'rating':'unsatisfied'})

}

return (<>


{is_not_expired? <div className="container">
    <div class="card" >
  <div class="card-body">
    <h5 class="card-title">Card title</h5>
  </div>
</div>
    <div class="card">
  <div className="card-body" style={{'text-align':"left","padding":"1%"}}>
  <p>Dear valued customer,</p>
    <p>We value your feedback and always strive to provide you with the best possible service. We understand that sometimes you may encounter issues while using our helpdesk, and we want to ensure that we address any concerns you may have.</p>
    <p>To assist us in improving our services, we kindly request that you take a moment to rate your experience with our helpdesk. Your honest feedback is extremely valuable to us and will help us to identify areas for improvement and enhance the overall customer experience.</p>  </div>

<div className="row">
    <div className="col">
        
    <button type="button" class="btn btn-light" onClick={()=>handlesatisfy()}> <SentimentSatisfiedAltIcon  style={{"fontSize":"100px"}}></SentimentSatisfiedAltIcon></button>

        
       </div>
    <div className="col">
    <button type="button" class="btn btn-light" onClick={()=>handleunsatisfy()}>
        <SentimentVeryDissatisfiedIcon   style={{"fontSize":"100px"}}></SentimentVeryDissatisfiedIcon>
        </button>
        </div>
</div>
</div>
    </div>:<div>
        The Link Expired
        </div>}










   













    </>

        
    
        
   
);
}

export default CustomerRating;