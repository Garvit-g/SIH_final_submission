import {React, useState} from 'react'
// import Search from './search'
import { Link } from 'react-router-dom'


function Auth() { 
    const [password, setPwd] = useState('');
    const [email, setEmail] = useState('');
    function handleSubmit(){
        if(password == ''||email == '')
         alert('Must enter email and password!')
        else
            window.location.href = './review'
    }
  return (
    <div className="Auth-form-container">
        <form className="Auth-form">
            <div className="Auth-form-content">
                <h3 className="Auth-form-title">
                    Sign In
                </h3>
                {/* <Search/> */}
                <label >Ministry</label>
                <select class="form-control" >
                <option selected="selected" value="0">All Ministry </option>
                    <option value="1">President&#39;s Secretariat</option>
                    <option value="2">Vice President&#39;s Secretariat</option>
                    <option value="3">Prime Minister&#39;s Office</option>
                    <option value="61">Cabinet</option>
                    <option value="62">Cabinet Committee Decisions</option>
                    <option value="63">Cabinet Committee on Economic Affairs (CCEA)</option>
                    <option value="68">Cabinet Secretariat</option>
                    <option value="70">Cabinet Committee on Infrastructure</option>
                    <option value="71">Cabinet Committee on Price</option>
                    <option value="75">Cabinet Committee on Investment</option>
                    <option value="80">AYUSH</option>
                    <option value="72">Other Cabinet Committees</option>
                    <option value="14">Department of Space</option>
                    <option value="45">Department of Ocean Development</option>
                    <option value="56">Department of Atomic Energy</option>
                    <option value="35">Election Commission</option>
                    <option value="1330">Finance Commission </option>
                    <option value="27">Ministry of Agriculture &amp;Farmers Welfare</option>
                    <option value="58">Ministry of Agro &amp; Rural Industries</option>
                    <option value="41">Ministry of Chemicals and Fertilizers</option>
                    <option value="26">Ministry of Civil Aviation</option>
                    <option value="42">Ministry of Coal</option>
                    <option value="16">Ministry of Commerce &amp; Industry</option>
                    <option value="24">Ministry of Communications</option>
                    <option value="60">Ministry of Company Affairs</option>
                    <option value="39">Ministry of Consumer Affairs, Food &amp; Public Distribution</option>
                    <option value="1440">Ministry of Cooperation</option>
                    <option value="66">Ministry of Corporate Affairs</option>
                    <option value="17">Ministry of Culture</option>
                    <option value="33">Ministry of Defence</option>
                    <option value="57">Ministry of Development of North-East Region</option>
                    <option value="48">Ministry of Disinvestment</option>
                    <option value="73">Ministry of Drinking Water &amp; Sanitation</option>
                    <option value="67">Ministry of Earth Science</option>
                    <option value="8">Ministry of Education</option>
                    <option value="1323">Ministry of Electronics &amp; IT</option>
                    <option value="30">Ministry of Environment, Forest and Climate Change</option>
                    <option value="4">Ministry of External Affairs</option>
                    <option value="15">Ministry of Finance</option>
                    <option value="1340">Ministry of Fisheries, Animal Husbandry &amp; Dairying</option>
                    <option value="40">Ministry of Food Processing Industries</option>
                    <option value="31">Ministry of Health and Family Welfare</option>
                    <option value="53">Ministry of Heavy Industries </option>
                    <option value="5">Ministry of Home Affairs</option>
                    <option value="47">Ministry of Housing &amp; Urban Affairs</option>
                    <option value="11">Ministry of Information &amp; Broadcasting</option>
                    <option value="1336">Ministry of Jal Shakti</option>
                    <option value="21">Ministry of Labour &amp; Employment</option>
                    <option value="7">Ministry of Law and Justice</option>
                    <option value="51">Ministry of Micro,Small &amp; Medium Enterprises</option>
                    <option value="44">Ministry of Mines </option>
                    <option value="65">Ministry of Minority Affairs</option>
                    <option value="28">Ministry of New and Renewable Energy </option>
                    <option value="59">Ministry of Overseas Indian Affairs</option>
                    <option value="10">Ministry of Panchayati Raj</option>
                    <option value="12">Ministry of Parliamentary Affairs</option>
                    <option value="6">Ministry of Personnel, Public Grievances &amp; Pensions</option>
                    <option value="20">Ministry of Petroleum &amp; Natural Gas</option>
                    <option value="79">Ministry of Planning</option>
                    <option value="52">Ministry of Power</option>
                    <option value="23">Ministry of Railways</option>
                    <option value="69">Ministry of Road Transport &amp; Highways</option>
                    <option value="43">Ministry of Rural Development</option>
                    <option value="13">Ministry of Science &amp; Technology</option>
                    <option value="46">Ministry of Ports, Shipping and Waterways</option>
                    <option value="77">Ministry of Skill Development and Entrepreneurship</option>
                    <option value="50">Ministry of Social Justice &amp; Empowerment</option>
                    <option value="55">Ministry of Statistics &amp; Programme Implementation</option>
                    <option value="18">Ministry of Steel</option>
                    <option value="25">Ministry of Surface Transport</option>
                    <option value="19">Ministry of Textiles</option>
                    <option value="36">Ministry of Tourism</option>
                    <option value="49">Ministry of Tribal Affairs</option>
                    <option value="32">Ministry of Urban Development</option>
                    <option value="38">Ministry of  Water Resources, River Development and Ganga Rejuvenation</option>
                    <option value="64">Ministry of Women and Child Development</option>
                    <option value="9">Ministry of Youth Affairs and Sports</option>
                    <option value="78">NITI Aayog</option>
                    <option value="1325">PM Speech</option>
                    <option value="74">EAC-PM</option>
                    <option value="34">UPSC</option>
                    <option value="37">Special Service and Features</option>
                    <option value="1005">PIB Headquarters</option>
                    <option value="1406">Office of Principal Scientific Advisor to GoI</option>
                    <option value="1454">National Financial Reporting Authority</option>
                    <option value="1458">Competition Commission of India</option>
                    <option value="1470">IFSC Authority</option>
                    <option value="1484">National Security Council Secretariat </option>
                </select>
                <div className="form-group mt-3">
                    <label >Email Address</label>
                    <input type="email" className="form-control mt-1" placeholder="Enter email"
                    onChange={e => setEmail(e.target.value)} />
                </div>
                <div className="form-group mt-3">
                <label >Password</label>
                    <input type="password" className="form-control mt-1" placeholder="Enter password" 
                    onChange={e => setPwd(e.target.value)}/>
                </div>
                <div className="d-grip gap-2 mt-3">
                   
                    <button className="btn btn-primary" type="button" onClick={handleSubmit}>
                      Submit
                    </button>
                    
                </div>
                <p className="forgot-password text-right mt-2">
                    Forgot <a href="#">Password?</a>
                </p>
            </div>
        </form>
    </div>
  )
}

export default Auth