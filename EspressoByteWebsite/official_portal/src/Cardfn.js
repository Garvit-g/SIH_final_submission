import { Grid } from "@mui/material";
import ClickToEdit from "react-click-to-edit";
const Bloglist = ({blogs, title, handleApprove}) => {
  return (
        <>
        {title.map((title)=>(
          <>
          <h3>{title.head}</h3>
          <div className="blog-list">
          {blogs.map((blog) => (
            <>
          
              <div className="blog-preview" key={blog.id}>
                  <textarea className="blog-body">{blog.body}</textarea>
                  <button className = 'btn' onClick={()=>handleApprove(blog.id)}>Approve</button>
                  {/* <button onClick={()=>handleDelete(blog.id)}>Delete</button> */}
              </div>
            </>
            
          ))}
          </div>
          </>
        ))}
        </>
  );
}

export default Bloglist;