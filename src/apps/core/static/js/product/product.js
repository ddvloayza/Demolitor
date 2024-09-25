
function fetchProducts(categoryUuid = null) {
    const query = `
        query GetProductsByCategory{
            productQueries{
                productListByCategory(categoryUuid: ${categoryUuid}) {
                    uuid
                    name
                    price
                    slug
                    image
                    imageUrl
                    description
                    urlDetail
                }
            }
        }
    `;

    fetch('/api/v1/graph/demolitor', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
        },
        body: JSON.stringify({ query })
    })
    .then(response => response.json())
    .then(data => {
        console.log("data", data)
        const products = data.data.productQueries.productListByCategory;
        const productGrid = document.getElementById('product-grid');
        productGrid.innerHTML = ''; // Limpiar la cuadrícula de productos
        products.forEach(product => {
            const productCard = `
                <div class="bg-white py-6 px-8 rounded-lg shadow-md hover:shadow-2xl cursor-pointer">
                    <a href="${product.urlDetail}">
                        <div class="py-2 flex items-center text-[#5F2311] font-semibold text-sm justify-end">
                            <div class="w-4 h-4 bg-[#5F2311] rounded-full mr-2"></div>
                            <span>Chocolate</span>
                        </div>
                        <img src="${product.imageUrl}" alt="${product.name}" class="w-full h-auto mb-4">
                        
                        <h3 class="text-black text-center text-lg font-bold">${product.name}</h3>
                        <p class=" text-gray-600">S/${product.price}</p>
                        <button class="mt-4 bg-orange-600 text-white w-full py-3 rounded hover:bg-orange-700">
                            Añadir al carrito
                            <i class="fa fa-shopping-cart"></i>
                        </button>
                    </a>
                </div>`;
            productGrid.innerHTML += productCard;
        });
    });
}

// Fetch all products on page load
fetchProducts();
