import logo from './logo.svg';
import './App.css';
import Main from './Kanban/Main';
import 'bootstrap/dist/css/bootstrap.css'
import MainEnquiry from './Enquiry/MainEnquiry';

function App() {
  return (
    <div className="App">
<MainEnquiry></MainEnquiry>

    <Main></Main>
    </div>
  );
}

export default App;
