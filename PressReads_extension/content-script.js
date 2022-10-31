//document.body.style.backgroundColor = 'orange';
/*async function getCurrentTab(){
    let queryOptions = {active: true, currentWindow: true}

    let [tab] = await chrome.tabs.query(queryOptions)
    return tab
}

getCurrentTab()
    .then((tab) => {console.log(tab.url)})
    .catch((error) => {console.log("error")})*/


/*chrome.runtime.onMessage.addListener(
    function(request, sender, sendResponse){
        console.log("got message")

        if(request.task === "getSelect"){
            //document.body.style.backgroundColor = 'orange';
            sendResponse({data: window.getSelection().toString()});
        }
        else
            sendResponse({})

    }
)


var selText = '';
if(document.getSelection){
    selText = document.getSelection().toString();
    console.log(selText)
}*/
console.log('yeet');