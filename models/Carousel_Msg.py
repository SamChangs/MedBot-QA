from linebot.models import *

# --------------------------------- 衛教資訊選單----------------------------------
def information_carousel_template():
    information_menu = TemplateSendMessage(
        alt_text='衛教資訊選單',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    title='衛教資訊選單-1/10',
                    text='請選擇以下',
                    actions=[
                        MessageTemplateAction(
                            label='一般照護',
                            text='一般照護'
                        ),
                        MessageTemplateAction(
                            label='心臟血管疾病',
                            text='心臟血管疾病'
                        ),
                        MessageTemplateAction(
                            label='手術相關',
                            text='手術相關'
                        )
                    ]
                ),
                CarouselColumn(
                    title='衛教資訊選單-2/10',
                    text='請選擇以下',
                    actions=[
                        MessageTemplateAction(
                            label='牙科',
                            text='牙科'
                        ),
                        MessageTemplateAction(
                            label='出院準備',
                            text='出院準備'
                        ),
                        MessageTemplateAction(
                            label='外科',
                            text='外科'
                        )
                    ]
                ),
                CarouselColumn(
                    title='衛教資訊選單-3/10',
                    text='請選擇以下',
                    actions=[
                        MessageTemplateAction(
                            label='外語護理指導',
                            text='外語護理指導'
                        ),
                        MessageTemplateAction(
                            label='皮膚疾病',
                            text='皮膚疾病'
                        ),
                        MessageTemplateAction(
                            label='耳鼻喉疾病',
                            text='耳鼻喉疾病'
                        )
                    ]
                ),
                CarouselColumn(
                    title='衛教資訊選單-4/10',
                    text='請選擇以下',
                    actions=[
                        MessageTemplateAction(
                            label='血液腫瘤',
                            text='血液腫瘤'
                        ),
                        MessageTemplateAction(
                            label='肝膽疾病',
                            text='肝膽疾病'
                        ),
                        MessageTemplateAction(
                            label='兒科疾病',
                            text='兒科疾病'
                        )
                    ]
                ),
                CarouselColumn(
                    title='衛教資訊選單-5/10',
                    text='請選擇以下',
                    actions=[
                        MessageTemplateAction(
                            label='泌尿疾病',
                            text='泌尿疾病'
                        ),
                        MessageTemplateAction(
                            label='肺部、胸腔疾病',
                            text='肺部、胸腔疾病'
                        ),
                        MessageTemplateAction(
                            label='侵入性檢查相關',
                            text='侵入性檢查相關'
                        )
                    ]
                ),
                CarouselColumn(
                    title='衛教資訊選單-6/10',
                    text='請選擇以下',
                    actions=[
                        MessageTemplateAction(
                            label='急診相關',
                            text='急診相關'
                        ),
                        MessageTemplateAction(
                            label='重症加護',
                            text='重症加護'
                        ),
                        MessageTemplateAction(
                            label='骨科疾病',
                            text='骨科疾病'
                        )
                    ]
                ),
                CarouselColumn(
                    title='衛教資訊選單-7/10',
                    text='請選擇以下',
                    actions=[
                        MessageTemplateAction(
                            label='健康保健',
                            text='健康保健'
                        ),
                        MessageTemplateAction(
                            label='產科、婦科疾病',
                            text='產科、婦科疾病'
                        ),
                        MessageTemplateAction(
                            label='感染疾病',
                            text='感染疾病'
                        )
                    ]
                ),
                CarouselColumn(
                    title='衛教資訊選單-8/10',
                    text='請選擇以下',
                    actions=[
                        MessageTemplateAction(
                            label='腦神經系統疾病',
                            text='腦神經系統疾病'
                        ),
                        MessageTemplateAction(
                            label='精神科疾病',
                            text='精神科疾病'
                        ),
                        MessageTemplateAction(
                            label='糖尿病疾病',
                            text='糖尿病疾病'
                        )
                    ]
                ),
                CarouselColumn(
                    title='衛教資訊選單-9/10',
                    text='請選擇以下',
                    actions=[
                        MessageTemplateAction(
                            label='癌症相關',
                            text='癌症相關'
                        ),
                        MessageTemplateAction(
                            label='醫療美容',
                            text='醫療美容'
                        ),
                        URITemplateAction(
                            label='衛教園地首頁',
                            uri='https://kmsh-imc.org/health_education'
                        )
                    ]
                ),
            ]
        )
    )
    return information_menu

def information_carousel_template_en():
    information_menu_en = TemplateSendMessage(
    alt_text='Health Education Menu',
    template=CarouselTemplate(
        columns=[
            CarouselColumn(
                title='Health Education-1/10',
                text='Choose a topic below',
                actions=[
                    MessageTemplateAction(
                        label='General Care',
                        text='General Care'
                    ),
                    MessageTemplateAction(
                        label='Cardiovascular',
                        text='Cardiovascular'
                    ),
                    MessageTemplateAction(
                        label='Surgery',
                        text='Surgery'
                    )
                ]
            ),
            CarouselColumn(
                title='Health Education-2/10',
                text='Choose a topic below',
                actions=[
                    MessageTemplateAction(
                        label='Dentistry',
                        text='Dentistry'
                    ),
                    MessageTemplateAction(
                        label='Discharge Prep',
                        text='Discharge Prep'
                    ),
                    MessageTemplateAction(
                        label='Surgery Info',
                        text='Surgery Info'
                    )
                ]
            ),
            CarouselColumn(
                title='Health Education-3/10',
                text='Choose a topic below',
                actions=[
                    MessageTemplateAction(
                        label='Nursing Guides',
                        text='Nursing Guides'
                    ),
                    MessageTemplateAction(
                        label='Skin Diseases',
                        text='Skin Diseases'
                    ),
                    MessageTemplateAction(
                        label='ENT Issues',
                        text='ENT Issues'
                    )
                ]
            ),
            CarouselColumn(
                title='Health Education-4/10',
                text='Choose a topic below',
                actions=[
                    MessageTemplateAction(
                        label='Hematologic Oncology',
                        text='Hematologic Oncology'
                    ),
                    MessageTemplateAction(
                        label='Liver Disorders',
                        text='Liver Disorders'
                    ),
                    MessageTemplateAction(
                        label='Pediatric Care',
                        text='Pediatric Care'
                    )
                ]
            ),
            CarouselColumn(
                title='Health Education-5/10',
                text='Choose a topic below',
                actions=[
                    MessageTemplateAction(
                        label='Urology',
                        text='Urology'
                    ),
                    MessageTemplateAction(
                        label='Lung/Chest Issues',
                        text='Lung/Chest Issues'
                    ),
                    MessageTemplateAction(
                        label='Invasive Exams',
                        text='Invasive Exams'
                    )
                ]
            ),
            CarouselColumn(
                title='Health Education-6/10',
                text='Choose a topic below',
                actions=[
                    MessageTemplateAction(
                        label='Emergency Care',
                        text='Emergency Care'
                    ),
                    MessageTemplateAction(
                        label='ICU Care',
                        text='ICU Care'
                    ),
                    MessageTemplateAction(
                        label='Orthopedics',
                        text='Orthopedics'
                    )
                ]
            ),
            CarouselColumn(
                title='Health Education-7/10',
                text='Choose a topic below',
                actions=[
                    MessageTemplateAction(
                        label='Health Care',
                        text='Health Care'
                    ),
                    MessageTemplateAction(
                        label='OB/GYN Care',
                        text='OB/GYN Care'
                    ),
                    MessageTemplateAction(
                        label='Infectious Diseases',
                        text='Infectious Diseases'
                    )
                ]
            ),
            CarouselColumn(
                title='Health Education-8/10',
                text='Choose a topic below',
                actions=[
                    MessageTemplateAction(
                        label='Neurological',
                        text='Neurological'
                    ),
                    MessageTemplateAction(
                        label='Mental Health',
                        text='Mental Health'
                    ),
                    MessageTemplateAction(
                        label='Diabetes',
                        text='Diabetes'
                    )
                ]
            ),
            CarouselColumn(
                title='Health Education-9/10',
                text='Choose a topic below',
                actions=[
                    MessageTemplateAction(
                        label='Cancer Info',
                        text='Cancer Info'
                    ),
                    MessageTemplateAction(
                        label='Cosmetic Care',
                        text='Cosmetic Care'
                    ),
                    URITemplateAction(
                        label='Home Page',
                        uri='https://kmsh-imc.org/health_education'
                    )
                ]
            ),
        ]
    )
)
    return information_menu_en

def information_carousel_template_idn():
    information_menu_idn = TemplateSendMessage(
    alt_text='Menu Pendidikan Kesehatan',
    template=CarouselTemplate(
        columns=[
            CarouselColumn(
                title='Pendidikan Kesehatan-1/10',
                text='Pilih topik di bawah',
                actions=[
                    MessageTemplateAction(
                        label='Perawatan Umum',
                        text='Perawatan Umum'
                    ),
                    MessageTemplateAction(
                        label='Penyakit Jantung',
                        text='Penyakit Jantung'
                    ),
                    MessageTemplateAction(
                        label='Bedah',
                        text='Bedah'
                    )
                ]
            ),
            CarouselColumn(
                title='Pendidikan Kesehatan-2/10',
                text='Pilih topik di bawah',
                actions=[
                    MessageTemplateAction(
                        label='Kedokteran Gigi',
                        text='Kedokteran Gigi'
                    ),
                    MessageTemplateAction(
                        label='Persiapan Pulang',
                        text='Persiapan Pulang'
                    ),
                    MessageTemplateAction(
                        label='Informasi Bedah',
                        text='Informasi Bedah'
                    )
                ]
            ),
            CarouselColumn(
                title='Pendidikan Kesehatan-3/10',
                text='Pilih topik di bawah',
                actions=[
                    MessageTemplateAction(
                        label='Panduan Keperawatan',
                        text='Panduan Keperawatan'
                    ),
                    MessageTemplateAction(
                        label='Penyakit Kulit',
                        text='Penyakit Kulit'
                    ),
                    MessageTemplateAction(
                        label='Masalah THT',
                        text='Masalah THT'
                    )
                ]
            ),
            CarouselColumn(
                title='Pendidikan Kesehatan-4/10',
                text='Pilih topik di bawah',
                actions=[
                    MessageTemplateAction(
                        label='Kanker Darah',
                        text='Kanker Darah'
                    ),
                    MessageTemplateAction(
                        label='Gangguan Hati',
                        text='Gangguan Hati'
                    ),
                    MessageTemplateAction(
                        label='Perawatan Anak',
                        text='Perawatan Anak'
                    )
                ]
            ),
            CarouselColumn(
                title='Pendidikan Kesehatan-5/10',
                text='Pilih topik di bawah',
                actions=[
                    MessageTemplateAction(
                        label='Urologi',
                        text='Urologi'
                    ),
                    MessageTemplateAction(
                        label='Masalah Paru',
                        text='Masalah Paru'
                    ),
                    MessageTemplateAction(
                        label='Pemeriksaan Invasif',
                        text='Pemeriksaan Invasif'
                    )
                ]
            ),
            CarouselColumn(
                title='Pendidikan Kesehatan-6/10',
                text='Pilih topik di bawah',
                actions=[
                    MessageTemplateAction(
                        label='Perawatan Darurat',
                        text='Perawatan Darurat'
                    ),
                    MessageTemplateAction(
                        label='Perawatan ICU',
                        text='Perawatan ICU'
                    ),
                    MessageTemplateAction(
                        label='Ortopedi',
                        text='Ortopedi'
                    )
                ]
            ),
            CarouselColumn(
                title='Pendidikan Kesehatan-7/10',
                text='Pilih topik di bawah',
                actions=[
                    MessageTemplateAction(
                        label='Perawatan Kesehatan',
                        text='Perawatan Kesehatan'
                    ),
                    MessageTemplateAction(
                        label='Perawatan Obstetri',
                        text='Perawatan Obstetri'
                    ),
                    MessageTemplateAction(
                        label='Penyakit Menular',
                        text='Penyakit Menular'
                    )
                ]
            ),
            CarouselColumn(
                title='Pendidikan Kesehatan-8/10',
                text='Pilih topik di bawah',
                actions=[
                    MessageTemplateAction(
                        label='Gangguan Saraf',
                        text='Gangguan Saraf'
                    ),
                    MessageTemplateAction(
                        label='Kesehatan Mental',
                        text='Kesehatan Mental'
                    ),
                    MessageTemplateAction(
                        label='Diabetes',
                        text='Diabetes'
                    )
                ]
            ),
            CarouselColumn(
                title='Pendidikan Kesehatan-9/10',
                text='Pilih topik di bawah',
                actions=[
                    MessageTemplateAction(
                        label='Info Kanker',
                        text='Info Kanker'
                    ),
                    MessageTemplateAction(
                        label='Perawatan Kosmetik',
                        text='Perawatan Kosmetik'
                    ),
                    URITemplateAction(
                        label='Beranda',
                        uri='https://kmsh-imc.org/health_education'
                    )
                ]
            ),
        ]
    )
)
    return information_menu_idn

def information_carousel_template_vn():
    information_menu_vn = TemplateSendMessage(
    alt_text='Menu Giáo Dục Sức Khỏe',
    template=CarouselTemplate(
        columns=[
            CarouselColumn(
                title='Giáo Dục Sức Khỏe-1/10',
                text='Chọn một chủ đề dưới đây',
                actions=[
                    MessageTemplateAction(
                        label='Chăm Sóc Chung',
                        text='Chăm Sóc Chung'
                    ),
                    MessageTemplateAction(
                        label='Bệnh Tim Mạch',
                        text='Bệnh Tim Mạch'
                    ),
                    MessageTemplateAction(
                        label='Phẫu Thuật',
                        text='Phẫu Thuật'
                    )
                ]
            ),
            CarouselColumn(
                title='Giáo Dục Sức Khỏe-2/10',
                text='Chọn một chủ đề dưới đây',
                actions=[
                    MessageTemplateAction(
                        label='Nha Khoa',
                        text='Nha Khoa'
                    ),
                    MessageTemplateAction(
                        label='Chuẩn Bị Xuất Viện',
                        text='Chuẩn Bị Xuất Viện'
                    ),
                    MessageTemplateAction(
                        label='Thông Tin Phẫu Thuật',
                        text='Thông Tin Phẫu Thuật'
                    )
                ]
            ),
            CarouselColumn(
                title='Giáo Dục Sức Khỏe-3/10',
                text='Chọn một chủ đề dưới đây',
                actions=[
                    MessageTemplateAction(
                        label='Hướng Dẫn Điều Dưỡng',
                        text='Hướng Dẫn Điều Dưỡng'
                    ),
                    MessageTemplateAction(
                        label='Bệnh Da Liễu',
                        text='Bệnh Da Liễu'
                    ),
                    MessageTemplateAction(
                        label='Vấn Đề Tai Mũi Họng',
                        text='Vấn Đề Tai Mũi Họng'
                    )
                ]
            ),
            CarouselColumn(
                title='Giáo Dục Sức Khỏe-4/10',
                text='Chọn một chủ đề dưới đây',
                actions=[
                    MessageTemplateAction(
                        label='Ung Thư Máu',
                        text='Ung Thư Máu'
                    ),
                    MessageTemplateAction(
                        label='Rối Loạn Gan',
                        text='Rối Loạn Gan'
                    ),
                    MessageTemplateAction(
                        label='Chăm Sóc Nhi Khoa',
                        text='Chăm Sóc Nhi Khoa'
                    )
                ]
            ),
            CarouselColumn(
                title='Giáo Dục Sức Khỏe-5/10',
                text='Chọn một chủ đề dưới đây',
                actions=[
                    MessageTemplateAction(
                        label='Tiết Niệu',
                        text='Tiết Niệu'
                    ),
                    MessageTemplateAction(
                        label='Vấn Đề Phổi',
                        text='Vấn Đề Phổi'
                    ),
                    MessageTemplateAction(
                        label='Xét Nghiệm Xâm Lấn',
                        text='Xét Nghiệm Xâm Lấn'
                    )
                ]
            ),
            CarouselColumn(
                title='Giáo Dục Sức Khỏe-6/10',
                text='Chọn một chủ đề dưới đây',
                actions=[
                    MessageTemplateAction(
                        label='Chăm Sóc Cấp Cứu',
                        text='Chăm Sóc Cấp Cứu'
                    ),
                    MessageTemplateAction(
                        label='Chăm Sóc ICU',
                        text='Chăm Sóc ICU'
                    ),
                    MessageTemplateAction(
                        label='Chấn Thương',
                        text='Chấn Thương'
                    )
                ]
            ),
            CarouselColumn(
                title='Giáo Dục Sức Khỏe-7/10',
                text='Chọn một chủ đề dưới đây',
                actions=[
                    MessageTemplateAction(
                        label='Chăm Sóc Sức Khỏe',
                        text='Chăm Sóc Sức Khỏe'
                    ),
                    MessageTemplateAction(
                        label='Chăm Sóc Sản Phụ',
                        text='Chăm Sóc Sản Phụ'
                    ),
                    MessageTemplateAction(
                        label='Bệnh Truyền Nhiễm',
                        text='Bệnh Truyền Nhiễm'
                    )
                ]
            ),
            CarouselColumn(
                title='Giáo Dục Sức Khỏe-8/10',
                text='Chọn một chủ đề dưới đây',
                actions=[
                    MessageTemplateAction(
                        label='Rối Loạn Thần Kinh',
                        text='Rối Loạn Thần Kinh'
                    ),
                    MessageTemplateAction(
                        label='Sức Khỏe Tinh Thần',
                        text='Sức Khỏe Tinh Thần'
                    ),
                    MessageTemplateAction(
                        label='Tiểu Đường',
                        text='Tiểu Đường'
                    )
                ]
            ),
            CarouselColumn(
                title='Giáo Dục Sức Khỏe-9/10',
                text='Chọn một chủ đề dưới đây',
                actions=[
                    MessageTemplateAction(
                        label='Thông Tin Ung Thư',
                        text='Thông Tin Ung Thư'
                    ),
                    MessageTemplateAction(
                        label='Chăm Sóc Thẩm Mỹ',
                        text='Chăm Sóc Thẩm Mỹ'
                    ),
                    URITemplateAction(
                        label='Trang Chính',
                        uri='https://kmsh-imc.org/health_education'
                    )
                ]
            ),
        ]
    )
)
    return information_menu_vn

def information_carousel_template_th():
    information_menu_th = TemplateSendMessage(
    alt_text='เมนูการศึกษาเรื่องสุขภาพ',
    template=CarouselTemplate(
        columns=[
            CarouselColumn(
                title='การศึกษาเรื่องสุขภาพ-1/10',
                text='เลือกหัวข้อด้านล่าง',
                actions=[
                    MessageTemplateAction(
                        label='การดูแลทั่วไป',
                        text='การดูแลทั่วไป'
                    ),
                    MessageTemplateAction(
                        label='โรคหัวใจ',
                        text='โรคหัวใจ'
                    ),
                    MessageTemplateAction(
                        label='การผ่าตัด',
                        text='การผ่าตัด'
                    )
                ]
            ),
            CarouselColumn(
                title='การศึกษาเรื่องสุขภาพ-2/10',
                text='เลือกหัวข้อด้านล่าง',
                actions=[
                    MessageTemplateAction(
                        label='ทันตกรรม',
                        text='ทันตกรรม'
                    ),
                    MessageTemplateAction(
                        label='เตรียมออกจากโรงพยาบาล',
                        text='เตรียมออกจากโรงพยาบาล'
                    ),
                    MessageTemplateAction(
                        label='ข้อมูลการผ่าตัด',
                        text='ข้อมูลการผ่าตัด'
                    )
                ]
            ),
            CarouselColumn(
                title='การศึกษาเรื่องสุขภาพ-3/10',
                text='เลือกหัวข้อด้านล่าง',
                actions=[
                    MessageTemplateAction(
                        label='แนวทางการพยาบาล',
                        text='แนวทางการพยาบาล'
                    ),
                    MessageTemplateAction(
                        label='โรคผิวหนัง',
                        text='โรคผิวหนัง'
                    ),
                    MessageTemplateAction(
                        label='ปัญหาหู คอ จมูก',
                        text='ปัญหาหู คอ จมูก'
                    )
                ]
            ),
            CarouselColumn(
                title='การศึกษาเรื่องสุขภาพ-4/10',
                text='เลือกหัวข้อด้านล่าง',
                actions=[
                    MessageTemplateAction(
                        label='มะเร็งเลือด',
                        text='มะเร็งเลือด'
                    ),
                    MessageTemplateAction(
                        label='โรคตับ',
                        text='โรคตับ'
                    ),
                    MessageTemplateAction(
                        label='การดูแลเด็ก',
                        text='การดูแลเด็ก'
                    )
                ]
            ),
            CarouselColumn(
                title='การศึกษาเรื่องสุขภาพ-5/10',
                text='เลือกหัวข้อด้านล่าง',
                actions=[
                    MessageTemplateAction(
                        label='ระบบปัสสาวะ',
                        text='ระบบปัสสาวะ'
                    ),
                    MessageTemplateAction(
                        label='ปัญหาปอด',
                        text='ปัญหาปอด'
                    ),
                    MessageTemplateAction(
                        label='การตรวจสอบ',
                        text='การตรวจสอบ'
                    )
                ]
            ),
            CarouselColumn(
                title='การศึกษาเรื่องสุขภาพ-6/10',
                text='เลือกหัวข้อด้านล่าง',
                actions=[
                    MessageTemplateAction(
                        label='การดูแลฉุกเฉิน',
                        text='การดูแลฉุกเฉิน'
                    ),
                    MessageTemplateAction(
                        label='การดูแล ICU',
                        text='การดูแล ICU'
                    ),
                    MessageTemplateAction(
                        label='ศัลยกรรมกระดูก',
                        text='ศัลยกรรมกระดูก'
                    )
                ]
            ),
            CarouselColumn(
                title='การศึกษาเรื่องสุขภาพ-7/10',
                text='เลือกหัวข้อด้านล่าง',
                actions=[
                    MessageTemplateAction(
                        label='การดูแลสุขภาพ',
                        text='การดูแลสุขภาพ'
                    ),
                    MessageTemplateAction(
                        label='การดูแลสตรี',
                        text='การดูแลสตรี'
                    ),
                    MessageTemplateAction(
                        label='โรคติดเชื้อ',
                        text='โรคติดเชื้อ'
                    )
                ]
            ),
            CarouselColumn(
                title='การศึกษาเรื่องสุขภาพ-8/10',
                text='เลือกหัวข้อด้านล่าง',
                actions=[
                    MessageTemplateAction(
                        label='โรคระบบประสาท',
                        text='โรคระบบประสาท'
                    ),
                    MessageTemplateAction(
                        label='สุขภาพจิต',
                        text='สุขภาพจิต'
                    ),
                    MessageTemplateAction(
                        label='เบาหวาน',
                        text='เบาหวาน'
                    )
                ]
            ),
            CarouselColumn(
                title='การศึกษาเรื่องสุขภาพ-9/10',
                text='เลือกหัวข้อด้านล่าง',
                actions=[
                    MessageTemplateAction(
                        label='ข้อมูลมะเร็ง',
                        text='ข้อมูลมะเร็ง'
                    ),
                    MessageTemplateAction(
                        label='การดูแลความงาม',
                        text='การดูแลความงาม'
                    ),
                    URITemplateAction(
                        label='หน้าแรก',
                        uri='https://kmsh-imc.org/health_education'
                    )
                ]
            ),
        ]
    )
)
    return information_menu_th

# --------------------------------- 衛教主題選單----------------------------------
def info_topic_carousel_template(topic_name):
    topics_info = {
    "一般照護": [
        {"label": "靜脈注射含碘顯影劑檢查後衛教", "uri": "https://kmsh-imc.org/assets/file/20230420002.pdf"},
        {"label": "生活保健之預防痠痛衛教", "uri": "https://kmsh-imc.org/assets/file/20180502040.pdf"},
        {"label": "預防胃食道逆流衛教", "uri": "https://kmsh-imc.org/assets/file/20180502029.pdf"}
    ],
    "心臟血管疾病": [
        {"label": "認識心臟震波治療", "uri": "https://kmsh-imc.org/assets/file/20210705019.pdf"},
        {"label": "冠狀動脈氣球擴張術或置放支架術後注意事項", "uri": "https://kmsh-imc.org/assets/file/20210705018.pdf"},
        {"label": "心臟衰竭照護及飲食控制", "uri": "https://kmsh-imc.org/assets/file/20210705017.pdf"}
    ],
    "手術相關": [
        {"label": "子宮頸擴張刮除術之術後衛教", "uri": "https://kmsh-imc.org/assets/file/20231229001.pdf"},
        {"label": "眼瞼下垂手術", "uri": "https://kmsh-imc.org/assets/file/20210705035.pdf"},
        {"label": "顏面骨骨折手術照護", "uri": "https://kmsh-imc.org/assets/file/20210705034.pdf"}
    ],
    "牙科": [
        {"label": "齒齦下刮除術暨牙根整平術", "uri": "https://kmsh-imc.org/assets/file/20180511004.pdf"},
        {"label": "牙齒矯正口腔清潔", "uri": "https://kmsh-imc.org/assets/file/20180511003.pdf"}
    ],
    "出院準備": [
        {"label": "輔具資源租借介紹", "uri": "https://kmsh-imc.org/assets/file/20180306018.pdf"}
    ],
    "外科": [
        {"label": "內視鏡靜脈曲張摘除術後照護", "uri": "https://kmsh-imc.org/assets/file/20180514031.pdf"}
    ],
    "外語護理指導": [
        {"label": "預防跌倒(中英 )English", "uri": "https://www.kmsh.org.tw/Web/wwwKMHK/hygr_Edu/hygr/20180514018.pdf"}
    ],
    "皮膚疾病": [
        {"label": "高齡者壓瘡傷口照護衛教", "uri": "https://kmsh-imc.org/assets/file/20180306021.pdf"},
        {"label": "燒燙傷的癒後照顧", "uri": "https://kmsh-imc.org/assets/file/20180306020.pdf"},
        {"label": "手或足部傷口浸泡與護理", "uri": "https://kmsh-imc.org/assets/file/20180306019.pdf"}
    ],
    "耳鼻喉疾病": [
        {"label": "聽力喪失的治療與注意事項", "uri": "https://kmsh-imc.org/assets/file/20180502018.pdf"},
        {"label": "醫生我是頭痛不是鼻子痛", "uri": "https://kmsh-imc.org/assets/file/20180502017.pdf"},
        {"label": "打鼾/呼吸中止之照護", "uri": "https://kmsh-imc.org/assets/file/20180502016.pdf"}
    ],
    "血液腫瘤": [
        {"label": "認識骨髓抽吸檢查及護理", "uri": "https://kmsh-imc.org/assets/file/20210705015.pdf"}
    ],
    "肝膽疾病": [
        {"label": "胰臟頭十二指腸切除術後照護", "uri": "https://kmsh-imc.org/assets/file/20210705005.pdf"},
        {"label": "腹腔鏡肝葉切除術及照護", "uri": "https://kmsh-imc.org/assets/file/20180306031.pdf"},
        {"label": "急性胰臟炎", "uri": "https://kmsh-imc.org/assets/file/20180306030.pdf"}
    ],
    "兒科疾病": [
        {"label": "熱性痙攣", "uri": "https://kmsh-imc.org/assets/file/20180514016.pdf"},
        {"label": "認識腸病毒", "uri": "https://kmsh-imc.org/assets/file/20180514015.pdf"},
        {"label": "認識哮吼及其照護", "uri": "https://kmsh-imc.org/assets/file/20180514014.pdf"}
    ],
    "泌尿疾病": [
        {"label": "迴腸膀胱造瘻手術衛教", "uri": "https://kmsh-imc.org/assets/file/20180514021.pdf"},
        {"label": "認識尿失禁衛教", "uri": "https://kmsh-imc.org/assets/file/20180502005.pdf"},
        {"label": "預防泌尿道感染衛教", "uri": "https://kmsh-imc.org/assets/file/20180502004.pdf"}
    ],
    "肺部、胸腔疾病": [
        {"label": "正確洗手法", "uri": "https://kmsh-imc.org/assets/file/20231215001.pdf"},
        {"label": "肺結核入住負壓隔離病房須知", "uri": "https://kmsh-imc.org/assets/file/20210705041.pdf"},
        {"label": "抗結核藥物副作用及注意事項", "uri": "https://kmsh-imc.org/assets/file/20210705040.pdf"}
    ],
    "侵入性檢查相關": [
        {"label": "膀胱鏡檢查後衛教", "uri": "https://kmsh-imc.org/assets/file/20230420001.pdf"},
        {"label": "肺部軟式支氣管鏡檢查前後衛教", "uri": "https://kmsh-imc.org/assets/file/20210705007.pdf"},
        {"label": "超音波導引下抽吸", "uri": "https://kmsh-imc.org/assets/file/20180502041.pdf"}
    ],    
    "急診相關": [
        {"label": "兒童頭部外傷照護需知", "uri": "https://kmsh-imc.org/assets/file/20240222001.pdf"},
        {"label": "轉診注意需知", "uri": "https://kmsh-imc.org/assets/file/20210705033.pdf"},
        {"label": "手術前準備及注意事項", "uri": "https://kmsh-imc.org/assets/file/20180514027.pdf"}
    ],
    "重症加護": [
        {"label": "認識肋膜腔鏡檢查", "uri": "https://kmsh-imc.org/assets/file/20210705009.pdf"}
    ],
    "骨科疾病": [
        {"label": "認識大拇趾外翻", "uri": "https://kmsh-imc.org/assets/file/20210705043.pdf"},
        {"label": "椎體成型術及照護", "uri": "https://kmsh-imc.org/assets/file/20210705012.pdf"},
        {"label": "人工髖關節置換病人衛教指南", "uri": "https://kmsh-imc.org/assets/file/20210705011.pdf"}
    ],
    "健康保健": [
        {"label": "認識檳榔危害", "uri": "https://kmsh-imc.org/assets/file/20180814002.pdf"},
        {"label": "戒菸防治", "uri": "https://kmsh-imc.org/assets/file/20180814001.pdf"}
    ],
    "產科、婦科疾病": [
        {"label": "認識子宮頸癌", "uri": "https://kmsh-imc.org/assets/file/20180306071.pdf"}
    ],
    "感染疾病": [
        {"label": "流行性感冒防治", "uri": "https://kmsh-imc.org/assets/file/20180514030.pdf"},
        {"label": "疥瘡預防與照顧須知", "uri": "https://kmsh-imc.org/assets/file/20180514029.pdf"},
        {"label": "門診-蜂窩性組織炎衛教", "uri": "https://kmsh-imc.org/assets/file/20180502034.pdf"}
    ],
    "腦神經系統疾病": [
        {"label": "暫時性腦缺血發作", "uri": "https://kmsh-imc.org/assets/file/20210705028.pdf"},
        {"label": "顏面神經麻痺如何自我照顧", "uri": "https://kmsh-imc.org/assets/file/20180502031.pdf"},
        {"label": "偏頭痛的預防", "uri": "https://kmsh-imc.org/assets/file/20180502023.pdf"}
    ],
    "精神科疾病": [
        {"label": "談精神病患如何生活管理", "uri": "https://kmsh-imc.org/assets/file/20180502044.pdf"},
        {"label": "家屬如何協助慢性精神病患居家生活", "uri": "https://kmsh-imc.org/assets/file/20180502043.pdf"},
        {"label": "認識精神科藥物副作用(門診版)", "uri": "https://kmsh-imc.org/assets/file/20180502042.pdf"}
    ],
    "糖尿病疾病": [
        {"label": "糖尿病高血糖處理", "uri": "https://kmsh-imc.org/assets/file/20180502047.pdf"},
        {"label": "糖尿病低血糖處理", "uri": "https://kmsh-imc.org/assets/file/20180502046.pdf"},
        {"label": "糖尿病人生病時應注意事項", "uri": "https://kmsh-imc.org/assets/file/20180502045.pdf"}
    ],
    "癌症相關": [
        {"label": "乳癌的飲食原則", "uri": "https://kmsh-imc.org/assets/file/20210705032.pdf"},
        {"label": "認識乳癌化學治療與雙標靶治療", "uri": "https://kmsh-imc.org/assets/file/20180514020.pdf"},
        {"label": "認識乳房腫瘤微創式安可兒切除手術", "uri": "https://kmsh-imc.org/assets/file/20210705008.pdf"}
    ],
    "醫療美容": [
        {"label": "肉毒桿菌注射", "uri": "https://kmsh-imc.org/assets/file/20210705042.pdf"},
        {"label": "煥膚術", "uri": "https://kmsh-imc.org/assets/file/20210705037.pdf"},
        {"label": "鉺雅鉻雷射", "uri": "https://kmsh-imc.org/assets/file/20180514043.pdf"}
    ]
}
    
    # 獲取對應topic_name的label和uri列表
    topic_info = topics_info.get(topic_name, [])
    if not topic_info:
        return None  # 如果找不到對應的topic_name，返回None或者其他處理方式

    columns = []
    for info in topic_info:
        columns.append(
            URITemplateAction(
                label=info["label"],
                uri=info["uri"]
            )
        )
    
    information_topic = TemplateSendMessage(
        alt_text='衛教主題選單',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    title='衛教主題類別',
                    text='請選擇以下主題',
                    actions=columns
                )
            ]
        )
    )
    return information_topic

def info_topic_carousel_template_en(topic_name):
    topics_info = {
    "General Care": [
        {"label": "Post-Iodine Care", "uri": "https://kmsh-imc.org/assets/file/20230420002-1.pdf"},
        {"label": "Prevent Muscle Pain", "uri": "https://kmsh-imc.org/assets/file/20180502040-1.pdf"},
        {"label": "Prevent GERD", "uri": "https://kmsh-imc.org/assets/file/20180502029-1.pdf"}
    ],
    "Cardiovascular": [
        {"label": "Cardiac Shockwave", "uri": "https://kmsh-imc.org/assets/file/20210705019-1.pdf"},
        {"label": "Balloon Angioplasty", "uri": "https://kmsh-imc.org/assets/file/20210705018-1.pdf"},
        {"label": "Heart Failure Care", "uri": "https://kmsh-imc.org/assets/file/20210705017-1.pdf"}
    ],
    "Surgery": [
        {"label": "Cervical Curettage", "uri": "https://kmsh-imc.org/assets/file/20231229001-1.pdf"},
        {"label": "Ptosis Surgery", "uri": "https://kmsh-imc.org/assets/file/20210705035-1.pdf"},
        {"label": "Facial Fracture", "uri": "https://kmsh-imc.org/assets/file/20210705034-1.pdf"}
    ],
    "Dentistry": [
        {"label": "Scaling & Rooting", "uri": "https://kmsh-imc.org/assets/file/20180511004-1.pdf"},
        {"label": "Braces Oral Care", "uri": "https://kmsh-imc.org/assets/file/20180511003-1.pdf"}
    ],
    "Discharge Prep": [
        {"label": "Assistive Device", "uri": "https://kmsh-imc.org/assets/file/20180306018-1.pdf"}
    ],
    "Surgery Info": [
        {"label": "Post-Endoscopy", "uri": "https://kmsh-imc.org/assets/file/20180514031-1.pdf"}
    ],
    "Nursing Guides": [
        {"label": "Fall Prevention", "uri": "https://www.kmsh.org.tw/Web/wwwKMHK/hygr_Edu/hygr/20180514018.pdf"}
    ],
    "Skin Diseases": [
        {"label": "Pressure Ulcers", "uri": "https://kmsh-imc.org/assets/file/20180306021-1.pdf"},
        {"label": "Burn Care", "uri": "https://kmsh-imc.org/assets/file/20180306020-1.pdf"},
        {"label": "Hand/Foot Wounds", "uri": "https://kmsh-imc.org/assets/file/20180306019-1.pdf"}
    ],
    "ENT Issues": [
        {"label": "Hearing Loss Care", "uri": "https://kmsh-imc.org/assets/file/20180502018-1.pdf"},
        {"label": "Headache vs. Sinus", "uri": "https://kmsh-imc.org/assets/file/20180502017-1.pdf"},
        {"label": "Snoring Care", "uri": "https://kmsh-imc.org/assets/file/20180502016-1.pdf"}
    ],
    "Hematologic Oncology": [
        {"label": "Bone Marrow Test", "uri": "https://kmsh-imc.org/assets/file/20210705015-1.pdf"}
    ],
    "Liver Disorders": [
        {"label": "Pancreatic Surgery", "uri": "https://kmsh-imc.org/assets/file/20210705005-1.pdf"},
        {"label": "Liver Resection", "uri": "https://kmsh-imc.org/assets/file/20180306031-1.pdf"},
        {"label": "Acute Pancreatitis", "uri": "https://kmsh-imc.org/assets/file/20180306030-1.pdf"}
    ],
    "Pediatric Care": [
        {"label": "Febrile Seizures", "uri": "https://kmsh-imc.org/assets/file/20180514016-1.pdf"},
        {"label": "Enterovirus Care", "uri": "https://kmsh-imc.org/assets/file/20180514015-1.pdf"},
        {"label": "Croup Management", "uri": "https://kmsh-imc.org/assets/file/20180514014-1.pdf"}
    ],
    "Urology": [
        {"label": "Ileal Conduit", "uri": "https://kmsh-imc.org/assets/file/20180514021-1.pdf"},
        {"label": "Urinary Incontinence", "uri": "https://kmsh-imc.org/assets/file/20180502005-1.pdf"},
        {"label": "UTI Prevention", "uri": "https://kmsh-imc.org/assets/file/20180502004-1.pdf"}
    ],
    "Pulmonary/Chest Issues": [
        {"label": "Hand Hygiene", "uri": "https://kmsh-imc.org/assets/file/20231215001-1.pdf"},
        {"label": "TB Isolation", "uri": "https://kmsh-imc.org/assets/file/20210705041-1.pdf"},
        {"label": "Anti-TB Effects", "uri": "https://kmsh-imc.org/assets/file/20210705040-1.pdf"}
    ],
    "Invasive Exam Care": [
        {"label": "Post-Cystoscopy", "uri": "https://kmsh-imc.org/assets/file/20230420001-1.pdf"},
        {"label": "Pre/Post Bronch", "uri": "https://kmsh-imc.org/assets/file/20210705007-1.pdf"},
        {"label": "Ultrasound Asp.", "uri": "https://kmsh-imc.org/assets/file/20180502041-1.pdf"}
    ],
    "Emergency Care": [
        {"label": "Child Head Trauma", "uri": "https://kmsh-imc.org/assets/file/20240222001-1.pdf"},
        {"label": "Referral Notice", "uri": "https://kmsh-imc.org/assets/file/20210705033-1.pdf"},
        {"label": "Pre-Surgery Prep", "uri": "https://kmsh-imc.org/assets/file/20180514027-1.pdf"}
    ],
    "ICU Care": [
        {"label": "Pleural Lapar.", "uri": "https://kmsh-imc.org/assets/file/20210705009-1.pdf"}
    ],
    "Orthopedics": [
        {"label": "Bunion Awareness", "uri": "https://kmsh-imc.org/assets/file/20210705043-1.pdf"},
        {"label": "Vertebroplasty", "uri": "https://kmsh-imc.org/assets/file/20210705012-1.pdf"},
        {"label": "Hip Replacement", "uri": "https://kmsh-imc.org/assets/file/20210705011-1.pdf"}
    ],
    "Health Care": [
        {"label": "Betel Nut Hazards", "uri": "https://kmsh-imc.org/assets/file/20180814002.pdf"},
        {"label": "Smoking Cessation", "uri": "https://kmsh-imc.org/assets/file/20180814001.pdf"}
    ],
    "OB/GYN Care": [
        {"label": "Cervical Cancer", "uri": "https://kmsh-imc.org/assets/file/20180306071-1.pdf"}
    ],
    "Infectious Diseases": [
        {"label": "Flu Prevention", "uri": "https://kmsh-imc.org/assets/file/20180514030-1.pdf"},
        {"label": "Scabies Care", "uri": "https://kmsh-imc.org/assets/file/20180514029-1.pdf"},
        {"label": "Cellulitis Care", "uri": "https://kmsh-imc.org/assets/file/20180502034-1.pdf"}
    ],
    "Neurological": [
        {"label": "TIA Awareness", "uri": "https://kmsh-imc.org/assets/file/20210705028-1.pdf"},
        {"label": "Facial Nerve Care", "uri": "https://kmsh-imc.org/assets/file/20180502031-1.pdf"},
        {"label": "Migraine Prev.", "uri": "https://kmsh-imc.org/assets/file/20180502023-1.pdf"}
    ],
    "Mental Health": [
        {"label": "Schizophrenia", "uri": "https://kmsh-imc.org/assets/file/20180502044-1.pdf"},
        {"label": "Chronic Mental", "uri": "https://kmsh-imc.org/assets/file/20180502043-1.pdf"},
        {"label": "Psych Meds", "uri": "https://kmsh-imc.org/assets/file/20180502042-1.pdf"}
    ],
    "Diabetes": [
        {"label": "High Blood Sugar", "uri": "https://kmsh-imc.org/assets/file/20180502047-1.pdf"},
        {"label": "Low Blood Sugar", "uri": "https://kmsh-imc.org/assets/file/20180502046-1.pdf"},
        {"label": "Sick Day Care", "uri": "https://kmsh-imc.org/assets/file/20180502045-1.pdf"}
    ],
    "Cancer Info": [
        {"label": "Breast Cancer Diet", "uri": "https://kmsh-imc.org/assets/file/20210705032-1.pdf"},
        {"label": "Breast Cancer Care", "uri": "https://kmsh-imc.org/assets/file/20180514020-1.pdf"},
        {"label": "Minimally Invasive", "uri": "https://kmsh-imc.org/assets/file/20210705008-1.pdf"}
    ],
    "Cosmetic Care": [
        {"label": "Botox Injection", "uri": "https://kmsh-imc.org/assets/file/20210705042-1.pdf"},
        {"label": "Skin Resurfacing", "uri": "https://kmsh-imc.org/assets/file/20210705037-1.pdf"},
        {"label": "Er:YAG Laser", "uri": "https://kmsh-imc.org/assets/file/20180514043-1.pdf"}
    ]
}

    # 獲取對應topic_name的label和uri列表
    topic_info = topics_info.get(topic_name, [])
    if not topic_info:
        return None  # 如果找不到對應的topic_name，返回None或者其他處理方式

    columns = []
    for info in topic_info:
        columns.append(
            URITemplateAction(
                label=info["label"],
                uri=info["uri"]
            )
        )
    
    information_topic = TemplateSendMessage(
        alt_text='Health Education Topic Menu',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    title='Health Education Categories',
                    text='Please choose a topic below',
                    actions=columns
                )
            ]
        )
    )
    return information_topic

def info_topic_carousel_template_idn(topic_name):
    topics_info = {
        "Perawatan Umum": [
            {"label": "Pasca Iodin", "uri": "https://kmsh-imc.org/assets/file/20230420002-2.pdf"},
            {"label": "Cegah Nyeri Otot", "uri": "https://kmsh-imc.org/assets/file/20180502040-2.pdf"},
            {"label": "Cegah GERD", "uri": "https://kmsh-imc.org/assets/file/20180502029-2.pdf"}
        ],
        "Penyakit Jantung": [
            {"label": "Terapi Gelombang", "uri": "https://kmsh-imc.org/assets/file/20210705019-2.pdf"},
            {"label": "Angioplasti Balon", "uri": "https://kmsh-imc.org/assets/file/20210705018-2.pdf"},
            {"label": "Rawat Gagal Jantung", "uri": "https://kmsh-imc.org/assets/file/20210705017-2.pdf"}
        ],
        "Bedah": [
            {"label": "Kuretase Serviks", "uri": "https://kmsh-imc.org/assets/file/20231229001-2.pdf"},
            {"label": "Bedah Ptosis", "uri": "https://kmsh-imc.org/assets/file/20210705035-2.pdf"},
            {"label": "Fraktur Wajah", "uri": "https://kmsh-imc.org/assets/file/20210705034-2.pdf"}
        ],
        "Kedokteran Gigi": [
            {"label": "Scaling & Rooting", "uri": "https://kmsh-imc.org/assets/file/20180511004-2.pdf"},
            {"label": "Rawat Behel", "uri": "https://kmsh-imc.org/assets/file/20180511003-2.pdf"}
        ],
        "Persiapan Pulang": [
            {"label": "Alat Bantu", "uri": "https://kmsh-imc.org/assets/file/20180306018-2.pdf"}
        ],
        "Informasi Bedah": [
            {"label": "Pasca Endoskopi", "uri": "https://kmsh-imc.org/assets/file/20180514031-2.pdf"}
        ],
        "Panduan Keperawatan": [
            {"label": "Cegah Jatuh", "uri": "https://www.kmsh.org.tw/Web/wwwKMHK/hygr_Edu/hygr/20180514017.pdf"}
        ],
        "Penyakit Kulit": [
            {"label": "Ulkus Tekanan", "uri": "https://kmsh-imc.org/assets/file/20180306021-2.pdf"},
            {"label": "Rawat Luka Bakar", "uri": "https://kmsh-imc.org/assets/file/20180306020-2.pdf"},
            {"label": "Luka Tangan/Kaki", "uri": "https://kmsh-imc.org/assets/file/20180306019-2.pdf"}
        ],
        "Masalah THT": [
            {"label": "Rawat Dengar Hilang", "uri": "https://kmsh-imc.org/assets/file/20180502018-2.pdf"},
            {"label": "Sakit Kepala & Sinus", "uri": "https://kmsh-imc.org/assets/file/20180502017-2.pdf"},
            {"label": "Rawat Mendengkur", "uri": "https://kmsh-imc.org/assets/file/20180502016-2.pdf"}
        ],
        "Kanker Darah": [
            {"label": "Tes Sumsum Tulang", "uri": "https://kmsh-imc.org/assets/file/20210705015-2.pdf"}
        ],
        "Gangguan Hati": [
            {"label": "Bedah Pankreas", "uri": "https://kmsh-imc.org/assets/file/20210705005-2.pdf"},
            {"label": "Reseksi Hati", "uri": "https://kmsh-imc.org/assets/file/20180306031-2.pdf"},
            {"label": "Pankreatitis Akut", "uri": "https://kmsh-imc.org/assets/file/20180306030-2.pdf"}
        ],
        "Perawatan Anak": [
            {"label": "Kejang Demam", "uri": "https://kmsh-imc.org/assets/file/20180514016-2.pdf"},
            {"label": "Rawat Enterovirus", "uri": "https://kmsh-imc.org/assets/file/20180514015-2.pdf"},
            {"label": "Manajemen Croup", "uri": "https://kmsh-imc.org/assets/file/20180514014-2.pdf"}
        ],
        "Urologi": [
            {"label": "Konduit Ileum", "uri": "https://kmsh-imc.org/assets/file/20180514021-2.pdf"},
            {"label": "Inkontinensia Urin", "uri": "https://kmsh-imc.org/assets/file/20180502005-2.pdf"},
            {"label": "Cegah ISK", "uri": "https://kmsh-imc.org/assets/file/20180502004-2.pdf"}
        ],
        "Masalah Paru": [
            {"label": "Cuci Tangan", "uri": "https://kmsh-imc.org/assets/file/20231215001-2.pdf"},
            {"label": "Isolasi TB", "uri": "https://kmsh-imc.org/assets/file/20210705041-2.pdf"},
            {"label": "Efek Anti-TB", "uri": "https://kmsh-imc.org/assets/file/20210705040-2.pdf"}
        ],
        "Pemeriksaan Invasif": [
            {"label": "Pasca Sistoskopi", "uri": "https://kmsh-imc.org/assets/file/20230420001-2.pdf"},
            {"label": "Bronkoskopi", "uri": "https://kmsh-imc.org/assets/file/20210705007-2.pdf"},
            {"label": "Aspirasi USG", "uri": "https://kmsh-imc.org/assets/file/20180502041-2.pdf"}
        ],
        "Perawatan Darurat": [
            {"label": "Trauma Kepala Anak", "uri": "https://kmsh-imc.org/assets/file/20240222001-2.pdf"},
            {"label": "Instruksi Rujukan", "uri": "https://kmsh-imc.org/assets/file/20210705033-2.pdf"},
            {"label": "Pra-Bedah", "uri": "https://kmsh-imc.org/assets/file/20180514027-2.pdf"}
        ],
        "Perawatan ICU": [
            {"label": "Laparoskopi Pleura", "uri": "https://kmsh-imc.org/assets/file/20210705009-2.pdf"}
        ],
        "Ortopedi": [
            {"label": "Kesadaran Bunion", "uri": "https://kmsh-imc.org/assets/file/20210705043-2.pdf"},
            {"label": "Vertebroplasti", "uri": "https://kmsh-imc.org/assets/file/20210705012-2.pdf"},
            {"label": "Ganti Pinggul", "uri": "https://kmsh-imc.org/assets/file/20210705011-2.pdf"}
        ],
        "Perawatan Kesehatan": [
            {"label": "Bahaya Pinang", "uri": "https://kmsh-imc.org/assets/file/20180814002.pdf"},
            {"label": "Berhenti Merokok", "uri": "https://kmsh-imc.org/assets/file/20180814001.pdf"}
        ],
        "Perawatan Obstetri": [
            {"label": "Kanker Serviks", "uri": "https://kmsh-imc.org/assets/file/20180306071-2.pdf"}
        ],
        "Penyakit Menular": [
            {"label": "Cegah Flu", "uri": "https://kmsh-imc.org/assets/file/20180514030-2.pdf"},
            {"label": "Rawat Skabies", "uri": "https://kmsh-imc.org/assets/file/20180514029-2.pdf"},
            {"label": "Rawat Selulitis", "uri": "https://kmsh-imc.org/assets/file/20180502034-2.pdf"}
        ],
        "Gangguan Saraf": [
            {"label": "Kesadaran TIA", "uri": "https://kmsh-imc.org/assets/file/20210705028-2.pdf"},
            {"label": "Rawat Saraf Wajah", "uri": "https://kmsh-imc.org/assets/file/20180502031-2.pdf"},
            {"label": "Cegah Migrain", "uri": "https://kmsh-imc.org/assets/file/20180502023-2.pdf"}
        ],
        "Kesehatan Mental": [
            {"label": "Skizofrenia", "uri": "https://kmsh-imc.org/assets/file/20180502044-2.pdf"},
            {"label": "Gangguan Mental", "uri": "https://kmsh-imc.org/assets/file/20180502043-2.pdf"},
            {"label": "Obat Psikosis", "uri": "https://kmsh-imc.org/assets/file/20180502042-2.pdf"}
        ],
        "Diabetes": [
            {"label": "Gula Darah Tinggi", "uri": "https://kmsh-imc.org/assets/file/20180502047-2.pdf"},
            {"label": "Gula Darah Rendah", "uri": "https://kmsh-imc.org/assets/file/20180502046-2.pdf"},
            {"label": "Rawat Saat Sakit", "uri": "https://kmsh-imc.org/assets/file/20180502045-2.pdf"}
        ],
        "Info Kanker": [
            {"label": "Diet Kanker Payudara", "uri": "https://kmsh-imc.org/assets/file/20210705032-2.pdf"},
            {"label": "Rawat Kanker", "uri": "https://kmsh-imc.org/assets/file/20180514020-2.pdf"},
            {"label": "Bedah Invasif", "uri": "https://kmsh-imc.org/assets/file/20210705008-2.pdf"}
        ],
        "Perawatan Kosmetik": [
            {"label": "Injeksi Botox", "uri": "https://kmsh-imc.org/assets/file/20210705042-2.pdf"},
            {"label": "Resurfacing Kulit", "uri": "https://kmsh-imc.org/assets/file/20210705037-2.pdf"},
            {"label": "Laser Er:YAG", "uri": "https://kmsh-imc.org/assets/file/20180514043-2.pdf"}
        ]
    }

    # 獲取對應topic_name的label和uri列表
    topic_info = topics_info.get(topic_name, [])
    if not topic_info:
        return None  # 如果找不到對應的topic_name，返回None或者其他處理方式

    columns = []
    for info in topic_info:
        columns.append(
            URITemplateAction(
                label=info["label"],
                uri=info["uri"]
            )
        )
    
    information_topic = TemplateSendMessage(
        alt_text='Menu Topik Edukasi Kesehatan',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    title='Kategori Edukasi Kesehatan',
                    text='Silakan pilih topik di bawah',
                    actions=columns
                )
            ]
        )
    )

    return information_topic

def info_topic_carousel_template_vn(topic_name):
    topics_info= {
        "Chăm Sóc Chung": [
            {"label": "Sau Iốt", "uri": "https://kmsh-imc.org/assets/file/20230420002-4.pdf"},
            {"label": "Phòng Đau Cơ", "uri": "https://kmsh-imc.org/assets/file/20180502040-4.pdf"},
            {"label": "Ngừa GERD", "uri": "https://kmsh-imc.org/assets/file/20180502029-4.pdf"}
        ],
        "Bệnh Tim Mạch": [
            {"label": "Liệu Pháp Sóng", "uri": "https://kmsh-imc.org/assets/file/20210705019-4.pdf"},
            {"label": "Nong Bóng Mạch", "uri": "https://kmsh-imc.org/assets/file/20210705018-4.pdf"},
            {"label": "Chăm Sóc Suy Tim", "uri": "https://kmsh-imc.org/assets/file/20210705017-4.pdf"}
        ],
        "Phẫu Thuật": [
            {"label": "Nạo Cổ Tử Cung", "uri": "https://kmsh-imc.org/assets/file/20231229001-4.pdf"},
            {"label": "Phẫu Thuật Ptosis", "uri": "https://kmsh-imc.org/assets/file/20210705035-4.pdf"},
            {"label": "Gãy Xương Mặt", "uri": "https://kmsh-imc.org/assets/file/20210705034-4.pdf"}
        ],
        "Nha Khoa": [
            {"label": "Cạo Vôi Răng", "uri": "https://kmsh-imc.org/assets/file/20180511004-4.pdf"},
            {"label": "Chăm Sóc Niềng", "uri": "https://kmsh-imc.org/assets/file/20180511003-4.pdf"}
        ],
        "Chuẩn Bị Xuất Viện": [
            {"label": "Dụng Cụ Hỗ Trợ", "uri": "https://kmsh-imc.org/assets/file/20180306018-4.pdf"}
        ],
        "Thông Tin Phẫu Thuật": [
            {"label": "Sau Nội Soi", "uri": "https://kmsh-imc.org/assets/file/20180514031-4.pdf"}
        ],
        "Hướng Dẫn Điều Dưỡng": [
            {"label": "Phòng Ngã", "uri": "https://www.kmsh.org.tw/Web/wwwKMHK/hygr_Edu/hygr/20180514019.pdf"}
        ],
        "Bệnh Da Liễu": [
            {"label": "Loét Áp Lực", "uri": "https://kmsh-imc.org/assets/file/20180306021-4.pdf"},
            {"label": "Chăm Sóc Bỏng", "uri": "https://kmsh-imc.org/assets/file/20180306020-4.pdf"},
            {"label": "Vết Thương Tay/Chân", "uri": "https://kmsh-imc.org/assets/file/20180306019-4.pdf"}
        ],
        "Vấn Đề Tai Mũi Họng": [
            {"label": "Điếc Tai", "uri": "https://kmsh-imc.org/assets/file/20180502018-4.pdf"},
            {"label": "Đau Đầu Xoang", "uri": "https://kmsh-imc.org/assets/file/20180502017-4.pdf"},
            {"label": "Ngủ Ngáy", "uri": "https://kmsh-imc.org/assets/file/20180502016-4.pdf"}
        ],
        "Ung Thư Máu": [
            {"label": "Kiểm Tra Tủy", "uri": "https://kmsh-imc.org/assets/file/20210705015-4.pdf"}
        ],
        "Rối Loạn Gan": [
            {"label": "Phẫu Thuật Tụy", "uri": "https://kmsh-imc.org/assets/file/20210705005-4.pdf"},
            {"label": "Cắt Gan", "uri": "https://kmsh-imc.org/assets/file/20180306031-4.pdf"},
            {"label": "Viêm Tụy Cấp", "uri": "https://kmsh-imc.org/assets/file/20180306030-4.pdf"}
        ],
        "Chăm Sóc Nhi Khoa": [
            {"label": "Sốt Co Giật", "uri": "https://kmsh-imc.org/assets/file/20180514016-4.pdf"},
            {"label": "Chăm Sóc Enterovirus", "uri": "https://kmsh-imc.org/assets/file/20180514015-4.pdf"},
            {"label": "Điều Trị Croup", "uri": "https://kmsh-imc.org/assets/file/20180514014-4.pdf"}
        ],
        "Tiết Niệu": [
            {"label": "Ống Dẫn Tiểu Ileum", "uri": "https://kmsh-imc.org/assets/file/20180514021-4.pdf"},
            {"label": "Tiểu Không Kiểm Soát", "uri": "https://kmsh-imc.org/assets/file/20180502005-4.pdf"},
            {"label": "Ngừa Nhiễm Trùng", "uri": "https://kmsh-imc.org/assets/file/20180502004-4.pdf"}
        ],
        "Vấn Đề Phổi": [
            {"label": "Rửa Tay", "uri": "https://kmsh-imc.org/assets/file/20231215001-4.pdf"},
            {"label": "Cách Ly Lao", "uri": "https://kmsh-imc.org/assets/file/20210705041-4.pdf"},
            {"label": "Tác Dụng Phụ Lao", "uri": "https://kmsh-imc.org/assets/file/20210705040-4.pdf"}
        ],
        "Xét Nghiệm Xâm Lấn": [
            {"label": "Sau Nội Soi Bàng Quang", "uri": "https://kmsh-imc.org/assets/file/20230420001-4.pdf"},
            {"label": "Nội Soi Phế Quản", "uri": "https://kmsh-imc.org/assets/file/20210705007-4.pdf"},
            {"label": "Chọc Hút Siêu Âm", "uri": "https://kmsh-imc.org/assets/file/20180502041-4.pdf"}
        ],
        "Chăm Sóc Cấp Cứu": [
            {"label": "Chấn Thương Trẻ Em", "uri": "https://kmsh-imc.org/assets/file/20240222001-4.pdf"},
            {"label": "Chuyển Viện", "uri": "https://kmsh-imc.org/assets/file/20210705033-4.pdf"},
            {"label": "Chuẩn Bị Phẫu Thuật", "uri": "https://kmsh-imc.org/assets/file/20180514027-4.pdf"}
        ],
        "Chăm Sóc ICU": [
            {"label": "Nội Soi Màng Phổi", "uri": "https://kmsh-imc.org/assets/file/20210705009-4.pdf"}
        ],
        "Chấn Thương": [
            {"label": "Nhận Thức Bunions", "uri": "https://kmsh-imc.org/assets/file/20210705043-4.pdf"},
            {"label": "Nắn Cột Sống", "uri": "https://kmsh-imc.org/assets/file/20210705012-4.pdf"},
            {"label": "Thay Khớp Hông", "uri": "https://kmsh-imc.org/assets/file/20210705011-4.pdf"}
        ],
        "Chăm Sóc Sức Khỏe": [
            {"label": "Nguy Hiểm Trầu Cau", "uri": "https://kmsh-imc.org/assets/file/20180814002.pdf"},
            {"label": "Bỏ Thuốc Lá", "uri": "https://kmsh-imc.org/assets/file/20180814001.pdf"}
        ],
        "Chăm Sóc Sản Phụ": [
            {"label": "Ung Thư Cổ Tử Cung", "uri": "https://kmsh-imc.org/assets/file/20180306071-4.pdf"}
        ],
        "Bệnh Truyền Nhiễm": [
            {"label": "Phòng Cúm", "uri": "https://kmsh-imc.org/assets/file/20180514030-4.pdf"},
            {"label": "Chăm Sóc Ghẻ", "uri": "https://kmsh-imc.org/assets/file/20180514029-4.pdf"},
            {"label": "Chăm Sóc Viêm Mô", "uri": "https://kmsh-imc.org/assets/file/20180502034-4.pdf"}
        ],
        "Rối Loạn Thần Kinh": [
            {"label": "Nhận Thức TIA", "uri": "https://kmsh-imc.org/assets/file/20210705028-4.pdf"},
            {"label": "Thần Kinh Mặt", "uri": "https://kmsh-imc.org/assets/file/20180502031-4.pdf"},
            {"label": "Phòng Đau Nửa Đầu", "uri": "https://kmsh-imc.org/assets/file/20180502023-4.pdf"}
        ],
        "Sức Khỏe Tinh Thần": [
            {"label": "Tâm Thần Phân Liệt", "uri": "https://kmsh-imc.org/assets/file/20180502044-4.pdf"},
            {"label": "Rối Loạn Tâm Thần", "uri": "https://kmsh-imc.org/assets/file/20180502043-4.pdf"},
            {"label": "Thuốc Loạn Thần", "uri": "https://kmsh-imc.org/assets/file/20180502042-4.pdf"}
        ],
        "Tiểu Đường": [
            {"label": "Đường Huyết Cao", "uri": "https://kmsh-imc.org/assets/file/20180502047-4.pdf"},
            {"label": "Đường Huyết Thấp", "uri": "https://kmsh-imc.org/assets/file/20180502046-4.pdf"},
            {"label": "Chăm Sóc Khi Ốm", "uri": "https://kmsh-imc.org/assets/file/20180502045-4.pdf"}
        ],
        "Thông Tin Ung Thư": [
            {"label": "Chế Độ Ăn K", "uri": "https://kmsh-imc.org/assets/file/20210705032-4.pdf"},
            {"label": "Chăm Sóc Ung Thư Vú", "uri": "https://kmsh-imc.org/assets/file/20180514020-4.pdf"},
            {"label": "Phẫu Thuật Nhỏ Gọn", "uri": "https://kmsh-imc.org/assets/file/20210705008-4.pdf"}
        ],
        "Chăm Sóc Thẩm Mỹ": [
            {"label": "Tiêm Botox", "uri": "https://kmsh-imc.org/assets/file/20210705042-4.pdf"},
            {"label": "Tái Tạo Da", "uri": "https://kmsh-imc.org/assets/file/20210705037-4.pdf"},
            {"label": "Laser Er:YAG", "uri": "https://kmsh-imc.org/assets/file/20180514043-4.pdf"}
        ]
    }


# 獲取對應topic_name的label和uri列表
    topic_info = topics_info.get(topic_name, [])
    if not topic_info:
        return None  # 如果找不到對應的topic_name，返回None或者其他處理方式

    columns = []
    for info in topic_info:
        columns.append(
            URITemplateAction(
                label=info["label"],
                uri=info["uri"]
            )
        )
    
    information_topic = TemplateSendMessage(
        alt_text='Menu Topik Edukasi Kesehatan',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    title='Kategori Edukasi Kesehatan',
                    text='Silakan pilih topik di bawah',
                    actions=columns
                )
            ]
        )
    )

    return information_topic

def info_topic_carousel_template_th(topic_name):
    topics_info = {
        "การดูแลทั่วไป": [
            {"label": "การดูแลพื้นฐาน", "uri": "https://kmsh-imc.org/assets/file/20230420002-3.pdf"},
            {"label": "ป้องกันปวดกล้ามเนื้อ", "uri": "https://kmsh-imc.org/assets/file/20180502040-3.pdf"},
            {"label": "ป้องกัน GERD", "uri": "https://kmsh-imc.org/assets/file/20180502029-3.pdf"}
        ],
        "โรคหัวใจ": [
            {"label": "รักษาคลื่น", "uri": "https://kmsh-imc.org/assets/file/20210705019-3.pdf"},
            {"label": "บอลลูนหลอดเลือด", "uri": "https://kmsh-imc.org/assets/file/20210705018-3.pdf"},
            {"label": "ดูแลหัวใจล้มเหลว", "uri": "https://kmsh-imc.org/assets/file/20210705017-3.pdf"}
        ],
        "การผ่าตัด": [
            {"label": "ขูดมดลูก", "uri": "https://kmsh-imc.org/assets/file/20231229001-3.pdf"},
            {"label": "ผ่าตัดตากระตุก", "uri": "https://kmsh-imc.org/assets/file/20210705035-3.pdf"},
            {"label": "กระดูกหน้าแตก", "uri": "https://kmsh-imc.org/assets/file/20210705034-3.pdf"}
        ],
        "ทันตกรรม": [
            {"label": "ขูดหินปูน", "uri": "https://kmsh-imc.org/assets/file/20180511004-3.pdf"},
            {"label": "ดูแลฟันจัดฟัน", "uri": "https://kmsh-imc.org/assets/file/20180511003-3.pdf"}
        ],
        "เตรียมออกจากโรงพยาบาล": [
            {"label": "อุปกรณ์ช่วย", "uri": "https://kmsh-imc.org/assets/file/20180306018-3.pdf"}
        ],
        "ข้อมูลการผ่าตัด": [
            {"label": "หลังส่องกล้อง", "uri": "https://kmsh-imc.org/assets/file/20180514031-3.pdf"}
        ],
        "แนวทางการพยาบาล": [
            {"label": "ป้องกันการล้ม", "uri": "https://www.kmsh.org.tw/Web/wwwKMHK/hygr_Edu/hygr/20180514018.pdf"}
        ],
        "โรคผิวหนัง": [
            {"label": "แผลกดทับ", "uri": "https://kmsh-imc.org/assets/file/20180306021-3.pdf"},
            {"label": "ดูแลแผลไฟไหม้", "uri": "https://kmsh-imc.org/assets/file/20180306020-3.pdf"},
            {"label": "บาดแผลที่มือ/เท้า", "uri": "https://kmsh-imc.org/assets/file/20180306019-3.pdf"}
        ],
        "ปัญหาหู คอ จมูก": [
            {"label": "ดูแลการสูญเสียการได้ยิน", "uri": "https://kmsh-imc.org/assets/file/20180502018-3.pdf"},
            {"label": "ปวดหัวและไซนัส", "uri": "https://kmsh-imc.org/assets/file/20180502017-3.pdf"},
            {"label": "ดูแลการกรน", "uri": "https://kmsh-imc.org/assets/file/20180502016-3.pdf"}
        ],
        "มะเร็งเลือด": [
            {"label": "ตรวจไขกระดูก", "uri": "https://kmsh-imc.org/assets/file/20210705015-3.pdf"}
        ],
        "โรคตับ": [
            {"label": "ผ่าตัดตับอ่อน", "uri": "https://kmsh-imc.org/assets/file/20210705005-3.pdf"},
            {"label": "ตัดตับ", "uri": "https://kmsh-imc.org/assets/file/20180306031-3.pdf"},
            {"label": "ตับอ่อนอักเสบเฉียบพลัน", "uri": "https://kmsh-imc.org/assets/file/20180306030-3.pdf"}
        ],
        "การดูแลเด็ก": [
            {"label": "ชักจากไข้", "uri": "https://kmsh-imc.org/assets/file/20180514016-3.pdf"},
            {"label": "ดูแลโรคเอนเทอโรไวรัส", "uri": "https://kmsh-imc.org/assets/file/20180514015-3.pdf"},
            {"label": "จัดการคอพอก", "uri": "https://kmsh-imc.org/assets/file/20180514014-3.pdf"}
        ],
        "ระบบปัสสาวะ": [
            {"label": "ใส่ท่อปัสสาวะ", "uri": "https://kmsh-imc.org/assets/file/20180514021-3.pdf"},
            {"label": "ปัสสาวะไม่หยุด", "uri": "https://kmsh-imc.org/assets/file/20180502005-3.pdf"},
            {"label": "ป้องกัน UTI", "uri": "https://kmsh-imc.org/assets/file/20180502004-3.pdf"}
        ],
        "ปัญหาปอด": [
            {"label": "ล้างมือ", "uri": "https://kmsh-imc.org/assets/file/20231215001-3.pdf"},
            {"label": "กักตัววัณโรค", "uri": "https://kmsh-imc.org/assets/file/20210705041-3.pdf"},
            {"label": "ผลข้างเคียงวัณโรค", "uri": "https://kmsh-imc.org/assets/file/20210705040-3.pdf"}
        ],
        "การตรวจสอบ": [
            {"label": "หลังส่องกล้องกระเพาะ", "uri": "https://kmsh-imc.org/assets/file/20230420001-3.pdf"},
            {"label": "ส่องกล้องหลอดลม", "uri": "https://kmsh-imc.org/assets/file/20210705007-3.pdf"},
            {"label": "เจาะดูดด้วยอัลตราซาวด์", "uri": "https://kmsh-imc.org/assets/file/20180502041-3.pdf"}
        ],
        "การดูแลฉุกเฉิน": [
            {"label": "บาดเจ็บศีรษะเด็ก", "uri": "https://kmsh-imc.org/assets/file/20240222001-3.pdf"},
            {"label": "คำแนะนำการส่งต่อ", "uri": "https://kmsh-imc.org/assets/file/20210705033-3.pdf"},
            {"label": "ก่อนการผ่าตัด", "uri": "https://kmsh-imc.org/assets/file/20180514027-3.pdf"}
        ],
        "การดูแล ICU": [
            {"label": "ส่องกล้องปอด", "uri": "https://kmsh-imc.org/assets/file/20210705009-3.pdf"}
        ],
        "ศัลยกรรมกระดูก": [
            {"label": "ตระหนักเกี่ยวกับ bunion", "uri": "https://kmsh-imc.org/assets/file/20210705043-3.pdf"},
            {"label": "การยึดกระดูกสันหลัง", "uri": "https://kmsh-imc.org/assets/file/20210705012-3.pdf"},
            {"label": "เปลี่ยนข้อสะโพก", "uri": "https://kmsh-imc.org/assets/file/20210705011-3.pdf"}
        ],
        "การดูแลสุขภาพ": [
            {"label": "ความเสี่ยงของกรด", "uri": "https://kmsh-imc.org/assets/file/20180814002.pdf"},
            {"label": "เลิกสูบบุหรี่", "uri": "https://kmsh-imc.org/assets/file/20180814001.pdf"}
        ],
        "การดูแลสตรี": [
            {"label": "มะเร็งปากมดลูก", "uri": "https://kmsh-imc.org/assets/file/20180306071-3.pdf"}
        ],
        "โรคติดเชื้อ": [
            {"label": "ป้องกันไข้หวัด", "uri": "https://kmsh-imc.org/assets/file/20180514030-3.pdf"},
            {"label": "รักษาโรคหิด", "uri": "https://kmsh-imc.org/assets/file/20180514029-3.pdf"},
            {"label": "รักษาเซลล์อักเสบ", "uri": "https://kmsh-imc.org/assets/file/20180502034-3.pdf"}
        ],
        "โรคระบบประสาท": [
            {"label": "ตระหนักถึง TIA", "uri": "https://kmsh-imc.org/assets/file/20210705028-3.pdf"},
            {"label": "ดูแลเส้นประสาทใบหน้า", "uri": "https://kmsh-imc.org/assets/file/20180502031-3.pdf"},
            {"label": "ป้องกันไมเกรน", "uri": "https://kmsh-imc.org/assets/file/20180502023-3.pdf"}
        ],
        "สุขภาพจิต": [
            {"label": "โรคจิตเภท", "uri": "https://kmsh-imc.org/assets/file/20180502044-3.pdf"},
            {"label": "โรคจิตเรื้อรัง", "uri": "https://kmsh-imc.org/assets/file/20180502043-3.pdf"},
            {"label": "ยาแก้ซึมเศร้า", "uri": "https://kmsh-imc.org/assets/file/20180502042-3.pdf"}
        ],
        "เบาหวาน": [
            {"label": "น้ำตาลในเลือดสูง", "uri": "https://kmsh-imc.org/assets/file/20180502047-3.pdf"},
            {"label": "น้ำตาลในเลือดต่ำ", "uri": "https://kmsh-imc.org/assets/file/20180502046-3.pdf"},
            {"label": "ดูแลเมื่อป่วย", "uri": "https://kmsh-imc.org/assets/file/20180502045-3.pdf"}
        ],
        "ข้อมูลมะเร็ง": [
            {"label": "อาหารสำหรับมะเร็งเต้านม", "uri": "https://kmsh-imc.org/assets/file/20210705032-3.pdf"},
            {"label": "ดูแลมะเร็งเต้านม", "uri": "https://kmsh-imc.org/assets/file/20180514020-3.pdf"},
            {"label": "การผ่าตัดแบบน้อย", "uri": "https://kmsh-imc.org/assets/file/20210705008-3.pdf"}
        ],
        "การดูแลความงาม": [
            {"label": "ฉีดโบท็อกซ์", "uri": "https://kmsh-imc.org/assets/file/20210705042-3.pdf"},
            {"label": "การฟื้นฟูผิว", "uri": "https://kmsh-imc.org/assets/file/20210705037-3.pdf"},
            {"label": "เลเซอร์ Er:YAG", "uri": "https://kmsh-imc.org/assets/file/20180514043-3.pdf"}
        ]
    }

# 獲取對應topic_name的label和uri列表
    topic_info = topics_info.get(topic_name, [])
    if not topic_info:
        return None  # 如果找不到對應的topic_name，返回None或者其他處理方式

    columns = []
    for info in topic_info:
        columns.append(
            URITemplateAction(
                label=info["label"],
                uri=info["uri"]
            )
        )
    
    information_topic = TemplateSendMessage(
        alt_text='Menu Topik Edukasi Kesehatan',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    title='Kategori Edukasi Kesehatan',
                    text='Silakan pilih topik di bawah',
                    actions=columns
                )
            ]
        )
    )

    return information_topic
