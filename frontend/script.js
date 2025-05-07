const categorySelect = document.getElementById('category');
const itemSelect = document.getElementById('item');
const itemSearch = document.getElementById('itemSearch');

let fullItemList = [];

// Fetch categories on load
window.onload = async () => {
  const res = await fetch('http://localhost:5000/categories');
  const categories = await res.json();

  categories.forEach(cat => {
    const opt = document.createElement('option');
    opt.value = cat;
    opt.textContent = cat;
    categorySelect.appendChild(opt);
  });
};

// Fetch items when category changes
categorySelect.addEventListener('change', async () => {
  const category = categorySelect.value;
  const res = await fetch(`http://localhost:5000/items?category=${encodeURIComponent(category)}`);
  fullItemList = await res.json();
  renderItems(fullItemList);
  itemSearch.value = '';
});

// Filter items as user types
itemSearch.addEventListener('input', () => {
  const query = itemSearch.value.toLowerCase();
  const filtered = fullItemList.filter(item => item.toLowerCase().includes(query));
  renderItems(filtered);
});

// Render items into second dropdown
function renderItems(items) {
  itemSelect.innerHTML = '';
  items.forEach(item => {
    const opt = document.createElement('option');
    opt.value = item;
    opt.textContent = item;
    itemSelect.appendChild(opt);
  });
}
