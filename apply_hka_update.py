import sqlite3
import datetime

conn = sqlite3.connect('/Users/alenpak/Desktop/kato/db.sqlite3')
c = conn.cursor()

# 1. Archive September conference in events
sept_slugs = ('conf-2026', 'conf-2026-astana', 'upcoming-scientific-conference-2026')
c.execute(f"UPDATE webkato_event SET is_active = 0 WHERE slug IN {sept_slugs};")
print(f"Archived September events, updated rows: {c.rowcount}")

# 2. Add HKA 2026 Event
hka_desc = """
<div class="hka-announcement">
    <div class="card border-0 shadow-sm rounded-4 mb-4" style="background: linear-gradient(135deg, #f0fdf4 0%, #e8f5e9 100%); border-left: 5px solid #198754 !important;">
        <div class="card-body p-4">
            <span class="badge bg-success mb-2 px-3 py-2 rounded-pill fw-semibold">HKA 2026</span>
            <h4 class="fw-bold mb-3 text-dark">Международная научно-практическая конференция</h4>
            <h5 class="fw-bold mb-3 text-primary">«Сложное эндопротезирование тазобедренного и коленного суставов в 2026 году: решённые вопросы, вызовы, перспективы и извлечённые уроки»</h5>
            <p class="lead mb-0">Приглашаем вас принять участие в международной научно-образовательной конференции <strong>«Complex Hip and Knee Arthroplasty in 2026: Solved Issues, Challenges, Perspectives, and Lessons Learned»</strong> (HKA 2026), которая состоится 30–31 октября 2026 года в городе Астане.</p>
        </div>
    </div>

    <div class="card border-0 shadow-sm rounded-4 mb-4 bg-light">
        <div class="card-body p-4">
            <h5 class="fw-bold text-primary mb-3"><i class="bi bi-award-fill me-2 text-warning"></i>Почётный приглашённый спикер</h5>
            <div>
                <h6 class="fw-bold mb-1 fs-5">Профессор Javad Parvizi (Джавад Парвизи)</h6>
                <p class="text-muted mb-0">Всемирно признанный эксперт в области эндопротезирования тазобедренного и коленного суставов и перипротезной инфекции (h-index 169, более 1000 научных публикаций).</p>
            </div>
        </div>
    </div>

    <div class="row g-4 mb-4">
        <div class="col-md-6">
            <div class="h-100 p-4 rounded-4 bg-light shadow-sm">
                <h5 class="fw-bold text-primary mb-3"><i class="bi bi-geo-alt-fill me-2"></i>Программа и локации</h5>
                <ul class="list-unstyled mb-0">
                    <li class="mb-3">
                        <strong class="text-dark d-block">📅 30 октября 2026 г.:</strong>
                        <span>ННЦТО им. акад. Н.Д. Батпенова (г. Астана, пр. Абылай хана, 15а) — мастер-классы и Live Surgery</span>
                    </li>
                    <li class="mb-0">
                        <strong class="text-dark d-block">📅 31 октября 2026 г.:</strong>
                        <span>Wyndham Garden Astana (г. Астана, пр. Хусейн бен Талал, 25) — научно-образовательная конференция</span>
                    </li>
                </ul>
            </div>
        </div>
        <div class="col-md-6">
            <div class="h-100 p-4 rounded-4 bg-light shadow-sm">
                <h5 class="fw-bold text-primary mb-3"><i class="bi bi-check2-circle me-2"></i>Ключевые темы</h5>
                <ul class="list-unstyled small mb-0">
                    <li class="mb-2"><i class="bi bi-dot text-primary fs-5"></i>Сложное первичное и ревизионное эндопротезирование суставов</li>
                    <li class="mb-2"><i class="bi bi-dot text-primary fs-5"></i>Перипротезная инфекция: современные алгоритмы диагностики и лечения</li>
                    <li class="mb-2"><i class="bi bi-dot text-primary fs-5"></i>Остеотомии и костная пластика при дефектах</li>
                    <li class="mb-2"><i class="bi bi-dot text-primary fs-5"></i>3D-технологии, робототехника и навигация</li>
                    <li class="mb-0"><i class="bi bi-dot text-primary fs-5"></i>Реабилитация и профилактика осложнений</li>
                </ul>
            </div>
        </div>
    </div>

    <div class="alert alert-primary rounded-4 border-0 shadow-sm p-4 mb-4 d-flex flex-column flex-md-row align-items-center justify-content-between gap-3">
        <div>
            <h5 class="fw-bold mb-1"><i class="bi bi-globe me-2"></i>Официальный сайт конференции</h5>
            <p class="mb-0 text-muted">Ознакомьтесь с подробной программой, спикерами и условиями участия на сайте конференции.</p>
        </div>
        <a href="https://arthroplasty.kz/ru" target="_blank" rel="noopener noreferrer" class="btn btn-primary rounded-pill px-4 py-2 text-nowrap fw-semibold shadow-sm">
            <i class="bi bi-box-arrow-up-right me-2"></i>Перейти на сайт конференции
        </a>
    </div>
</div>
""".strip()

hka_title = 'Международная научно-практическая конференция «Сложное эндопротезирование тазобедренного и коленного суставов в 2026 году: решённые вопросы, вызовы, перспективы и извлечённые уроки»'
hka_slug = 'hka-2026'
hka_date = '2026-10-30 04:00:00'
hka_date_text = '30–31 октября 2026 г.'
hka_location = 'г. Астана (ННЦТО им. акад. Н.Д. Батпенова / Wyndham Garden Astana)'
hka_link = 'https://arthroplasty.kz/ru'
hka_img = 'events/hka_2026_banner.jpg'

c.execute("SELECT id FROM webkato_event WHERE slug = ?", (hka_slug,))
row = c.fetchone()
if row:
    c.execute("""
        UPDATE webkato_event 
        SET title = ?, date = ?, date_text = ?, location = ?, description = ?, external_link = ?, image = ?, is_active = 1, is_international = 0
        WHERE slug = ?
    """, (hka_title, hka_date, hka_date_text, hka_location, hka_desc, hka_link, hka_img, hka_slug))
    print(f"Updated event {hka_slug}")
else:
    c.execute("""
        INSERT INTO webkato_event (title, slug, date, date_text, location, description, external_link, image, is_active, is_international)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, 1, 0)
    """, (hka_title, hka_slug, hka_date, hka_date_text, hka_location, hka_desc, hka_link, hka_img))
    print(f"Inserted event {hka_slug}")

# 3. Add HKA 2026 News
news_title = 'Международная научно-практическая конференция «Сложное эндопротезирование тазобедренного и коленного суставов в 2026 году: решённые вопросы, вызовы, перспективы и извлечённые уроки» (HKA 2026)'
news_slug = 'hka-2026-announcement'
news_img = 'news/hka_2026_banner.jpg'
now_str = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# Find category_id for conferences (usually 2)
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
    """, (news_title, cat_id, news_img, hka_desc, now_str, news_slug))
    print(f"Updated news {news_slug}")
else:
    c.execute("""
        INSERT INTO webkato_news (title, slug, category_id, image, content, created_at, is_published)
        VALUES (?, ?, ?, ?, ?, ?, 1)
    """, (news_title, news_slug, cat_id, news_img, hka_desc, now_str))
    print(f"Inserted news {news_slug}")

# Ensure September news exists in news list/archive
c.execute("SELECT id FROM webkato_news WHERE slug = 'news-conf-2026-astana'")
s_news = c.fetchone()
if not s_news:
    c.execute("""
        INSERT INTO webkato_news (title, slug, category_id, image, content, created_at, is_published)
        VALUES (?, 'news-conf-2026-astana', ?, 'events/conf2026.jpg', 
        'XIII Международная научно-практическая конференция «Междисциплинарная травматология и ортопедия: от диагностики к реабилитации», 10-11 сентября 2026 г., г. Астана.',
        '2026-09-01 10:00:00', 1)
    """, ('XIII Международная научно-практическая конференция «Междисциплинарная травматология и ортопедия: от диагностики к реабилитации»', cat_id))
    print("Inserted September conference news into archive")
else:
    c.execute("UPDATE webkato_news SET is_published = 1 WHERE slug = 'news-conf-2026-astana'")
    print("Ensured September conference news is published in archive")

# Record migration 0018 as applied in sqlite
c.execute("SELECT id FROM django_migrations WHERE app = 'webkato' AND name = '0018_hka_2026_and_archive_september'")
if not c.fetchone():
    c.execute("INSERT INTO django_migrations (app, name, applied) VALUES ('webkato', '0018_hka_2026_and_archive_september', ?)", (now_str,))
    print("Recorded migration 0018 in django_migrations")

conn.commit()
conn.close()
print("All DB operations completed successfully.")
