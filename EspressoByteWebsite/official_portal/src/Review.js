import Bloglist from "./Cardfn";
import { useState } from 'react';
import Navbar from "./navbar"
import "./review.css";
const Review = () => {
  const[title, setTitle] = useState([
    {head:'NO CHANGE OF GUARD CEREMONY ON AUGUST 27', group:1},
    {head: 'PM addresses Grand Finale of Smart India Hackathon 2022', group:2},
])
  const[blogs, setBlogs]=useState([
      {head:'NO CHANGE OF GUARD CEREMONY ON AUGUST 27',body: 'COVID-19 vaccination for the age group 12-14 years was started on 16 March, 2022. So far, more than 3.99 Cr (3,99,63,095) adolescents have been administered with the first dose of COVID-19 vaccine.Similarly, the COVID-19 precaution dose administration for age group 18-59 years also started from 10th April, 2022 onwards.', group:1, id: 1 },
      {head:'NO CHANGE OF GUARD CEREMONY ON AUGUST 27',body: 'The Union Government is committed to accelerating the pace and expanding the scope of COVID-19 vaccination throughout the country. The nationwide COVID 19 vaccination started on 16th January 2021. The new phase of universalization of COVID-19 vaccination commenced from 21st June 2021. The vaccination drive has been', group:1, id: 2 },
      {head:'NO CHANGE OF GUARD CEREMONY ON AUGUST 27',body: 'As part of the nationwide vaccination drive, Government of India has been supporting the States and UTs by providing them COVID Vaccines free of cost. In the new phase of the universalization of the COVID19 vaccination drive, the Union Government will procure and supply (free of cost) 75% of the vaccines being produced by the vaccine manufacturers in the country to States and UTs.', group:1, id: 3 },
      {head: 'PM addresses Grand Finale of Smart India Hackathon 2022',body: 'Random 1.', group:2, id: 4 },
      {head: 'PM addresses Grand Finale of Smart India Hackathon 2022',body: 'Random 2', group:2, id: 5},
      {head: 'PM addresses Grand Finale of Smart India Hackathon 2022',body: 'Random 3', group: 2, id: 6}
  ]);
  const handleDelete=(id)=>{
    var newBlogs = []
     newBlogs = blogs.filter(blog => blog.id !== id);
     setBlogs(newBlogs); 
  }

 
  return (
    <>
    <Navbar/>
    <div className="home" >
        <Bloglist blogs={blogs} title={title} handleDelete={handleDelete}/>
    </div>
    </>
  );
}
 
export default Review;