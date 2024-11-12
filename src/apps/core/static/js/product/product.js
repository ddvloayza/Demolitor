// Función para obtener el parámetro de la URL
function getUrlParameter(name) {
    const urlParams = new URLSearchParams(window.location.search);
    return urlParams.get(name);
}

// Verificar si el parámetro "category_uuid" está presente
const categoryUuid = getUrlParameter('category_uuid');
const objective = getUrlParameter('objective');
console.log("categoryUuid", categoryUuid);
if (categoryUuid) {
    console.log("categoryUuid", categoryUuid)
    fetchProducts(categoryUuid);
}
else if (objective) {
    console.log("objective", objective)
    fetchProducts(null,null,null, objective);
}
else {
    console.log("no objective");
    fetchProducts();
}


function fetchProducts(categoryUuid = null, sortOrder = null, priceRange = null, objective = null) {
    // Construir la consulta GraphQL con variables
    const query = `
        query GetProductsByCategory($categoryUuid: String, $sortOrder: String, $minPrice: Float, $maxPrice: Float, $objective: ObjectiveChoices) {
            productQueries {
                productListByCategory(categoryUuid: $categoryUuid, sortBy: $sortOrder, minPrice: $minPrice, maxPrice: $maxPrice, objective: $objective) {
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

    // Define las variables de la consulta
    const variables = {
        categoryUuid: categoryUuid,
        sortOrder: sortOrder,
        minPrice: priceRange ? parseFloat(priceRange.split('-')[0]) : null,
        maxPrice: priceRange ? parseFloat(priceRange.split('-')[1]) : null,
        objective: objective,
    };

    // Realiza la consulta a la API
    fetch('/api/v1/graph/demolitor', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
        },
        body: JSON.stringify({ query, variables })
    })
    .then(response => response.json())
    .then(data => {
        console.log("API response:", data);  // Verifica la estructura completa de la respuesta
        if (data.data && data.data.productQueries) {
            const products = data.data.productQueries.productListByCategory;
            const productGrid = document.getElementById('product-grid');
            productGrid.innerHTML = ''; // Limpiar la cuadrícula de productos

            products.forEach(product => {
                const productCard = `
                    <div class="bg-white py-6 px-8 rounded-lg shadow-md hover:shadow-2xl cursor-pointer">
                        <a href="${product.urlDetail}">
                            <img src="${product.imageUrl}" alt="${product.name}" class="w-full h-auto mb-4">
                            <h3 class="text-black text-center text-lg font-bold">${product.name}</h3>
                            <p class="text-gray-600 text-2xl ">S/${product.price}</p>

                            <button class="mt-4 bg-[#DE3704] text-white w-full py-3 rounded hover:bg-orange-700">
                                Ver más
                            </button>
                        </a>
                    </div>`;
                productGrid.innerHTML += productCard;
            });
        } else {
            console.error("No se encontró la propiedad 'productQueries' en la respuesta de la API.");
        }
    });
}
function applyObjectiveFilter(objective) {
    console.log(objective);
    fetchProducts(null, null, null, objective);
}



// Ejecutar fetch inicial sin filtros
