"""
Bundle Script for Toyland.id
Merges modular React code into a standalone bundle for instant zero-dependency browser execution.
"""
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(base_dir, "src")

# 1. Read data & utils
with open(os.path.join(src_dir, "data", "products.js"), "r", encoding="utf-8") as f:
    products_code = f.read()

with open(os.path.join(src_dir, "utils", "formatters.js"), "r", encoding="utf-8") as f:
    formatters_code = f.read()

# 2. Components list in dependency order
components = [
    "GrowthRoadmap.jsx",
    "PromoBanner.jsx",
    "Testimonial.jsx",
    "CategoryCard.jsx",
    "ProductCard.jsx",
    "ProductDetailModal.jsx",
    "CartDrawer.jsx",
    "CheckoutModal.jsx",
    "WhatsAppButton.jsx",
    "Hero.jsx",
    "Navbar.jsx",
    "Footer.jsx"
]

# 3. Pages list
pages = [
    "Home.jsx",
    "About.jsx",
    "Products.jsx",
    "Promo.jsx",
    "Reseller.jsx",
    "Contact.jsx"
]

def clean_imports_and_exports(code, is_data=False):
    lines = code.split("\n")
    cleaned = []
    for line in lines:
        stripped = line.strip()
        # Remove import statements
        if stripped.startswith("import ") or (stripped.startswith("import{") or stripped.startswith("import {")):
            continue
        # Replace export default function / export function / export const
        if stripped.startswith("export default function "):
            line = line.replace("export default function ", "function ")
        elif stripped.startswith("export function "):
            line = line.replace("export function ", "function ")
        elif stripped.startswith("export const "):
            line = line.replace("export const ", "const ")
        elif stripped.startswith("export default "):
            continue
        cleaned.append(line)
    return "\n".join(cleaned)

clean_products = clean_imports_and_exports(products_code, is_data=True)
clean_formatters = clean_imports_and_exports(formatters_code, is_data=True)

comp_codes = []
for comp in components:
    with open(os.path.join(src_dir, "components", comp), "r", encoding="utf-8") as f:
        comp_codes.append(f"// --- Component: {comp} ---\n" + clean_imports_and_exports(f.read()))

page_codes = []
for page in pages:
    with open(os.path.join(src_dir, "pages", page), "r", encoding="utf-8") as f:
        page_codes.append(f"// --- Page: {page} ---\n" + clean_imports_and_exports(f.read()))

with open(os.path.join(src_dir, "App.jsx"), "r", encoding="utf-8") as f:
    app_code = clean_imports_and_exports(f.read())

bundle_content = f"""/**
 * TOYLAND.ID - STANDALONE BUNDLE FOR INSTANT PRESENTATION
 * React 18 + Babel Standalone + Full Component Hierarchy
 */

const {{ useState, useEffect, useMemo, useRef }} = React;

// === 1. DATA & CONSTANTS ===
{clean_products}

// === 2. UTILS & HELPERS ===
{clean_formatters}

// === 3. COMPONENTS ===
{"\n\n".join(comp_codes)}

// === 4. PAGES ===
{"\n\n".join(page_codes)}

// === 5. ROOT APPLICATION ===
{app_code}

// === 6. MOUNT TO DOM ===
const rootElement = document.getElementById('root');
if (rootElement) {{
  const root = ReactDOM.createRoot(rootElement);
  root.render(<App />);
}}
"""

bundle_path = os.path.join(src_dir, "app.bundle.js")
with open(bundle_path, "w", encoding="utf-8") as f:
    f.write(bundle_content)

print(f"Successfully generated standalone bundle: {bundle_path} ({len(bundle_content)} bytes)")
