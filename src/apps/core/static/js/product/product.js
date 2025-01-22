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
                    priceDiscount
                    slug
                    rating
                    keyFeatures{
                        name
                    }
                    skillTags{
                        name
                        color
                    }
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
        if (data.data && data.data.productQueries && data.data.productQueries.productListByCategory.length > 0) {
            const products = data.data.productQueries.productListByCategory;
            const productGrid = document.getElementById('product-grid');
            productGrid.innerHTML = ''; // Limpiar la cuadrícula de productos

            products.forEach(product => {
                // Convert rating to stars (full ★, half ★, and empty ☆)
                const fullStars = Math.floor(product.rating); // Cantidad de estrellas llenas
                const halfStar = product.rating % 1 >= 0.5; // Verdadero si hay media estrella
                const emptyStars = 5 - fullStars - (halfStar ? 1 : 0); // Restantes son estrellas vacías

                // Generar HTML para las estrellas
                let starsHtml = '';
                for (let i = 0; i < fullStars; i++) {
                    starsHtml += '<span class="text-yellow-500 text-3xl">★</span>'; // Estrella llena
                }
                if (halfStar) {
                    starsHtml += '<span class="text-yellow-500 text-3xl">★</span>'; // Media estrella (puedes usar un icono diferente si prefieres)
                }
                for (let i = 0; i < emptyStars; i++) {
                    starsHtml += '<span class="text-gray-400 text-3xl">★</span>'; // Estrella vacía
                }
                // Generar etiquetas dinámicas para skillTags
                let skillTagsHtml = '';
                if (product.skillTags && product.skillTags.length > 0) {
                    skillTagsHtml = product.skillTags.map(tag => `
                        <div class="text-center text-white text-xs font-bold px-2 py-1 rounded-lg w-full"
                             style="background-color: ${tag.color}">
                            ${tag.name}
                        </div>
                    `).join('');
                }
                // Generar atributos dinámicamente
                let attributesHtml = '';
                if (product.keyFeatures && product.keyFeatures.length > 0) {
                    attributesHtml = product.keyFeatures.map(feature => `
                        <span class="bg-gray-100 text-gray-600 text-base font-bold px-4 py-2 rounded-full">
                            ${feature.name}
                        </span>
                    `).join('');
                }
                let priceHtml = '';
                if (product.price_discount && Int(product.price_discount) > 0) {
                    // If there is a discount, show the discounted price and original price (strikethrough)
                    priceHtml = `
                      <span class="text-2xl text-gray-500 header_text font-black line-through price">
                        S/ ${product.price}
                      </span>
                      <span class="text-4xl text-gray-800 header_text font-black price" id="product-price">
                        S/ ${product.price_discount}
                      </span>
                    `;
                  } else {
                    // If price_discount is 0, show only the regular price
                    priceHtml = `
                      <p class="text-gray-600 text-base md:text-2xl">
                        S/ ${product.price}
                      </p>
                    `;
                  }
                const productCard = `
                    <div class="bg-white p-4  rounded-lg shadow-md hover:shadow-2xl cursor-pointer">
                        <div class="grid grid-cols-1 md:grid-cols-2 gap-2 my-2">
                            ${skillTagsHtml}
                        </div>
                        
                        <a href="${product.urlDetail}">
                            <img src="${product.imageUrl}" alt="${product.name}" class="w-full h-auto mb-4">
                            <h3 class="text-black text-center text-xs md:text-lg font-bold overflow-hidden h-16" style="display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical;">${product.name}</h3>
                            <div class="flex items-center space-x-1 my-2">
                              <span class="text-yellow-500 text-lg">
                                ${starsHtml}
                              </span>
                            </div>
                            
                            <!-- Product Attributes -->
                            <div class="flex flex-wrap sm:flex-row flex-col justify-center items-center gap-2 my-2">
                              ${attributesHtml}
                            </div>
                            ${priceHtml}
                            <button class="mt-4 bg-[#DE3704] text-white w-full py-3 rounded hover:bg-orange-700">
                                Ver más
                            </button>
                        </a>
                    </div>`;
                productGrid.innerHTML += productCard;
            });
        } else {
            const productGrid = document.getElementById('product-grid');
            productGrid.innerHTML = ''; // Limpiar la cuadrícula de productos
            const notFoundProduct = `
                    <div class="bg-white py-6 px-8 rounded-lg shadow-md hover:shadow-2xl cursor-pointer">
                        NO SE ENCONTRARON PRODUCTOS
                    </div>`;
                productGrid.innerHTML += notFoundProduct;
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
