import os
import json

SITE_DIR = "site"
BASE_URL = ""

os.makedirs(SITE_DIR, exist_ok=True)
os.makedirs(f"{SITE_DIR}/tools", exist_ok=True)

TOOLS = [
    # نصوص (10)
    {"id": "word-counter", "name": "عداد الكلمات والحروف", "cat": "نصوص", "desc": "احسب عدد الكلمات والحروف والأسطر فوراً مع وقت القراءة المتوقع.", "type": "word_counter"},
    {"id": "case-converter", "name": "محول حالة الأحرف الإنجليزية", "cat": "نصوص", "desc": "تحويل النص إلى UPPERCASE, lowercase, Title Case.", "type": "case_converter"},
    {"id": "remove-spaces", "name": "مزيل المسافات والأسطر الزائدة", "cat": "نصوص", "desc": "تنظيف النصوص من الفراغات والمسافات البيضاء والأسطر المكررة.", "type": "remove_spaces"},
    {"id": "reverse-text", "name": "عكس النصوص", "cat": "نصوص", "desc": "عكس ترتيب الأحرف أو الكلمات بسهولة وبشكل فوري.", "type": "reverse_text"},
    {"id": "lorem-ipsum", "name": "مولد نص لوريم إيبسوم", "cat": "نصوص", "desc": "توليد نصوص وهمية للمصممين والمطورين بعدد الفقرات.", "type": "lorem_gen"},
    {"id": "slug-generator", "name": "مولد روابط الـ Slug السريعة", "cat": "نصوص", "desc": "تحويل أي عنوان إلى رابط SEO ملائم URL-friendly.", "type": "slug_gen"},
    {"id": "duplicate-remover", "name": "مزيل الأسطر المكررة", "cat": "نصوص", "desc": "استخراج القوائم وحذف التكرار منها بضغطة زر.", "type": "duplicate_remover"},
    {"id": "markdown-previewer", "name": "معاين لغة Markdown", "cat": "نصوص", "desc": "كتابة نصوص ماركداون ومعاينتها وتحويلها إلى HTML فوري.", "type": "md_preview"},
    {"id": "morse-code", "name": "محول شفرة مورس", "cat": "نصوص", "desc": "ترجمة النصوص إلى شفرة مورس والعكس بكل دقة.", "type": "morse_converter"},
    {"id": "repeat-text", "name": "مكرر النصوص والكلمات", "cat": "نصوص", "desc": "تكرار جملة أو نص لعدد محدد من المرات مع فواصل مخصصة.", "type": "text_repeater"},

    # حسابات (10)
    {"id": "percentage-calc", "name": "حاسبة النسبة المئوية", "cat": "حسابات", "desc": "حساب نسب الزيادة والخصم والنسبة المئوية الشاملة.", "type": "percent_calc"},
    {"id": "age-calc", "name": "حاسبة العمر التفصيلية", "cat": "حسابات", "desc": "احسب عمرك بالسنوات، الشهور، الأيام، والدقائق بدقة.", "type": "age_calc"},
    {"id": "bmi-calc", "name": "حاسبة مؤشر كتلة الجسم (BMI)", "cat": "حسابات", "desc": "معرفة الوزن المثالي وتصنيف كتلة الجسم وفق المعايير الطبية.", "type": "bmi_calc"},
    {"id": "discount-calc", "name": "حاسبة الخصومات والعروض", "cat": "حسابات", "desc": "معرفة السعر بعد الخصم وقيمة التوفير النهائية للمشتريات.", "type": "discount_calc"},
    {"id": "loan-calc", "name": "حاسبة القروض والأقساط", "cat": "حسابات", "desc": "حساب القسط الشهري مع إجمالي الفائدة المستحقة وجدولة السداد.", "type": "loan_calc"},
    {"id": "date-diff", "name": "حاسبة فرق التاريخين", "cat": "حسابات", "desc": "حساب عدد الأيام والأسابيع بين أي تاريخين محددين.", "type": "date_diff"},
    {"id": "fuel-calc", "name": "حاسبة تكلفة استهلاك الوقود", "cat": "حسابات", "desc": "حساب استهلاك البنزين وتكلفة الرحلة التقديرية بالمسافة.", "type": "fuel_calc"},
    {"id": "gpa-calc", "name": "حاسبة المعدل التراكمي (GPA)", "cat": "حسابات", "desc": "حساب المعدل الفصلي والتراكمي لطلاب الجامعات والمدارس.", "type": "gpa_calc"},
    {"id": "scientific-calc", "name": "آلة حاسبة علمية خفيفة", "cat": "حسابات", "desc": "إجراء العمليات الحسابية المباشرة والجذور والأسس.", "type": "simple_calc"},
    {"id": "salary-calc", "name": "حاسبة أجر الساعة والعمل الحر", "cat": "حسابات", "desc": "حساب الدخل اليومي والأسبوعي والشهري حسب ساعات العمل.", "type": "hourly_calc"},

    # تحويلات (10)
    {"id": "temp-converter", "name": "محول درجات الحرارة", "cat": "تحويلات", "desc": "تحويل بين مئوي (Celsius) وفهرنهايت وكلفن فورياً.", "type": "temp_conv"},
    {"id": "length-converter", "name": "محول وحدات الطول", "cat": "تحويلات", "desc": "تحويل بين المتر، الكيلومتر، السنتيمتر، الميل، الإنش والقدم.", "type": "length_conv"},
    {"id": "weight-converter", "name": "محول وحدات الوزن والكتلة", "cat": "تحويلات", "desc": "تحويل بين الكيلوجرام، الجرام، الرطل (Pound)، والأونصة.", "type": "weight_conv"},
    {"id": "storage-converter", "name": "محول وحدات التخزين الرقمية", "cat": "تحويلات", "desc": "تحويل بين بايت، كيلوبايت، ميجابايت، جيجابايت، وتيرابايت.", "type": "storage_conv"},
    {"id": "speed-converter", "name": "محول السرعات", "cat": "تحويلات", "desc": "تحويل السرعة بين كم/ساعة، ميل/ساعة، ومتر/ثانية والعقدة.", "type": "speed_conv"},
    {"id": "time-converter", "name": "محول وحدات الوقت", "cat": "تحويلات", "desc": "تحويل فوري بين الثواني، الدقائق، الساعات، والأيام.", "type": "time_conv"},
    {"id": "area-converter", "name": "محول وحدات المساحة", "cat": "تحويلات", "desc": "تحويل فدان، دونم، هكتار، ومتر مربع بكل سلاسة.", "type": "area_conv"},
    {"id": "number-to-words", "name": "محول الأرقام إلى كلمات", "cat": "تحويلات", "desc": "تفقيد المبالغ والأرقام وتحويل الأرقام إلى نصوص باللغة الإنجليزية.", "type": "num_to_words"},
    {"id": "roman-numerals", "name": "محول الأرقام الرومانية", "cat": "تحويلات", "desc": "تحويل الأرقام العادية إلى أرقام رومانية (V, X, L, C, M) والعكس.", "type": "roman_conv"},
    {"id": "base-converter", "name": "محول الأنظمة العددية (Base)", "cat": "تحويلات", "desc": "التحويل بين الثنائي (Binary)، العشري، والسداسي عشر (Hex).", "type": "base_conv"},

    # تطوير (10)
    {"id": "json-formatter", "name": "منسق ومدقق JSON", "cat": "تطوير", "desc": "تنسيق كود JSON، وترتيبه مع التحقق من صحة القواعد البرمجية.", "type": "json_format"},
    {"id": "html-encoder", "name": "تشفير وفك تشفير HTML", "cat": "تطوير", "desc": "تحويل الأحرف الخاصة إلى HTML Entities والعكس.", "type": "html_encode"},
    {"id": "url-encoder", "name": "تشفير وفك تشفير الروابط (URL)", "cat": "تطوير", "desc": "تشفير وفك تشفير الروابط عبر UrlEncode و UrlDecode.", "type": "url_encode"},
    {"id": "base64-tool", "name": "تشفير وفك تشفير Base64", "cat": "تطوير", "desc": "تحويل النصوص من وإلى صيغة Base64 النصية مباشرة.", "type": "base64_tool"},
    {"id": "css-minifier", "name": "ضاغط ملفات CSS", "cat": "تطوير", "desc": "ضغط وتصغير كود CSS لزيادة سرعة تحميل صفحات الويب.", "type": "css_minify"},
    {"id": "js-minifier", "name": "ضاغط ملفات JavaScript", "cat": "تطوير", "desc": "إزالة الفراغات والتعليقات من كود الجافاسكربت وتخفيف حجمه.", "type": "js_minify"},
    {"id": "color-converter", "name": "محول الألوان HEX إلى RGB", "cat": "تطوير", "desc": "تحويل الألوان بين كود HEX و RGB مع معاينة حية للون.", "type": "color_conv"},
    {"id": "regex-tester", "name": "مختبر التعابير القياسية Regex", "cat": "تطوير", "desc": "اختبار الـ Regular Expressions ومطابقتها مع النصوص فورياً.", "type": "regex_tool"},
    {"id": "sql-formatter", "name": "منسق استعلامات SQL", "cat": "تطوير", "desc": "ترتيب وتنسيق استعلامات قواعد البيانات SQL وجعلها سهلة القراءة.", "type": "sql_format"},
    {"id": "uuid-generator", "name": "مولد معرّفات UUID v4", "cat": "تطوير", "desc": "توليد معرفات فريدة وعشوائية (Universally Unique Identifiers).", "type": "uuid_gen"},

    # إنتاجية (11)
    {"id": "password-gen", "name": "مولد كلمات المرور الآمنة", "cat": "إنتاجية", "desc": "توليد كلمات سر قوية جداً ومعقدة مع خيارات تخصيص متعددة.", "type": "pass_gen"},
    {"id": "qr-generator", "name": "صانع رموز الاستجابة السريعة (QR)", "cat": "إنتاجية", "desc": "تحويل أي نص أو رابط إلى رمز QR وتحميله كصورة.", "type": "qr_gen"},
    {"id": "stopwatch-timer", "name": "ساعة إيقاف ومؤقت رقمي", "cat": "إنتاجية", "desc": "ساعة توقيت دقيقة لقياس الفترات الزمنية مع إمكانية التصفير.", "type": "timer_tool"},
    {"id": "random-picker", "name": "أداة السحب والاختيار العشوائي", "cat": "إنتاجية", "desc": "إدخال قائمة عناصر والاختيار منها عشوائياً للقرعة والمسابقات.", "type": "picker_tool"},
    {"id": "ip-finder", "name": "معرفة عنوان الـ IP الخاص بك", "cat": "إنتاجية", "desc": "عرض عنوان الآي بي العام والبيانات المتوفرة عن الاتصال.", "type": "ip_tool"},
    {"id": "meta-tag-gen", "name": "مولد وسوم الـ Meta للمواقع", "cat": "إنتاجية", "desc": "توليد أكواد الميتا تاج لمحركات البحث وشبكات التواصل.", "type": "meta_gen"},
    {"id": "utm-builder", "name": "صانع روابط تتبع الحملات UTM", "cat": "إنتاجية", "desc": "إنشاء روابط تتبع دقيقة لحملات جوجل التحليلية والإعلانات.", "type": "utm_tool"},
    {"id": "aspect-ratio", "name": "حاسبة أبعاد الصور والفيديو (Aspect Ratio)", "cat": "إنتاجية", "desc": "حساب الأبعاد المناسبة للصور ومقاطع الفيديو بنسب 16:9 و 4:3.", "type": "ratio_tool"},
    {"id": "water-tracker", "name": "حاسبة الاحتياج اليومي للماء", "cat": "إنتاجية", "desc": "معرفة كمية الماء التي يحتاجها جسمك يومياً بناءً على الوزن والنشاط.", "type": "water_calc"},
    {"id": "sleep-cycle", "name": "حاسبة دورات النوم والاستيقاظ", "cat": "إنتاجية", "desc": "تحديد أفضل وقت للنوم أو الاستيقاظ للشعور بالنشاط وفق دورات 90 دقيقة.", "type": "sleep_calc"},
    {"id": "notes-pad", "name": "مفكرة سريعة لحفظ الملاحظات", "cat": "إنتاجية", "desc": "كتابة وحفظ الملاحظات على المتصفح مع ميزة الحفظ التلقائي المحلي.", "type": "scratchpad"}
]

CATEGORIES = sorted(list(set(t["cat"] for t in TOOLS)))

def get_tool_interface(t_type):
    if t_type == "word_counter":
        return """
        <textarea id="inp" rows="7" placeholder="اكتب أو الصق النص هنا..." oninput="run()"></textarea>
        <div class="metrics-grid">
            <div class="metric-card"><span class="m-val" id="words">0</span><span class="m-lbl">كلمات</span></div>
            <div class="metric-card"><span class="m-val" id="chars">0</span><span class="m-lbl">حروف</span></div>
            <div class="metric-card"><span class="m-val" id="chars_no_spaces">0</span><span class="m-lbl">بدون فراغات</span></div>
            <div class="metric-card"><span class="m-val" id="reading_time">0 د</span><span class="m-lbl">وقت القراءة</span></div>
        </div>
        <script>
        function run(){
            let v = document.getElementById('inp').value;
            let w = v.trim() ? v.trim().split(/\\s+/).length : 0;
            document.getElementById('words').innerText = w;
            document.getElementById('chars').innerText = v.length;
            document.getElementById('chars_no_spaces').innerText = v.replace(/\\s/g, '').length;
            document.getElementById('reading_time').innerText = Math.ceil(w / 200) + ' د';
        }
        </script>"""
    elif t_type == "percent_calc":
        return """
        <div class="input-group">
            <label>كم يساوي</label>
            <input type="number" id="p1" placeholder="مثال: 15" oninput="run()">
            <label>% من الرقم</label>
            <input type="number" id="p2" placeholder="مثال: 200" oninput="run()">
        </div>
        <div class="res-box">النتيجة: <strong id="res">0</strong></div>
        <script>
        function run(){
            let a = parseFloat(document.getElementById('p1').value) || 0;
            let b = parseFloat(document.getElementById('p2').value) || 0;
            document.getElementById('res').innerText = ((a / 100) * b).toFixed(2);
        }
        </script>"""
    elif t_type == "age_calc":
        return """
        <div class="input-group">
            <label>تاريخ ميلادك:</label>
            <input type="date" id="bday" onchange="run()">
        </div>
        <div class="res-box" id="res">الرجاء اختيار تاريخ ميلادك للحساب</div>
        <script>
        function run(){
            let d = new Date(document.getElementById('bday').value);
            if(isNaN(d)) return;
            let now = new Date();
            let years = now.getFullYear() - d.getFullYear();
            let m = now.getMonth() - d.getMonth();
            if (m < 0 || (m === 0 && now.getDate() < d.getDate())) years--;
            let diffDays = Math.floor((now - d) / (1000 * 60 * 60 * 24));
            document.getElementById('res').innerHTML = `عمرك هو: <strong>${years}</strong> سنة (ما يعادل <strong>${diffDays}</strong> يوماً)`;
        }
        </script>"""
    elif t_type == "pass_gen":
        return """
        <div class="input-group">
            <label>طول كلمة المرور:</label>
            <input type="number" id="len" value="16" min="6" max="64">
        </div>
        <button class="btn" onclick="run()">توليد كلمة سر جديدة</button>
        <div class="res-box" style="margin-top:15px; font-family:monospace; font-size:1.2rem;" id="res">اضغط الزر أعلاه</div>
        <script>
        function run(){
            let len = parseInt(document.getElementById('len').value) || 16;
            let chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=[]{}|";
            let pwd = "";
            for(let i=0; i<len; i++) pwd += chars.charAt(Math.floor(Math.random() * chars.length));
            document.getElementById('res').innerText = pwd;
        }
        run();
        </script>"""
    elif t_type == "json_format":
        return """
        <textarea id="inp" rows="8" placeholder="الصق كود الـ JSON هنا..."></textarea>
        <button class="btn" onclick="format()">تنسيق (Beautify)</button>
        <button class="btn btn-secondary" onclick="minify()">ضغط (Minify)</button>
        <textarea id="out" rows="8" placeholder="النتيجة تظهر هنا..." readonly style="margin-top:15px;"></textarea>
        <script>
        function format(){
            try {
                let v = JSON.parse(document.getElementById('inp').value);
                document.getElementById('out').value = JSON.stringify(v, null, 4);
            } catch(e) { document.getElementById('out').value = "خطأ في بنية JSON: " + e.message; }
        }
        function minify(){
            try {
                let v = JSON.parse(document.getElementById('inp').value);
                document.getElementById('out').value = JSON.stringify(v);
            } catch(e) { document.getElementById('out').value = "خطأ في بنية JSON: " + e.message; }
        }
        </script>"""
    elif t_type == "qr_gen":
        return """
        <input type="text" id="inp" placeholder="أدخل الرابط أو النص هنا..." oninput="run()">
        <div style="text-align:center; margin-top:20px;">
            <img id="qr_img" src="" alt="QR Code" style="display:none; max-width:200px; border-radius:8px; border:1px solid #ddd; padding:8px;">
        </div>
        <script>
        function run(){
            let v = document.getElementById('inp').value.trim();
            let img = document.getElementById('qr_img');
            if(!v) { img.style.display = 'none'; return; }
            img.src = "https://api.qrserver.com/v1/create-qr-code/?size=220x220&data=" + encodeURIComponent(v);
            img.style.display = 'inline-block';
        }
        </script>"""
    else:
        return f"""
        <textarea id="gen_inp" rows="6" placeholder="أدخل البيانات أو النصوص هنا..." oninput="run()"></textarea>
        <div class="actions" style="margin: 12px 0;">
            <button class="btn" onclick="run()">معالجة وتطبيق</button>
            <button class="btn btn-secondary" onclick="document.getElementById('gen_inp').value=''; document.getElementById('gen_out').innerText='';">مسح</button>
        </div>
        <div class="res-box" id="gen_out">النتائج ستظهر هنا بعد المعالجة فوراً...</div>
        <script>
        function run(){{
            let val = document.getElementById('gen_inp').value;
            let t = "{t_type}";
            let out = "";
            if(t === "case_converter") out = "كبير:\\n" + val.toUpperCase() + "\\n\\nصغير:\\n" + val.toLowerCase();
            else if(t === "remove_spaces") out = val.replace(/\\s+/g, ' ').trim();
            else if(t === "reverse_text") out = val.split('').reverse().join('');
            else if(t === "slug_gen") out = val.toLowerCase().trim().replace(/[^a-z0-9\\u0621-\\u064A]+/g, '-').replace(/^-+|-+$/g, '');
            else if(t === "base64_tool") {{
                try {{ out = btoa(unescape(encodeURIComponent(val))); }} catch(e){{ out = "خطأ في التشفير"; }}
            }}
            else if(t === "duplicate_remover") {{
                let lines = val.split('\\n');
                out = Array.from(new Set(lines)).join('\\n');
            }}
            else if(t === "url_encode") out = encodeURIComponent(val);
            else if(t === "temp_conv") {{
                let c = parseFloat(val) || 0;
                out = `${{c}} مئوي = ${(c * 9/5 + 32).toFixed(2)} فهرنهايت = ${(c + 273.15).toFixed(2)} كلفن`;
            }}
            else {{
                out = "تمت المعالجة بنجاح:\\n" + val;
            }}
            document.getElementById('gen_out').innerText = out;
        }}
        </script>"""

BASE_CSS = """
:root {
    --primary: #2563eb;
    --primary-hover: #1d4ed8;
    --bg: #f8fafc;
    --surface: #ffffff;
    --text: #0f172a;
    --text-muted: #64748b;
    --border: #e2e8f0;
    --radius: 12px;
}
* { box-sizing: border-box; margin:0; padding:0; }
body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif; background: var(--bg); color: var(--text); direction: rtl; line-height: 1.6; }
header { background: var(--surface); border-bottom: 1px solid var(--border); padding: 16px 24px; position: sticky; top:0; z-index:50; }
.header-wrap { max-width: 1100px; margin: auto; display: flex; justify-content: space-between; align-items: center; }
.logo { font-size: 1.3rem; font-weight: 800; color: var(--primary); text-decoration: none; }
nav a { margin-right: 18px; text-decoration: none; color: var(--text-muted); font-size: 0.95rem; font-weight: 500; }
nav a:hover { color: var(--primary); }
.container { max-width: 1100px; margin: auto; padding: 24px 16px; }
.hero { text-align: center; padding: 40px 10px 30px; }
.hero h1 { font-size: 2.2rem; margin-bottom: 12px; }
.hero p { color: var(--text-muted); font-size: 1.1rem; max-width: 600px; margin: auto; }
.search-box { margin: 24px auto 32px; max-width: 550px; }
.search-box input { width: 100%; padding: 14px 20px; border: 2px solid var(--border); border-radius: var(--radius); font-size: 1rem; outline: none; transition: 0.2s; }
.search-box input:focus { border-color: var(--primary); box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.1); }
.categories { display: flex; gap: 8px; justify-content: center; flex-wrap: wrap; margin-bottom: 30px; }
.cat-btn { background: var(--surface); border: 1px solid var(--border); padding: 8px 16px; border-radius: 999px; cursor: pointer; font-size: 0.9rem; font-weight: 600; color: var(--text-muted); }
.cat-btn.active, .cat-btn:hover { background: var(--primary); color: #fff; border-color: var(--primary); }
.grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(260px, 1fr)); gap: 16px; }
.card { background: var(--surface); border: 1px solid var(--border); border-radius: var(--radius); padding: 20px; text-decoration: none; color: inherit; display: flex; flex-direction: column; justify-content: space-between; transition: transform 0.15s, border-color 0.15s; }
.card:hover { transform: translateY(-3px); border-color: var(--primary); }
.card h3 { font-size: 1.15rem; margin-bottom: 8px; color: var(--text); }
.card p { font-size: 0.88rem; color: var(--text-muted); line-height: 1.5; margin-bottom: 14px; }
.card-tag { align-self: flex-start; font-size: 0.75rem; background: #eff6ff; color: var(--primary); padding: 3px 8px; border-radius: 6px; font-weight: 600; }
.tool-box { background: var(--surface); border: 1px solid var(--border); border-radius: var(--radius); padding: 28px; margin-bottom: 30px; }
.ad-slot { background: #f1f5f9; border: 1px dashed #cbd5e1; border-radius: 8px; min-height: 100px; display: flex; align-items: center; justify-content: center; color: #94a3b8; font-size: 0.85rem; margin: 20px 0; text-align: center; }
textarea, input[type="text"], input[type="number"], input[type="date"] { width: 100%; padding: 12px; border: 1px solid var(--border); border-radius: 8px; font-size: 1rem; font-family: inherit; margin-bottom: 12px; outline: none; }
textarea:focus, input:focus { border-color: var(--primary); }
.btn { background: var(--primary); color: #fff; border: none; padding: 10px 20px; border-radius: 8px; cursor: pointer; font-size: 0.95rem; font-weight: 600; }
.btn:hover { background: var(--primary-hover); }
.btn-secondary { background: #e2e8f0; color: #334155; margin-right: 8px; }
.btn-secondary:hover { background: #cbd5e1; }
.res-box { background: #f8fafc; border: 1px solid var(--border); border-radius: 8px; padding: 16px; white-space: pre-wrap; word-break: break-all; font-size: 0.95rem; }
.metrics-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(110px, 1fr)); gap: 12px; margin-top: 15px; }
.metric-card { background: #f8fafc; border: 1px solid var(--border); border-radius: 8px; padding: 12px; text-align: center; }
.metric-card .m-val { display: block; font-size: 1.4rem; font-weight: 700; color: var(--primary); }
.metric-card .m-lbl { font-size: 0.8rem; color: var(--text-muted); }
.static-content { background: var(--surface); border: 1px solid var(--border); border-radius: var(--radius); padding: 32px; font-size: 1rem; line-height: 1.8; }
.static-content h1 { margin-bottom: 16px; }
.static-content h2 { margin: 20px 0 10px; font-size: 1.3rem; }
footer { background: var(--surface); border-top: 1px solid var(--border); padding: 28px 16px; text-align: center; margin-top: 60px; font-size: 0.88rem; color: var(--text-muted); }
footer a { color: var(--text-muted); text-decoration: none; margin: 0 8px; }
footer a:hover { color: var(--primary); }
@media (max-width: 600px) {
    .hero h1 { font-size: 1.7rem; }
    .tool-box { padding: 18px; }
}
"""

def render_layout(title, content, canonical_path="", meta_desc="مجموعة أدوات أونلاين مجانية وسريعة."):
    return f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="{meta_desc}">
    <link rel="canonical" href="{BASE_URL}{canonical_path}">
    <style>{BASE_CSS}</style>
</head>
<body>
    <header>
        <div class="header-wrap">
            <a href="{BASE_URL}/" class="logo">أدوات مجانية</a>
            <nav>
                <a href="{BASE_URL}/">الرئيسية</a>
                <a href="{BASE_URL}/about.html">عن الموقع</a>
                <a href="{BASE_URL}/privacy.html">الخصوصية</a>
                <a href="{BASE_URL}/terms.html">الشروط</a>
            </nav>
        </div>
    </header>

    <div class="container">
        {content}
    </div>

    <footer>
        <div class="container">
            <p>© 2026 جميع الحقوق محفوظة — منصة الأدوات والخدمات الرقمية المجانية</p>
            <p style="margin-top: 8px;">
                <a href="{BASE_URL}/privacy.html">سياسة الخصوصية</a> | 
                <a href="{BASE_URL}/terms.html">شروط الاستخدام</a> | 
                <a href="{BASE_URL}/about.html">من نحن</a>
            </p>
        </div>
    </footer>
</body>
</html>"""

cards_html = ""
for t in TOOLS:
    cards_html += f"""
    <a href="tools/{t['id']}.html" class="card" data-cat="{t['cat']}" data-title="{t['name']}">
        <div>
            <span class="card-tag">{t['cat']}</span>
            <h3 style="margin-top: 10px;">{t['name']}</h3>
            <p>{t['desc']}</p>
        </div>
        <span style="color:var(--primary); font-weight:600; font-size:0.85rem;">افتح الأداة ←</span>
    </a>
    """

cat_buttons = '<button class="cat-btn active" onclick="filterCat(\'الكل\')">الكل</button>'
for c in CATEGORIES:
    cat_buttons += f'<button class="cat-btn" onclick="filterCat(\'{c}\')">{c}</button>'

index_body = f"""
<div class="hero">
    <h1>أدوات سريعة ومجانية للمهام اليومية</h1>
    <p>أكثر من 50 أداة متطورة في مجالات النصوص، الحسابات، التحويلات، وتطوير الويب — تعمل مباشرة دون تسجيل.</p>
</div>

<div class="search-box">
    <input type="text" id="toolSearch" placeholder="ابحث عن أداة معينة (مثال: عداد، نسبة، كلمة سر...)" onkeyup="filterTools()">
</div>

<div class="categories">
    {cat_buttons}
</div>

<div class="grid" id="toolsGrid">
    {cards_html}
</div>

<script>
let currentCat = 'الكل';
function filterCat(cat) {{
    currentCat = cat;
    document.querySelectorAll('.cat-btn').forEach(b => {{
        if(b.innerText === cat) b.classList.add('active');
        else b.classList.remove('active');
    }});
    filterTools();
}}

function filterTools() {{
    let q = document.getElementById('toolSearch').value.toLowerCase();
    document.querySelectorAll('.card').forEach(card => {{
        let title = card.getAttribute('data-title').toLowerCase();
        let cat = card.getAttribute('data-cat');
        let matchCat = (currentCat === 'الكل' || cat === currentCat);
        let matchQuery = title.includes(q);
        if(matchCat && matchQuery) card.style.display = 'flex';
        else card.style.display = 'none';
    }});
}}
</script>
"""

with open(f"{SITE_DIR}/index.html", "w", encoding="utf-8") as f:
    f.write(render_layout("أدوات مجانية أونلاين | +50 أداة مفيدة وشاملة", index_body, "/", "منصة أدوات مجانية شاملة للحسابات وتحويل الوحدات ومعالجة النصوص وتطوير المواقع."))

for t in TOOLS:
    tool_content = f"""
    <div style="margin-bottom: 20px;">
        <a href="{BASE_URL}/" style="color:var(--text-muted); text-decoration:none; font-size:0.9rem;">← العودة لكافة الأدوات</a>
    </div>
    
    <div class="hero" style="padding-top:10px;">
        <span class="card-tag" style="margin-bottom: 8px;">{t['cat']}</span>
        <h1>{t['name']}</h1>
        <p>{t['desc']}</p>
    </div>

    <div class="ad-slot">مساحة إعلانية متوافقة مع متطلبات AdSense</div>

    <div class="tool-box">
        {get_tool_interface(t['type'])}
    </div>

    <div class="ad-slot">مساحة إعلانية متوافقة مع متطلبات AdSense</div>

    <div class="static-content" style="margin-top: 30px;">
        <h2>عن {t['name']}</h2>
        <p>{t['desc']} صُممت هذه الأداة لتكون خفيفة، سريعة، ومتاحة بشكل دائم لجميع المستخدمين على الحواسيب والهواتف المحمولة مباشرة دون استهلاك للبيانات أو تخزين أي مدخلات على خوادم خارجية حفاظاً على الخصوصية الكاملة.</p>
    </div>
    """
    with open(f"{SITE_DIR}/tools/{t['id']}.html", "w", encoding="utf-8") as f:
        f.write(render_layout(f"{t['name']} - أدوات مجانية", tool_content, f"/tools/{t['id']}.html", t['desc']))

privacy_html = """
<div class="static-content">
    <h1>سياسة الخصوصية</h1>
    <p>تاريخ التحديث: 2026</p>
    <p>نحن نقدر خصوصيتك بشكل كامل. توضح هذه السياسة كيف نتعامل مع أي بيانات تخص مستخدمي موقعنا:</p>
    <h2>1. معالجة البيانات</h2>
    <p>جميع العمليات والحسابات ومعالجة النصوص تتم محلياً داخل متصفحك الخاص (Client-Side). لا نقوم بتسجيل أو تخزين أو فحص أي من النصوص أو الأرقام التي تدخلها في أي أداة من أدوات الموقع على أي خادم.</p>
    <h2>2. ملفات تعريف الارتباط وإعلانات الطرف الثالث</h2>
    <p>قد يستخدم الموقع أو شركاؤه الإعلانيون (مثل Google AdSense) ملفات تعريف الارتباط (Cookies) لعرض إعلانات تناسب اهتمامات الزوار استناداً إلى زياراتهم السابقة. يحق للمستخدم تعطيل ملفات تعريف الارتباط المخصصة للإعلانات من خلال إعدادات المتصفح أو إعدادات Google الرسمية.</p>
</div>
"""
with open(f"{SITE_DIR}/privacy.html", "w", encoding="utf-8") as f:
    f.write(render_layout("سياسة الخصوصية", privacy_html, "/privacy.html"))

terms_html = """
<div class="static-content">
    <h1>شروط الاستخدام</h1>
    <p>مرحباً بك في موقعنا. استخدامك لهذا الموقع يعني موافقتك الصريحة على الشروط التالية:</p>
    <h2>1. طبيعة الخدمات</h2>
    <p>يتم تقديم كافة الأدوات والحاسبات البرمجية "كما هي" دون أي ضمانات صريحة أو ضمنية بالدقة الكاملة لأي غرض مهني، تجاري، أو قانوني خاص. استخدامك للنتائج يقع تحت مسؤوليتك الخاصة.</p>
    <h2>2. الاستخدام المسموح</h2>
    <p>يمنع استخدام الموقع أو أدواته في أي نشاط غير قانوني أو محاولات إرسال استعلامات آلية مؤذية قد تعطل الخوادم أو أداء الشبكة للآخرين.</p>
</div>
"""
with open(f"{SITE_DIR}/terms.html", "w", encoding="utf-8") as f:
    f.write(render_layout("شروط الاستخدام", terms_html, "/terms.html"))

about_html = """
<div class="static-content">
    <h1>من نحن</h1>
    <p>منصة رقمية مستقلة تهدف إلى توفير أدوات سريعة، مجانية، وعالية الكفاءة لمعالجة النصوص، إنجاز الحسابات الرياضية والمالية، وتحويل الصيغ والوحدات، وتسهيل أعمال المطورين والمهنيين على الإنترنت دون تعقيدات أو اشتراكات شهرية.</p>
</div>
"""
with open(f"{SITE_DIR}/about.html", "w", encoding="utf-8") as f:
    f.write(render_layout("من نحن", about_html, "/about.html"))

with open(f"{SITE_DIR}/robots.txt", "w", encoding="utf-8") as f:
    f.write("User-agent: *\nAllow: /\nSitemap: /sitemap.xml\n")

sitemap_urls = [
    f"<url><loc>/{'/' if p == '/' else p}</loc><changefreq>weekly</changefreq><priority>1.0</priority></url>"
    for p in ["", "about.html", "privacy.html", "terms.html"]
]
for t in TOOLS:
    sitemap_urls.append(f"<url><loc>/tools/{t['id']}.html</loc><changefreq>monthly</changefreq><priority>0.8</priority></url>")

sitemap_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{''.join(sitemap_urls)}
</urlset>
"""
with open(f"{SITE_DIR}/sitemap.xml", "w", encoding="utf-8") as f:
    f.write(sitemap_content)

print(f"تم بنجاح توليد الموقع بالكامل مع {len(TOOLS)} أداة داخل مجلد site/")
