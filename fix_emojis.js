const fs = require('fs');
const path = require('path');

const root = __dirname;
const iconMap = {
  'Beranda': '🏠',
  'Statistik': '📊',
  'Evaluasi SNBT': '🎓',
  'Pencapaian': '🏆',
  'Materi': '📚',
  'Library': '📖',
  'Pengaturan': '⚙️',
  'Panduan': '📋',
  'Feedback': '💬',
  'Masuk Akun': '🔑',
  'Masuk / Daftar': '🔑'
};

const brokenArrow = String.fromCharCode(0x00e2, 0x2013, 0x00b8);
const brokenDegree = '100' + String.fromCharCode(0x00c2) + '°C';
const files = fs.readdirSync(root).filter((file) => /\.(html|js|css)$/.test(file) && file !== 'fix_emojis.js');
let changedFiles = 0;

for (const file of files) {
  const fullPath = path.join(root, file);
  let content = fs.readFileSync(fullPath, 'utf8');
  const before = content;

  for (const [label, icon] of Object.entries(iconMap)) {
    const escaped = label.replace(/[.*+?^$\{\}()|[\]\\]/g, '\\$&');
    content = content.replace(new RegExp('(<span class="menu-icon"[^>]*>)[^<]*(<\\/span><span[^>]*>\\s*' + escaped + ')', 'g'), '$1' + icon + '$2');
    content = content.replace(new RegExp('(<span class="sb-icon"[^>]*>)[^<]*(<\\/span>\\s*' + escaped + ')', 'g'), '$1' + icon + '$2');
  }

  content = content
    .replace(new RegExp("content:\\s*'" + brokenArrow + "';", 'g'), "content: '▸';")
    .replace(new RegExp(brokenDegree, 'g'), '100°C')
    .replace(/(<span id="themeIcon"[^>]*>)[^<]*(<\/span>)/g, '$1🌙$2')
    .replace(/(<span id="musicIcon"[^>]*>)[^<]*(<\/span>)/g, '$1🔊$2');

  if (content !== before) {
    fs.writeFileSync(fullPath, content, 'utf8');
    changedFiles++;
  }
}

console.log(`Updated ${changedFiles} files.`);
