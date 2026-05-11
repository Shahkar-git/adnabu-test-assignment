# AdNabu Test Store — QA Assignment
**Tester:** Mohammad Shahkar Alam  
**Store:** https://adnabu-store-assignment1.myshopify.com  
**Store Password:** AdNabuQA  
**Tools:** Python, Selenium, Pytest

---

## 📋 TASK 1 — Test Cases

---

### A) Product Search — Test Cases

---

**TC_SEARCH_001 — Search with valid product name (Positive)**
- **Steps:** Open store → Click search icon → Type "T-Shirt" → Press Enter
- **Expected Result:** Search results page displays products matching "T-Shirt"

---

**TC_SEARCH_002 — Search with invalid/random keyword (Negative)**
- **Steps:** Open store → Click search icon → Type "xyzabc123" → Press Enter
- **Expected Result:** "No results found" message is displayed; no products shown

---

**TC_SEARCH_003 — Search with empty input (Negative)**
- **Steps:** Open store → Click search icon → Leave input blank → Press Enter
- **Expected Result:** Either search is not submitted OR all products are shown; no crash occurs

---

**TC_SEARCH_004 — Search with special characters (Edge Case)**
- **Steps:** Open store → Click search icon → Type "@#$%^&*()" → Press Enter
- **Expected Result:** Application handles gracefully — shows "No results" or empty results; no error/crash

---

**TC_SEARCH_005 — Search with partial product name (Positive)**
- **Steps:** Open store → Click search icon → Type "T-S" → Press Enter
- **Expected Result:** Products containing "T-S" in name are shown in results

---

**TC_SEARCH_006 — Search result relevance (Positive)**
- **Steps:** Search for "Shirt" → Check all result titles
- **Expected Result:** All displayed products are relevant to the keyword "Shirt"; irrelevant products are not shown

---

### B) Add to Cart — Test Cases

---

**TC_CART_001 — Add a single product to cart (Positive)**
- **Steps:** Search "T-Shirt" → Click first result → Click "Add to Cart" → Go to Cart
- **Expected Result:** Product is visible in cart with correct name and quantity 1

---

**TC_CART_002 — Add multiple different products to cart (Positive)**
- **Steps:** Add Product A → Continue shopping → Add Product B → Go to Cart
- **Expected Result:** Both products appear in cart with correct details

---

**TC_CART_003 — Add out-of-stock product (Negative)**
- **Steps:** Navigate to an out-of-stock product page
- **Expected Result:** "Add to Cart" button is disabled or shows "Sold Out"; product cannot be added

---

**TC_CART_004 — Add product without selecting required variant (Negative)**
- **Steps:** Open a product with size/color variants → Do NOT select variant → Click "Add to Cart"
- **Expected Result:** Error message shown asking user to select a variant; product not added to cart

---

**TC_CART_005 — Add maximum quantity of a product (Edge Case)**
- **Steps:** Open a product → Set quantity to 999 → Click "Add to Cart"
- **Expected Result:** Either maximum allowed quantity is added OR error message shown for exceeding limit; no crash

---

**TC_CART_006 — Verify cart count updates after adding product (Positive)**
- **Steps:** Note cart count (0) → Add a product → Check cart icon count
- **Expected Result:** Cart count increments from 0 to 1 after product is added

---

## 🤖 TASK 2 — Automation Setup

---

### Project Structure

```
adnabu_test/
├── pages/
│   ├── base_page.py           → Shared Selenium utilities
│   ├── password_page.py       → Store password entry
│   ├── home_page.py           → Search functionality
│   ├── search_results_page.py → Results page interactions
│   ├── product_page.py        → Product detail + Add to Cart
│   └── cart_page.py           → Cart verification
├── tests/
│   └── test_search_add_to_cart.py  → Main automation test
├── conftest.py                → Pytest fixtures (WebDriver setup)
├── pytest.ini                 → Pytest configuration
├── requirements.txt           → Dependencies
└── README.md                  → This file
```

---

### ⚙️ Setup Instructions

**Step 1 — Clone the repository**
```bash
git clone https://github.com/YOUR_USERNAME/adnabu-test-assignment.git
cd adnabu-test-assignment
```

**Step 2 — Create virtual environment**
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

**Step 3 — Install dependencies**
```bash
pip install -r requirements.txt
```

**Step 4 — Make sure Chrome is installed**
- Download Chrome: https://www.google.com/chrome/
- ChromeDriver is managed automatically via webdriver-manager

**Step 5 — Run the test**
```bash
pytest tests/test_search_add_to_cart.py -v
```

**Step 6 — Run with HTML report**
```bash
pip install pytest-html
pytest tests/test_search_add_to_cart.py -v --html=reports/report.html --self-contained-html
```

---

### ▶️ Running Tests

| Command | Description |
|---|---|
| `pytest` | Run all tests |
| `pytest -v` | Verbose output |
| `pytest --html=reports/report.html` | Generate HTML report |
| `pytest -s` | Show print statements |

---

### 🎯 Automated Scenario

**Search for a product and add it to cart successfully**

1. Open the store URL and enter password
2. Click the search icon and search for "T-Shirt"
3. Verify search results are displayed
4. Click the first product result
5. Click "Add to Cart" button
6. Navigate to cart page
7. Assert product is present in cart

---

### ✅ Design Decisions

- **Page Object Model** — Each page has its own class; test logic is separate from page logic
- **No hardcoded sleeps** — All waits use Selenium's `WebDriverWait` with `expected_conditions`
- **Session-scoped driver** — Browser opens once per test session, not per test
- **Modular pages** — Each page class is independent and reusable
- **CSS Selectors preferred** — Faster and more stable than XPath where possible
- **Multiple fallback locators** — CSS selectors include alternatives to handle Shopify theme variations
