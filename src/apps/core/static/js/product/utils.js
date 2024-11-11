function parsePrice(priceText) {
    // Si contiene una coma y un punto (formato 1,000.00 o 1.000,00)
    if (priceText.includes(',') && priceText.includes('.')) {
        if (priceText.indexOf(',') > priceText.indexOf('.')) {
            // Asume que el punto es separador de miles y la coma es decimal
            priceText = priceText.replace(/\./g, '').replace(',', '.');
        } else {
            // Asume que la coma es separador de miles y el punto es decimal
            priceText = priceText.replace(/,/g, '');
        }
    } else if (priceText.includes(',')) {
        // Si solo contiene una coma, asume que es decimal
        priceText = priceText.replace(',', '.');
    }
    // Convierte a número flotante
    console.log("priceText",priceText);
    return parseFloat(priceText);
}