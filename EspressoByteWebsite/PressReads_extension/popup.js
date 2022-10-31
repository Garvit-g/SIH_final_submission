
    let result;
    document.getElementById('btn').onclick = async () => {
        const [tab] = await chrome.tabs.query({active: true, currentWindow: true});
       
        try {
          [{result}] = await chrome.scripting.executeScript({
            target: {tabId: tab.id},
            function: () => getSelection().toString(),
          });
        } catch (e) {
          return; 
        }
       
        const data = {
          "text" : result
      }
      const options = {
          method: 'POST',
          headers:{
              'Access-Control-Allow-Origin': '*',
              'Content-Type': 'application/json'
          },
          body: JSON.stringify(data)
      }
      
      var summText
      fetch('http://127.0.0.1:5000/get_pegasus/', options)
      .then((response) => {
          response.json().then(function(json){
            var pc = JSON.stringify(json.pegasus_summary); 
           summText = pc.slice(1, pc.length-1) 
          console.log(pc)
            var transTo = document.getElementById('lang').value
            console.log(transTo)
            fetch("https://translate-pressread.herokuapp.com/get_translation/", {
              method: "POST",
              body: JSON.stringify({
                  text: summText,
                  src: "en",
                  dest: transTo,
              }),
              headers: { "Content-Type": "application/json" }
          }).then((res)=>{
              res.json().then(data =>{ 
                var dd =  JSON.stringify(data.translation)
                var dslice = dd.slice(3, dd.length-3)
                document.getElementById('para').innerHTML = dslice })
          })
          })
      })
      .catch((error) => console.log(error))      
      };
      
        