document.querySelector('#add_item').addEventListener('click', function() {
    var listItem = document.createElement('li');
    listItem.textContent = 'Item';
    document.querySelector('.my_list').appendChild(listItem);
});
