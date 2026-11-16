import streamlit as st

# إعدادات الصفحة: الوضع العريض وإغلاق القائمة الجانبية تلقائياً لتناسب الوضع الأفقي للجهاز اللوحي
st.set_page_config(
    page_title="Periodic Energy Table | Dr. Khalid Abdelfattah M. Osman",
    page_icon="⚛️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# تنسيق CSS متجاوب للوضع الأفقي والأجهزة اللوحية
st.markdown("""
<style>
    .block-container { padding-top: 1rem; padding-bottom: 1rem; max-width: 98%; }
    .main-header { 
        text-align: center; padding: 12px; background: linear-gradient(135deg, #f0f4f8 0%, #d9e2ec 100%); 
        border-radius: 10px; margin-bottom: 12px; border-bottom: 3px solid #1a365d;
    }
    .main-header h2 { margin: 0; color: #102a43; font-size: 1.45rem; }
    .main-header p { margin: 3px 0; color: #334e68; font-size: 0.85rem; }
    
    .matrix-table { 
        width: 100%; border-collapse: collapse; text-align: center; 
        font-size: 10.5px; font-family: 'Segoe UI', Tahoma, sans-serif; table-layout: fixed;
    }
    .matrix-table th, .matrix-table td { 
        border: 1px solid #222; padding: 2px 1px; overflow: hidden; text-overflow: ellipsis;
    }
    .shell-col { background-color: #d9e2ec; font-weight: bold; width: 62px !important; color: #102a43; }
    .iupac-row { background-color: #f0f4f8; font-weight: bold; color: #243b53; font-size: 10px; }
    .grp-row { background-color: #e6fffa; font-weight: bold; color: #234e52; font-size: 10px; }
    
    .s-block { background-color: #70ad47; color: #000; }
    .p-block { background-color: #8ea9db; color: #000; }
    .d-block { background-color: #ffff00; color: #000; }
    .f-block { background-color: #f4b084; color: #000; }
    .g-block { background-color: #d9d9d9; color: #000; }
    
    .el-137 { background-color: #e53e3e !important; color: #fff !important; font-weight: bold; }
    .highlight-cell { 
        outline: 2.5px solid #102a43; box-shadow: 0 0 8px rgba(16, 42, 67, 0.8); 
        transform: scale(1.06); font-weight: bold; z-index: 10; position: relative;
    }
    .dim-cell { opacity: 0.22; }
    .e-badge { 
        font-size: 8.5px; background: rgba(255,255,255,0.75); border-radius: 2px; 
        padding: 0 2px; display: inline-block; margin-top: 1px; color: #000; font-weight: 600;
    }
    .el-137 .e-badge { background: rgba(0,0,0,0.4); color: #fff; }
    
    .aufbau-box {
        background-color: #fffbeb; border: 1px solid #f59e0b; border-radius: 8px;
        padding: 8px 12px; margin-bottom: 10px; font-size: 0.85rem; color: #78350f;
    }
</style>
""", unsafe_allow_html=True)

# الترويسة الأكاديمية
st.markdown("""
<div class="main-header">
    <h2>⚛️ Periodic Energy Table of Chemical Elements (جدول الطاقة الدوري للعناصر الكيميائية)</h2>
    <p><strong>By: Dr. Khalid Abdelfattah M. Osman</strong> | Merowe Institute of Technology, Merowe University of Technology, Sudan</p>
    <p><em>Matrix-Based Quantum Mechanics & Madelung (n + ℓ) Rule Pedagogical Model</em></p>
</div>
""", unsafe_allow_html=True)

# شريط تحكم سريع أفقي مدمج أعلى الجدول لسهولة الاستخدام على الجهاز اللوحي
col1, col2, col3, col4 = st.columns([2.2, 2.2, 2.2, 1.4])

with col1:
    view_mode = st.selectbox(
        "👁️ وضع العرض (Display Mode):",
        ["العناصر + قيم الطاقة (Elements + E)", "مصفوفة الطاقة فقط (FIG. 1: n + ℓ Only)"]
    )

with col2:
    selected_energy = st.selectbox(
        "⚡ تظليل مستوى الطاقة (Highlight n + ℓ):",
        ["عرض جميع المستويات (All)", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    )

with col3:
    search_query = st.text_input("🔍 ابحث برمز العنصر أو العدد الذري (مثلاً: Fe أو 26 أو 137):", "").strip().lower()

with col4:
    st.markdown("<div style='height: 28px;'></div>", unsafe_allow_html=True)
    try:
        with open("paper.pdf", "rb") as pdf_file:
            st.download_button(
                label="📄 الورقة البحثية (PDF)",
                data=pdf_file,
                file_name="Periodic_Energy_Table_Dr_Khalid_Osman.pdf",
                mime="application/pdf",
                use_container_width=True
            )
    except FileNotFoundError:
        st.caption("📁 أضف `paper.pdf` للمستودع")

# شريط توضيحي ديناميكي عند اختيار مستوى طاقة معين
energy_explanations = {
    1: "المستوى الطاقي E = 1: يشمل المدار 1s فقط (الهيدروجين 1H والهيليوم 2He).",
    2: "المستوى الطاقي E = 2: يشمل المدار 2s فقط (الليثيوم 3Li والبريليوم 4Be).",
    3: "المستوى الطاقي E = 3: يتساوى فيه المداران 2p (n=2, ℓ=1) و 3s (n=3, ℓ=0) في الطاقة!",
    4: "المستوى الطاقي E = 4: يتساوى فيه المداران 3p (n=3, ℓ=1) و 4s (n=4, ℓ=0) في الطاقة!",
    5: "المستوى الطاقي E = 5: تداخل ثلاثي بين المدارات 3d (3+2) و 4p (4+1) و 5s (5+0).",
    6: "المستوى الطاقي E = 6: تداخل ثلاثي بين المدارات 4d (4+2) و 5p (5+1) و 6s (6+0).",
    7: "المستوى الطاقي E = 7: تداخل رباعي يشمل 4f (4+3) و 5d (5+2) و 6p (6+1) و 7s (7+0).",
    8: "المستوى الطاقي E = 8: تداخل رباعي يشمل 5f (5+3) و 6d (6+2) و 7p (7+1) و 8s (8+0) للعناصر فائقة الثقل.",
    9: "المستوى الطاقي E = 9: يظهر هنا مدار الفئة الجديدة 5g (n=5, ℓ=4) للعناصر الافتراضية (121-137) متساوياً مع 6f و 7d و 8p.",
    10: "المستوى الطاقي E = 10: يمثل مستويات الطاقة العليا في الغلاف السابع (7f) وما بعده."
}

if selected_energy != "عرض جميع المستويات (All)":
    st.markdown(f"<div class='aufbau-box'>💡 <strong>التفسير الكمي:</strong> {energy_explanations[selected_energy]}</div>", unsafe_allow_html=True)

# تعريف الأعمدة والمدارات
orbitals = [
    ('s', '0', 'S-Block', 's-block'),
    ('p1', '1', 'P-Block', 'p-block'), ('p2', '1', 'P-Block', 'p-block'), ('p3', '1', 'P-Block', 'p-block'),
    ('d1', '2', 'D-Block', 'd-block'), ('d2', '2', 'D-Block', 'd-block'), ('d3', '2', 'D-Block', 'd-block'), ('d4', '2', 'D-Block', 'd-block'), ('d5', '2', 'D-Block', 'd-block'),
    ('f1', '3', 'F-Block', 'f-block'), ('f2', '3', 'F-Block', 'f-block'), ('f3', '3', 'F-Block', 'f-block'), ('f4', '3', 'F-Block', 'f-block'), ('f5', '3', 'F-Block', 'f-block'), ('f6', '3', 'F-Block', 'f-block'), ('f7', '3', 'F-Block', 'f-block'),
    ('g1', '4', 'G-Block', 'g-block'), ('g2', '4', 'G-Block', 'g-block'), ('g3', '4', 'G-Block', 'g-block'), ('g4', '4', 'G-Block', 'g-block'), ('g5', '4', 'G-Block', 'g-block'), ('g6', '4', 'G-Block', 'g-block'), ('g7', '4', 'G-Block', 'g-block'), ('g8', '4', 'G-Block', 'g-block'), ('g9', '4', 'G-Block', 'g-block')
]

top_half = [
    ("8", [('119', 8), ('', 9), ('', 9), ('', 9)]),
    ("7", [('87 Fr', 7), ('113 Nh', 8), ('114 Fl', 8), ('115 Mc', 8), ('', 9), ('', 9), ('', 9), ('', 8), ('', 9), ('', 10), ('', 10), ('', 10), ('', 10), ('', 10), ('', 10), ('', 10)]),
    ("6", [('55 Cs', 6), ('81 Tl', 7), ('82 Pb', 7), ('83 Bi', 7), ('103 Lr', 6), ('104 Rf', 8), ('105 Db', 8), ('106 Sg', 8), ('107 Bh', 6), ('', 9), ('', 9), ('', 9), ('', 9), ('', 9), ('', 9), ('', 9)]),
    ("5", [('37 Rb', 5), ('49 In', 5), ('50 Sn', 6), ('51 Sb', 6), ('71 Lu', 7), ('72 Hf', 7), ('73 Ta', 7), ('74 W', 7), ('75 Re', 7), ('89 Ac', 8), ('90 Th', 8), ('91 Pa', 8), ('92 U', 8), ('93 Np', 8), ('94 Pu', 8), ('95 Am', 8), ('121', 9), ('122', 9), ('123', 9), ('124', 9), ('125', 9), ('126', 9), ('127', 9), ('128', 9), ('129', 9)]),
    ("4", [('19 K', 4), ('31 Ga', 5), ('32 Ge', 5), ('33 As', 5), ('39 Y', 6), ('40 Zr', 6), ('41 Nb', 6), ('42 Mo', 6), ('43 Tc', 6), ('57 La', 7), ('58 Ce', 7), ('59 Pr', 7), ('60 Nd', 7), ('61 Pm', 7), ('62 Sm', 7), ('63 Eu', 7)]),
    ("3", [('11 Na', 3), ('13 Al', 4), ('14 Si', 4), ('15 P', 4), ('21 Sc', 5), ('22 Ti', 5), ('23 V', 5), ('24 Cr', 5), ('25 Mn', 5)]),
    ("2", [('3 Li', 2), ('5 B', 3), ('6 C', 3), ('7 N', 3)]),
    ("1", [('1 H', 1)])
]

bottom_half = [
    ("1'", [('2 He', 1)]),
    ("2'", [('4 Be', 2), ('8 O', 3), ('9 F', 3), ('10 Ne', 3)]),
    ("3'", [('12 Mg', 3), ('16 S', 4), ('17 Cl', 4), ('18 Ar', 4), ('26 Fe', 5), ('27 Co', 5), ('28 Ni', 5), ('29 Cu', 5), ('30 Zn', 5)]),
    ("4'", [('20 Ca', 4), ('34 Se', 5), ('35 Br', 5), ('36 Kr', 5), ('44 Ru', 6), ('45 Rh', 6), ('46 Pd', 8), ('47 Ag', 6), ('48 Cd', 6), ('64 Gd', 7), ('65 Tb', 7), ('66 Dy', 7), ('67 Ho', 7), ('68 Er', 7), ('69 Tm', 7), ('70 Yb', 7)]),
    ("5'", [('38 Sr', 5), ('52 Te', 6), ('53 I', 6), ('54 Xe', 6), ('76 Os', 7), ('77 Ir', 7), ('78 Pt', 7), ('79 Au', 7), ('80 Hg', 7), ('96 Cm', 8), ('97 Bk', 8), ('98 Cf', 8), ('99 Es', 8), ('100 Fm', 8), ('101 Md', 8), ('102 No', 8), ('130', 9), ('131', 9), ('132', 9), ('133', 9), ('134', 9), ('135', 9), ('136', 9), ('137', 9)]),
    ("6'", [('56 Ba', 6), ('84 Po', 7), ('85 At', 7), ('86 Rn', 7), ('108 Hs', 8), ('109 Mt', 8), ('110 Ds', 8), ('111 Rg', 8), ('112 Cn', 8), ('', 9), ('', 9), ('', 9), ('', 9), ('', 9), ('', 9), ('', 9)]),
    ("7'", [('88 Ra', 7), ('116 Lv', 8), ('117 Ts', 8), ('118 Og', 8), ('', 9), ('', 9), ('', 9), ('', 5), ('', 5), ('', 10), ('', 10), ('', 10), ('', 10), ('', 10), ('', 10), ('', 10)]),
    ("8'", [('120', 8), ('', 9), ('', 9), ('', 9)])
]

def build_full_matrix():
    html = '<table class="matrix-table">'
    
    # 1. صف العدد الكمي الثانوي (ℓ)
    html += '<tr><th class="shell-col">Azimuthal (ℓ)</th>'
    for _, l_val, _, _ in orbitals:
        html += f'<th class="iupac-row">ℓ={l_val}</th>'
    html += '</tr>'

    # 2. صف أسماء المدارات
    html += '<tr><th class="shell-col">Shell / Orbital</th>'
    for orb_name, _, _, _ in orbitals:
        html += f'<th class="shell-col">{orb_name}</th>'
    html += '</tr>'

    # 3. صف IUPAC العلوي
    html += '<tr><td style="border:none;"></td><td colspan="16" class="iupac-row">Groups Numbers according to IUPAC version 4 May 2022</td><td colspan="9" style="border:none;"></td></tr>'
    
    top_groups = ['1', '13', '14', '15', '3', '4', '5', '6', '7', '19', '20', '21', '22', '23', '24', '25']
    html += '<tr><td style="border:none;"></td>' + ''.join([f'<td class="grp-row">{g}</td>' for g in top_groups]) + '<td colspan="9" style="border:none;"></td></tr>'

    # دالة بناء الصفوف
    def render_section(rows):
        sec_html = ''
        for shell, cells in rows:
