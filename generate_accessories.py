
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

    .product-container {{
        padding-top: 50px;
        padding-bottom: 80px;
    }}

    .gallery-wrapper {{
        display: flex;
        gap: 20px;
    }}

    .thumbnail-strip {{
        display: flex;
        flex-direction: column;
        gap: 15px;
        width: 80px;
    }}

    .thumb-item {{
        width: 80px;
        height: 80px;
        border-radius: 12px;
        overflow: hidden;
        cursor: pointer;
        border: 2px solid transparent;
        transition: 0.2s;
    }}

    .thumb-item:hover, .thumb-item.active {{
        border-color: var(--accent-color);  
        transform: translateX(5px);
    }}

    .thumb-item img {{
        width: 100%;
        height: 100%;
        object-fit: cover;
    }}

    .main-image-viewport {{
        flex-grow: 1;
        border-radius: 24px;
        overflow: hidden;
        background: #f8f9fa;
        position: relative;
        box-shadow: var(--shadow-sm);
    }}

    .main-image-viewport img {{
        width: 100%;
        height: 700px;
        display: block;
        transition: transform 0.5s ease;
        object-fit: contain;
        background: white;
    }}

    .main-image-viewport:hover img {{
        transform: scale(1.05);
    }}

    .product-details-sticky {{
        position: sticky;
        top: 100px;
    }}

    .brand-tag {{
        color: var(--accent-color);
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: 2px;
        font-size: 0.8rem;
        margin-bottom: 10px;
        display: block;
    }}

    .product-title-big {{
        font-size: 2.5rem;
        font-weight: 800;
        color: var(--text-main);
        line-height: 1.1;
        margin-bottom: 15px;
    }}

    .price-tag-big {{
        font-size: 2rem;
        font-weight: 800;
        color: var(--accent-color);
        margin-bottom: 25px;
        display: flex;
        align-items: center;
        gap: 15px;
    }}

    .old-price {{
        font-size: 1.2rem;
        text-decoration: line-through;
        color: #b2bec3;
        font-weight: 600;
    }}

    .feature-list {{
        list-style: none;
        padding: 0;
        margin-bottom: 30px;
    }}

    .feature-list li {{
        display: flex;
        align-items: center;
        gap: 10px;
        margin-bottom: 10px;
        color: var(--text-secondary);
        font-size: 0.95rem;
    }}

    .feature-list i {{
        color: var(--accent-color);
        font-size: 0.8rem;
    }}

    .btn-action-group {{
        display: flex;
        gap: 15px;
        margin-top: 30px;
    }}

    .btn-premium-buy {{
        flex: 2;
        background: var(--text-main);
        color: white;
        border: none;
        padding: 18px;
        border-radius: 15px;
        font-weight: 800;
        transition: 0.3s;
        text-align: center;
        text-decoration: none;
    }}

    .btn-premium-buy:hover {{
        background: #000;
        transform: translateY(-3px);
        box-shadow: 0 10px 20px rgba(0,0,0,0.1);
        color: white;
    }}

    .btn-premium-cart {{
        flex: 1;
        background: var(--accent-color);
        color: white;
        border: none;
        padding: 18px;
        border-radius: 15px;
        font-weight: 800;
        transition: 0.3s;
    }}

    .btn-premium-cart:hover {{
        background: var(--accent-dark);
        transform: translateY(-3px);
    }}

    .related-section {{
        background: #fdfdfd;
        padding: 80px 0;
        border-top: 1px solid var(--border-color);
    }}

    .related-scroll-container {{
        display: flex;
        overflow-x: auto;
        gap: 25px;
        padding: 20px 0;
        scroll-behavior: smooth;
        -ms-overflow-style: none;
        scrollbar-width: none;
    }}

    .related-scroll-container::-webkit-scrollbar {{ display: none; }}

    .related-card {{
        min-width: 280px;
        background: white;
        border-radius: 20px;
        overflow: hidden;
        border: 1px solid var(--border-color);
        transition: 0.3s;
    }}

    .related-card:hover {{
        transform: translateY(-10px);
        box-shadow: var(--shadow-md);
    }}

    @media (max-width: 991px) {{
        .gallery-wrapper {{ flex-direction: column-reverse; }}
        .thumbnail-strip {{ flex-direction: row; width: 100%; }}
        .product-title-big {{ font-size: 2rem; }}
    }}

</style>

<div class="container product-container">
    <div class="row g-5">
        
        <!-- LEFT SIDE: GALLERY -->
        <div class="col-lg-7">
            <div class="gallery-wrapper">
                <div class="thumbnail-strip d-none d-lg-flex">
                    <div class="thumb-item active"><img src="{{% static 'assets/img/{main_img}' %}}" alt=""></div>
                    <div class="thumb-item"><img src="{{% static 'assets/img/{main_img}' %}}" alt=""></div>
                </div>

                <div class="main-image-viewport">
                    <img src="{{% static 'assets/img/{main_img}' %}}" alt="{title}" id="main-image">
                </div>
            </div>
        </div>

        <!-- RIGHT SIDE: PRODUCT INFO -->
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
                    <li><i class="fas fa-check"></i> Premium High-Quality Materials</li>
                    <li><i class="fas fa-check"></i> Designer Collection Style</li>
                    <li><i class="fas fa-check"></i> Limited Edition Availability</li>
                    <li><i class="fas fa-check"></i> Authentic Brand Packaging</li>
                </ul>

                <div class="btn-action-group">
                    <a href="{{% url '{url_name}' %}}" class="btn-premium-buy">BUY NOW</a>
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

<!-- Auto Scroll Script -->
<script>
    // Thumbnail switch logic
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

acc_data = {
    1: {"brand": "Ray-Ban", "title": "Classic Aviator Sunglasses", "price": "150.00", "img": "sunglass1.jpg", "desc": "The quintessential aviator silhouette that defined a generation. Featuring high-grade polarized lenses and iconic gold-tone frames."},
    2: {"brand": "Oakley", "title": "Sport Wayfarer Edition", "price": "120.00", "img": "sunglass2.jpg", "desc": "Engineered for performance and style. These lightweight frames provide maximum comfort and clarity for active lifestyles."},
    3: {"brand": "Gucci", "title": "Luxury Gold-Rimmed Shades", "price": "350.00", "img": "sunglass3.jpg", "desc": "Experience peak Italian luxury. These gold-rimmed sunglasses feature the iconic Gucci monogram and superior UV protection."},
    4: {"brand": "Prada", "title": "Premium Leather Handbag", "price": "450.00", "img": "bag1.jpg", "desc": "Meticulously crafted from Italian Saffiano leather, this Prada handbag is a timeless accessory for any high-fashion ensemble."},
    5: {"brand": "Fossil", "title": "Classic Bi-Fold Wallet", "price": "45.00", "img": "wallet1.jpg", "desc": "Genuine leather bi-fold wallet featuring multiple card slots and a sleek, minimalist design that fits perfectly in any pocket."},
    6: {"brand": "Levis", "title": "Genuine Leather Belt", "price": "35.00", "img": "belt.jpg", "desc": "Durable and stylish, this Levis belt is made from top-grain leather and features a classic brushed metal buckle."},
    7: {"brand": "Nike", "title": "Sport Performance Cap", "price": "25.00", "img": "cap.jpg", "desc": "Stay cool and focused with this breathable Nike performance cap. Featuring AeroBill technology for lightweight sweat-wicking comfort."},
    8: {"brand": "Burberry", "title": "Silk Patterned Scarf", "price": "180.00", "img": "Burberry.jpg", "desc": "The signature Burberry plaid reimagined in pure silk. A versatile accessory that adds a touch of British elegance to any look."},
    9: {"brand": "Herschel", "title": "Urban Explorer Backpack", "price": "85.00", "img": "bag2.jpg", "desc": "Designed for the modern nomad. This Herschel backpack combines retro mountaineering style with functional modern features like a laptop sleeve."}
}

output_dir = r"ecommerce/templates"

for i, data in acc_data.items():
    old_price = round(float(data["price"]) * 1.5, 2)
    content = template_content.format(
        title=data["title"],
        brand=data["brand"],
        price=data["price"],
        old_price=old_price,
        description=data["desc"],
        main_img=data["img"],
        url_name=f"acc_{i}"
    )
    file_path = os.path.join(output_dir, f"acc_{i}.html")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Created {file_path}")
