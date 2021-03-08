deleteButtons = document.querySelectorAll('.delete-button')
for (let button of deleteButtons){
    button.addEventListener('click', event => {
    const artistElement = event.target.parentElement
    const deleteURL = `artists/${event.target.id}/delete`
    fetch (deleteURL, {
        headers: {
            'Accept': 'application/json',
            'X-Requested-With': 'XMLHttpRequest',
        },
    })
    .then(response => response.json())
    .then(data => {
        console.log(data)
        artistElement.remove()
        })
    })
}
