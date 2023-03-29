function ChatterView(props) {
  console.log(props)
    return (  <>
    <div class="list-group">
{props.ticket.message_ids.map((message)=>(

<a href="#" class="list-group-item list-group-item-action flex-column align-items-start">
  <div className="row">
    <div className="col-1"><strong> {message.name} </strong></div>
  </div>
  <br></br>
  
    <div className="row">
    <div>{message.message}</div>
  </div>
</a>

))}
  
 
</div>
    </>);
}

export default ChatterView;