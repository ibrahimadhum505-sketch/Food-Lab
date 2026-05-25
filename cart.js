// cart.js

const CART_KEY = 'food_lab_cart';

// Retrieve cart from local storage
function getCart() {
    const cartStr = localStorage.getItem(CART_KEY);
    if (cartStr) {
        try {
            return JSON.parse(cartStr);
        } catch (e) {
            console.error("Error parsing cart data", e);
            return [];
        }
    }
    return [];
}

// Save cart to local storage
function saveCart(cart) {
    localStorage.setItem(CART_KEY, JSON.stringify(cart));
}

// Add item to cart
function addToCart(product) {
    const cart = getCart();
    const existingIndex = cart.findIndex(item => item.name === product.name);

    if (existingIndex > -1) {
        cart[existingIndex].qty += product.qty;
    } else {
        cart.push(product);
    }

    saveCart(cart);
    updateCartBadge();
    triggerPlusAnim();
}

// Update quantity of an item
function updateItemQuantity(name, change) {
    const cart = getCart();
    const itemIndex = cart.findIndex(item => item.name === name);

    if (itemIndex > -1) {
        cart[itemIndex].qty += change;
        if (cart[itemIndex].qty <= 0) {
            cart.splice(itemIndex, 1); // remove if qty 0
        }
        saveCart(cart);
        updateCartBadge();
        if (typeof renderCartPage === 'function') {
            renderCartPage();
        }
    }
}

// Calculate totals
function getCartTotals() {
    const cart = getCart();
    let totalItems = 0;
    let subTotal = 0;

    cart.forEach(item => {
        totalItems += item.qty;
        subTotal += (item.price * item.qty);
    });

    return { totalItems, subTotal };
}

// Update badge in header
function updateCartBadge() {
    const { totalItems } = getCartTotals();
    const badges = document.querySelectorAll('.cart-badge');

    badges.forEach(badge => {
        if (totalItems > 0) {
            badge.innerText = totalItems;
            badge.style.display = 'flex';
        } else {
            badge.style.display = 'none';
        }
    });
}

// Plus icon animation trigger
function triggerPlusAnim() {
    const el = document.querySelector('.cart-plus-anim');
    if (!el) return;
    el.classList.remove('play');
    void el.offsetWidth;
    el.classList.add('play');
}

// Run on page load
document.addEventListener('DOMContentLoaded', () => {
    updateCartBadge();

    // === BUY NOW BUTTON HANDLER (works on all product pages) ===
    const buyNowBtn = document.getElementById('buyNowBtn');
    if (buyNowBtn) {
        buyNowBtn.addEventListener('click', () => {
            const qtyInput = document.getElementById('qtyVal');
            const qty = qtyInput ? parseInt(qtyInput.value) : 1;

            const nameEl = document.querySelector('.product-name');
            const name = nameEl ? nameEl.innerText.trim() : 'Product';

            const priceEl = document.querySelector('.product-price');
            let price = 0;
            if (priceEl) price = parseInt(priceEl.innerText.replace(/[^0-9]/g, ''));

            const imgEl = document.querySelector('.card-crop');
            let image = 'https://i.imgur.com/BSt2lzH.png';
            if (imgEl && window.getComputedStyle(imgEl).backgroundImage !== 'none') {
                image = window.getComputedStyle(imgEl).backgroundImage.slice(4, -1).replace(/"/g, '');
            }

            addToCart({ name, price, qty, image });
            window.location.href = 'checkout.html';
        });
    }

    // === SEARCH AND LOGIN MODALS INITIALIZATION ===
    const ALL_PRODUCTS = [
        // Sweets & Desserts
        { name: "Chanar Murki", url: "Chanar-Murki.html", category: "Sweets & Desserts" },
        { name: "Shornomukhi", url: "Shornomukhi.html", category: "Sweets & Desserts" },
        { name: "Pera Sandesh", url: "Pera-Sandesh.html", category: "Sweets & Desserts" },
        { name: "Dudhmon", url: "Dudhmon.html", category: "Sweets & Desserts" },
        { name: "Lalmon", url: "Lalmon.html", category: "Sweets & Desserts" },

        // Bakery Delights
        { name: "Special Jhal Chanachur 250gm", url: "Special-Jhal-Chanachur.html", category: "Bakery Delights" },
        { name: "Premium Toast  ( 500 gm )", url: "Premium-Toast.html", category: "Bakery Delights" },
        { name: "Classic Toast ( 500 gm )", url: "Classic-Toast.html", category: "Bakery Delights" },
        { name: "Shanpapri ( 500gm )", url: "Shanpapri.html", category: "Bakery Delights" },
        { name: "Chanachur 250gm", url: "Chanachur.html", category: "Bakery Delights" },

        // Signature Yogurts
        { name: "Premium doi", url: "Premium-doi.html", category: "Signature Yogurts" },
        { name: "Malai doi", url: "malai-doi.html", category: "Signature Yogurts" },
        { name: "Cup Malai doi", url: "Cup-malai-doi.html", category: "Signature Yogurts" },
        { name: "Cup doi", url: "Cup-doi.html", category: "Signature Yogurts" },
        { name: "Sada doi", url: "Sada-doi.html", category: "Signature Yogurts" },

        // Semai Symphony
        { name: "Vermicelli Semai", url: "Vermicelli-Semai.html", category: "Semai Symphony" },
        { name: "Lachcha Semai white", url: "Lachcha-Semai-white.html", category: "Semai Symphony" },
        { name: "Lachcha Semai 200gm", url: "Lachcha-Semai-200gm.html", category: "Semai Symphony" },
        { name: "Lachcha Semai 300gm Box", url: "Lachcha-Semai-300gm-Box.html", category: "Semai Symphony" },
        { name: "Bhaja Semai", url: "Bhaja-Semai.html", category: "Semai Symphony" }
    ];

    // Inject Modals HTML
    const searchModalHTML = `
        <div id="search-modal-overlay" class="modal-blur-overlay">
            <div class="search-modal-card" onclick="event.stopPropagation()">
                <div class="search-row">
                    <div class="search-input-wrapper">
                        <svg class="search-input-icon" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                            <circle cx="11" cy="11" r="8"></circle>
                            <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
                        </svg>
                        <input type="text" id="search-input" class="search-input-field" placeholder="Search Your Product" autocomplete="off">
                    </div>
                    <button id="search-submit-btn" class="search-submit-btn">Search</button>
                </div>
                <div id="search-suggestions" class="search-suggestions-container"></div>
            </div>
        </div>
    `;

    const loginModalHTML = `
        <div id="login-modal-overlay" class="modal-blur-overlay">
            <div class="login-modal-card" onclick="event.stopPropagation()">
                <div class="login-title-text">Write down your email;\nFor us to recognize you later.</div>
                <div class="login-row">
                    <div class="login-input-wrapper">
                        <i class="fa-solid fa-envelope fa-sm login-input-icon" style="color: rgb(20, 21, 22);"></i>
                        <input type="email" id="login-email-input" class="login-input-field" placeholder="Enter E-mail" autocomplete="off">
                    </div>
                    <button id="login-submit-btn" class="login-submit-btn">Login</button>
                </div>
            </div>
        </div>
    `;

    document.body.insertAdjacentHTML('beforeend', searchModalHTML + loginModalHTML);

    const searchOverlay = document.getElementById('search-modal-overlay');
    const loginOverlay = document.getElementById('login-modal-overlay');
    const searchInput = document.getElementById('search-input');
    const loginInput = document.getElementById('login-email-input');
    const searchSubmit = document.getElementById('search-submit-btn');
    const loginSubmit = document.getElementById('login-submit-btn');
    const suggestionsContainer = document.getElementById('search-suggestions');

    // Find Header Buttons safely across all pages
    const searchIconBtn = document.querySelector('[aria-label="Search"]') || 
                         document.querySelector('.fa-searchengin')?.closest('a') ||
                         document.querySelector('.header-icons a:nth-child(1)');

    const loginIconBtn = document.querySelector('[aria-label="Profile"]') || 
                        document.querySelector('.fa-user-lock')?.closest('a') ||
                        document.querySelector('.header-icons a:nth-child(2)');

    function showModal(overlay, input) {
        overlay.classList.add('active');
        document.body.style.overflow = 'hidden';
        setTimeout(() => input.focus(), 100);
    }

    function closeModals() {
        searchOverlay.classList.remove('active');
        loginOverlay.classList.remove('active');
        document.body.style.overflow = '';
        searchInput.value = '';
        loginInput.value = '';
        suggestionsContainer.innerHTML = '';
    }

    if (searchIconBtn) {
        searchIconBtn.addEventListener('click', (e) => {
            e.preventDefault();
            e.stopPropagation();
            showModal(searchOverlay, searchInput);
        });
    }

    if (loginIconBtn) {
        loginIconBtn.addEventListener('click', (e) => {
            e.preventDefault();
            e.stopPropagation();
            showModal(loginOverlay, loginInput);
        });
    }

    // Close on overlay backdrop click
    searchOverlay.addEventListener('click', closeModals);
    loginOverlay.addEventListener('click', closeModals);

    // Escape key to close
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') closeModals();
    });

    // --- Search Autocomplete / Guess Logic ---
    let isDeleting = false;
    searchInput.addEventListener('keydown', (e) => {
        isDeleting = (e.key === 'Backspace' || e.key === 'Delete');
        if (e.key === 'Enter') performSearch();
    });

    searchInput.addEventListener('input', () => {
        const query = searchInput.value.toLowerCase().trim();
        if (query.length === 0) {
            suggestionsContainer.innerHTML = '';
            return;
        }

        if (isDeleting) {
            // If deleting, just show partial matches without autocompleting typed text
            const match = ALL_PRODUCTS.find(p => p.name.toLowerCase().startsWith(query));
            if (match) {
                renderSuggestions(match);
            } else {
                suggestionsContainer.innerHTML = '';
            }
            return;
        }

        // Find prefix match to autocomplete typed text
        const match = ALL_PRODUCTS.find(p => p.name.toLowerCase().startsWith(query));
        if (match) {
            const origLen = searchInput.value.length;
            searchInput.value = match.name;
            searchInput.setSelectionRange(origLen, match.name.length);
            renderSuggestions(match);
        } else {
            // Fallback: search for partial matches
            const partial = ALL_PRODUCTS.find(p => p.name.toLowerCase().includes(query));
            if (partial) {
                renderSuggestions(partial);
            } else {
                suggestionsContainer.innerHTML = '';
            }
        }
    });

    function renderSuggestions(matchedProduct) {
        // Filter out currently matched product, show other products in same category
        const others = ALL_PRODUCTS.filter(p => p.category === matchedProduct.category && p.name !== matchedProduct.name);
        
        suggestionsContainer.innerHTML = '';
        others.forEach(prod => {
            const item = document.createElement('a');
            item.href = prod.url;
            item.className = 'suggestion-item';
            item.innerHTML = `
                <svg class="suggestion-item-icon" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <circle cx="11" cy="11" r="8"></circle>
                    <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
                </svg>
                <span class="suggestion-item-text">${prod.name}</span>
            `;
            suggestionsContainer.appendChild(item);
        });
    }

    function performSearch() {
        const query = searchInput.value.trim().toLowerCase();
        if (!query) return;

        const exact = ALL_PRODUCTS.find(p => p.name.toLowerCase() === query);
        if (exact) {
            window.location.href = exact.url;
            return;
        }

        const partial = ALL_PRODUCTS.find(p => p.name.toLowerCase().includes(query));
        if (partial) {
            window.location.href = partial.url;
            return;
        }

        const catMatch = ALL_PRODUCTS.find(p => p.category.toLowerCase().includes(query));
        if (catMatch) {
            window.location.href = catMatch.url;
            return;
        }

        window.location.href = 'shop.html';
    }

    if (searchSubmit) {
        searchSubmit.addEventListener('click', performSearch);
    }

    // --- Login Submission Logic ---
    function performLogin() {
        const email = loginInput.value.trim();
        if (!email || !email.includes('@')) {
            alert("Please enter a valid e-mail address!");
            return;
        }

        localStorage.setItem('food_lab_user_email', email);

        // Show premium success notification using existing alert box
        const notif = document.getElementById('cart-notification');
        const notifText = document.getElementById('cart-notification-text');
        if (notif && notifText) {
            notifText.innerText = `Welcome back! Logged in as ${email}`;
            notif.classList.remove('show');
            void notif.offsetWidth;
            notif.classList.add('show');
            setTimeout(() => { notif.classList.remove('show'); }, 3000);
        } else {
            alert(`Welcome back! Recognized: ${email}`);
        }

        closeModals();
    }

    if (loginSubmit) {
        loginSubmit.addEventListener('click', performLogin);
    }
    loginInput.addEventListener('keydown', (e) => {
        if (e.key === 'Enter') performLogin();
    });
});
