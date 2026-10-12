#!/usr/bin/env python3
"""Usage: python apply_upgrade.py index.html   (writes index.html, keeps index.backup.html)"""
import re, sys, shutil
from html import escape as E

def chips(l): return '<div class="project-stack">' + ''.join(f'<span class="stack-chip">{E(c)}</span>' for c in l) + '</div>'
def lis(l): return '<ul class="project-highlights">' + ''.join(f'<li>{E(x)}</li>' for x in l) + '</ul>' if l else ''
def link(h, t, a): return f'<a href="{h}" target="_blank" rel="noopener noreferrer" class="project-link" aria-label="{E(a)} (opens in a new tab)">{E(t)}</a>'
def badge(t, c=''): return f'<span class="project-badge {c}">{E(t)}</span>'

def row(n, name, desc, stack, hl, links, badges):
    l = ''.join(link(*x) for x in links) + ''.join(badge(*b) for b in badges)
    return (f'      <div class="project-row">\n        <div>\n          <div class="project-num">{n}</div>\n'
            f'          <h4 class="project-name">{E(name)}</h4>\n          <p class="project-desc">{E(desc)}</p>\n'
            f'          {chips(stack)}\n          {lis(hl)}\n        </div>\n        <div class="project-links-col">{l}</div>\n      </div>\n')

def cat(t, p, rows): return f'    <div class="proj-cat"><h3>{E(t)}</h3><p>{E(p)}</p></div>\n    <div class="projects-list">\n{rows}    </div>\n'

CL = ('Internship / Client Project', '')
PR = 'Personal Project'
A = ''.join([
 row('A1', 'PyBot AI Solutions', 'Responsive client website with a React/Vite frontend integrated with a Django REST API backend.',
  ['React','Vite','Django','MySQL','Web3Forms','Hostinger'],
  ['Developed a responsive React/Vite frontend integrated with a Django REST API backend','Implemented customer registration and login with secure password hashing','Developed multi-step application forms and automated certificate downloads','Integrated MySQL and improved website metadata for SEO and GEO'],
  [('https://pybotaisolutions.com/','↗ Live Site','Visit the PyBot AI Solutions website')],[CL]),
 row('A2', 'Getzz Ready Kidzz School Website', 'Mobile-first, responsive school marketing website with admission inquiry forms.',
  ['HTML5','CSS3','JavaScript','Web3Forms'],
  ['Designed and deployed a mobile-first, responsive school marketing website','Integrated admission inquiry forms with automated email notifications using Web3Forms','Improved page structure, performance and search-engine visibility'],
  [('https://www.getzzreadykidzzschool.com/','↗ Live Site','Visit the Getzz Ready Kidzz School website')],[CL]),
 row('A3', 'Profenaa International Kids School — Educational Website', 'Multi-page website for Profenaa International Kids School, showcasing school information, preschool programs, kindergarten levels, daycare services, leadership profiles, activity galleries, educational content, and contact information.',
  ['HTML5','CSS3','JavaScript','SEO'],
  ['Dedicated pages for Play Group, Nursery, Junior KG, Senior KG and Day Care','About, Chairman Message and Principal Message pages','Photo gallery, blog, contact page and franchise information page','Admission registration form and franchise enquiry form'],
  [('https://profenaakidsschool.com/','↗ Live Site','Visit the Profenaa International Kids School website')],[CL]),
 row('A4', 'Chella Mazhalaigal Preschool & Daycare Website', 'Multi-page preschool and daycare website with program information, gallery, blog, and contact sections.',
  ['HTML5','CSS3','JavaScript','SEO'],
  ['Home, About Us, Day Care, Gallery, Blogs and Contact pages','Age-group program listings and an "Enroll Your Kid" enquiry form'],
  [('https://chellamazhalaigaldaycare.com/','↗ Live Site','Visit the Chella Mazhalaigal website')],[CL]),
 row('A5', 'Dr. Muthuraj Madamuthu — Leadership Portfolio', 'React/Vite personal branding website presenting professional information, initiatives, community impact, media coverage, gallery content and contact opportunities.',
  ['React.js','Vite','JavaScript','HTML5','CSS3'],
  ['Home, About, Initiatives, Impact, Gallery, Media and Connect sections','Bilingual Tamil/English contact experience'],
  [('https://drmuthurajmadamuthu.com/','↗ Live Site','Visit the Dr. Muthuraj Madamuthu website')],[CL]),
])
C = row('C1', 'Student & Staff Management System', 'Responsive student and admin dashboard interfaces integrated with backend REST API endpoints.',
  ['HTML5','CSS3','JavaScript','Bootstrap','REST APIs','MySQL'],
  ['Developed responsive student and admin dashboard interfaces','Worked on attendance, leave management, projects, certificates, performance, notifications, feedback, referrals and account management','Integrated frontend workflows with REST API endpoints provided by the backend team','Collaborated on API request/response structures, validation and integration workflows','Used AI-assisted development to analyze and troubleshoot implementation drafts'],
  [], [('Internal Project','internal'),('Collaborative Internship Project','internal'),('No Public Demo','internal')])
def P(n,name,desc,stack,prac,hl,links,when,label=PR):
    return row(n,name,desc,stack,[f'Practised: {prac}']+hl,links,[(label,'personal')]+([(when,'')] if when else []))
B = ''.join([
 P('B1','E-Commerce Web Application','Full-stack e-commerce platform with authentication, product management, cart, checkout, and integrated Razorpay payment gateway.',
  ['Python','Django','MySQL','Bootstrap','JavaScript','Razorpay API','HTML5','CSS3'],'session authentication, payment gateway integration, order workflows, relational data',
  ['Razorpay payment gateway for online transactions','Admin panel to manage products, orders, and users','Cart, Buy Now, checkout and order-processing workflows, including order status and cancellation','Responsive customer and administrative interfaces'],[],'Nov – Dec 2025'),
 P('B2','Employee CRUD App — Next.js + Django','Full-stack employee management system with JWT auth, role-based access, search, filtering and pagination.',
  ['Next.js 14','TypeScript','Django REST','PostgreSQL','JWT','Tailwind CSS'],'JWT authentication, role-based access control, connecting a Next.js frontend to a Django REST API',
  ['Built as a 2-day interview-preparation exercise','Frontend deployed on Vercel, backend on Render'],
  [('https://crud-nextjs-rosy.vercel.app/','↗ Frontend','Open the Employee CRUD frontend'),('https://django-nextjs-backend-m93z.onrender.com/api/backend/','↗ API','Open the Employee CRUD API')],'Jan – Feb 2026','Practice Project'),
 P('B3','Secure Login System with CAPTCHA','Authentication system with CAPTCHA verification, password validation rules, and a login/registration UI.',
  ['Django','Python','CAPTCHA','HTML','CSS','JavaScript'],'bot protection and password validation',
  ['CAPTCHA to prevent bot-based login attempts','Password validation for strong credentials'],[('https://captcha-verification-r0v7.onrender.com','↗ Live App','Open the CAPTCHA login demo')],'Jul 2025','Practice Project'),
 P('B4','Email Verification System with OTP','Registration system that verifies identity with an OTP sent over SMTP, with error handling for wrong OTP entries.',
  ['Django','SMTP','SQLite','JavaScript','Responsive Email'],'SMTP email delivery and OTP verification flow',
  ['SMTP integration to send OTP codes to email','Responsive email template design'],[],'Aug 2025','Practice Project'),
 P('B5','Admin Dashboard — Product & Order Control','Custom admin dashboard with CRUD operations for managing products, users, and orders with status display.',
  ['Django','Python','MySQL','Bootstrap','JavaScript'],'CRUD operations and admin dashboard design',[],[],'Jun – Jul 2025','Practice Project'),
 P('B6','Weather Forecast Application','Weather app using external API integration with a glassmorphism UI, displaying temperature, humidity, and conditions.',
  ['Django','Python','Weather API','JavaScript','CSS'],'consuming an external API and presenting live data',[],[('https://whether-application-ygep.onrender.com','↗ Live App','Open the Weather Forecast demo')],'Sep – Oct 2025','Practice Project'),
 P('B7','Quiz Application','25-question quiz app with light/dark themes and score & percentage display.',
  ['HTML5','CSS3','Bootstrap','JavaScript','Django'],'quiz logic, scoring and theme switching',[],[('https://quiz-application-wckb.onrender.com/','↗ Live App','Open the Quiz Application demo')],'','Practice Project'),
 P('B8','Smart Calculator','Calculator with Django backend logic and a responsive interface.',
  ['Django','Python','Responsive Design'],'handling calculation logic on a Django backend',[],[('https://calculator-django-w42b.onrender.com','↗ Live App','Open the Smart Calculator demo')],'','Practice Project'),
])
PROJECTS = ('<!-- PROJECTS -->\n  <section id="projects" class="fade-up">\n    <div class="label">Key Projects</div>\n    <h2 class="section-title">What I\'ve Built</h2>\n'
  + cat('A. Internship & Client Projects','Public websites built during my internship at Profenaa Infotech for clients and group organisations.',A)
  + cat('B. Personal Study & Learning Projects','Projects I built on my own to practise and demonstrate technical skills. These are not client or production work.',B)
  + cat('C. Internal / Collaborative Projects','Internal tools built with the Profenaa team. Not publicly accessible.',C)
  + '  </section>\n')

def card(icon, name, typ, desc, links, st, label):
    l = ''.join(f'<a href="{h}" target="_blank" rel="noopener noreferrer" class="deploy-link" aria-label="{E(a)} (opens in a new tab)">{E(t)}</a>' for h,t,a in links)
    return (f'      <div class="deploy-card" data-status="{st}"><span class="deploy-icon" aria-hidden="true">{icon}</span>'
            f'<span class="status {st}">{label}</span><div class="deploy-type">{typ}</div><h3 class="deploy-name">{E(name)}</h3>'
            f'<p class="deploy-desc">{E(desc)}</p><div class="deploy-links">{l}</div></div>\n')
LV, UV, DV = ('live','Live — confirmed'), ('unverified','Unverified'), ('dev','In Development')
def D(i,n,t,d,l,s): return card(i,n,t,d,l,s[0],s[1])
CW, PP = 'Client Website', 'Personal Project'
LIVE = ('<!-- LIVE DEPLOYMENTS -->\n  <section id="live" class="fade-up">\n    <div class="label">Production</div>\n    <h2 class="section-title">Live Deployments</h2>\n    <div class="deploy-grid">\n'
 + D('🤖','PyBot AI Solutions',CW,'React, Vite and Django REST API, hosted on Hostinger.',[('https://pybotaisolutions.com/','↗ Website','Visit pybotaisolutions.com')],LV)
 + D('🏫','Getzz Ready Kidzz School',CW,'Mobile-first school website with admission inquiry forms and email notifications.',[('https://www.getzzreadykidzzschool.com/','↗ Website','Visit getzzreadykidzzschool.com')],LV)
 + D('🧸','Chella Mazhalaigal Preschool & Daycare',CW,'Multi-page preschool and daycare website. HTML, CSS, JavaScript.',[('https://chellamazhalaigaldaycare.com/','↗ Visit Live Website','Visit chellamazhalaigaldaycare.com')],LV)
 + D('🎒','Profenaa International Kids School',CW,'Multi-page school website. HTML, CSS, JavaScript.',[('https://profenaakidsschool.com/','↗ Visit Live Website','Visit profenaakidsschool.com')],LV)
 + D('🎙️','Dr. Muthuraj Madamuthu — Leadership Portfolio',CW,'React, Vite and JavaScript personal branding website with a bilingual Tamil/English contact experience.',[('https://drmuthurajmadamuthu.com/','↗ Visit Live Website','Visit drmuthurajmadamuthu.com')],LV)
 + D('👥','Employee CRUD App',PP,'Next.js + Django REST API with JWT auth, role access, search & pagination.',[('https://crud-nextjs-rosy.vercel.app/','↗ App','Open the Employee CRUD app'),('https://django-nextjs-backend-m93z.onrender.com/api/backend/','↗ API','Open the Employee CRUD API')],LV)
 + D('🌦️','Weather Forecast',PP,'Weather data with a glassmorphism UI and live API integration.',[('https://whether-application-ygep.onrender.com','↗ Render','Open the Weather Forecast app')],UV)
 + D('🔐','CAPTCHA Auth System',PP,'Login with CAPTCHA verification and password validation.',[('https://captcha-verification-r0v7.onrender.com','↗ Render','Open the CAPTCHA Auth app')],UV)
 + D('📝','Quiz Application',PP,'25-question quiz with light/dark themes and score display.',[('https://quiz-application-wckb.onrender.com/','↗ Render','Open the Quiz app')],UV)
 + D('🧮','Smart Calculator',PP,'Calculator with Django backend logic.',[('https://calculator-django-w42b.onrender.com','↗ Render','Open the Smart Calculator')],UV)
 + D('🌐','Bakery Website',PP,'React SPA with component-based architecture and responsive layout. Still being built.',[('https://bakerywebsite12.netlify.app/','↗ Netlify','Open the Bakery website')],DV)
 + D('📊','More Coming Soon',PP,'E-Commerce platform deployment in progress.',[('https://github.com/Venkatesh-Developer-py','↗ GitHub','Open my GitHub profile')],DV)
 + '    </div>\n    <p class="deploy-note">Only deployments marked "Live — confirmed" are counted in the Live Apps statistic.</p>\n  </section>\n\n  ')

def sk(t, l): return f'      <div class="skill-cell"><h3>{t}</h3><div class="chips">' + ''.join(f'<span class="chip">{E(c)}</span>' for c in l) + '</div></div>\n'
EXP = '''<!-- PROFESSIONAL EXPERIENCE -->
  <section id="experience" class="fade-up">
    <div class="label">Professional Experience</div>
    <h2 class="section-title">Where I'm Working</h2>
    <div class="exp-wrap">
      <div class="exp-card">
        <div>
          <div class="exp-period">APR 2026 — PRESENT</div>
          <div class="exp-place">Coimbatore</div>
          <span class="project-badge">Internship · Current Role</span>
        </div>
        <div>
          <h3 class="exp-role">Python Full Stack Developer Intern</h3>
          <div class="exp-company">Profenaa Infotech</div>
          <div class="exp-sub">Hands-on contributions</div>
          <ul class="project-highlights">
            <li>Develop frontends and full-stack features with HTML, CSS, JavaScript, React/Vite, Python, Django and MySQL</li>
            <li>Implement authentication, form validation, password hashing and database operations</li>
            <li>Build responsive interfaces and dashboards</li>
            <li>Optimize production websites for performance, accessibility, SEO and GEO</li>
          </ul>
          <div class="exp-sub">Integration, support &amp; collaboration</div>
          <ul class="project-highlights">
            <li>Integrate frontends with REST API endpoints, working with backend developers on request/response structures</li>
            <li>Debug frontend, backend, API and production issues using browser developer tools and Postman</li>
            <li>Support deployment and maintenance of client websites on Hostinger VPS, including domain, web-server and SSL configuration</li>
            <li>Collaborate with backend developers, designers and other team members</li>
            <li>Use AI-assisted development and structured prompt engineering to analyze and troubleshoot implementation drafts</li>
          </ul>
          <div class="project-stack"><span class="stack-chip">Python</span><span class="stack-chip">Django</span><span class="stack-chip">React</span><span class="stack-chip">Vite</span><span class="stack-chip">JavaScript</span><span class="stack-chip">MySQL</span><span class="stack-chip">Postman</span><span class="stack-chip">Hostinger VPS</span></div>
        </div>
      </div>
    </div>
  </section>

  <!-- SKILLS -->
  <section id="skills" class="fade-up">
    <div class="label">Technical Stack</div>
    <h2 class="section-title">Skills &amp; Technologies</h2>
    <div class="skills-grid">
''' + sk('Frontend Development',['HTML5','CSS3','JavaScript','React.js','Vite','React Router','Bootstrap','Responsive Design','Form Validation']) \
    + sk('Backend Development',['Python','Django','Django ORM','Django Templates','MVT Architecture','Session Management','SMTP','OOP']) \
    + sk('Databases',['MySQL','SQLite','PostgreSQL','MySQL Connector','Database Design']) \
    + sk('APIs & Authentication',['REST API Development','Django REST Framework','API Integration','JWT','Authentication','Password Hashing']) \
    + sk('Developer Tools',['Git','GitHub','Postman','VS Code','PyCharm']) \
    + sk('Deployment & Hosting',['Hostinger VPS','Domain Management','SSL Configuration','Render','Vercel','Netlify']) \
    + sk('SEO & Web Optimization',['SEO','GEO (Generative Engine Optimization)','Google Search Console']) \
    + sk('AI-Assisted Development',['Prompt Engineering','AI-Assisted Development','AI-Assisted Debugging']) \
    + sk('Still Learning / Basic Level',['Basic Next.js','TypeScript','Supabase','Google Cloud']) \
    + '    </div>\n  </section>\n\n  '

CSS = '''
    /* ── UPGRADE ADDITIONS ── */
    .proj-cat { margin: 0 0 1rem; }
    .proj-cat:not(:first-of-type) { margin-top: 3rem; }
    .proj-cat h3 { font-family: 'DM Serif Display', serif; font-size: 1.5rem; font-weight: 400; color: var(--text); }
    .proj-cat p { font-size: 0.84rem; color: var(--muted2); max-width: 680px; }
    h4.project-name { font-size: 1.3rem; }
    .project-badge.personal { background: rgba(56,189,248,0.07); border-color: rgba(56,189,248,0.2); color: var(--accent); }
    .exp-sub { font-family: 'DM Mono', monospace; font-size: 0.7rem; letter-spacing: 0.14em; text-transform: uppercase; color: var(--accent); margin: 1.2rem 0 0.4rem; }
    .deploy-type { font-family: 'DM Mono', monospace; font-size: 0.64rem; letter-spacing: 0.1em; text-transform: uppercase; color: var(--muted); margin-bottom: 0.4rem; }
    .status { display: inline-flex; align-items: center; gap: 0.4rem; float: right; font-family: 'DM Mono', monospace; font-size: 0.64rem; padding: 0.2rem 0.55rem; border-radius: 3px; border: 1px solid var(--border); color: var(--muted2); }
    .status::before { content: ''; width: 6px; height: 6px; border-radius: 50%; background: currentColor; }
    .status.live { color: var(--accent3); border-color: rgba(52,211,153,0.25); background: rgba(52,211,153,0.07); }
    .status.dev { color: var(--accent2); border-color: rgba(129,140,248,0.25); background: rgba(129,140,248,0.08); }
    .deploy-note { font-size: 0.74rem; color: var(--muted); font-family: 'DM Mono', monospace; margin-top: 0.8rem; }
    body:not(.cursor-on), body:not(.cursor-on) * { cursor: auto !important; }
    @media (hover: none), (pointer: coarse) { .cursor-dot, .cursor-ring { display: none; } }
'''
JS = '''const projEl = document.getElementById('statProjects'), liveEl = document.getElementById('statLive');
  if (projEl) projEl.dataset.count = document.querySelectorAll('.project-row').length;
  if (liveEl) liveEl.dataset.count = document.querySelectorAll('.deploy-card[data-status="live"]').length;
  if (matchMedia('(hover: hover) and (pointer: fine)').matches) document.body.classList.add('cursor-on');
  const counters = document.querySelectorAll('[data-count]');'''
HERO_EYE = '''<div class="hero-eyebrow-wrap">
          <div class="hero-eyebrow">Python Full Stack Developer | Django, React &amp; REST APIs</div>
          <div class="hero-eyebrow">Current: Python Full Stack Developer Intern · Profenaa Infotech</div>
        </div>'''
HERO_BIO = '''<p class="hero-bio">
          Computer Science graduate with hands-on experience in web application development, client website development, API integration and deployment workflows. I build responsive React.js frontends and Django backends with REST APIs, MySQL and secure authentication. Currently interning at Profenaa Infotech (since April 2026), working on client websites and internal tools with the development team.
        </p>'''
HERO_ACT = '''<div class="hero-actions">
          <a href="#projects" class="btn-primary">View Projects</a>
          <a href="#live" class="btn-ghost">Live Deployments</a>
          <a href="M._Thiru_Venkatesh_Python-Full-Stack-Developer.pdf" download class="btn-ghost">Download Resume</a>
          <a href="#contact" class="btn-ghost">Contact Me</a>
          <a href="https://github.com/Venkatesh-Developer-py" target="_blank" rel="noopener noreferrer" class="btn-ghost">GitHub</a>
          <a href="https://www.linkedin.com/in/thiruvenkatesh/" target="_blank" rel="noopener noreferrer" class="btn-ghost">LinkedIn</a>
        </div>'''
DESC = 'Portfolio of M. Thiru Venkatesh, Python Full Stack Developer (Django, React, REST APIs, MySQL). Client websites, personal projects and live deployments.'

def sub(h, pat, rep, flags=re.S):
    n = re.subn(pat, lambda m: rep, h, count=1, flags=flags)
    assert n[1] == 1, f'pattern not found: {pat[:50]}'
    return n[0]
def rep(h, a, b, count=1):
    assert a in h, f'text not found: {a[:50]}'
    return h.replace(a, b) if count == 0 else h.replace(a, b, count)

def main(path):
    h = open(path, encoding='utf-8').read()
    shutil.copy(path, path.replace('.html', '.backup.html'))
    h = rep(h, '<title>M. Thiru Venkatesh | Python Full Stack Developer</title>', '<title>M. Thiru Venkatesh | Python Full Stack Developer — Django, React &amp; REST APIs</title>')
    h = sub(h, r'<meta name="description" content=".*?" />', f'<meta name="description" content="{DESC}" />')
    h = sub(h, r'<meta property="og:description" content=".*?" />', f'<meta property="og:description" content="{DESC}" />')
    h = sub(h, r'<div class="hero-eyebrow-wrap">.*?(?=\s*<h1 class="hero-name">)', HERO_EYE)
    h = sub(h, r'<p class="hero-bio">.*?</p>', HERO_BIO)
    h = sub(h, r'<div class="hero-actions">.*?</div>', HERO_ACT)
    h = rep(h, '<span class="stat-num" data-count="18">0</span>', '<span class="stat-num" id="statProjects" data-count="0">0</span>')
    h = rep(h, '<span class="stat-num" data-count="10">0</span>', '<span class="stat-num" id="statLive" data-count="0">0</span>')
    h = rep(h, '<li>5 apps deployed on Railway, Render, Vercel &amp; Netlify</li>', '<li>Client websites deployed with domain &amp; SSL setup</li>')
    h = rep(h, "(isFloat ? '' : '+')", "''", 0)
    h = rep(h, "const counters = document.querySelectorAll('[data-count]');", JS)
    h = rep(h, '  </style>', CSS + '  </style>')
    h = rep(h, '</head>', '<noscript><style>.fade-up,.hero-eyebrow,.hero-name,.hero-role,.hero-bio,.hero-tags,.hero-actions,.hero-card{opacity:1!important;transform:none!important}</style></noscript>\n</head>')
    i_exp, i_proj, i_edu = (h.find(m) for m in ('<!-- PROFESSIONAL EXPERIENCE -->', '<!-- PROJECTS -->', '<!-- EDUCATION -->'))
    assert 0 < i_exp < i_proj < i_edu, 'section markers not found / out of order'
    h = h[:i_exp] + LIVE + EXP + PROJECTS + '  ' + h[i_edu:]
    open(path, 'w', encoding='utf-8').write(h)
    print('done: projects', h.count('class="project-row"'), '| deploy cards', h.count('class="deploy-card"'))

if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else 'index.html')