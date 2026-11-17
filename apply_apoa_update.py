import sqlite3
import datetime

conn = sqlite3.connect('db.sqlite3')
c = conn.cursor()

# 1. Archive HKA 2026 conference so it moves to past congresses / archive
c.execute("UPDATE webkato_event SET is_active = 0 WHERE slug = 'hka-2026';")
print(f'Archived HKA 2026 event, updated rows: {c.rowcount}')

# 2. Detailed description for APOA 2027
apoa_desc = """
<div class="apoa-announcement">
    <div class="card border-0 shadow-sm rounded-4 mb-4" style="background: linear-gradient(135deg, #f0fdf4 0%, #e8f5e9 100%); border-left: 5px solid #0d6efd !important;">
        <div class="card-body p-4">
            <div class="d-flex align-items-center gap-2 mb-2">
                <span class="badge bg-primary px-3 py-2 rounded-pill fw-semibold">APOA 2027</span>
                <span class="badge bg-danger px-3 py-2 rounded-pill fw-semibold">Тайбэй, Тайвань</span>
            </div>
            <h4 class="fw-bold mb-2 text-dark">26-й Конгресс Азиатско-Тихоокеанской ортопедической ассоциации</h4>
            <h5 class="fw-bold mb-3 text-primary">The 26th Congress of the Asia Pacific Orthopaedic Association (APOA 2027)</h5>
            <p class="lead mb-0 text-dark">Приглашаем травматологов, ортопедов, хирургов и исследователей Казахстана принять участие в 26-м Конгрессе Азиатско-Тихоокеанской ортопедической ассоциации (<strong>APOA 2027</strong>), который пройдет с <strong>21 по 24 апреля 2027 года</strong> в городе <strong>Тайбэй (Тайвань)</strong> в конгресс-отеле <strong>Taipei Marriott Hotel</strong>.</p>
        </div>
    </div>

    <div class="card border-0 shadow-sm rounded-4 mb-4 bg-light">
        <div class="card-body p-4">
            <h5 class="fw-bold text-primary mb-3"><i class="bi bi-people-fill me-2 text-primary"></i>О конгрессе и партнерстве с TOA</h5>
            <p class="text-dark mb-0">
                26-й Конгресс APOA проводится совместно с <strong>50-й юбилейной конференцией Тайваньской ортопедической ассоциации (Taiwan Orthopaedic Association — TOA)</strong>. Это крупнейшее международное научно-практическое событие года в Азиатско-Тихоокеанском регионе, объединяющее ведущих мировых экспертов, инновационные технологии хирургии и передовые клинические исследования.
            </p>
        </div>
    </div>

    <div class="row g-4 mb-4">
        <div class="col-md-6">
            <div class="h-100 p-4 rounded-4 bg-light shadow-sm">
                <h5 class="fw-bold text-primary mb-3"><i class="bi bi-geo-alt-fill me-2"></i>Даты и локация</h5>
                <ul class="list-unstyled mb-0">
                    <li class="mb-3">
                        <strong class="text-dark d-block">📅 Даты проведения:</strong>
                        <span>21 – 24 апреля 2027 года</span>
                    </li>
                    <li class="mb-3">
                        <strong class="text-dark d-block">📍 Место проведения:</strong>
                        <span>Taipei Marriott Hotel (г. Тайбэй, Тайвань)</span>
                    </li>
                    <li class="mb-0">
                        <strong class="text-dark d-block">🏛️ Организаторы:</strong>
                        <span>Asia Pacific Orthopaedic Association (APOA) & Taiwan Orthopaedic Association (TOA)</span>
                    </li>
                </ul>
            </div>
        </div>
        <div class="col-md-6">
            <div class="h-100 p-4 rounded-4 bg-light shadow-sm">
                <h5 class="fw-bold text-primary mb-3"><i class="bi bi-journal-medical me-2"></i>Ключевые секции и направления</h5>
                <ul class="list-unstyled small mb-0">
                    <li class="mb-2"><i class="bi bi-dot text-primary fs-5"></i>Эндопротезирование тазобедренного и коленного суставов (Arthroplasty)</li>
                    <li class="mb-2"><i class="bi bi-dot text-primary fs-5"></i>Травматология и политравма (Trauma & Fracture Care)</li>
                    <li class="mb-2"><i class="bi bi-dot text-primary fs-5"></i>Хирургия стопы и голеностопного сустава (APOA Foot & Ankle Council)</li>
                    <li class="mb-2"><i class="bi bi-dot text-primary fs-5"></i>Перипротезная инфекция и осложнения (APOA Infection Section)</li>
                    <li class="mb-2"><i class="bi bi-dot text-primary fs-5"></i>Детская ортопедия (Asia Pacific Paediatric Orthopaedic Society)</li>
                    <li class="mb-2"><i class="bi bi-dot text-primary fs-5"></i>Хирургия позвоночника и спортивная медицина (Spine & Sports Medicine)</li>
                    <li class="mb-0"><i class="bi bi-dot text-primary fs-5"></i>Форум молодых хирургов (APOA Young Surgeons Forum)</li>
                </ul>
            </div>
        </div>
    </div>

    <div class="alert alert-primary rounded-4 border-0 shadow-sm p-4 mb-4 d-flex flex-column flex-md-row align-items-center justify-content-between gap-3">
        <div>
            <h5 class="fw-bold mb-1"><i class="bi bi-globe me-2"></i>Официальный сайт конгресса APOA 2027</h5>
            <p class="mb-0 text-muted">Регистрация участников, подача тезисов, информация об отелях и визовая поддержка доступны на официальном сайте.</p>
        </div>
        <a href="https://apoa2027.org/" target="_blank" rel="noopener noreferrer" class="btn btn-primary rounded-pill px-4 py-2 text-nowrap fw-semibold shadow-sm">
            <i class="bi bi-box-arrow-up-right me-2"></i>Перейти на сайт apoa2027.org
        </a>
    </div>
</div>
""".strip()

apoa_title = '26-й Конгресс Азиатско-Тихоокеанской ортопедической ассоциации (APOA 2027)'
apoa_slug = 'apoa-2027'
apoa_date = '2027-04-21 09:00:00'
apoa_date_text = '21–24 апреля 2027 г.'
apoa_location = 'Тайбэй, Тайвань (Taipei Marriott Hotel)'
apoa_link = 'https://apoa2027.org/'
apoa_img = 'events/apoa_2027_banner.jpg'

c.execute("SELECT id FROM webkato_event WHERE slug = ?", (apoa_slug,))
row = c.fetchone()
if row:
    c.execute("""
        UPDATE webkato_event 
        SET title = ?, date = ?, date_text = ?, location = ?, description = ?, external_link = ?, image = ?, is_active = 1, is_international = 0
        WHERE slug = ?
    """, (apoa_title, apoa_date, apoa_date_text, apoa_location, apoa_desc, apoa_link, apoa_img, apoa_slug))
    print(f"Updated event {apoa_slug}")
else:
    c.execute("""
        INSERT INTO webkato_event (title, slug, date, date_text, location, description, external_link, image, is_active, is_international)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, 1, 0)
    """, (apoa_title, apoa_slug, apoa_date, apoa_date_text, apoa_location, apoa_desc, apoa_link, apoa_img))
    print(f"Inserted event {apoa_slug}")

# 3. Add APOA 2027 News
news_title = '26-й Конгресс Азиатско-Тихоокеанской ортопедической ассоциации (APOA 2027) в Тайбэе'
news_slug = 'apoa-2027-taipei-announcement'
news_img = 'news/apoa_2027_banner.jpg'
now_str = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

c.execute("SELECT id FROM webkato_newscategory WHERE slug = 'conferences' OR slug = 'news' LIMIT 1")
cat_row = c.fetchone()
cat_id = cat_row[0] if cat_row else 1

c.execute("SELECT id FROM webkato_news WHERE slug = ?", (news_slug,))
nrow = c.fetchone()
if nrow:
    c.execute("""
        UPDATE webkato_news
        SET title = ?, category_id = ?, image = ?, content = ?, is_published = 1, created_at = ?
        WHERE slug = ?
    """, (news_title, cat_id, news_img, apoa_desc, now_str, news_slug))
    print(f"Updated news {news_slug}")
else:
    c.execute("""
        INSERT INTO webkato_news (title, slug, category_id, image, content, created_at, is_published)
        VALUES (?, ?, ?, ?, ?, ?, 1)
    """, (news_title, news_slug, cat_id, news_img, apoa_desc, now_str))
    print(f"Inserted news {news_slug}")

# 4. Record migration 0019 as applied in django_migrations
c.execute("SELECT id FROM django_migrations WHERE app = 'webkato' AND name = '0019_apoa_2027_and_archive_hka_2026'")
if not c.fetchone():
    c.execute("INSERT INTO django_migrations (app, name, applied) VALUES ('webkato', '0019_apoa_2027_and_archive_hka_2026', ?)", (now_str,))
    print("Recorded migration 0019 in django_migrations")

conn.commit()
conn.close()
print("All DB operations completed successfully.")
