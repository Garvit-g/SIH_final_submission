import './review.css'
import logo from './images/logo_trans.png'
const Navbar = () =>{
    return(
        <>
        <div className="nav">
            <img src={logo}/>
        </div>
        <div className="nav2">
            <h2>Latest Releases</h2>
        </div>
        </>
    )
}

export default Navbar