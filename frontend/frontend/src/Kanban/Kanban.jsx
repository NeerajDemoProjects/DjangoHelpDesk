function Kanban(prop) {
    return (
<div className="col-3">
    <br></br>
<div className="list-group">
  
  <a  className="list-group-item list-group-item-action flex-column align-items-start">
    <div className="d-flex w-100 justify-content-between">
      <h5 className="mb-1">{prop.ticket.number}</h5>
      <small className="text-muted">{prop.ticket.created_at}</small>
    </div>
    <br></br>
    <small className="text-muted">name : {prop.ticket.contact_id.name}</small>
    <br></br>

    <small className="text-muted">Email: {prop.ticket.contact_id.email}</small>
    <br></br>

    <small className="text-muted">Phone: {prop.ticket.contact_id.phone}</small>
<br></br>
    <small className="text-muted">Query: {prop.ticket.query}</small>
  </a>
</div>
<br></br>
</div>

      );
}

export default Kanban;