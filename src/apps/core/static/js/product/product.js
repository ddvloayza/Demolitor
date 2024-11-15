// Objeto global para almacenar los filtros seleccionados
let selectedFilters = {
    categoryUuid: null,
    sortOrder: null,
    priceRange: null,
    objective: null,
};

// Función para actualizar los filtros y realizar el fetch
function updateFilters(type, value) {
    console.log(type, value);
    if (type === "categoryUuid") {
        selectedFilters.categoryUuid = value;
    } else if (type === "sortOrder") {
        selectedFilters.sortOrder = value;
    } else if (type === "priceRange") {
        selectedFilters.priceRange = value;
    } else if (type === "objective") {
        selectedFilters.objective = value;
    }

    // Realizar el fetch con los filtros acumulados
    fetchProducts(
        selectedFilters.categoryUuid,
        selectedFilters.sortOrder,
        selectedFilters.priceRange,
        selectedFilters.objective
    );
}


// Función para obtener el parámetro de la URL
function getUrlParameter(name) {
    const urlParams = new URLSearchParams(window.location.search);
    return urlParams.get(name);
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
    // Extraer valores de rango de precio
    const minPrice = priceRange ? parseFloat(priceRange.split('-')[0]) : null;
    const maxPrice = priceRange ? parseFloat(priceRange.split('-')[1]) : null;
    // Define las variables de la consulta
    const variables = {
        categoryUuid: categoryUuid,
        sortOrder: sortOrder,
        minPrice: minPrice,
        maxPrice: maxPrice,
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
// Funciones para aplicar filtros individuales
function applyObjectiveFilter(objective) {
    updateFilters("objective", objective);
}

function applyCategoryFilter(categoryUuid) {
    updateFilters("categoryUuid", categoryUuid);
}

function applyPriceFilter() {
    // Obtener los valores directamente desde los elementos de entrada
    const minPrice = parseFloat(document.getElementById('minRange').value);
    const maxPrice = parseFloat(document.getElementById('maxRange').value);
    console.log("minPrice", minPrice)
    console.log("maxPrice", maxPrice)
    if (minPrice >= maxPrice) {
        console.error("El rango mínimo no puede ser mayor o igual al máximo.");
        return;
    }

    // Llamar a la función para actualizar los filtros globales
    updateFilters('priceRange',minPrice+'-'+maxPrice);
}

function applySortOrderFilter(sortOrder) {
    updateFilters("sortOrder", sortOrder);
}

// Inicializar filtros desde parámetros de URL
const categoryUuid = getUrlParameter('category_uuid');
const objective = getUrlParameter('objective');
if (categoryUuid) {
    updateFilters("categoryUuid", categoryUuid);
} else if (objective) {
    updateFilters("objective", objective);
} else {
    fetchProducts();
}



// Ejecutar fetch inicial sin filtros
