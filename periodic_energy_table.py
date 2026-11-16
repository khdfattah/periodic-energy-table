import streamlit as st
import pandas as pd

# إعدادات الصفحة
st.set_page_config(
    page_title="Periodic Energy Table | Dr. Khalid Abdelfattah M. Osman",
    page_icon="⚛️",
    layout="wide"
)

# تنسيق CSS مخصص للألوان والمصفوفة
st.markdown("""
<style>
    .main-header { text-align: center; padding: 15px; background-color: #f0f4f8; border-radius: 10px; margin-bottom: 20px; }
    .matrix-table { width: 100%; border-collapse: collapse; text-align: center; font-size: 12px; font-family: sans-serif; }
    .matrix-table th, .matrix-table td { border: 1px solid #333; padding: 4px 2px; min-width: 38px; }
    .shell-col { background-color: #e2e8f0; font-weight: bold; }
    .s-block { background-color: #70ad47; color: #000; }
    .p-block { background-color: #8ea9db; color: #000; }
    .d-block { background-color: #ffff00; color: #000; }
    .f-block { background-color: #f4b084; color: #000; }
    .g-block { background-color: #d9d9d9; color: #000; }
    .el-137 { background-color: #e53e3e !important; color: #fff !important; font-weight: bold; }
    .highlight-cell { outline: 3px solid #1a365d; box-shadow: 0 0 10px #1a365d; transform: scale(1.05); font-weight: bold; }
    .dim-cell { opacity: 0.25; }
    .e-badge { font-size: 10px; background: rgba(255,255,255,0.7); border-radius: 3px; padding: 0 2px; display: inline-block; margin-top: 2px; color: #000; }
</style>
""", unsafe_allow_html=True)

# العنوان الأكاديمي
st.markdown("""
<div class="main-header">
    <h2>⚛️ Periodic Energy Table of Chemical Elements</h2>
    <p><strong>By: Dr. Khalid Abdelfattah M. Osman</strong> | Merowe Institute of Technology, Merowe University of Technology, Sudan</p>
    <p><em>An Integrated Quantum Mechanics & Madelung (n + ℓ) Rule Matrix Model</em></p>
</div>
""", unsafe_allow_html=True)

# الشريط الجانبي للتحكم التفاعلي
st.sidebar.header("🎛️ أدوات التحكم التعليمية")

view_mode = st.sidebar.radio(
    "وضع العرض (Display Mode):",
    ["العناصر الكيميائية + قيم الطاقة (Elements + E)", "مصفوفة الطاقة المجردة (FIG. 1: n + ℓ Only)"]
)

selected_energy = st.sidebar.selectbox(
    "تظليل المدارات متساوية الطاقة (Highlight Energy Level n + ℓ):",
    ["عرض الكل (Show All)", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
)

selected_block = st.sidebar.multiselect(
    "تصفية الفئات المدارية (Filter Blocks):",
    ["S-Block", "P-Block", "D-Block", "F-Block", "G-Block"],
    default=["S-Block", "P-Block", "D-Block", "F-Block", "G-Block"]
)

# زر تحميل الورقة البحثية إذا كانت مرفوعة
try:
    with open("paper.pdf", "rb") as pdf_file:
        st.sidebar.download_button(
            label="📄 تحميل الورقة البحثية (PDF)",
            data=pdf_file,
            file_name="Periodic_Energy_Table_Dr_Khalid_Osman.pdf",
            mime="application/pdf"
        )
except FileNotFoundError:
    st.sidebar.info("💡 ارفع ملف الورقة باسم paper.pdf في المستودع لتفعيل زر التحميل.")

# تعريف الأعمدة والبيانات
orbitals = [
    ('s', 'S-Block', 's-block'),
    ('p1', 'P-Block', 'p-block'), ('p2', 'P-Block', 'p-block'), ('p3', 'P-Block', 'p-block'),
    ('d1', 'D-Block', 'd-block'), ('d2', 'D-Block', 'd-block'), ('d3', 'D-Block', 'd-block'), ('d4', 'D-Block', 'd-block'), ('d5', 'D-Block', 'd-block'),
    ('f1', 'F-Block', 'f-block'), ('f2', 'F-Block', 'f-block'), ('f3', 'F-Block', 'f-block'), ('f4', 'F-Block', 'f-block'), ('f5', 'F-Block', 'f-block'), ('f6', 'F-Block', 'f-block'), ('f7', 'F-Block', 'f-block'),
    ('g1', 'G-Block', 'g-block'), ('g2', 'G-Block', 'g-block'), ('g3', 'G-Block', 'g-block'), ('g4', 'G-Block', 'g-block'), ('g5', 'G-Block', 'g-block'), ('g6', 'G-Block', 'g-block'), ('g7', 'G-Block', 'g-block'), ('g8', 'G-Block', 'g-block'), ('g9', 'G-Block', 'g-block')
]

top_half = [
    ("8", [('119', 8), ('', 9), ('', 9), ('', 9)]),
    ("7", [('87 Fr', 7), ('113 Nh', 8), ('114 Fl', 8), ('115 Mc', 8), ('', 9), ('', 9), ('', 9), ('', 9), ('', 9), ('', 10), ('', 10), ('', 10), ('', 10), ('', 10), ('', 10), ('', 10)]),
    ("6", [('55 Cs', 6), ('81 Tl', 7), ('82 Pb', 7), ('83 Bi', 7), ('103 Lr', 8), ('104 Rf', 8), ('105 Db', 8), ('106 Sg', 8), ('107 Bh', 8), ('', 9), ('', 9), ('', 9), ('', 9), ('', 9), ('', 9), ('', 9)]),
    ("5", [('37 Rb', 5), ('49 In', 6), ('50 Sn', 6), ('51 Sb', 6), ('71 Lu', 7), ('72 Hf', 7), ('73 Ta', 7), ('74 W', 7), ('75 Re', 7), ('89 Ac', 8), ('90 Th', 8), ('91 Pa', 8), ('92 U', 8), ('93 Np', 8), ('94 Pu', 8), ('95 Am', 8), ('121', 9), ('122', 9), ('123', 9), ('124', 9), ('125', 9), ('126', 9), ('127', 9), ('128', 9), ('129', 9)]),
    ("4", [('19 K', 4), ('31 Ga', 5), ('32 Ge', 5), ('33 As', 5), ('39 Y', 6), ('40 Zr', 6), ('41 Nb', 6), ('42 Mo', 6), ('43 Tc', 6), ('57 La', 7), ('58 Ce', 7), ('59 Pr', 7), ('60 Nd', 7), ('61 Pm', 7), ('62 Sm', 7), ('63 Eu', 7)]),
    ("3", [('11 Na', 3), ('13 Al', 4), ('14 Si', 4), ('15 P', 4), ('21 Sc', 5), ('22 Ti', 5), ('23 V', 5), ('24 Cr', 5), ('25 Mn', 5)]),
    ("2", [('3 Li', 2), ('5 B', 3), ('6 C', 3), ('7 N', 3)]),
    ("1", [('1 H', 1)])
]

bottom_half = [
    ("1'", [('2 He', 1)]),
    ("2'", [('4 Be', 2), ('8 O', 3), ('9 F', 3), ('10 Ne', 3)]),
    ("3'", [('12 Mg', 3), ('16 S', 4), ('17 Cl', 4), ('18 Ar', 4), ('26 Fe', 5), ('27 Co', 5), ('28 Ni', 5), ('29 Cu', 5), ('30 Zn', 5)]),
    ("4'", [('20 Ca', 4), ('34 Se', 5), ('35 Br', 5), ('36 Kr', 5), ('44 Ru', 6), ('45 Rh', 6), ('46 Pd', 6), ('47 Ag', 6), ('48 Cd', 6), ('64 Gd', 7), ('65 Tb', 7), ('66 Dy', 7), ('67 Ho', 7), ('68 Er', 7), ('69 Tm', 7), ('70 Yb', 7)]),
    ("5'", [('38 Sr', 5), ('52 Te', 6), ('53 I', 6), ('54 Xe', 6), ('76 Os', 7), ('77 Ir', 7), ('78 Pt', 7), ('79 Au', 7), ('80 Hg', 7), ('96 Cm', 8), ('97 Bk', 8), ('98 Cf', 8), ('99 Es', 8), ('100 Fm', 8), ('101 Md', 8), ('102 No', 8), ('130', 9), ('131', 9), ('132', 9), ('133', 9), ('134', 9), ('135', 9), ('136', 9), ('137', 9)]),
    ("6'", [('56 Ba', 6), ('84 Po', 7), ('85 At', 7), ('86 Rn', 7), ('108 Hs', 8), ('109 Mt', 8), ('110 Ds', 8), ('111 Rg', 8), ('112 Cn', 8), ('', 9), ('', 9), ('', 9), ('', 9), ('', 9), ('', 9), ('', 9)]),
    ("7'", [('88 Ra', 7), ('116 Lv', 8), ('117 Ts', 8), ('118 Og', 8), ('', 9), ('', 9), ('', 9), ('', 9), ('', 9), ('', 10), ('', 10), ('', 10), ('', 10), ('', 10), ('', 10), ('', 10)]),
    ("8'", [('120', 8), ('', 9), ('', 9), ('', 9)])
]

def build_html_table():
    html = '<div style="overflow-x:auto;"><table class="matrix-table">'
    # صف المدارات
    html += '<tr><th class="shell-col">Shell/Orbital</th>'
    for orb_name, block_name, _ in orbitals:
        html += f'<th class="shell-col">{orb_name}</th>'
    html += '</tr>'

    # دالة بناء الصفوف
    def render_section(rows):
        sec_html = ''
        for shell, cells in rows:
            sec_html += f'<tr><td class="shell-col">{shell}</td>'
            for i in range(25):
                orb_name, block_name, css_class = orbitals[i]
                if i < len(cells) and block_name in selected_block:
                    sym, energy = cells[i]
                    extra_class = ""
                    if sym == '137' and "FIG. 1" not in view_mode:
                        extra_class += " el-137"
                    if selected_energy != "عرض الكل (Show All)":
                        if energy == selected_energy:
                            extra_class += " highlight-cell"
                        else:
                            extra_class += " dim-cell"
                    
                    if "FIG. 1" in view_mode:
                        content = f"<strong>{energy}</strong>"
                    else:
                        content = f"<div><strong>{sym}</strong></div><div class='e-badge'>E={energy}</div>" if sym else f"<div class='e-badge'>E={energy}</div>"
                    
                    sec_html += f'<td class="{css_class} {extra_class}">{content}</td>'
                else:
                    sec_html += '<td style="border:none;"></td>'
            sec_html += '</tr>'
        return sec_html

    html += render_section(top_half)
    html += '<tr><td colspan="26" style="height:15px; border:none;"></td></tr>'
    html += render_section(bottom_half)
    
    # صف الفئات السفلي
    html += '''
    <tr>
        <th class="shell-col">Blocks</th>
        <th class="s-block">S-Block</th>
        <th colspan="3" class="p-block">P-Block</th>
        <th colspan="5" class="d-block">D-Block</th>
        <th colspan="7" class="f-block">F-Block</th>
        <th colspan="9" class="g-block">G-Block</th>
    </tr>
    '''
    html += '</table></div>'
    return html

st.markdown(build_html_table(), unsafe_allow_html=True)

# قسم الشرح التعليمي أسفل الجدول
with st.expander("📖 شرح النموذج التعليمي وقواعد الاستخدام (Educational Guide)"):
    st.markdown("""
    * **قاعدة مادلونغ ($n + \\ell$):** استخدم القائمة الجانبية لاختيار أي مستوى طاقة (مثلاً $E = 7$ أو $E = 8$) لمشاهدة كيف تتوزع المدارات المتساوية في الطاقة قطرياً عبر الفئات المختلفة.
    * **توسيع الفئة G:** يوضح الجدول المدارات التسعة للفئة $g$ ($g_1$ إلى $g_9$) التي تتسع لـ 18 إلكتروناً، وتستوعب العناصر الافتراضية فائقة الثقل من $Z=121$ حتى $Z=137$.
    * **التبديل بين العرضين:** يمكنك التبديل الفوري بين عرض العناصر الكيميائية مع طاقتها، أو عرض مصفوفة الطاقة المجردة كما وردت في الشكل (FIG. 1) من الورقة البحثية.
    """)
