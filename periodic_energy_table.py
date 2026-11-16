import streamlit as st
import glob

st.set_page_config(
    page_title="Periodic Energy Table | Dr. Khalid Abdelfattah M. Osman",
    page_icon="⚛️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.html("""
<div style="text-align:center; padding:12px; background:#f0f4f8; border-radius:10px; border-bottom:3px solid #1a365d; font-family:sans-serif;">
    <h3 style="margin:0; color:#102a43;">⚛️ Periodic Energy Table of Chemical Elements (جدول الطاقة الدوري للعناصر الكيميائية)</h3>
    <p style="margin:4px 0 0 0; color:#334e68; font-size:0.85rem;"><strong>Dr. Khalid Abdelfattah M. Osman</strong> | Merowe University of Technology, Sudan — Madelung (n + ℓ) Quantum Matrix</p>
</div>
""")

col1, col2, col3, col4 = st.columns([2.2, 2.2, 2.2, 1.4])
with col1:
    view_mode = st.selectbox("👁️ وضع العرض:", ["العناصر + قيم الطاقة (Elements + E)", "مصفوفة الطاقة فقط (FIG. 1: n + ℓ)"])
with col2:
    selected_energy = st.selectbox("⚡ تظليل مستوى الطاقة (n + ℓ):", ["عرض الكل (All)", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
with col3:
    search_query = st.text_input("🔍 بحث (رمز العنصر أو العدد الذري):", "").strip()
with col4:
    st.markdown("<div style='height: 28px;'></div>", unsafe_allow_html=True)
    pdf_files = glob.glob("*.pdf")
    if pdf_files:
        with open(pdf_files[0], "rb") as pdf_file:
            st.download_button("📄 تحميل الورقة PDF", pdf_file, pdf_files[0], "application/pdf", use_container_width=True)

def get_electron_config(z):
    subshells = [("1s",2),("2s",2),("2p",6),("3s",2),("3p",6),("4s",2),("3d",10),("4p",6),("5s",2),("4d",10),("5p",6),("6s",2),("4f",14),("5d",10),("6p",6),("7s",2),("5f",14),("6d",10),("7p",6),("8s",2),("5g",18)]
    rem, cfg = z, []
    for orb, cap in subshells:
        if rem <= 0:
            break
        fill = min(rem, cap)
        cfg.append(f"{orb}<sup>{fill}</sup>")
        rem -= fill
    return " ".join(cfg)

if search_query.isdigit() and 1 <= int(search_query) <= 137:
    st.html(f"<div style='background:#fffbeb; border:1px solid #f59e0b; border-radius:8px; padding:8px 12px; font-family:sans-serif; color:#78350f;'>🧬 <strong>التوزيع الإلكتروني (Z = {search_query}):</strong> {get_electron_config(int(search_query))}</div>")

explanations = {
    1: "E = 1: مدار 1s فقط (1H, 2He).",
    2: "E = 2: مدار 2s فقط (3Li, 4Be).",
    3: "E = 3: تساوي طاقة المدارين 2p (2+1) و 3s (3+0).",
    4: "E = 4: تساوي طاقة المدارين 3p (3+1) و 4s (4+0).",
    5: "E = 5: تداخل 3d (3+2) و 4p (4+1) و 5s (5+0).",
    6: "E = 6: تداخل 4d (4+2) و 5p (5+1) و 6s (6+0).",
    7: "E = 7: تداخل رباعي: 4f (4+3) و 5d (5+2) و 6p (6+1) و 7s (7+0).",
    8: "E = 8: تداخل رباعي: 5f (5+3) و 6d (6+2) و 7p (7+1) و 8s (8+0).",
    9: "E = 9: ظهور مدار الفئة الجديدة 5g (5+4) للعناصر (121-137) متساوياً مع 6f و 7d و 8p.",
    10: "E = 10: مستويات الطاقة العليا في الغلاف السابع (7f) وما بعده."
}
if selected_energy != "عرض الكل (All)":
    st.html(f"<div style='background:#fffbeb; border:1px solid #f59e0b; border-radius:8px; padding:8px 12px; font-family:sans-serif; color:#78350f;'>💡 <strong>التفسير الكمي:</strong> {explanations[selected_energy]}</div>")

orbitals = [('s','0','#70ad47')] + [(f'p{i}','1','#8ea9db') for i in range(1,4)] + [(f'd{i}','2','#ffff00') for i in range(1,6)] + [(f'f{i}','3','#f4b084') for i in range(1,8)] + [(f'g{i}','4','#d9d9d9') for i in range(1,10)]

top_half = [
    ("8", [('119',8),('',9),('',9),('',9)]),
    ("7", [('87 Fr',7),('113 Nh',8),('114 Fl',8),('115 Mc',8),('',9),('',9),('',9),('',8),('',9),('',10),('',10),('',10),('',10),('',10),('',10),('',10)]),
    ("6", [('55 Cs',6),('81 Tl',7),('82 Pb',7),('83 Bi',7),('103 Lr',6),('104 Rf',8),('105 Db',8),('106 Sg',8),('107 Bh',6),('',9),('',9),('',9),('',9),('',9),('',9),('',9)]),
    ("5", [('37 Rb',5),('49 In',5),('50 Sn',6),('51 Sb',6),('71 Lu',7),('72 Hf',7),('73 Ta',7),('74 W',7),('75 Re',7),('89 Ac',8),('90 Th',8),('91 Pa',8),('92 U',8),('93 Np',8),('94 Pu',8),('95 Am',8),('121',9),('122',9),('123',9),('124',9),('125',9),('126',9),('127',9),('128',9),('129',9)]),
    ("4", [('19 K',4),('31 Ga',5),('32 Ge',5),('33 As',5),('39 Y',6),('40 Zr',6),('41 Nb',6),('42 Mo',6),('43 Tc',6),('57 La',7),('58 Ce',7),('59 Pr',7),('60 Nd',7),('61 Pm',7),('62 Sm',7),('63 Eu',7)]),
    ("3", [('11 Na',3),('13 Al',4),('14 Si',4),('15 P',4),('21 Sc',5),('22 Ti',5),('23 V',5),('24 Cr',5),('25 Mn',5)]),
    ("2", [('3 Li',2),('5 B',3),('6 C',3),('7 N',3)]),
    ("1", [('1 H',1)])
]

bottom_half = [
    ("1'", [('2 He',1)]),
    ("2'", [('4 Be',2),('8 O',3),('9 F',3),('10 Ne',3)]),
    ("3'", [('12 Mg',3),('16 S',4),('17 Cl',4),('18 Ar',4),('26 Fe',5),('27 Co',5),('28 Ni',5),('29 Cu',5),('30 Zn',5)]),
    ("4'", [('20 Ca',4),('34 Se',5),('35 Br',5),('36 Kr',5),('44 Ru',6),('45 Rh',6),('46 Pd',8),('47 Ag',6),('48 Cd',6),('64 Gd',7),('65 Tb',7),('66 Dy',7),('67 Ho',7),('68 Er',7),('69 Tm',7),('70 Yb',7)]),
    ("5'", [('38 Sr',5),('52 Te',6),('53 I',6),('54 Xe',6),('76 Os',7),('77 Ir',7),('78 Pt',7),('79 Au',7),('80 Hg',7),('96 Cm',8),('97 Bk',8),('98 Cf',8),('99 Es',8),('100 Fm',8),('101 Md',8),('102 No',8),('130',9),('131',9),('132',9),('133',9),('134',9),('135',9),('136',9),('137',9)]),
    ("6'", [('56 Ba',6),('84 Po',7),('85 At',7),('86 Rn',7),('108 Hs',8),('109 Mt',8),('110 Ds',8),('111 Rg',8),('112 Cn',8),('',9),('',9),('',9),('',9),('',9),('',9),('',9)]),
    ("7'", [('88 Ra',7),('116 Lv',8),('117 Ts',8),('118 Og',8),('',9),('',9),('',9),('',5),('',5),('',10),('',10),('',10),('',10),('',10),('',10),('',10)]),
    ("8'", [('120',8),('',9),('',9),('',9)])
]

def render_rows(rows):
    out = ""
    q = search_query.lower()
    for shell, cells in rows:
        out += f'<tr><td style="background:#d9e2ec; font-weight:bold; border:1px solid #333; padding:3px;">n={shell}</td>'
        for i in range(25):
            orb, l_val, bg = orbitals[i]
            if i < len(cells):
                sym, e = cells[i]
                fg = "#000"
                if sym == '137' and "FIG. 1" not in view_mode:
                    bg = "#e53e3e"
                    fg = "#fff"
                
                opacity = "1"
                border = "1px solid #333"
                if q:
                    if sym and q in sym.lower():
                        border = "3px solid #1a365d"
                    else:
                        opacity = "0.22"
                elif selected_energy != "عرض الكل (All)":
                    if e == selected_energy:
                        border = "3px solid #1a365d"
                    else:
                        opacity = "0.22"
                
                if "FIG. 1" in view_mode:
                    txt = f"<strong>{e}</strong>"
                else:
                    txt = f"<div><strong>{sym}</strong></div><div style='font-size:8.5px; background:rgba(255,255,255,0.7); color:#000; border-radius:2px;'>E={e}</div>" if sym else f"<div style='font-size:8.5px;'>E={e}</div>"
                out += f'<td style="background:{bg}; color:{fg}; opacity:{opacity}; border:{border}; padding:2px; min-width:38px;">{txt}</td>'
            else:
                out += '<td style="border:none;"></td>'
        out += '</tr>'
    return out

table_html = '<div style="width:100%; overflow-x:auto; padding-bottom:10px;"><table style="width:100%; min-width:1050px; border-collapse:collapse; text-align:center; font-size:10.5px; font-family:sans-serif;">'
table_html += '<tr><th style="background:#d9e2ec; border:1px solid #333; padding:3px;">Azimuthal (ℓ)</th>' + ''.join([f'<th style="background:#f0f4f8; border:1px solid #333; padding:2px;">ℓ={x[1]}</th>' for x in orbitals]) + '</tr>'
table_html += '<tr><th style="background:#d9e2ec; border:1px solid #333; padding:3px;">Shell/Orbital</th>' + ''.join([f'<th style="background:#d9e2ec; border:1px solid #333; padding:2px;">{x[0]}</th>' for x in orbitals]) + '</tr>'
table_html += '<tr><td style="border:none;"></td><td colspan="16" style="background:#f0f4f8; font-weight:bold; border:1px solid #333; padding:2px;">Groups Numbers according to IUPAC version 4 May 2022</td><td colspan="9" style="border:none;"></td></tr>'
table_html += '<tr><td style="border:none;"></td>' + ''.join([f'<td style="background:#e6fffa; font-weight:bold; border:1px solid #333; padding:2px;">{g}</td>' for g in ['1','13','14','15','3','4','5','6','7','19','20','21','22','23','24','25']]) + '<td colspan="9" style="border:none;"></td></tr>'
table_html += render_rows(top_half)
table_html += '<tr><td colspan="26" style="height:8px; border:none;"></td></tr>'
table_html += '<tr><td style="border:none;"></td>' + ''.join([f'<td style="background:#e6fffa; font-weight:bold; border:1px solid #333; padding:2px;">{g}</td>' for g in ['1','13','14','15','3','4','5','6','7']]) + '<td colspan="7" style="background:#f0f4f8; font-weight:bold; border:1px solid #333;">Lanthanoids & Actinoids</td><td colspan="9" style="border:none;"></td></tr>'
table_html += '<tr><td style="border:none;"></td>' + ''.join([f'<td style="background:#e6fffa; font-weight:bold; border:1px solid #333; padding:2px;">{g}</td>' for g in ['2','16','17','18','8','9','10','11','12']]) + '<td colspan="7" style="background:#f0f4f8; font-weight:bold; border:1px solid #333;">Lanthanoids & Actinoids</td><td colspan="9" style="border:none;"></td></tr>'
table_html += '<tr><td colspan="26" style="height:8px; border:none;"></td></tr>'
table_html += render_rows(bottom_half)
table_html += '<tr><td colspan="26" style="height:8px; border:none;"></td></tr>'
table_html += '<tr><td style="border:none;"></td>' + ''.join([f'<td style="background:#e6fffa; font-weight:bold; border:1px solid #333; padding:2px;">{g}</td>' for g in ['2','16','17','18','8','9','10','11','12','26','27','28','29','30','31','32']]) + '<td colspan="9" style="border:none;"></td></tr>'
