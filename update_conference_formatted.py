import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from webkato.models import Event

def update_conference():
    slug = 'conf-2026-astana'
    
    # Matching the specific event
    event = Event.objects.filter(slug=slug).first()
    
    if not event:
        print("Event not found!")
        return

    formatted_description = """
<div class="announcement-content">
    <div class="card border-0 shadow-sm rounded-4 mb-4" style="background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%); border-left: 5px solid #0d6efd !important;">
        <div class="card-body p-4">
            <h4 class="fw-bold mb-3 text-primary">АНОНС</h4>
            <h5 class="fw-bold mb-3">XIII МЕЖДУНАРОДНОЙ НАУЧНО-ПРАКТИЧЕСКОЙ КОНФЕРЕНЦИИ ТРАВМАТОЛОГОВ-ОРТОПЕДОВ</h5>
            <p class="lead mb-0">Приглашаем вас принять участие в Юбилейной Международной научно-практической конференции травматологов-ортопедов <strong>«МЕЖДИСЦИПЛИНАРНАЯ ТРАВМАТОЛОГИЯ И ОРТОПЕДИЯ: ОТ ДИАГНОСТИКИ К РЕАБИЛИТАЦИИ»</strong>, посвящённой 25-летию РГП на ПХВ «Национального научного центра травматологии и ортопедии имени академика Батпенова Н. Д.»</p>
        </div>
    </div>

    <div class="mb-4">
        <h5 class="fw-bold text-primary mb-3"><i class="bi bi-people-fill me-2"></i>Организаторы</h5>
        <ul class="list-unstyled">
            <li class="mb-2"><i class="bi bi-check2-circle text-primary me-2"></i>Министерство здравоохранения Республики Казахстан</li>
            <li class="mb-2"><i class="bi bi-check2-circle text-primary me-2"></i>РГП на ПХВ «Национальный научный центр травматологии и ортопедии имени академика Батпенова Н.Д.»</li>
            <li class="mb-2"><i class="bi bi-check2-circle text-primary me-2"></i>РОО «Казахстанская Ассоциация травматологов-ортопедов»</li>
            <li class="mb-2"><i class="bi bi-check2-circle text-primary me-2"></i>Общественный фонд имени академика Нурлана Батпенова</li>
        </ul>
    </div>

    <div class="row g-4 mb-4">
        <div class="col-md-6">
            <div class="h-100 p-4 rounded-4 bg-light shadow-sm">
                <h5 class="fw-bold text-primary mb-3"><i class="bi bi-bullseye me-2"></i>Цель конференции</h5>
                <p class="mb-0">Обмен опытом, обсуждение актуальных вопросов диагностики, лечения и реабилитации пациентов с травмами и заболеваниями опорно-двигательного аппарата, а также внедрение современных научных достижений в практику.</p>
            </div>
        </div>
        <div class="col-md-6">
            <div class="h-100 p-4 rounded-4 bg-light shadow-sm">
                <h5 class="fw-bold text-primary mb-3"><i class="bi bi-grid-3x3-gap me-2"></i>В программе</h5>
                <ul class="list-unstyled small mb-0">
                    <li class="mb-1">Пленарные и секционные заседания</li>
                    <li class="mb-1">Мастер-классы и саттелитные курсы</li>
                    <li class="mb-1">Постерные доклады</li>
                    <li class="mb-1">Конкурс молодых ученых «Батпеновские чтения»</li>
                    <li class="mb-1">Выставка оборудования</li>
                </ul>
            </div>
        </div>
    </div>

    <div class="alert alert-info rounded-4 border-0 shadow-sm p-4 mb-4">
        <h5 class="fw-bold"><i class="bi bi-info-circle-fill me-2"></i>Участники и Формат</h5>
        <p>К участию приглашаются врачи-травматологи, ортопеды, нейрохирурги, реабилитологи, представители вузов и научных центров.</p>
        <p class="mb-0"><strong>Формат:</strong> Очное и онлайн участие.<br><strong>Языки:</strong> Казахский, русский, английский.</p>
    </div>

    <div class="card border-0 shadow-sm rounded-4 mb-4 overflow-hidden">
        <div class="bg-primary text-white p-3">
            <h5 class="fw-bold mb-0"><i class="bi bi-calendar-check me-2"></i>Важные даты и ссылки</h5>
        </div>
        <div class="card-body p-4">
            <div class="row g-3">
                <div class="col-sm-6">
                    <div class="p-3 border rounded-3 h-100">
                        <small class="text-muted d-block mb-1">Регистрация</small>
                        <p class="fw-bold mb-2">Открыта с 10 марта 2026</p>
                        <a href="https://25yearsnscto.online" target="_blank" class="btn btn-sm btn-outline-primary rounded-pill">Перейти на сайт</a>
                    </div>
                </div>
                <div class="col-sm-6">
                    <div class="p-3 border rounded-3 h-100">
                        <small class="text-muted d-block mb-1">Приём тезисов</small>
                        <p class="fw-bold mb-2">Дедлайн: 20 июня 2026</p>
                        <a href="https://www.journaltokaz.org" target="_blank" class="btn btn-sm btn-outline-primary rounded-pill">Подать тезис</a>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <div class="mt-4">
        <h5 class="fw-bold text-primary mb-3"><i class="bi bi-journal-text me-2"></i>Публикация и условия</h5>
        <ul class="list-unstyled small">
            <li class="mb-2"><strong>Журнал:</strong> Тезисы на английском языке будут опубликованы в специальном выпуске «Traumatology and Orthopaedics of Kazakhstan».</li>
            <li class="mb-2"><strong>Сертификаты:</strong> По завершении выдаются именные сертификаты.</li>
            <li class="mb-2"><strong>Контакты:</strong> <a href="mailto:trauma@nscto.kz">trauma@nscto.kz</a> | Гл. редактор: <a href="mailto:editor.journaltokaz@gmail.com">editor.journaltokaz@gmail.com</a></li>
        </ul>
    </div>
</div>

<style>
.announcement-content {
    color: #333;
}
.announcement-content strong {
    color: #000;
}
.announcement-content p, .announcement-content li {
    text-align: justify;
}
</style>
"""
    event.description = formatted_description
    event.save()
    print(f"Updated event: {event.title}")

if __name__ == "__main__":
    update_conference()
