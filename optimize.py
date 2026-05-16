import os
import re

css_path = r"c:\Users\zakii\OneDrive\Dokumen\DUODANIEL\index.css"
with open(css_path, "r", encoding="utf-8") as f:
    content = f.read()

# Reduce blur radiuses for better performance
content = content.replace("blur(60px)", "blur(12px)")
content = content.replace("blur(36px)", "blur(12px)")
content = content.replace("blur(24px)", "blur(8px)")
content = content.replace("blur(20px)", "blur(8px)")
content = content.replace("blur(18px)", "blur(8px)")
content = content.replace("blur(12px)", "blur(6px)")

# Add will-change to background circles
content = content.replace(".circle {", ".circle {\n    will-change: transform;")

# Reduce the size of the box-shadows slightly to improve rendering
content = content.replace("0 20px 60px", "0 10px 30px")
content = content.replace("0 8px 32px", "0 4px 16px")

# Append performance mode classes
perf_css = """

/* =========================================
   PERFORMANCE MODE OPTIMIZATIONS
   (Smooth & Lightweight Rendering)
   ========================================= */
body.performance-mode .bg-animation,
body.performance-mode #particleCanvas {
    display: none !important;
}

body.performance-mode * {
    backdrop-filter: none !important;
    -webkit-backdrop-filter: none !important;
}

body.performance-mode .content-section,
body.performance-mode .sidebar,
body.performance-mode .card-glass,
body.performance-mode .stat-box,
body.performance-mode .snbt-card {
    background: var(--bg-surface-md) !important;
    border: 1px solid var(--glass-border-md) !important;
}

/* Force hardware acceleration on heavily animated elements */
.hero-section, .bg-animation, .content-section {
    transform: translateZ(0);
    backface-visibility: hidden;
    perspective: 1000px;
}

/* Optimizing animations to reduce repaint cost */
@media screen and (max-width: 768px) {
    .bg-animation {
        opacity: 0.3;
    }
    .circle {
        animation-duration: 40s !important;
    }
}
"""

if "PERFORMANCE MODE OPTIMIZATIONS" not in content:
    content += perf_css

with open(css_path, "w", encoding="utf-8") as f:
    f.write(content)

print("CSS Optimization applied successfully.")
