import { getDocumentScrollBarWidth } from './base.js';
import { fadeIn, fadeOut } from './animations.js';
import { lenis } from "./lenis";

const MODAL_ID = 'universal-modal'; // Фиксированный ID для единого модального окна
const MODAL_INNER_SELECTOR = '.modal__inner'; // Селектор контейнера для контента

// Основные функции модального окна (адаптированы под единое окно)
const openModal = (callback) => {
    const targetModal = document.querySelector(`[data-modal="${MODAL_ID}"]`);
    console.log(targetModal);
    const pageHeader = document.querySelector('.page-header');
    const scrollBarWidth = getDocumentScrollBarWidth();

    if (document.body.contains(targetModal)) {
        lenis.stop();
    }

    if (document.body.contains(pageHeader)) {
        pageHeader.style.paddingRight = scrollBarWidth + 'px';
    }

    targetModal.classList.add('modal--open');

    fadeIn(targetModal, 300, () => {
        if (callback) {
            callback();
        }
    });
};

const closeModal = (callback) => {
    const targetModal = document.querySelector(`[data-modal="${MODAL_ID}"]`);
    const pageHeader = document.querySelector('.page-header');

    targetModal.classList.remove('modal--open');

    fadeOut(targetModal, 300, () => {
        if (document.body.contains(targetModal)) {
            lenis.start();
        }

        if (document.body.contains(pageHeader)) {
            pageHeader.style.paddingRight = '';
        }

        if (callback) {
            callback();
        }
    });
};

// Новая функция для загрузки контента
const loadModalContent = async (url) => {
    const targetModal = document.querySelector(`[data-modal="${MODAL_ID}"]`);
    if (!targetModal) return false;

    const modalInner = targetModal.querySelector(MODAL_INNER_SELECTOR);
    if (!modalInner) return false;

    try {
        // Можно добавить индикатор загрузки
        modalInner.innerHTML = '<div class="loading-indicator">Загрузка...</div>';

        const response = await fetch(url);
        if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
        
        const html = await response.text();
        modalInner.innerHTML = html;
        return true;
    } catch (error) {
        console.error('Error loading modal content:', error);
        modalInner.innerHTML = `
            <div class="error-message">
                Ошибка загрузки контента
                <button class="js-modal-close">Закрыть</button>
            </div>
        `;
        return false;
    }
};

// Комбинированная функция для загрузки и открытия
const loadAndOpenModal = async (url, callback) => {
    const success = await loadModalContent(url);
    if (success) {
        openModal(callback);
    }
};

// Обработчики событий (адаптированы под единое окно)
const modalOpenTrigger = (event) => {
    const target = event.target.closest('[data-modal-trigger]');
    if (!target) return;

    const url = target.getAttribute('data-url');
    if (!url) {
        console.error('data-url attribute is required');
        return;
    }

    loadAndOpenModal(url);
};

// Остальные обработчики остаются без изменений
const modalCloseTrigger = (event) => {
    const target = event.target.closest('.js-modal-close');
    if (target) {
        closeModal();
    }
};

const modalCloseEscape = (event) => {
    const activeModal = document.querySelector('.modal--open');
    if (event.key === 'Escape' && document.contains(activeModal)) {
        closeModal();
    }
};

const modalCloseOutside = (event) => {
    const activeModal = document.querySelector('.modal--open');
    const modalTriggers = document.querySelectorAll('[data-modal-trigger]');
    const modalTriggersArr = [...modalTriggers];
    const eventTarget = event.target;

    if (document.contains(activeModal)) {
        const doesContainTarget = modalTriggersArr.some((element) => {
            return element.contains(eventTarget);
        });

        let modalContent = activeModal.querySelector('.modal__inner');
        if (!modalContent.contains(event.target) && !doesContainTarget) {
            closeModal();
        }
    }
};

export { 
    modalOpenTrigger, 
    modalCloseTrigger, 
    modalCloseEscape, 
    modalCloseOutside, 
    closeModal,
    loadAndOpenModal // Добавляем новую функцию в экспорт
};