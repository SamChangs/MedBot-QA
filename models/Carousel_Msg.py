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
                            label='腎臟疾病',
                            text='腎臟疾病'
                        )
                    ]
                ),
                CarouselColumn(
                    title='衛教資訊選單-8/10',
                    text='請選擇以下',
                    actions=[
                        MessageTemplateAction(
                            label='感染疾病',
                            text='感染疾病'
                        ),
                        MessageTemplateAction(
                            label='腸胃疾病',
                            text='腸胃疾病'
                        ),
                        MessageTemplateAction(
                            label='腦神經系統疾病',
                            text='腦神經系統疾病'
                        )
                    ]
                ),
                CarouselColumn(
                    title='衛教資訊選單-9/10',
                    text='請選擇以下',
                    actions=[
                        MessageTemplateAction(
                            label='精神科疾病',
                            text='精神科疾病'
                        ),
                        MessageTemplateAction(
                            label='糖尿病疾病',
                            text='糖尿病疾病'
                        ),
                        MessageTemplateAction(
                            label='營養衛教單張',
                            text='營養衛教單張'
                        )
                    ]
                ),
                CarouselColumn(
                    title='衛教資訊選單-10/10',
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
                )
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
                        label='Blood Cancer',
                        text='Blood Cancer'
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
                        label='Kidney Issues',
                        text='Kidney Issues'
                    )
                ]
            ),
            CarouselColumn(
                title='Health Education-8/10',
                text='Choose a topic below',
                actions=[
                    MessageTemplateAction(
                        label='Infectious Diseases',
                        text='Infectious Diseases'
                    ),
                    MessageTemplateAction(
                        label='GI Disorders',
                        text='GI Disorders'
                    ),
                    MessageTemplateAction(
                        label='Neurological',
                        text='Neurological'
                    )
                ]
            ),
            CarouselColumn(
                title='Health Education-9/10',
                text='Choose a topic below',
                actions=[
                    MessageTemplateAction(
                        label='Mental Health',
                        text='Mental Health'
                    ),
                    MessageTemplateAction(
                        label='Diabetes',
                        text='Diabetes'
                    ),
                    MessageTemplateAction(
                        label='Nutrition Info',
                        text='Nutrition Info'
                    )
                ]
            ),
            CarouselColumn(
                title='Health Education-10/10',
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
            )
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
                        label='Masalah Ginjal',
                        text='Masalah Ginjal'
                    )
                ]
            ),
            CarouselColumn(
                title='Pendidikan Kesehatan-8/10',
                text='Pilih topik di bawah',
                actions=[
                    MessageTemplateAction(
                        label='Penyakit Menular',
                        text='Penyakit Menular'
                    ),
                    MessageTemplateAction(
                        label='Gangguan Pencernaan',
                        text='Gangguan Pencernaan'
                    ),
                    MessageTemplateAction(
                        label='Gangguan Saraf',
                        text='Gangguan Saraf'
                    )
                ]
            ),
            CarouselColumn(
                title='Pendidikan Kesehatan-9/10',
                text='Pilih topik di bawah',
                actions=[
                    MessageTemplateAction(
                        label='Kesehatan Mental',
                        text='Kesehatan Mental'
                    ),
                    MessageTemplateAction(
                        label='Diabetes',
                        text='Diabetes'
                    ),
                    MessageTemplateAction(
                        label='Info Nutrisi',
                        text='Info Nutrisi'
                    )
                ]
            ),
            CarouselColumn(
                title='Pendidikan Kesehatan-10/10',
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
            )
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
                        label='Vấn Đề Thận',
                        text='Vấn Đề Thận'
                    )
                ]
            ),
            CarouselColumn(
                title='Giáo Dục Sức Khỏe-8/10',
                text='Chọn một chủ đề dưới đây',
                actions=[
                    MessageTemplateAction(
                        label='Bệnh Truyền Nhiễm',
                        text='Bệnh Truyền Nhiễm'
                    ),
                    MessageTemplateAction(
                        label='Rối Loạn Tiêu Hóa',
                        text='Rối Loạn Tiêu Hóa'
                    ),
                    MessageTemplateAction(
                        label='Rối Loạn Thần Kinh',
                        text='Rối Loạn Thần Kinh'
                    )
                ]
            ),
            CarouselColumn(
                title='Giáo Dục Sức Khỏe-9/10',
                text='Chọn một chủ đề dưới đây',
                actions=[
                    MessageTemplateAction(
                        label='Sức Khỏe Tinh Thần',
                        text='Sức Khỏe Tinh Thần'
                    ),
                    MessageTemplateAction(
                        label='Tiểu Đường',
                        text='Tiểu Đường'
                    ),
                    MessageTemplateAction(
                        label='Thông Tin Dinh Dưỡng',
                        text='Thông Tin Dinh Dưỡng'
                    )
                ]
            ),
            CarouselColumn(
                title='Giáo Dục Sức Khỏe-10/10',
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
            )
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
                        label='ปัญหาไต',
                        text='ปัญหาไต'
                    )
                ]
            ),
            CarouselColumn(
                title='การศึกษาเรื่องสุขภาพ-8/10',
                text='เลือกหัวข้อด้านล่าง',
                actions=[
                    MessageTemplateAction(
                        label='โรคติดเชื้อ',
                        text='โรคติดเชื้อ'
                    ),
                    MessageTemplateAction(
                        label='โรคทางเดินอาหาร',
                        text='โรคทางเดินอาหาร'
                    ),
                    MessageTemplateAction(
                        label='โรคระบบประสาท',
                        text='โรคระบบประสาท'
                    )
                ]
            ),
            CarouselColumn(
                title='การศึกษาเรื่องสุขภาพ-9/10',
                text='เลือกหัวข้อด้านล่าง',
                actions=[
                    MessageTemplateAction(
                        label='สุขภาพจิต',
                        text='สุขภาพจิต'
                    ),
                    MessageTemplateAction(
                        label='เบาหวาน',
                        text='เบาหวาน'
                    ),
                    MessageTemplateAction(
                        label='ข้อมูลโภชนาการ',
                        text='ข้อมูลโภชนาการ'
                    )
                ]
            ),
            CarouselColumn(
                title='การศึกษาเรื่องสุขภาพ-10/10',
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
            )
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
        {"label": "高血壓居家自我照顧", "uri": "https://kmsh-imc.org/assets/file/20180502022.pdf"},
        {"label": "心肌梗塞復健運動衛教", "uri": "https://kmsh-imc.org/assets/file/20180306015.pdf"}
    ],
    "手術相關": [
        {"label": "靜脈注射含碘顯影劑檢查後衛教", "uri": "https://kmsh-imc.org/assets/file/20230420002.pdf"},
        {"label": "生活保健之預防痠痛衛教", "uri": "https://kmsh-imc.org/assets/file/20180502040.pdf"},
        {"label": "預防胃食道逆流衛教", "uri": "https://kmsh-imc.org/assets/file/20180502029.pdf"}
    ],
    "牙科": [
        {"label": "靜脈注射含碘顯影劑檢查後衛教", "uri": "https://kmsh-imc.org/assets/file/20230420002.pdf"},
        {"label": "生活保健之預防痠痛衛教", "uri": "https://kmsh-imc.org/assets/file/20180502040.pdf"},
        {"label": "預防胃食道逆流衛教", "uri": "https://kmsh-imc.org/assets/file/20180502029.pdf"}
    ],
    "出院準備": [
        {"label": "認識心臟震波治療", "uri": "https://kmsh-imc.org/assets/file/20210705019.pdf"},
    ],
    "外科": [
        {"label": "靜脈注射含碘顯影劑檢查後衛教", "uri": "https://kmsh-imc.org/assets/file/20230420002.pdf"},
        {"label": "生活保健之預防痠痛衛教", "uri": "https://kmsh-imc.org/assets/file/20180502040.pdf"},
        {"label": "預防胃食道逆流衛教", "uri": "https://kmsh-imc.org/assets/file/20180502029.pdf"}
    ],
    "外語護理指導": [
        {"label": "靜脈注射含碘顯影劑檢查後衛教", "uri": "https://kmsh-imc.org/assets/file/20230420002.pdf"},
        {"label": "生活保健之預防痠痛衛教", "uri": "https://kmsh-imc.org/assets/file/20180502040.pdf"},
        {"label": "預防胃食道逆流衛教", "uri": "https://kmsh-imc.org/assets/file/20180502029.pdf"}
    ],
    "皮膚疾病": [
        {"label": "認識心臟震波治療", "uri": "https://kmsh-imc.org/assets/file/20210705019.pdf"},
        {"label": "高血壓居家自我照顧", "uri": "https://kmsh-imc.org/assets/file/20180502022.pdf"},
        {"label": "心肌梗塞復健運動衛教", "uri": "https://kmsh-imc.org/assets/file/20180306015.pdf"}
    ],
    "耳鼻喉疾病": [
        {"label": "靜脈注射含碘顯影劑檢查後衛教", "uri": "https://kmsh-imc.org/assets/file/20230420002.pdf"},
        {"label": "生活保健之預防痠痛衛教", "uri": "https://kmsh-imc.org/assets/file/20180502040.pdf"},
        {"label": "預防胃食道逆流衛教", "uri": "https://kmsh-imc.org/assets/file/20180502029.pdf"}
    ],
    "血液腫瘤": [
        {"label": "靜脈注射含碘顯影劑檢查後衛教", "uri": "https://kmsh-imc.org/assets/file/20230420002.pdf"},
        {"label": "生活保健之預防痠痛衛教", "uri": "https://kmsh-imc.org/assets/file/20180502040.pdf"},
        {"label": "預防胃食道逆流衛教", "uri": "https://kmsh-imc.org/assets/file/20180502029.pdf"}
    ],
    "肝膽疾病": [
        {"label": "認識心臟震波治療", "uri": "https://kmsh-imc.org/assets/file/20210705019.pdf"},
        {"label": "高血壓居家自我照顧", "uri": "https://kmsh-imc.org/assets/file/20180502022.pdf"},
        {"label": "心肌梗塞復健運動衛教", "uri": "https://kmsh-imc.org/assets/file/20180306015.pdf"}
    ],
    "兒科疾病": [
        {"label": "靜脈注射含碘顯影劑檢查後衛教", "uri": "https://kmsh-imc.org/assets/file/20230420002.pdf"},
        {"label": "生活保健之預防痠痛衛教", "uri": "https://kmsh-imc.org/assets/file/20180502040.pdf"},
        {"label": "預防胃食道逆流衛教", "uri": "https://kmsh-imc.org/assets/file/20180502029.pdf"}
    ],
    "泌尿疾病": [
        {"label": "靜脈注射含碘顯影劑檢查後衛教", "uri": "https://kmsh-imc.org/assets/file/20230420002.pdf"},
        {"label": "生活保健之預防痠痛衛教", "uri": "https://kmsh-imc.org/assets/file/20180502040.pdf"},
        {"label": "預防胃食道逆流衛教", "uri": "https://kmsh-imc.org/assets/file/20180502029.pdf"}
    ],
    "肺部、胸腔疾病": [
        {"label": "認識心臟震波治療", "uri": "https://kmsh-imc.org/assets/file/20210705019.pdf"},
        {"label": "高血壓居家自我照顧", "uri": "https://kmsh-imc.org/assets/file/20180502022.pdf"},
        {"label": "心肌梗塞復健運動衛教", "uri": "https://kmsh-imc.org/assets/file/20180306015.pdf"}
    ],
    "侵入性檢查相關": [
        {"label": "靜脈注射含碘顯影劑檢查後衛教", "uri": "https://kmsh-imc.org/assets/file/20230420002.pdf"},
        {"label": "生活保健之預防痠痛衛教", "uri": "https://kmsh-imc.org/assets/file/20180502040.pdf"},
        {"label": "預防胃食道逆流衛教", "uri": "https://kmsh-imc.org/assets/file/20180502029.pdf"}
    ],    
    "急診相關": [
        {"label": "靜脈注射含碘顯影劑檢查後衛教", "uri": "https://kmsh-imc.org/assets/file/20230420002.pdf"},
        {"label": "生活保健之預防痠痛衛教", "uri": "https://kmsh-imc.org/assets/file/20180502040.pdf"},
        {"label": "預防胃食道逆流衛教", "uri": "https://kmsh-imc.org/assets/file/20180502029.pdf"}
    ],
    "重症加護": [
        {"label": "認識心臟震波治療", "uri": "https://kmsh-imc.org/assets/file/20210705019.pdf"},
        {"label": "高血壓居家自我照顧", "uri": "https://kmsh-imc.org/assets/file/20180502022.pdf"},
        {"label": "心肌梗塞復健運動衛教", "uri": "https://kmsh-imc.org/assets/file/20180306015.pdf"}
    ],
    "骨科疾病": [
        {"label": "靜脈注射含碘顯影劑檢查後衛教", "uri": "https://kmsh-imc.org/assets/file/20230420002.pdf"},
        {"label": "生活保健之預防痠痛衛教", "uri": "https://kmsh-imc.org/assets/file/20180502040.pdf"},
        {"label": "預防胃食道逆流衛教", "uri": "https://kmsh-imc.org/assets/file/20180502029.pdf"}
    ],
    "健康保健": [
        {"label": "靜脈注射含碘顯影劑檢查後衛教", "uri": "https://kmsh-imc.org/assets/file/20230420002.pdf"},
        {"label": "生活保健之預防痠痛衛教", "uri": "https://kmsh-imc.org/assets/file/20180502040.pdf"},
        {"label": "預防胃食道逆流衛教", "uri": "https://kmsh-imc.org/assets/file/20180502029.pdf"}
    ],
    "產科、婦科疾病": [
        {"label": "認識心臟震波治療", "uri": "https://kmsh-imc.org/assets/file/20210705019.pdf"},
        {"label": "高血壓居家自我照顧", "uri": "https://kmsh-imc.org/assets/file/20180502022.pdf"},
        {"label": "心肌梗塞復健運動衛教", "uri": "https://kmsh-imc.org/assets/file/20180306015.pdf"}
    ],
    "腎臟疾病": [
        {"label": "靜脈注射含碘顯影劑檢查後衛教", "uri": "https://kmsh-imc.org/assets/file/20230420002.pdf"},
        {"label": "生活保健之預防痠痛衛教", "uri": "https://kmsh-imc.org/assets/file/20180502040.pdf"},
        {"label": "預防胃食道逆流衛教", "uri": "https://kmsh-imc.org/assets/file/20180502029.pdf"}
    ],
    "感染疾病": [
        {"label": "認識心臟震波治療", "uri": "https://kmsh-imc.org/assets/file/20210705019.pdf"},
        {"label": "高血壓居家自我照顧", "uri": "https://kmsh-imc.org/assets/file/20180502022.pdf"},
        {"label": "心肌梗塞復健運動衛教", "uri": "https://kmsh-imc.org/assets/file/20180306015.pdf"}
    ],
    "腸胃疾病": [
        {"label": "靜脈注射含碘顯影劑檢查後衛教", "uri": "https://kmsh-imc.org/assets/file/20230420002.pdf"},
        {"label": "生活保健之預防痠痛衛教", "uri": "https://kmsh-imc.org/assets/file/20180502040.pdf"},
        {"label": "預防胃食道逆流衛教", "uri": "https://kmsh-imc.org/assets/file/20180502029.pdf"}
    ],
    "腦神經系統疾病": [
        {"label": "靜脈注射含碘顯影劑檢查後衛教", "uri": "https://kmsh-imc.org/assets/file/20230420002.pdf"},
        {"label": "生活保健之預防痠痛衛教", "uri": "https://kmsh-imc.org/assets/file/20180502040.pdf"},
        {"label": "預防胃食道逆流衛教", "uri": "https://kmsh-imc.org/assets/file/20180502029.pdf"}
    ],
    "精神科疾病": [
        {"label": "認識心臟震波治療", "uri": "https://kmsh-imc.org/assets/file/20210705019.pdf"},
        {"label": "高血壓居家自我照顧", "uri": "https://kmsh-imc.org/assets/file/20180502022.pdf"},
        {"label": "心肌梗塞復健運動衛教", "uri": "https://kmsh-imc.org/assets/file/20180306015.pdf"}
    ],
    "糖尿病疾病": [
        {"label": "靜脈注射含碘顯影劑檢查後衛教", "uri": "https://kmsh-imc.org/assets/file/20230420002.pdf"},
        {"label": "生活保健之預防痠痛衛教", "uri": "https://kmsh-imc.org/assets/file/20180502040.pdf"},
        {"label": "預防胃食道逆流衛教", "uri": "https://kmsh-imc.org/assets/file/20180502029.pdf"}
    ],
    "營養衛教單張": [
        {"label": "靜脈注射含碘顯影劑檢查後衛教", "uri": "https://kmsh-imc.org/assets/file/20230420002.pdf"},
        {"label": "生活保健之預防痠痛衛教", "uri": "https://kmsh-imc.org/assets/file/20180502040.pdf"},
        {"label": "預防胃食道逆流衛教", "uri": "https://kmsh-imc.org/assets/file/20180502029.pdf"}
    ],
    "癌症相關": [
        {"label": "認識心臟震波治療", "uri": "https://kmsh-imc.org/assets/file/20210705019.pdf"},
        {"label": "高血壓居家自我照顧", "uri": "https://kmsh-imc.org/assets/file/20180502022.pdf"},
        {"label": "心肌梗塞復健運動衛教", "uri": "https://kmsh-imc.org/assets/file/20180306015.pdf"}
    ],
    "醫療美容": [
        {"label": "靜脈注射含碘顯影劑檢查後衛教", "uri": "https://kmsh-imc.org/assets/file/20230420002.pdf"},
        {"label": "生活保健之預防痠痛衛教", "uri": "https://kmsh-imc.org/assets/file/20180502040.pdf"},
        {"label": "預防胃食道逆流衛教", "uri": "https://kmsh-imc.org/assets/file/20180502029.pdf"}
    ],
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