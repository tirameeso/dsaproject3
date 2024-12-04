// Sample data (replace with API or backend integration when done!)
const sampleData = [
    "Floral Bliss - Notes: floral, citrus",
    "Woody Wonder - Notes: woody, spicy",
    "Citrus Spark - Notes: citrus, fresh",
    "Ocean Breeze - Notes: marine, fresh",
    "Vanilla Dream - Notes: vanilla, musk",
    "Amber Glow - Notes: amber, warm spicy",
    "Patchouli Essence - Notes: patchouli, earthy",
    "Rose Garden - Notes: floral, rose",
];

// Elements
const searchInput = document.getElementById("search-input");
const resultsList = document.getElementById("results-list");

// Function to filter and display results
function displayResults(query) {
    // Clear current results
    resultsList.innerHTML = "";

    // Filter data
    const filteredData = sampleData.filter(item =>
        item.toLowerCase().includes(query.toLowerCase())
    );

    // Display results
    if (filteredData.length > 0) {
        filteredData.forEach(item => {
            const listItem = document.createElement("li");
            listItem.textContent = item;
            resultsList.appendChild(listItem);
        });
    } else {
        const noResultItem = document.createElement("li");
        noResultItem.textContent = "No results found.";
        resultsList.appendChild(noResultItem);
    }
}
// Event Listener for Search Input
searchInput.addEventListener("input", (e) => {
    const query = e.target.value;
    displayResults(query);
});
