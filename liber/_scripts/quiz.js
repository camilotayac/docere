// quiz.js — Interactive ICFES quiz system for Docere
// Makes multiple choice options clickable with immediate feedback
// Degrades gracefully: PDF/EPUB render without JS

(function () {
  'use strict';

  const LETTERS = ['A', 'B', 'C', 'D'];
  const STORAGE_KEY = 'docere-quiz-results';

  // Cache results to prevent redundant JSON parsing (performance optimization)
  let cachedResults = null;

  function getResults() {
    if (cachedResults) return cachedResults;
    try {
      cachedResults = JSON.parse(sessionStorage.getItem(STORAGE_KEY)) || {};
    } catch (e) {
      cachedResults = {};
    }
    return cachedResults;
  }

  function saveResult(questionId, letter) {
    const results = getResults();
    results[questionId] = letter;
    try {
      sessionStorage.setItem(STORAGE_KEY, JSON.stringify(results));
    } catch (e) { /* ignore */ }
  }

  function getCorrectLetter(grid) {
    return grid.getAttribute('data-correct');
  }

  function initQuiz() {
    const grids = document.querySelectorAll('.icfes-grid');
    if (!grids.length) return;

    const results = getResults();

    grids.forEach(grid => {
      const questionId = grid.getAttribute('data-question-id');
      const correctAnswer = getCorrectLetter(grid);
      if (!questionId || !correctAnswer) return;

      const options = grid.querySelectorAll('.icfes-opcion');
      const previouslySelected = results[questionId];

      options.forEach((opt, i) => {
        opt.setAttribute('tabindex', '0');
        opt.setAttribute('role', 'button');
        opt.setAttribute('aria-pressed', 'false');
        opt.setAttribute('data-letter', LETTERS[i]);

        if (previouslySelected) {
          const isSelected = previouslySelected === LETTERS[i];
          opt.setAttribute('aria-pressed', isSelected ? 'true' : 'false');
          if (isSelected) opt.classList.add('selected');
        }
      });

      if (previouslySelected) {
        showFeedback(grid, previouslySelected === correctAnswer, correctAnswer);
      }
    });

    updateScorePanel();
  }

  function handleSelect(opt, questionId, correctAnswer, options) {
    const letter = opt.getAttribute('data-letter');
    if (opt.classList.contains('verified')) return;

    options.forEach(o => {
      o.classList.remove('selected');
      o.setAttribute('aria-pressed', 'false');
    });

    opt.classList.add('selected');
    opt.setAttribute('aria-pressed', 'true');
    saveResult(questionId, letter);

    const isCorrect = letter === correctAnswer;
    showFeedback(opt.closest('.icfes-grid'), isCorrect, correctAnswer);

    const liveRegion = document.getElementById('quiz-live-region');
    if (liveRegion) {
      liveRegion.textContent = isCorrect
        ? 'Correcta'
        : `Incorrecta. La respuesta correcta es ${correctAnswer}`;
    }

    updateScorePanel();
  }

  function showFeedback(grid, isCorrect, correctLetter) {
    const options = grid.querySelectorAll('.icfes-opcion');
    options.forEach(opt => {
      opt.classList.add('verified');
      opt.setAttribute('tabindex', '-1');
      opt.setAttribute('aria-disabled', 'true');
      const letter = opt.getAttribute('data-letter');
      
      if (letter === correctLetter) {
        opt.classList.add('correct');
        opt.setAttribute('aria-label', `Opción ${letter} — correcta`);
      } else if (opt.classList.contains('selected')) {
        opt.classList.add('incorrect');
        opt.setAttribute('aria-invalid', 'true');
        opt.setAttribute('aria-label', `Opción ${letter} — incorrecta`);
      }
    });
    grid.setAttribute('aria-disabled', 'true');
  }

  function updateScorePanel() {
    const results = getResults();
    const grids = document.querySelectorAll('.icfes-grid[data-question-id]');
    const total = grids.length;
    
    if (total === 0) return;

    let answered = 0;
    let correct = 0;

    grids.forEach(grid => {
      const qId = grid.getAttribute('data-question-id');
      if (results[qId]) {
        answered++;
        if (results[qId] === getCorrectLetter(grid)) correct++;
      }
    });

    let panel = document.getElementById('quiz-score-panel');
    if (!panel) {
      panel = document.createElement('div');
      panel.id = 'quiz-score-panel';
      panel.className = 'icfes-score-panel';
      panel.setAttribute('aria-live', 'polite');
      panel.setAttribute('aria-atomic', 'true');
      
      const evaluacion = document.querySelector('.evaluacion');
      if (evaluacion) {
        const collapse = evaluacion.querySelector('.collapse') || evaluacion;
        collapse.appendChild(panel);
      }
    }

    if (answered === 0) {
      panel.innerHTML = '';
      panel.style.display = 'none';
      return;
    }

    const percentage = Math.round((correct / answered) * 100);
    const progressWidth = (answered / total) * 100;

    panel.style.display = '';
    panel.innerHTML = `
      <div class="icfes-score-bar">
        <span class="icfes-score-label">Progreso</span>
        <div class="icfes-score-track">
          <div class="icfes-score-fill" style="width:${progressWidth}%"></div>
        </div>
        <span class="icfes-score-text">${answered}/${total} respondidas</span>
      </div>
      ${answered > 0 ? `<div class="icfes-score-result">${correct} de ${answered} correctas (${percentage}%)</div>` : ''}
    `;
  }

  function addLiveRegion() {
    if (document.getElementById('quiz-live-region')) return;
    const region = document.createElement('div');
    region.id = 'quiz-live-region';
    region.setAttribute('role', 'status');
    region.setAttribute('aria-live', 'polite');
    region.setAttribute('aria-atomic', 'true');
    region.className = 'sr-only';
    document.body.appendChild(region);
  }

  function setupDelegatedEvents() {
    document.addEventListener('click', e => {
      const opt = e.target.closest('.icfes-opcion');
      if (!opt) return;
      
      const grid = opt.closest('.icfes-grid');
      if (!grid) return;
      
      const questionId = grid.getAttribute('data-question-id');
      const correctAnswer = getCorrectLetter(grid);
      const options = grid.querySelectorAll('.icfes-opcion');
      handleSelect(opt, questionId, correctAnswer, options);
    });

    document.addEventListener('keydown', e => {
      const opt = e.target.closest('.icfes-opcion');
      if (!opt || opt.classList.contains('verified')) return;
      
      const grid = opt.closest('.icfes-grid');
      if (!grid) return;

      const options = Array.from(grid.querySelectorAll('.icfes-opcion'));
      const idx = options.indexOf(opt);

      switch (e.key) {
        case 'Enter':
        case ' ':
          e.preventDefault();
          handleSelect(opt, grid.getAttribute('data-question-id'), getCorrectLetter(grid), options);
          break;
        case 'ArrowRight':
        case 'ArrowDown':
          e.preventDefault();
          if (idx < options.length - 1) options[idx + 1].focus();
          break;
        case 'ArrowLeft':
        case 'ArrowUp':
          e.preventDefault();
          if (idx > 0) options[idx - 1].focus();
          break;
        case 'Home':
          e.preventDefault();
          if (options.length) options[0].focus();
          break;
        case 'End':
          e.preventDefault();
          if (options.length) options[options.length - 1].focus();
          break;
      }
    });
  }

  const runInit = () => {
    addLiveRegion();
    initQuiz();
    setupDelegatedEvents();
  };

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', runInit);
  } else {
    runInit();
  }
})();
