async function CarregarProdutos() {

    try{
        const res = await fetch('/api/produtos/');
        const produtos = await res.json();


        const container = document.getElementById("produtos");
        container.innerHTML = '';
        produtos.forEach(p =>{
            container.innerHTML += `
            <div class="produto-card">
            <h3>${p.nome}</h3>
            <p>R$ ${p.preco}</p>
            <a href="${p.link_afiliado}" target="_blank"> Compar </a>
            </div>
            `;
        });
    }catch (error){
        console.log("Erro ao carregar produtos: ", error);
    }
}

CarregarProdutos();