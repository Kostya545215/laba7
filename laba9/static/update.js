function updateProd(el) {
    part_id = el.value
    fetch('/used/' + part_id, {
        method: 'patch',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({'used': el.checked})
    })
    console.log(part_id)
}

function addPart() {
    let prodName = document.getElementById('part_name').value
    let price = document.getElementById('price').value
    fetch('/add', {
        method: 'post',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({'part_name': prodName,
                             'price': price,
                             'used': true})
    })
//    console.log("Add")
}