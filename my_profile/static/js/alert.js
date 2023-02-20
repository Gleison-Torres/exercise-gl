function raiseAlert(){
    const forms = document.querySelectorAll('.delete-address');

    for( const form of forms) {
        form.addEventListener('submit', function (e) {
            e.preventDefault();
            const confirmed = confirm('Tem certeza que deseja excluir este endereço?');
            if(confirmed){
                form.submit();
            }
        })
    }
}



