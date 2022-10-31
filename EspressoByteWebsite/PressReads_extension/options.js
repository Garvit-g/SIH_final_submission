function saveOptions(){
    var lang = document.getElementById('lang').value;
    chrome.storage.sync.set({
        transTo: lang
    }, function(){
        var stat = document.getElementById('status')
        stat.textContent = 'Saved'
        setTimeout(()=>{stat.textContent = ''}, 500)
    })
}

function restoreOptions(){
    chrome.storage.sync.get({
        transTo: 'en'
    }, function(){
        document.getElementById('lang').value = 'en'
    })
}

document.addEventListener('DOMContentLoaded', restoreOptions);
document.getElementById('save').addEventListener('click',
    saveOptions);