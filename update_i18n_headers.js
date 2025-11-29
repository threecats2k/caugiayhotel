// Helper script to add i18n support to all HTML files
// This script can be run manually or used as reference

const fs = require('fs');
const path = require('path');

const htmlFiles = [
    'about.html',
    'services.html',
    'contact.html',
    'policies.html',
    'process.html',
    'portfolio.html',
    'news.html',
    'company-info.html'
];

// Common header pattern with i18n
const headerTemplate = `    <link rel="stylesheet" href="css/styles.css">
    <link rel="canonical" href="https://uniform-quockhanh.store/">
    <script src="js/i18n.js" defer></script>
</head>
<body>
    <!-- Header -->
    <header class="header">
        <div class="container">
            <div class="header-top">
                <div class="logo">
                    <h1 data-i18n="common.logo">QUỐC KHÁNH UNIFORM</h1>
                    <p class="tagline" data-i18n="common.tagline">Chất lượng - Uy tín - Chuyên nghiệp</p>
                </div>
                <div class="header-contact">
                    <a href="tel:0366333168" class="phone-link">📞 <span data-i18n="common.phone">0366 333 168</span></a>
                    <a href="contact.html" class="btn btn-primary" data-i18n="common.contactNow">Liên hệ ngay</a>
                </div>
            </div>
            <nav class="navbar">
                <ul class="nav-menu">
                    <li><a href="index.html" data-i18n="common.nav.home">Trang chủ</a></li>
                    <li><a href="about.html" data-i18n="common.nav.about">Giới thiệu</a></li>
                    <li><a href="services.html" data-i18n="common.nav.services">Dịch vụ</a></li>
                    <li><a href="process.html" data-i18n="common.nav.process">Quy trình</a></li>
                    <li><a href="portfolio.html" data-i18n="common.nav.portfolio">Dự án</a></li>
                    <li><a href="news.html" data-i18n="common.nav.news">Tin tức</a></li>
                    <li><a href="policies.html" data-i18n="common.nav.policies">Chính sách</a></li>
                    <li><a href="contact.html" data-i18n="common.nav.contact">Liên hệ</a></li>
                </ul>
                <button class="mobile-menu-toggle" aria-label="Toggle menu" data-i18n-aria-label="common.nav.menu">☰</button>
            </nav>
        </div>
    </header>`;

console.log('Helper script created. Use this as reference to update HTML files manually.');
console.log('All HTML files need:');
console.log('1. Add <script src="js/i18n.js" defer></script> in <head>');
console.log('2. Add data-i18n attributes to translatable elements');
console.log('3. Update header/footer with i18n attributes');

