import os

directory = r'c:\Users\DELL\OneDrive\Desktop\Ibrahim A\Food Lab'

sidebar_html = """
    <!-- Mobile Sidebar -->
    <div class="sidebar-overlay" id="sidebar-overlay"></div>
    <aside class="mobile-sidebar" id="mobile-sidebar">
        <button class="mobile-sidebar-close" id="sidebar-close" aria-label="Close Navigation">
            <svg width="40" height="40" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
                <path d="M25 25 C 35 30, 65 70, 75 75 M75 25 C 65 30, 35 70, 25 75" stroke="#ff1a1a" stroke-width="12" stroke-linecap="round" stroke-linejoin="round" style="filter: url(#brush-texture);" />
                <defs>
                    <filter id="brush-texture">
                        <feTurbulence type="fractalNoise" baseFrequency="0.5" numOctaves="3" result="noise" />
                        <feDisplacementMap in="SourceGraphic" in2="noise" scale="5" xChannelSelector="R" yChannelSelector="G" />
                    </filter>
                </defs>
            </svg>
        </button>
        <nav class="mobile-sidebar-nav">
            <a href="index.html" class="mobile-nav-link">Home</a>
            <a href="shop.html" class="mobile-nav-link">Shop</a>
            <a href="cart.html" class="mobile-nav-link">Cart</a>
            <a href="about.html" class="mobile-nav-link">About Us</a>
            <a href="contacts.html" class="mobile-nav-link">Contacts</a>
        </nav>
    </aside>
"""

sidebar_script = """
    <script>
        const mobileToggle = document.getElementById('mobile-nav-toggle');
        const sidebar = document.getElementById('mobile-sidebar');
        const overlay = document.getElementById('sidebar-overlay');
        const closeBtn = document.getElementById('sidebar-close');

        function toggleSidebar() {
            sidebar.classList.toggle('open');
            overlay.classList.toggle('visible');
            document.body.style.overflow = sidebar.classList.contains('open') ? 'hidden' : '';
        }

        if (mobileToggle) mobileToggle.addEventListener('click', toggleSidebar);
        if (closeBtn) closeBtn.addEventListener('click', toggleSidebar);
        if (overlay) overlay.addEventListener('click', toggleSidebar);

        document.querySelectorAll('.mobile-nav-link').forEach(link => {
            link.addEventListener('click', () => {
                if (sidebar.classList.contains('open')) toggleSidebar();
            });
        });

        // Sticky Header / Shrink on Scroll
        window.addEventListener('scroll', () => {
            if (window.scrollY > 50) {
                document.body.classList.add('scrolled');
            } else {
                document.body.classList.remove('scrolled');
            }
        });
    </script>
"""

for filename in os.listdir(directory):
    if filename.endswith('.html') and filename not in ['index.html', 'about.html', 'contacts.html', 'shop.html', 'cart.html', 'checkout.html']:
        path = os.path.join(directory, filename)
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 1. Link Fixes
        content = content.replace('<a href="#" class="nav-link">Contacts</a>', '<a href="contacts.html" class="nav-link">Contacts</a>')
        content = content.replace('<a href="#" class="nav-link">About Us</a>', '<a href="about.html" class="nav-link">About Us</a>')
        content = content.replace('<a href="index.html" class="nav-link">Shop</a>', '<a href="shop.html" class="nav-link">Shop</a>')
        
        # 2. Inject Sidebar if missing
        if 'id="mobile-sidebar"' not in content:
            content = content.replace('</body>', sidebar_html + sidebar_script + '</body>')
            print(f'Injected sidebar into {filename}')
        
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)

print("Done.")
