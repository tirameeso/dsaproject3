const TESTData = [
    "Good Girl by Christina Herrerra with notes of: floral, musk",
    "Coco De Lait by Le Monde Gourmand with notes of: coconut, milk",
    "You by Glossier with notes of: iris, pepper"
];

const searchInput = document.getElementById("search-input");
const resultsList = document.getElementById("results-list");

function displayResults(query) {
    resultsList.innerHTML = "";

    const filteredData = TESTData.filter(item =>item.toLowerCase().includes(query.toLowerCase()));

    if (filteredData.length > 0) {
        filteredData.forEach(item => {
            const listItem = document.createElement("li");
            listItem.textContent = item;
            resultsList.appendChild(listItem);
        });
    } 

    else {
        const noResultItem = document.createElement("li");
        noResultItem.textContent = "No fragrances found";
        resultsList.appendChild(noResultItem);
    }
}

searchInput.addEventListener("input", (e) => {
    const query = e.target.value;
    displayResults(query);
});
