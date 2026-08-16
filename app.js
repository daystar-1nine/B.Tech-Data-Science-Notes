/* ==========================================================================
   DataSci Notes Studio - Main Application Logic
   ========================================================================== */

(function () {
  'use strict';

  // Global State
  let selectedSemester = 'All';
  let selectedSubject = 'All';
  let selectedContentType = 'notes'; // 'notes' or 'qa'
  let searchQuery = '';
  let activeTopicId = null;
  let openSubjects = {};
  let openModules = {};

  // Q&A Bank Hub State
  let qaSelectedSubject = 'All';
  let qaSelectedMarks = 'All';

  // Flashcards State
  let flashcardSubject = 'All';
  let flashcardIndex = 0;
  let flashcardList = [];

  // SVG Icons Palette
  const ICONS = {
    book: `<svg class="icon" viewBox="0 0 24 24"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path></svg>`,
    fileText: `<svg class="icon" viewBox="0 0 24 24"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line></svg>`,
    chevronDown: `<svg class="icon" viewBox="0 0 24 24"><polyline points="6 9 12 15 18 9"></polyline></svg>`,
    chevronRight: `<svg class="icon" viewBox="0 0 24 24"><polyline points="9 18 15 12 9 6"></polyline></svg>`,
    copy: `<svg class="icon" viewBox="0 0 24 24"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>`,
    check: `<svg class="icon" viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"></polyline></svg>`,
    clock: `<svg class="icon" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 16 14 14"></polyline></svg>`
  };

  // DOM Elements
  const themeToggle = document.getElementById('themeToggle');
  const themeToggleMobile = document.getElementById('themeToggleMobile');
  const semSelect = document.getElementById('semSelect');
  const semSelectMobile = document.getElementById('semSelectMobile');
  const treeView = document.getElementById('treeView');
  const searchInput = document.getElementById('searchInput');
  const readerArticle = document.getElementById('readerArticle');
  const pdfDownloadBtn = document.getElementById('pdfDownloadBtn');
  const readerSidebar = document.getElementById('readerSidebar');
  const sidebarOverlay = document.getElementById('sidebarOverlay');
  const mobileNavDrawer = document.getElementById('mobileNavDrawer');
  const sidebarSubTabs = document.getElementById('sidebarSubTabs');
  const progressBar = document.getElementById('scrollProgressBar');
  const readerContainer = document.querySelector('.reader-container');

  // Theme Management
  const currentTheme = localStorage.getItem('theme') || 'dark';
  document.documentElement.setAttribute('data-theme', currentTheme);
  updateThemeBtns(currentTheme);

  function handleThemeToggle() {
    const next = document.documentElement.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
    document.documentElement.setAttribute('data-theme', next);
    localStorage.setItem('theme', next);
    updateThemeBtns(next);
  }

  if (themeToggle) themeToggle.addEventListener('click', handleThemeToggle);
  if (themeToggleMobile) themeToggleMobile.addEventListener('click', handleThemeToggle);

  function updateThemeBtns(theme) {
    const iconHtml = theme === 'dark' ? 
      `<svg class="icon" viewBox="0 0 24 24"><circle cx="12" cy="12" r="5"></circle><line x1="12" y1="1" x2="12" y2="3"></line><line x1="12" y1="21" x2="12" y2="23"></line><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line><line x1="1" y1="12" x2="3" y2="12"></line><line x1="21" y1="12" x2="23" y2="12"></line><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line></svg>` : 
      `<svg class="icon" viewBox="0 0 24 24"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path></svg>`;
    
    if (themeToggle) themeToggle.innerHTML = iconHtml;
    if (themeToggleMobile) themeToggleMobile.innerHTML = iconHtml;
  }

  // Horizontal Sub Tabs Scroll Helper
  window.scrollSubTabs = function (amount) {
    if (sidebarSubTabs) {
      sidebarSubTabs.scrollBy({ left: amount, behavior: 'smooth' });
    }
  };

  // Reading Progress Bar
  if (readerContainer && progressBar) {
    readerContainer.addEventListener('scroll', () => {
      const scrollTop = readerContainer.scrollTop;
      const scrollHeight = readerContainer.scrollHeight - readerContainer.clientHeight;
      const progress = scrollHeight > 0 ? (scrollTop / scrollHeight) * 100 : 0;
      progressBar.style.width = `${progress}%`;
    });
  }

  // Mobile Navigation Drawer Toggle
  window.toggleMobileMenu = function () {
    if (mobileNavDrawer) {
      mobileNavDrawer.classList.toggle('active');
    }
  };

  // Populate Semester Selectors
  function initSemesters() {
    if (!window.NOTES_DATA) return;
    const semesters = Array.from(new Set(window.NOTES_DATA.map(i => i.semester))).sort();
    
    let html = `<option value="All">All Semesters</option>`;
    semesters.forEach(s => {
      html += `<option value="${s}">${s}</option>`;
    });

    if (semSelect) semSelect.innerHTML = html;
    if (semSelectMobile) semSelectMobile.innerHTML = html;

    function handleSemChange(e) {
      selectedSemester = e.target.value;
      if (semSelect) semSelect.value = selectedSemester;
      if (semSelectMobile) semSelectMobile.value = selectedSemester;
      renderSidebarTabs();
      renderSidebarTree();
    }

    if (semSelect) semSelect.addEventListener('change', handleSemChange);
    if (semSelectMobile) semSelectMobile.addEventListener('change', handleSemChange);
  }

  // Monster Modal Popup Functions
  window.openMonsterModal = function () {
    if (mobileNavDrawer) mobileNavDrawer.classList.remove('active');
    const el = document.getElementById('monsterModal');
    if (el) {
      el.classList.add('active');
      el.style.display = 'flex';
      el.style.visibility = 'visible';
      el.style.opacity = '1';
    }
  };

  window.closeMonsterModal = function () {
    const el = document.getElementById('monsterModal');
    if (el) {
      el.classList.remove('active');
      el.style.display = 'none';
      el.style.opacity = '0';
    }
  };

  window.copyUpiId = function () {
    const upiText = '9168772121@mbk';
    navigator.clipboard.writeText(upiText).then(() => {
      const label = document.getElementById('copyUpiText');
      if (label) {
        label.textContent = 'Copied!';
        setTimeout(() => { label.textContent = 'Copy UPI ID'; }, 2000);
      }
    }).catch(() => {
      const label = document.getElementById('copyUpiText');
      if (label) label.textContent = '9168772121@mbk';
    });
  };

  // Render Reader Welcome Dashboard
  window.renderReaderWelcomeState = function () {
    if (!readerArticle) return;
    activeTopicId = null;
    if (pdfDownloadBtn) pdfDownloadBtn.style.display = 'none';

    readerArticle.innerHTML = `
      <div class="welcome-reader-card" style="text-align: center; padding: 32px 16px; max-width: 800px; margin: 0 auto;">
        <div style="width: 56px; height: 56px; border-radius: 16px; background: var(--primary-red-light); color: var(--accent-primary); display: inline-flex; align-items: center; justify-content: center; margin-bottom: 16px; border: 1px solid var(--accent-primary);">
          <svg class="icon icon-xl" viewBox="0 0 24 24"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path></svg>
        </div>

        <h2 style="font-size: 1.8rem; font-weight: 900; color: var(--text-primary); margin-bottom: 8px;">
          Welcome to DataSci Notes Reader
        </h2>
        <p style="color: var(--text-secondary); max-width: 620px; margin: 0 auto 24px; font-size: 0.94rem; line-height: 1.6;">
          Select any topic from the sidebar explorer on the left or pick a core subject below to start reading exam-ready notes, must-write points, and question banks.
        </p>

        <!-- Subject Quick Launch Grid -->
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 12px; margin-bottom: 28px; text-align: left;">
          
          <div class="welcome-sub-box" onclick="window.selectSubjectFirstTopic('DBMS')" style="background: var(--bg-card); border: 1px solid var(--border-color); padding: 16px; border-radius: 14px; cursor: pointer; transition: all 0.2s ease;">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 8px;">
              <span style="font-weight: 800; font-size: 1rem; color: var(--text-primary);">Database Systems</span>
              <span class="count-badge">48 Notes</span>
            </div>
            <p style="font-size: 0.78rem; color: var(--text-secondary); margin-bottom: 10px;">DBMS Architecture, ER Modeling, Relational Algebra, SQL, Normalization, Query Optimization, Concurrency Control & IBM Db2.</p>
            <span style="font-size: 0.78rem; font-weight: 700; color: var(--accent-primary);">Start DBMS Notes &rarr;</span>
          </div>

          <div class="welcome-sub-box" onclick="window.selectSubjectFirstTopic('Data Structure')" style="background: var(--bg-card); border: 1px solid var(--border-color); padding: 16px; border-radius: 14px; cursor: pointer; transition: all 0.2s ease;">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 8px;">
              <span style="font-weight: 800; font-size: 1rem; color: var(--text-primary);">Data Structures</span>
              <span class="count-badge">47 Notes</span>
            </div>
            <p style="font-size: 0.78rem; color: var(--text-secondary); margin-bottom: 10px;">ADT Concepts, Arrays, Stacks, Queues, Linked Lists, Trees (BST, AVL, B-Tree), Graphs (BFS/DFS), Sorting & Hashing.</p>
            <span style="font-size: 0.78rem; font-weight: 700; color: var(--accent-primary);">Start DSA Notes &rarr;</span>
          </div>

          <div class="welcome-sub-box" onclick="window.selectSubjectFirstTopic('MPCA')" style="background: var(--bg-card); border: 1px solid var(--border-color); padding: 16px; border-radius: 14px; cursor: pointer; transition: all 0.2s ease;">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 8px;">
              <span style="font-weight: 800; font-size: 1rem; color: var(--text-primary);">Microprocessors</span>
              <span class="count-badge">32 Notes</span>
            </div>
            <p style="font-size: 0.78rem; color: var(--text-secondary); margin-bottom: 10px;">8086 CPU Architecture, Addressing Modes, Instruction Pipelining & Timing.</p>
            <span style="font-size: 0.78rem; font-weight: 700; color: var(--accent-primary);">Start MPCA Notes &rarr;</span>
          </div>

        </div>

        <!-- Developer Profile Quick Info Card -->
        <div style="background: var(--bg-card); border: 1.5px solid var(--border-color); border-radius: 16px; padding: 20px; text-align: left; display: flex; align-items: center; gap: 16px; flex-wrap: wrap;">
          <img src="suraj_avatar.jpg" alt="Suraj" style="width: 60px; height: 60px; border-radius: 50%; object-fit: cover; border: 2px solid var(--accent-primary);" onerror="this.src='https://ui-avatars.com/api/?name=Suraj&background=A90E02&color=FFFBD4&size=128'">
          
          <div style="flex: 1; min-width: 220px;">
            <div style="font-weight: 800; font-size: 1.05rem; color: var(--text-primary);">Created by Suraj</div>
            <div style="font-size: 0.8rem; color: var(--accent-primary); font-weight: 700; margin-bottom: 4px;">🎓 B.Tech DS | GATE 2028 CSE & DS</div>
            <div style="font-size: 0.78rem; color: var(--text-secondary);">Designed for B.Tech Data Science students preparing for university exams and GATE. Includes 5-tier answer formulation and 1-click PDF downloads.</div>
          </div>

          <button class="btn-primary" onclick="openMonsterModal()" style="font-size: 0.8rem; padding: 8px 14px; min-height: 38px;">
            🔋 Developer Support
          </button>
        </div>

        <!-- Spotlight Shortcut Prompt -->
        <div style="margin-top: 20px; font-size: 0.8rem; color: var(--text-muted);">
          Tip: Press <span class="shortcut-kbd">Ctrl + K</span> anytime to search topics, keywords, or question banks instantly!
        </div>
      </div>
    `;
  };

  window.selectSubjectFirstTopic = function (sub) {
    selectedSubject = sub;
    openSubjects[sub] = true;
    renderSidebarTabs();
    renderSidebarTree();

    if (window.NOTES_DATA) {
      const firstItem = window.NOTES_DATA.find(i => i.subject === sub);
      if (firstItem) {
        selectTopic(firstItem.id);
      }
    }
  };

  // View Navigation
  window.switchView = function (viewId, subject = null, topicId = null) {
    if (mobileNavDrawer) mobileNavDrawer.classList.remove('active');
    document.querySelectorAll('.view-section').forEach(sec => sec.classList.remove('active'));
    document.querySelectorAll('.nav-item').forEach(item => item.classList.remove('active'));

    const activeSec = document.getElementById(`view-${viewId}`);
    if (activeSec) activeSec.classList.add('active');

    const activeNav = document.querySelectorAll(`.nav-item[onclick*="'${viewId}'"]`);
    activeNav.forEach(n => n.classList.add('active'));

    if (subject) {
      selectedSubject = subject;
      openSubjects[subject] = true;
    }

    if (viewId === 'reader') {
      renderSidebarTypeToggleUI();
      renderSidebarTabs();
      renderSidebarTree();

      if (topicId) {
        selectTopic(topicId);
      } else if (activeTopicId && window.NOTES_DATA && window.NOTES_DATA.some(t => t.id === activeTopicId)) {
        selectTopic(activeTopicId);
      } else {
        renderReaderWelcomeState();
      }
    } else if (viewId === 'qa') {
      selectedContentType = 'qa';
      renderSidebarTypeToggleUI();
      initQABankView();
    } else if (viewId === 'flashcards') {
      initFlashcardSubjectBar();
      initFlashcards();
    } else if (viewId === 'about') {
      setTimeout(() => {
        window.openMonsterModal();
      }, 150);
    }

    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  // Sidebar Content Type Segment Toggle ('notes' vs 'qa') with Instant Auto-Expansion
  window.setSidebarContentType = function (type) {
    selectedContentType = type;
    
    // Auto-expand subjects and modules so content change is 100% visible
    if (window.NOTES_DATA) {
      window.NOTES_DATA.forEach(item => {
        openSubjects[item.subject] = true;
        openModules[`${item.subject}-${item.module}`] = true;
      });
    }

    renderSidebarTypeToggleUI();
    renderSidebarTabs();
    renderSidebarTree();
  };

  function renderSidebarTypeToggleUI() {
    const btnNotes = document.getElementById('btnNotesType');
    const btnQA = document.getElementById('btnQAType');

    if (btnNotes && btnQA) {
      if (selectedContentType === 'notes') {
        btnNotes.classList.add('active');
        btnQA.classList.remove('active');
      } else {
        btnQA.classList.add('active');
        btnNotes.classList.remove('active');
      }
    }
  }

  // Dedicated Q&A Bank Hub Functions
  function initQABankView() {
    renderQAFilterBar();
    renderQAGridCards();
  }

  function renderQAFilterBar() {
    const filterContainer = document.getElementById('qaFilterBar');
    if (!filterContainer || !window.NOTES_DATA) return;

    const subjects = ['All', ...Array.from(new Set(window.NOTES_DATA.map(i => i.subject))).sort()];
    const markTypes = ['All', '2 Marks', '3 Marks', '5 Marks', '10 Marks'];

    let html = `<div style="display: flex; align-items: center; gap: 6px; flex-wrap: wrap;">`;
    subjects.forEach(s => {
      const active = qaSelectedSubject === s ? 'active' : '';
      html += `<div class="sub-tab ${active}" onclick="window.setQASubject('${s}')">${s === 'All' ? 'All Subjects' : s}</div>`;
    });
    html += `</div>`;

    html += `<div style="display: flex; align-items: center; gap: 6px; flex-wrap: wrap; margin-left: 12px;">`;
    markTypes.forEach(m => {
      const active = qaSelectedMarks === m ? 'active' : '';
      html += `<div class="flash-chip ${active}" onclick="window.setQAMarks('${m}')">${m}</div>`;
    });
    html += `</div>`;

    filterContainer.innerHTML = html;
  }

  window.setQASubject = function (sub) {
    qaSelectedSubject = sub;
    renderQAFilterBar();
    renderQAGridCards();
  };

  window.setQAMarks = function (marks) {
    qaSelectedMarks = marks;
    renderQAFilterBar();
    renderQAGridCards();
  };

  function renderQAGridCards() {
    const gridContainer = document.getElementById('qaGridContainer');
    if (!gridContainer || !window.NOTES_DATA) return;

    const qaFiles = window.NOTES_DATA.filter(item => {
      const isQA = item.module === 'Question & Answers Bank' || item.filename.endsWith('M.md');
      const matchSub = qaSelectedSubject === 'All' || item.subject === qaSelectedSubject;
      
      let matchMark = true;
      if (qaSelectedMarks !== 'All') {
        const markNum = qaSelectedMarks.split(' ')[0];
        matchMark = item.filename.toLowerCase().startsWith(`${markNum}m`) || item.title.includes(`${markNum}-Mark`);
      }

      return isQA && matchSub && matchMark;
    });

    if (qaFiles.length === 0) {
      gridContainer.innerHTML = `<div style="grid-column: 1 / -1; text-align: center; color: var(--text-muted); padding: 40px 14px;">No Question & Answers Bank found matching selected filters.</div>`;
      return;
    }

    let html = '';
    qaFiles.forEach(item => {
      html += `<div class="subject-card" onclick="window.selectSpotlightTopic('${item.id}')">
        <div class="subject-header">
          <div class="subject-logo">
            <svg class="icon icon-lg" viewBox="0 0 24 24"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line></svg>
          </div>
          <div>
            <div style="font-size: 0.76rem; font-weight: 800; color: var(--accent-primary); text-transform: uppercase;">${item.subject} • ${item.module}</div>
            <div class="subject-name">${item.title}</div>
          </div>
        </div>
        <p class="subject-desc">
          Exam-ready solved questions, key memory points, structured step-by-step answers, and downloadable PDF bank.
        </p>
        <div class="subject-footer">
          <span>${item.pdfPath ? '📄 PDF Available' : '📖 Solved Bank'}</span>
          <span style="font-weight: 800; color: var(--accent-primary);">Read Q&A &rarr;</span>
        </div>
      </div>`;
    });

    gridContainer.innerHTML = html;
  }

  // Toggle Reader Sidebar Drawer
  window.toggleSidebar = function () {
    if (!readerSidebar) return;
    if (window.innerWidth <= 768) {
      readerSidebar.classList.toggle('open-mobile');
      if (sidebarOverlay) sidebarOverlay.classList.toggle('active');
    } else {
      readerSidebar.classList.toggle('collapsed');
    }
  };

  function closeMobileSidebar() {
    if (window.innerWidth <= 768 && readerSidebar) {
      readerSidebar.classList.remove('open-mobile');
      if (sidebarOverlay) sidebarOverlay.classList.remove('active');
    }
  }

  // Sidebar Subject Tabs
  function renderSidebarTabs() {
    if (!sidebarSubTabs || !window.NOTES_DATA) return;
    const subjects = ['All', ...Array.from(new Set(window.NOTES_DATA.map(i => i.subject))).sort()];
    
    let html = '';
    subjects.forEach(s => {
      const active = selectedSubject === s ? 'active' : '';
      html += `<div class="sub-tab ${active}" onclick="window.setSidebarSubject('${s}')">${s}</div>`;
    });
    sidebarSubTabs.innerHTML = html;
  }

  window.setSidebarSubject = function (sub) {
    selectedSubject = sub;
    if (sub !== 'All') openSubjects[sub] = true;
    renderSidebarTabs();
    renderSidebarTree();
  };

  // Global Expand All & Collapse All Controls
  window.expandAllAccordion = function () {
    if (!window.NOTES_DATA) return;
    window.NOTES_DATA.forEach(item => {
      openSubjects[item.subject] = true;
      openModules[`${item.subject}-${item.module}`] = true;
    });
    renderSidebarTree();
  };

  window.collapseAllAccordion = function () {
    openSubjects = {};
    openModules = {};
    renderSidebarTree();
  };

  // Render 2-Level Accordion Tree View
  function renderSidebarTree() {
    if (!window.NOTES_DATA || !treeView) return;

    let filtered = window.NOTES_DATA.filter(item => {
      const matchSem = selectedSemester === 'All' || item.semester === selectedSemester;
      const matchSub = selectedSubject === 'All' || item.subject === selectedSubject;
      
      let matchType = true;
      if (selectedContentType === 'notes') {
        matchType = item.module !== 'Question & Answers Bank';
      } else if (selectedContentType === 'qa') {
        matchType = item.module === 'Question & Answers Bank';
      }

      const q = (searchQuery || '').toLowerCase();
      const matchSearch = !q || item.title.toLowerCase().includes(q) || item.content.toLowerCase().includes(q);
      return matchSem && matchSub && matchType && matchSearch;
    });

    if (filtered.length === 0) {
      treeView.innerHTML = `<div style="text-align: center; color: var(--text-muted); padding: 24px 10px; font-size: 0.82rem;">No matching ${selectedContentType === 'notes' ? 'lecture notes' : 'Q&A banks'} found.</div>`;
      return;
    }

    // Group by Subject -> Module
    const grouped = {};
    filtered.forEach(item => {
      if (!grouped[item.subject]) grouped[item.subject] = {};
      if (!grouped[item.subject][item.module]) grouped[item.subject][item.module] = [];
      grouped[item.subject][item.module].push(item);
    });

    let html = '';
    for (const [sub, modules] of Object.entries(grouped)) {
      let isSubOpen;
      if (openSubjects[sub] !== undefined) {
        isSubOpen = openSubjects[sub];
      } else {
        isSubOpen = searchQuery !== '' || selectedSubject === sub || selectedContentType === 'qa';
      }

      const subOpenClass = isSubOpen ? 'open' : '';
      const subChevron = isSubOpen ? ICONS.chevronDown : ICONS.chevronRight;
      
      let totalCount = 0;
      Object.values(modules).forEach(m => totalCount += m.length);

      html += `<div class="acc-subject ${subOpenClass}">
        <div class="acc-subject-btn" onclick="window.toggleAccordionSubject('${sub}')">
          <div style="display: flex; align-items: center; gap: 4px;">
            <span>${sub}</span>
            <span class="count-badge">${totalCount}</span>
          </div>
          ${subChevron}
        </div>
        <div class="acc-subject-body">`;

      for (const [mod, items] of Object.entries(modules)) {
        const modKey = `${sub}-${mod}`;
        
        let isModOpen;
        if (openModules[modKey] !== undefined) {
          isModOpen = openModules[modKey];
        } else {
          isModOpen = searchQuery !== '' || (activeTopicId && items.some(i => i.id === activeTopicId)) || selectedContentType === 'qa';
        }

        const modOpenClass = isModOpen ? 'open' : '';
        const modChevron = isModOpen ? ICONS.chevronDown : ICONS.chevronRight;

        html += `<div class="acc-module ${modOpenClass}">
          <div class="acc-module-btn" onclick="window.toggleAccordionModule('${modKey}')">
            <div style="display: flex; align-items: center; gap: 4px;">
              <span>${mod}</span>
              <span style="font-size: 0.7rem; opacity: 0.7;">(${items.length})</span>
            </div>
            ${modChevron}
          </div>
          <div class="acc-module-body">`;

        items.forEach(item => {
          const isActive = item.id === activeTopicId ? 'active' : '';
          html += `<div class="tree-link ${isActive}" onclick="window.selectTopic('${item.id}')" title="${item.title}">
            ${ICONS.fileText}
            <span>${item.title}</span>
          </div>`;
        });

        html += `</div></div>`;
      }

      html += `</div></div>`;
    }

    treeView.innerHTML = html;
  }

  window.toggleAccordionSubject = function (sub) {
    const currentState = openSubjects[sub];
    openSubjects[sub] = currentState === undefined ? false : !currentState;
    renderSidebarTree();
  };

  window.toggleAccordionModule = function (modKey) {
    const currentState = openModules[modKey];
    openModules[modKey] = currentState === undefined ? false : !currentState;
    renderSidebarTree();
  };

  function calculateReadTime(text) {
    const words = text ? text.trim().split(/\s+/).length : 0;
    const minutes = Math.ceil(words / 180);
    return minutes < 1 ? 1 : minutes;
  }

  // Select Topic in Reader
  window.selectTopic = function (id) {
    if (!window.NOTES_DATA) {
      renderReaderWelcomeState();
      return;
    }
    const topic = window.NOTES_DATA.find(t => t.id === id);
    if (!topic) {
      renderReaderWelcomeState();
      return;
    }

    activeTopicId = id;
    closeMobileSidebar();
    
    // Automatically set correct content type ('notes' or 'qa') based on selected topic
    selectedContentType = topic.module === 'Question & Answers Bank' ? 'qa' : 'notes';
    renderSidebarTypeToggleUI();

    openSubjects[topic.subject] = true;
    openModules[`${topic.subject}-${topic.module}`] = true;

    // PDF Button
    if (topic.pdfPath) {
      pdfDownloadBtn.style.display = 'inline-flex';
      pdfDownloadBtn.href = topic.pdfPath;
      pdfDownloadBtn.setAttribute('download', '');
    } else {
      pdfDownloadBtn.style.display = 'none';
    }

    const readTime = calculateReadTime(topic.content);

    // Find Previous & Next Topics for sequential reading
    const currentIndex = window.NOTES_DATA.findIndex(t => t.id === id);
    const prevTopic = currentIndex > 0 ? window.NOTES_DATA[currentIndex - 1] : null;
    const nextTopic = currentIndex < window.NOTES_DATA.length - 1 ? window.NOTES_DATA[currentIndex + 1] : null;

    let paginationHtml = `<div class="topic-pagination">`;
    if (prevTopic) {
      paginationHtml += `<button class="btn-secondary" onclick="window.selectTopic('${prevTopic.id}')">&larr; ${prevTopic.title}</button>`;
    } else {
      paginationHtml += `<div></div>`;
    }
    if (nextTopic) {
      paginationHtml += `<button class="btn-primary" onclick="window.selectTopic('${nextTopic.id}')">${nextTopic.title} &rarr;</button>`;
    }
    paginationHtml += `</div>`;

    // Article Content
    readerArticle.innerHTML = `
      <div style="display: flex; align-items: center; justify-content: space-between; font-size: 0.82rem; color: var(--text-muted); margin-bottom: 8px;">
        <span>${topic.semester} &rsaquo; ${topic.subject} &rsaquo; ${topic.module}</span>
        <span>${ICONS.clock} ${readTime} min read</span>
      </div>
      ${topic.html}
      ${paginationHtml}
    `;

    // Attach Copy Code Buttons
    attachCopyCodeButtons();

    renderSidebarTree();
    
    if (readerContainer) readerContainer.scrollTop = 0;
  };

  function attachCopyCodeButtons() {
    const pres = readerArticle.querySelectorAll('pre');
    pres.forEach(pre => {
      if (pre.querySelector('.copy-code-btn')) return;
      const btn = document.createElement('button');
      btn.className = 'copy-code-btn';
      btn.style.cssText = 'position: absolute; top: 8px; right: 8px; background: rgba(255,255,255,0.1); border: 1px solid var(--border-color); color: var(--text-secondary); padding: 4px 8px; border-radius: 4px; font-size: 0.75rem; cursor: pointer; display: flex; align-items: center; gap: 4px;';
      btn.innerHTML = `${ICONS.copy} Copy`;
      
      btn.addEventListener('click', () => {
        const code = pre.querySelector('code') ? pre.querySelector('code').innerText : pre.innerText;
        navigator.clipboard.writeText(code).then(() => {
          btn.innerHTML = `${ICONS.check} Copied!`;
          setTimeout(() => { btn.innerHTML = `${ICONS.copy} Copy`; }, 2000);
        });
      });
      pre.style.position = 'relative';
      pre.appendChild(btn);
    });
  }

  // Search Filter Input
  if (searchInput) {
    searchInput.addEventListener('input', (e) => {
      searchQuery = e.target.value;
      renderSidebarTree();
    });
  }

  // Spotlight Search Modal (Ctrl+K)
  const spotlightModal = document.getElementById('spotlightModal');
  const spotlightInput = document.getElementById('spotlightInput');
  const spotlightResults = document.getElementById('spotlightResults');

  window.openSpotlight = function () {
    if (mobileNavDrawer) mobileNavDrawer.classList.remove('active');
    if (spotlightModal) {
      spotlightModal.classList.add('active');
      if (spotlightInput) {
        spotlightInput.value = '';
        spotlightInput.focus();
        renderSpotlightResults('');
      }
    }
  };

  window.closeSpotlight = function () {
    if (spotlightModal) spotlightModal.classList.remove('active');
  };

  document.addEventListener('keydown', (e) => {
    if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 'k') {
      e.preventDefault();
      openSpotlight();
    } else if (e.key === 'Escape') {
      closeSpotlight();
      closeMonsterModal();
    }
  });

  if (spotlightInput) {
    spotlightInput.addEventListener('input', (e) => {
      renderSpotlightResults(e.target.value);
    });
  }

  function renderSpotlightResults(q) {
    if (!window.NOTES_DATA || !spotlightResults) return;
    const query = q.toLowerCase().trim();
    
    let filtered = window.NOTES_DATA;
    if (query) {
      filtered = window.NOTES_DATA.filter(item => 
        item.title.toLowerCase().includes(query) || 
        item.subject.toLowerCase().includes(query) || 
        item.content.toLowerCase().includes(query)
      );
    }
    
    filtered = filtered.slice(0, 10);

    if (filtered.length === 0) {
      spotlightResults.innerHTML = `<div style="padding: 20px; text-align: center; color: var(--text-muted); font-size: 0.88rem;">No matching notes found.</div>`;
      return;
    }

    let html = '';
    filtered.forEach(item => {
      html += `<div class="spotlight-item" onclick="window.selectSpotlightTopic('${item.id}')">
        <div>
          <strong style="font-size: 0.92rem;">${item.title}</strong>
          <div style="font-size: 0.78rem; color: var(--text-muted);">${item.semester} &bull; ${item.subject} &bull; ${item.module}</div>
        </div>
        <span style="font-size: 0.8rem; color: var(--accent-primary);">Jump &rarr;</span>
      </div>`;
    });

    spotlightResults.innerHTML = html;
  }

  window.selectSpotlightTopic = function (id) {
    closeSpotlight();
    switchView('reader', null, id);
  };

  // Flashcards Module
  function initFlashcardSubjectBar() {
    const container = document.getElementById('flashSubjectBar');
    if (!container || !window.NOTES_DATA) return;

    const subjects = ['All', ...Array.from(new Set(window.NOTES_DATA.map(i => i.subject))).sort()];
    let html = '';
    subjects.forEach(s => {
      const active = flashcardSubject === s ? 'active' : '';
      html += `<div class="flash-chip ${active}" onclick="window.setFlashcardSubject('${s}')">${s}</div>`;
    });
    container.innerHTML = html;
  }

  window.setFlashcardSubject = function (subject) {
    flashcardSubject = subject;
    initFlashcardSubjectBar();
    initFlashcards();
  };

  function initFlashcards() {
    if (!window.NOTES_DATA) return;
    
    flashcardList = window.NOTES_DATA.filter(item => {
      const matchSub = flashcardSubject === 'All' || item.subject === flashcardSubject;
      return matchSub && (item.definition || item.mustWrite.length > 0);
    });

    flashcardIndex = 0;
    renderFlashcard();
  }

  function renderFlashcard() {
    const cardEl = document.getElementById('flashcardCard');
    const counterEl = document.getElementById('flashCounter');
    if (!cardEl) return;

    if (flashcardList.length === 0) {
      cardEl.innerHTML = `<div class="flashcard-body">No flashcards available for selected subject.</div>`;
      counterEl.textContent = `0 of 0`;
      return;
    }

    const item = flashcardList[flashcardIndex];
    
    let backHtml = `<div class="flashcard-tag">${item.subject} • ${item.module}</div>
      <div class="flashcard-title">${item.title}</div>`;

    if (item.mustWrite && item.mustWrite.length > 0) {
      backHtml += `<div style="text-align: left; font-size: 0.88rem; margin-top: 10px;">
        <strong style="color: var(--accent-primary);">⭐ Must-Write Points:</strong>
        <ul style="margin-top: 6px; padding-left: 18px; color: var(--text-secondary);">`;
      item.mustWrite.forEach(pt => {
        backHtml += `<li style="margin-bottom: 3px;">${pt}</li>`;
      });
      backHtml += `</ul></div>`;
    }

    if (item.quickRecall) {
      backHtml += `<div style="margin-top: 12px; padding: 8px 12px; background: var(--callout-quick-bg); border-left: 3px solid var(--callout-quick-border); font-size: 0.82rem; color: var(--text-primary); text-align: left; border-radius: 4px;">
        ⚡ <strong>Quick Recall:</strong> ${item.quickRecall}
      </div>`;
    }

    if (!item.mustWrite.length && !item.quickRecall) {
      backHtml += `<div class="flashcard-body">${item.definition || 'Key concept review'}</div>`;
    }

    cardEl.innerHTML = backHtml;
    counterEl.textContent = `Card ${flashcardIndex + 1} of ${flashcardList.length}`;
  }

  window.nextCard = function () {
    if (flashcardList.length === 0) return;
    flashcardIndex = (flashcardIndex + 1) % flashcardList.length;
    renderFlashcard();
  };

  window.prevCard = function () {
    if (flashcardList.length === 0) return;
    flashcardIndex = (flashcardIndex - 1 + flashcardList.length) % flashcardList.length;
    renderFlashcard();
  };

  // Init on DOM Load
  document.addEventListener('DOMContentLoaded', () => {
    initSemesters();
    renderSidebarTypeToggleUI();
    renderSidebarTabs();
    renderSidebarTree();
    renderReaderWelcomeState();
  });

})();
