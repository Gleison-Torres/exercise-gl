document.getElementById('tabStandard').click();
function openTab(event, idTab) {
    var contents = document.getElementsByClassName('content');

    for (var i = 0; i < contents.length; i++) {
        contents[i].style.display = 'none';
    }

    var tabs = document.getElementsByClassName('tab-button');
    for (var i = 0; i < tabs.length; i++) {
        tabs[i].className = tabs[i].className.replace('active', '');
    }
    document.getElementById(idTab).style.display = 'block';
    event.currentTarget.className += ' active'
}