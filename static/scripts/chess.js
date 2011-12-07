function dragStart(event) {
    event.dataTransfer.effectAllowed = 'move';
    event.dataTransfer.setData("Text", event.target.getAttribute('id'));
}

function dragOver(event) {
    return false;
}

function drop(event) {
    var coordinate = event.dataTransfer.getData("Text");
    var element = document.getElementById(coordinate);
    var targetClasses = event.target.getAttribute('class').split(' ');
    var elementClasses = element.getAttribute('class').split(' ');
    //You don't want to kill your own pieces
    if(targetClasses[0] != elementClasses[0]){
        event.target.innerHTML = element.innerHTML; // Move piece to new cell
        var newclass = elementClasses[0] + ' ' + targetClasses[1];
        event.target.setAttribute('class', newclass);
        element.innerHTML = ""; // Clear old cell
        element.setAttribute('class', 'none ' + elementClasses[1]); //Change the old cell's class names
    }
    event.preventDefault(); 
    return false;
}
function storeNotes(id) {
    var notes = document.getElementById('editable').innerHTML;
    localStorage.setItem('userScribble',notes);
}
function getNotes() {
    if ( localStorage.getItem('userScribble')) {
        var notes = localStorage.getItem('userScribble');
    }
    else {
        var notes = "<h3>Go ahead, edit me</h3><p>Write down your strategies so you won't forget and for next time you visit my blog!</p><p>Click \"clear local storage\" if you don't want your notes to be stored";
    }
    document.getElementById('editable').innerHTML = notes;
}

