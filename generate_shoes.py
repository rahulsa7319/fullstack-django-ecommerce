
import os

template_content = r"""{{% extends "base.html" %}}
{{% load static %}}

{{% block title %}}
Happing - {title} Detail
{{% endblock title %}}

{{% block content %}}

<style>
    :root {{
        --accent-color: #59ab6e;
        --accent-dark: #3e754d;
        --accent-soft: #e8f5e9;
        --text-main: #2d3436;
        --text-secondary: #636e72;
        --border-color: #edf2f7;
        --shadow-sm: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
        --shadow-md: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
    }}

    body {{
        background-color: #ffffff;
    }}

    /* PREMIUM PRODUCT LAYOUT (NO SIDEBAR) */
    .product-container {{
        padding-top: 50px;
        padding-bottom: 80px;
    }}

    /* LEFT SIDE: MODERN GALLERY */
    .gallery-wrapper {{
        display: flex;
        gap: 20px;
    }}

    .thumbnail-strip {{
        display: flex;
        flex-direction: column; gap: 15px; width: 80px;
    }}

    .thumb-item {{
        width: 80px; height: 80px; border-radius: 12px; overflow: hidden; cursor: pointer; border: 2px solid transparent; transition: 0.2s;
    }}

    .thumb-item:hover, .thumb-item.active {{
        border-color: var(--accent-color); transform: translateX(5px);
    }}

    .thumb-item img {{
        width: 100%; height: 100%; object-fit: cover;
    }}

    .main-image-viewport {{
        flex-grow: 1; border-radius: 24px; overflow: hidden; background: #f8f9fa; position: relative; box-shadow: var(--shadow-sm);
    }}

    .main-image-viewport img {{
        width: 100%; height: 786px; display: block; transition: transform 0.5s ease; object-fit: cover;
    }}

    .main-image-viewport:hover img {{
        transform: scale(1.05);
    }}

    /* RIGHT SIDE: STICKY INFO */
    .product-details-sticky {{
        position: sticky; top: 100px;
    }}

    .brand-tag {{
        color: var(--accent-color); font-weight: 800; text-transform: uppercase; letter-spacing: 2px; font-size: 0.8rem; margin-bottom: 10px; display: block;
    }}

    .product-title-big {{
        font-size: 2.5rem; font-weight: 800; color: var(--text-main); line-height: 1.1; margin-bottom: 15px;
    }}

    .price-tag-big {{
        font-size: 2rem; font-weight: 800; color: var(--accent-color); margin-bottom: 25px; display: flex; align-items: center; gap: 15px;
    }}

    .old-price {{
        font-size: 1.2rem; text-decoration: line-through; color: #b2bec3; font-weight: 600;
    }}

    .feature-list {{
        list-style: none; padding: 0; margin-bottom: 30px;
    }}

    .feature-list li {{
        display: flex; align-items: center; gap: 10px; margin-bottom: 10px; color: var(--text-secondary); font-size: 0.95rem;
    }}

    .feature-list i {{
        color: var(--accent-color); font-size: 0.8rem;
    }}

    /* BUTTONS */
    .btn-action-group {{
        display: flex; gap: 15px; margin-top: 30px;
    }}

    .btn-premium-buy {{
        flex: 2; background: var(--text-main); color: white; border: none; padding: 18px; border-radius: 15px; font-weight: 800; transition: 0.3s;
    }}

    .btn-premium-buy:hover {{
        background: #000; transform: translateY(-3px); box-shadow: 0 10px 20px rgba(0,0,0,0.1);
    }}

    .btn-premium-cart {{
        flex: 1; background: var(--accent-color); color: white; border: none; padding: 18px; border-radius: 15px; font-weight: 800; transition: 0.3s;
    }}

    .btn-premium-cart:hover {{
        background: var(--accent-dark); transform: translateY(-3px);
    }}

    /* RELATED PRODUCTS SCROLLBAR */
    .related-section {{
        background: #fdfdfd; padding: 80px 0; border-top: 1px solid var(--border-color);
    }}

    .related-scroll-container {{
        display: flex; overflow-x: auto; gap: 25px; padding: 20px 0; scroll-behavior: smooth; -ms-overflow-style: none; scrollbar-width: none;
    }}

    .related-scroll-container::-webkit-scrollbar {{ display: none; }}

    .related-card {{
        min-width: 280px; background: white; border-radius: 20px; overflow: hidden; border: 1px solid var(--border-color); transition: 0.3s;
    }}

    .related-card:hover {{
        transform: translateY(-10px); box-shadow: var(--shadow-md);
    }}

    @media (max-width: 991px) {{
        .gallery-wrapper {{ flex-direction: column-reverse; }}
        .thumbnail-strip {{ flex-direction: row; width: 100%; }}
        .product-title-big {{ font-size: 2rem; }}
    }}

    /* BUTTONS ON HOVER */
    .hover-overlay {{
        position: absolute; bottom: 15px; left: 50%; transform: translateX(-50%) translateY(20px); width: 90%; padding: 10px; background: rgba(255, 255, 255, 0.95); backdrop-filter: blur(4px); display: flex; justify-content: center; gap: 10px; transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1); opacity: 0; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); z-index: 10;
    }}

    .product-card:hover .hover-overlay, .related-card:hover .hover-overlay {{
        transform: translateX(-50%) translateY(0); opacity: 1;
    }}

    .overlay-btn {{
        padding: 10px 16px; border-radius: 8px; font-size: 0.85rem; font-weight: 600; text-decoration: none; text-align: center; transition: 0.2s; flex: 1; white-space: nowrap;
    }}
    
    .btn-buy {{
        background: var(--accent-color); color: white; border: 1px solid var(--accent-color);
    }}
    
    .btn-buy:hover {{
        background: var(--accent-dark); border-color: var(--accent-dark); color: white;
    }}
    
    .btn-cart {{
        background: white; border: 1px solid var(--border-color); color: var(--text-main);
    }}
    
    .btn-cart:hover {{
        background: var(--bg-page); border-color: var(--text-main); color: var(--text-main);
    }}

</style>

<div class="container product-container">
    <div class="row g-5">
        <div class="col-lg-7">
            <div class="gallery-wrapper">
                <div class="thumbnail-strip d-none d-lg-flex">
                    <div class="thumb-item active"><img src="{{% static 'assets/img/{img1}' %}}" alt=""></div>
                    <div class="thumb-item"><img src="{{% static 'assets/img/{img2}' %}}" alt=""></div>
                    <div class="thumb-item"><img src="{{% static 'assets/img/{img3}' %}}" alt=""></div>
                    <div class="thumb-item"><img src="{{% static 'assets/img/{img4}' %}}" alt=""></div>
                </div>
                <div class="main-image-viewport">
                    <img src="{{% static 'assets/img/{main_img}' %}}" alt="{title}" id="main-image">
                </div>
            </div>
            <div class="thumbnail-strip d-flex d-lg-none mt-3">
                <div class="thumb-item active"><img src="{{% static 'assets/img/{img1}' %}}" alt=""></div>
                <div class="thumb-item"><img src="{{% static 'assets/img/{img2}' %}}" alt=""></div>
                <div class="thumb-item"><img src="{{% static 'assets/img/{img3}' %}}" alt=""></div>
                <div class="thumb-item"><img src="{{% static 'assets/img/{img4}' %}}" alt=""></div>
            </div>
        </div>
        <div class="col-lg-5">
            <div class="product-details-sticky">
                <span class="brand-tag">{brand}</span>
                <h1 class="product-title-big">{title}</h1>
                <div class="price-tag-big">
                    ${price}
                    <span class="old-price">${old_price}</span>
                </div>
                <div class="mb-4">
                    <p class="text-muted">{description}</p>
                </div>
                <ul class="feature-list">
                    <li><i class="fas fa-check"></i> Breathable Performance Material</li>
                    <li><i class="fas fa-check"></i> Advanced Cushioning Technology</li>
                    <li><i class="fas fa-check"></i> High-Traction Durable Outsole</li>
                    <li><i class="fas fa-check"></i> 12-Month Performance Warranty</li>
                </ul>
                <div class="mb-4">
                    <h6 class="fw-bold small mb-3">SELECT COLOR</h6>
                    <div class="d-flex gap-2">
                        <input type="radio" class="btn-check" name="color" id="color-primary" autocomplete="off" checked>
                        <label class="btn btn-outline-dark px-3 py-2 rounded-3" for="color-primary">Default</label>
                        <input type="radio" class="btn-check" name="color" id="color-variant1" autocomplete="off">
                        <label class="btn btn-outline-dark px-3 py-2 rounded-3" for="color-variant1">Variant 1</label>
                        <input type="radio" class="btn-check" name="color" id="color-variant2" autocomplete="off">
                        <label class="btn btn-outline-dark px-3 py-2 rounded-3" for="color-variant2">Variant 2</label>
                    </div>
                </div>
                <div class="btn-action-group">
                    <a href="{{% url '{url_name}' %}}" class="btn-premium-buy text-center text-decoration-none">BUY NOW</a>
                    <button class="btn-premium-cart"><i class="fas fa-shopping-cart"></i></button>
                </div>
                <div class="mt-5 p-4 rounded-4 bg-light d-flex align-items-center gap-4">
                    <div class="text-center">
                        <i class="fas fa-truck text-success mb-2"></i>
                        <p class="m-0 small fw-bold">Free Shipping</p>
                    </div>
                    <div class="vr"></div>
                    <div class="text-center">
                        <i class="fas fa-shield-alt text-success mb-2"></i>
                        <p class="m-0 small fw-bold">Certified Authentic</p>
                    </div>
                    <div class="vr"></div>
                    <div class="text-center">
                        <i class="fas fa-undo text-success mb-2"></i>
                        <p class="m-0 small fw-bold">30-Day Returns</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>

<section class="related-section">
    <div class="container">
        <div class="d-flex justify-content-between align-items-end mb-4">
            <div>
                <h2 class="fw-bold m-0">Similar Footwear</h2>
                <p class="text-muted m-0">You might also be interested in these</p>
            </div>
            <div class="d-flex gap-2">
                <button class="btn btn-dark rounded-circle" onclick="document.getElementById('relatedScroll').scrollBy({{left: -300, behavior: 'smooth'}})">{{<i class="fas fa-chevron-left"></i>}}</button>
                <button class="btn btn-dark rounded-circle" onclick="document.getElementById('relatedScroll').scrollBy({{left: 300, behavior: 'smooth'}})">{{<i class="fas fa-chevron-right"></i>}}</button>
            </div>
        </div>
        <div class="related-scroll-container" id="relatedScroll">
            <div class="related-card">
                <div class="position-relative overflow-hidden" style="aspect-ratio: 1/1;">
                    <img src="{{% static 'assets/img/shoes1.jpg' %}}" class="w-100 h-100 object-fit-cover" alt="Nike Air Max Platinum Pro">
                    <div class="hover-overlay"> 
                        <a href="{{% url 'shoe_1' %}}" class="overlay-btn btn-buy">Buy Now</a>
                        <a href="{{% url 'shoe_1' %}}" class="overlay-btn btn-cart">Add to Cart</a>
                    </div>
                </div>
                <div class="p-3 text-center">
                    <h6 class="fw-bold mb-1">Nike Air Max Platinum Pro</h6>
                    <p class="text-success fw-bold m-0">$199.99</p>
                </div>
            </div>
            <div class="related-card">
                <div class="position-relative overflow-hidden" style="aspect-ratio: 1/1;">
                    <img src="{{% static 'assets/img/shose2.jpg' %}}" class="w-100 h-100 object-fit-cover" alt="Adidas Ultraboost Midnight Edition">
                    <div class="hover-overlay"> 
                        <a href="{{% url 'shoe_2' %}}" class="overlay-btn btn-buy">Buy Now</a>
                        <a href="{{% url 'shoe_2' %}}" class="overlay-btn btn-cart">Add to Cart</a>
                    </div>
                </div>
                <div class="p-3 text-center">
                    <h6 class="fw-bold mb-1">Adidas Ultraboost Midnight Edition</h6>
                    <p class="text-success fw-bold m-0">$499.99</p>
                </div>
            </div>
            <div class="related-card">
                <div class="position-relative overflow-hidden" style="aspect-ratio: 1/1;">
                    <img src="{{% static 'assets/img/shoes3.jpg' %}}" class="w-100 h-100 object-fit-cover" alt="Puma RS-X Neon Sport Runner">
                    <div class="hover-overlay"> 
                        <a href="{{% url 'shoe_3' %}}" class="overlay-btn btn-buy">Buy Now</a>
                        <a href="{{% url 'shoe_3' %}}" class="overlay-btn btn-cart">Add to Cart</a>
                    </div>
                </div>
                <div class="p-3 text-center">
                    <h6 class="fw-bold mb-1">Puma RS-X Neon Sport Runner</h6>
                    <p class="text-success fw-bold m-0">$349.99</p>
                </div>
            </div>
            <div class="related-card">
                <div class="position-relative overflow-hidden" style="aspect-ratio: 1/1;">
                    <img src="{{% static 'assets/img/shoes4.jpg' %}}" class="w-100 h-100 object-fit-cover" alt="Reebok Classic Leather Retro White">
                    <div class="hover-overlay"> 
                        <a href="{{% url 'shoe_4' %}}" class="overlay-btn btn-buy">Buy Now</a>
                        <a href="{{% url 'shoe_4' %}}" class="overlay-btn btn-cart">Add to Cart</a>
                    </div>
                </div>
                <div class="p-3 text-center">
                    <h6 class="fw-bold mb-1">Reebok Classic Leather Retro White</h6>
                    <p class="text-success fw-bold m-0">$279.99</p>
                </div>
            </div>
            <div class="related-card">
                <div class="position-relative overflow-hidden" style="aspect-ratio: 1/1;">
                    <img src="{{% static 'assets/img/shoes5.jpg' %}}" class="w-100 h-100 object-fit-cover" alt="Nike Revolution Electric Core">
                    <div class="hover-overlay"> 
                        <a href="{{% url 'shoe_5' %}}" class="overlay-btn btn-buy">Buy Now</a>
                        <a href="{{% url 'shoe_5' %}}" class="overlay-btn btn-cart">Add to Cart</a>
                    </div>
                </div>
                <div class="p-3 text-center">
                    <h6 class="fw-bold mb-1">Nike Revolution Electric Core</h6>
                    <p class="text-success fw-bold m-0">$129.99</p>
                </div>
            </div>
        </div>
    </div>
</section>

<script>
    const scrollContainer = document.getElementById('relatedScroll');
    let scrollAmount = 0;
    setInterval(() => {{
        if (scrollAmount >= scrollContainer.scrollWidth - scrollContainer.clientWidth) {{
            scrollAmount = 0;
            scrollContainer.scrollTo({{left: 0, behavior: 'smooth'}});
        }} else {{
            scrollAmount += 300;
            scrollContainer.scrollBy({{left: 300, behavior: 'smooth'}});
        }}
    }}, 3000);

    const mainImage = document.getElementById('main-image');
    const thumbs = document.querySelectorAll('.thumb-item');
    thumbs.forEach(thumb => {{
        thumb.addEventListener('click', () => {{
            thumbs.forEach(t => t.classList.remove('active'));
            thumb.classList.add('active');
            mainImage.src = thumb.querySelector('img').src;
        }});
    }});
</script>

{{% endblock content %}}
"""

shoes_data = {
    7: {"brand": "Puma", "title": "Velocity Nitro Pro Performance", "price": "599.99", "img": "shoes7.jpg", "desc": "Experience the ultimate in running technology with the Puma Velocity Nitro Pro Performance. Featuring advanced NITRO foam for superior responsiveness and cushioning."},
    8: {"brand": "New Balance", "title": "574 Heritage Classic Series", "price": "449.99", "img": "shoes8.jpg", "desc": "A timeless icon of comfort and style. The New Balance 574 Heritage Classic Series combines premium materials with legendary craftsmanship."},
    9: {"brand": "Nike", "title": "Air Jordan High Street Red", "price": "699.99", "img": "shoes9.jpg", "desc": "Elevate your street style with the iconic Air Jordan High Street Red. Featuring a classic high-top silhouette and premium leather construction."},
    10: {"brand": "Adidas", "title": "Forum Low Classic White", "price": "349.99", "img": "shoes10.jpg", "desc": "A classic basketball silhouette reimagined for everyday wear. The Adidas Forum Low Classic White offers a clean, versatile look with modern comfort."},
    11: {"brand": "Puma", "title": "Future Rider Play On Sneakers", "price": "259.99", "img": "shoes11.jpg", "desc": "Vibrant colors and retro design meet modern comfort. The Puma Future Rider Play On Sneakers are perfect for those who want to stand out."},
    12: {"brand": "Under Armour", "title": "Charged Running Core Series", "price": "189.99", "img": "shoes12.jpg", "desc": "Engineered for maximum performance and durability. The Under Armour Charged Running Core Series provides the support you need for your daily runs."}
}

output_dir = r"ecommerce/templates"

for i, data in shoes_data.items():
    old_price = round(float(data["price"]) * 1.5, 2)
    content = template_content.format(
        title=data["title"],
        brand=data["brand"],
        price=data["price"],
        old_price=old_price,
        description=data["desc"],
        main_img=data["img"],
        img1="shoes7.jpg",
        img2="shoes8.jpg",
        img3="shoes9.jpg",
        img4="shoes10.jpg",
        url_name=f"shoe_{i}"
    )
    file_path = os.path.join(output_dir, f"shoe_{i}.html")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Created {file_path}")
