function ChatterView(props) {
  console.log(props)
    return (  <>
    <div class="list-group">
{props.ticket.message_ids.map((message)=>(

<div class="list-group">
<div class="alert alert-primary" style={{'textAlign':'left'}} role="alert">
<h6>{message.name}</h6>
<small>{message.created_at}</small>
<hr></hr>
<p>{message.message}</p>
</div>


</div>
))}
  
 
</div>
    </>);
}

export default ChatterView;