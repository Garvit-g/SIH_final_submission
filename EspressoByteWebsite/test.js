
const options = {
    method: 'GET',
    headers:{
        'accept': 'application/json'
    }
}
var links=[];
var heading=[];
var articles=[];
fetch('https://sih-hackathon-api.herokuapp.com/get_latest_articles/', options)
.then((response) => {
    response.json().then(function(json){
        links=json.links_of_articles;
        heading=json.titles_of_articles;
        articles=json.full_text;

        // for(var i=0;i<links.length;i++)
        // {
        //     fetch("https://sih-hackathon-api.herokuapp.com/article_from_url/", {
        //       method: "POST",
        //       body: JSON.stringify({
        //             "url": links[i]
        //       }),
        //       headers: { "Accept": "application/json", 
        //        "Content-Type": "application/json" 
        //     }
        //   }).then((res)=>{
        //       res.json().then(data =>{ 
        //       articles =  data.entire_text})
        //     })
        // }
        console.log(articles);
        console.log(heading);
        console.log(links);
    })
        })
      .catch((error) => console.log(error))
